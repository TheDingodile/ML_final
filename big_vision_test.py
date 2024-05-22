import json
from PIL import Image
# import inference
# from inference.models.paligemma.paligemma import PaliGemma
import jax
import kagglehub
import os
import ml_collections
import sentencepiece
from big_vision.models.proj.paligemma import paligemma
# from big_vision_repo.big_vision.trainers.proj.paligemma import predict_fns
import functools
# os.environ["KAGGLE_USERNAME"] = 'thedingodile'
# os.environ["KAGGLE_KEY"] = 'c4990098f0d6b7470eaeb93faee607f0'
# pip3 install -q "overrides" "ml_collections" "einops~=0.7" "sentencepiece"

def big_vision_test():

    os.environ["KAGGLE_USERNAME"] = 'thedingodile'
    os.environ["KAGGLE_KEY"] = 'c4990098f0d6b7470eaeb93faee607f0'

    MODEL_PATH = kagglehub.model_download('google/paligemma/jax/paligemma-3b-pt-224', 'paligemma-3b-pt-224.f16.npz')
    print(MODEL_PATH)
    model_config = ml_collections.FrozenConfigDict({
        "llm": {"vocab_size": 257_152},
        "img": {"variant": "So400m/14", "pool_type": "none", "scan": True, "dtype_mm": "float16"}
    })

    model = paligemma.Model(**model_config)
    TOKENIZER_PATH = "./paligemma_tokenizer.model"
    tokenizer = sentencepiece.SentencePieceProcessor(TOKENIZER_PATH)

    # Load params - this can take up to 1 minute in T4 colabs.
    MODEL_PATH = "./paligemma-3b-pt-224.f16.npz"
    params = paligemma.load(None, MODEL_PATH, model_config)


    # # Define `decode` function to sample outputs from the model.
    # decode_fn = predict_fns.get_all(model)['decode']
    # decode = functools.partial(decode_fn, devices=jax.devices(), eos_token=tokenizer.eos_id())



