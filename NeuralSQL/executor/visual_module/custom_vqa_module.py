from .vqa_module import VQAModule
import big_vision.utils as bv_utils
import sentencepiece
import numpy as np
import tensorflow as tf
import jax.numpy as jnp
import jax
import functools


class CustomVQAModule(VQAModule):
    def __init__(self, model_path, tokenizer_path, file_name):
        self.model_path = "../../../../../../../work1/s183914/ml_healthcare/models/params_model_2-0.npz"
        self.tokenizer_path = "../../../../../../../work1/s183914/ml_healthcare/models/paligemma_tokenizer.model"
        self.file_name = file_name
        self.model = None
        self.tokenizer = None
        self.image_resolution = 224
        self.seqlen = 64

    def load_model(self):
        # Load the custom VQA model and tokenizer
        # Implement the logic to load the model and tokenizer from the provided paths
        # For example, using a deep learning framework like TensorFlow or PyTorch
        self.params = bv_utils.load_checkpoint_np(self.model_path) # check this
        self.tokenizer = sentencepiece.SentencePieceProcessor(self.tokenizer_path)

    def preprocess_input(self, images, questions):
        # Preprocess the input images and questions
        # Implement the logic to preprocess the images and tokenize the questions
        # For example, resizing images, normalizing pixel values, and converting questions to token IDs
        # preprocessed_images = ...
        # tokenized_questions = ...
        # tokens, mask_ar, mask_loss, _ = self.preprocess_tokens(prefix, suffix)
        tokens, mask_ar, mask_loss, mask_loss = self.preprocess_tokens(questions, None)
        return self.preprocess_image(images), np.asarray(tokens), np.asarray(mask_ar), np.asarray(mask_loss)

    def postprocess_output(self, raw_output):
        tokens = tokens.tolist()  # np.array to list[int]
        try:  # Remove tokens at and after EOS if any.
            eos_pos = tokens.index(self.tokenizer.eos_id())
            tokens = tokens[:eos_pos]
        except ValueError:
            pass
        return self.tokenizer.decode(tokens)

    def __call__(self, images, questions):
        # Load the model if not already loaded
        if self.model is None:
            self.load_model()

        if len(questions) > 1:
            return "null"
        print("1")
        preprocessed_images, tokenized_questions, mask_ar, mask_loss = self.preprocess_input(images, questions)
        mask_loss = mask_loss[:, 1:]
        print("2")
        

        # Run the model inference
        text_logits, _ = self.model.apply({"params": self.params}, preprocessed_images, tokenized_questions[:, :-1], mask_ar[:, :-1], train=False)
        raw_output = self.model(preprocessed_images, tokenized_questions)
        print("3")

        logp = jax.nn.log_softmax(text_logits, axis=-1)
        probs = jnp.exp(logp)
        max_probs = jnp.max(probs, axis=-1)
        argmax_probs = jnp.argmax(probs, axis=-1)
        threshold = 0.8
        abstain_filter = mask_loss * (max_probs > threshold)
        predicted_tokens = abstain_filter * argmax_probs
        print("4")

        if max_probs < threshold:
            raw_output = "null"
        elif not jnp.sum(predicted_tokens == 3276, axis=-1) > 0 or not jnp.sum(predicted_tokens == 956, axis=-1) > 0:
            raw_output = "null"

        # Postprocess the raw output to get the final answers
        answers = self.postprocess_output(raw_output)
        print("5")

        return answers
    
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
        tokens = self.tokenizer.encode(prefix, add_bos=True) + self.tokenizer.encode(separator)
        mask_ar = [0] * len(tokens)    # 0 to use full attention for prefix.
        mask_loss = [0] * len(tokens)  # 0 to not use prefix tokens in the loss.

        if suffix:
            suffix = self.tokenizer.encode(suffix, add_eos=True)
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

        # print(tokens)

        return jax.tree.map(np.array, (tokens, mask_ar, mask_loss, mask_input))
