import tensorflow as tf
import numpy as np
import os
from PIL import Image
import jax
import kagglehub
import ml_collections
import sentencepiece
import io

TOKENIZER_PATH = "./paligemma_tokenizer.model"
tokenizer = sentencepiece.SentencePieceProcessor(TOKENIZER_PATH)

class VQA_Dataset():
    def __init__(self, split):
        self.split = split
        self.image_resolution = 224
        self.images_path = "resized_ratio_short_side_768"
        self.questions_path = "mimic-cxr-vqa/train.json"
        self.seqlen = None

    def preprocess_image(self, image):
        # Model has been trained to handle images of different aspects ratios
        # resized to 224x224 in the range [-1, 1]. Bilinear and antialias resize
        # options are helpful to improve quality in some tasks.
        image = np.asarray(image)
        if image.ndim == 2:  # Convert image without last channel into greyscale.
            image = np.stack((image,)*3, axis=-1)
        image = image[..., :3]  # Remove alpha layer.
        assert image.shape[-1] == 3

        image = tf.constant(image)
        image = tf.image.resize(image, (self.image_resolution, self.image_resolution), method='bilinear', antialias=True)
        return image.numpy() / 127.5 - 1.0  # [0, 255]->[-1,1]

    def preprocess_tokens(self, prefix, suffix=None):
        # Model has been trained to handle tokenized text composed of a prefix with
        # full attention and a suffix with causal attention.
        separator = "\n"
        tokens = tokenizer.encode(prefix, add_bos=True) + tokenizer.encode(separator)
        mask_ar = [0] * len(tokens)    # 0 to use full attention for prefix.
        mask_loss = [0] * len(tokens)  # 0 to not use prefix tokens in the loss.

        if suffix:
            suffix = tokenizer.encode(suffix, add_eos=True)
            tokens += suffix
            mask_ar += [1] * len(suffix)    # 1 to use causal attention for suffix.
            mask_loss += [1] * len(suffix)  # 1 to use suffix tokens in the loss.

        mask_input = [1] * len(tokens)    # 1 if it's a token, 0 if padding.
        if self.seqlen:
            padding = [0] * max(0, self.seqlen - len(tokens))
            tokens = tokens[:self.seqlen] + padding
            mask_ar = mask_ar[:self.seqlen] + padding
            mask_loss = mask_loss[:self.seqlen] + padding
            mask_input = mask_input[:self.seqlen] + padding

        return jax.tree.map(np.array, (tokens, mask_ar, mask_loss, mask_input))

    def postprocess_tokens(tokens):
        tokens = tokens.tolist()  # np.array to list[int]
        try:  # Remove tokens at and after EOS if any.
            eos_pos = tokens.index(tokenizer.eos_id())
            tokens = tokens[:eos_pos]
        except ValueError:
            pass
        return tokenizer.decode(tokens)


    def get_dataset(self):
        pass


    def train_data_iterator(self):
        """Never ending iterator over training examples."""
        # Shuffle examples and repeat so one can train for many epochs.
        dataset = self.get_dataset()
        for example in dataset.as_numpy_iterator():
            image = Image.open(io.BytesIO(example["image"]))
            image = self.preprocess_image(image)

            prefix = "caption en"  # Could also be a different prefix per example.
            suffix = example["suffix"].decode().lower()
            tokens, mask_ar, mask_loss, _ = self.preprocess_tokens(prefix, suffix)

            yield {
                "image": np.asarray(image),
                "text": np.asarray(tokens),
                "mask_ar": np.asarray(mask_ar),
                "mask_loss": np.asarray(mask_loss),
            }