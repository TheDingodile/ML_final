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
from big_vision.trainers.proj.paligemma import predict_fns
import big_vision.datasets.jsonl
import big_vision.utils
import big_vision.sharding
import functools
import warnings
import jax.numpy as jnp


def big_vision_test(isServer: bool):

    # os.environ["KAGGLE_USERNAME"] = 'thedingodile'
    # os.environ["KAGGLE_KEY"] = 'c4990098f0d6b7470eaeb93faee607f0'

    # MODEL_PATH = kagglehub.model_download('google/paligemma/jax/paligemma-3b-pt-224', 'paligemma-3b-pt-224.f16.npz')
    # print(MODEL_PATH)

    model_config = ml_collections.FrozenConfigDict({
        "llm": {"vocab_size": 257_152},
        "img": {"variant": "So400m/14", "pool_type": "none", "scan": True, "dtype_mm": "float16"}
    })

    model = paligemma.Model(**model_config)
    if not (isServer): TOKENIZER_PATH = "./models/paligemma_tokenizer.model"
    else: TOKENIZER_PATH = "../../../../../../../work1/s183914/ml_healthcare/models/paligemma_tokenizer.model"
    tokenizer = sentencepiece.SentencePieceProcessor(TOKENIZER_PATH)

    # Load params - this can take up to 1 minute in T4 colabs.
    if not (isServer): MODEL_PATH = "./models/paligemma-3b-pt-224.f16.npz"
    else: MODEL_PATH = "../../../../../../../work1/s183914/ml_healthcare/models/paligemma-3b-pt-224.f16.npz"
    params = paligemma.load(None, MODEL_PATH, model_config)


    # Define `decode` function to sample outputs from the model.
    decode_fn = predict_fns.get_all(model)['decode']
    decode = functools.partial(decode_fn, devices=jax.devices(), eos_token=tokenizer.eos_id())

    # Create a pytree mask of the trainable params.
    def is_trainable_param(name, param):  # pylint: disable=unused-argument
        if name.startswith("llm/layers/attn/"):  return True
        if name.startswith("llm/"):              return False
        if name.startswith("img/"):              return False
        raise ValueError(f"Unexpected param name {name}")
    trainable_mask = big_vision.utils.tree_map_with_names(is_trainable_param, params)

    # If more than one device is available (e.g. multiple GPUs) the parameters can
    # be sharded across them to reduce HBM usage per device.
    mesh = jax.sharding.Mesh(jax.devices(), ("data"))

    data_sharding = jax.sharding.NamedSharding(
        mesh, jax.sharding.PartitionSpec("data"))

    params_sharding = big_vision.sharding.infer_sharding(
        params, strategy=[('.*', 'fsdp(axis="data")')], mesh=mesh)

    # Yes: Some donated buffers are not usable.
    warnings.filterwarnings(
        "ignore", message="Some donated buffers were not usable")

    @functools.partial(jax.jit, donate_argnums=(0,), static_argnums=(1,))
    def maybe_cast_to_f32(params, trainable):
        return jax.tree.map(lambda p, m: p.astype(jnp.float32) if m else p,
                            params, trainable)

    # Loading all params in simultaneous - albeit much faster and more succinct -
    # requires more RAM than the T4 colab runtimes have by default.
    # Instead we do it param by param.
    params, treedef = jax.tree.flatten(params)
    sharding_leaves = jax.tree.leaves(params_sharding)
    trainable_leaves = jax.tree.leaves(trainable_mask)
    for idx, (sharding, trainable) in enumerate(zip(sharding_leaves, trainable_leaves)):
        params[idx] = big_vision.utils.reshard(params[idx], sharding)
        params[idx] = maybe_cast_to_f32(params[idx], trainable)
        params[idx].block_until_ready()
    params = jax.tree.unflatten(treedef, params)

    # Print params to show what the model is made of.
    def parameter_overview(params):
        for path, arr in big_vision.utils.tree_flatten_with_names(params)[0]:
            print(f"{path:80s} {str(arr.shape):22s} {arr.dtype}")

    # print(" == Model params == ")
    # parameter_overview(params)
    return decode, tokenizer, trainable_mask, params



@functools.partial(jax.jit, donate_argnums=(0,))
def update_fn(params, batch, learning_rate, model, trainable_mask):
  imgs, txts, mask_ar = batch["image"], batch["text"], batch["mask_ar"]

  def loss_fn(params):
    text_logits, _ = model.apply({"params": params}, imgs, txts[:, :-1], mask_ar[:, :-1], train=True)
    logp = jax.nn.log_softmax(text_logits, axis=-1)

    # The model takes as input txts[:, :-1] but the loss is defined as predicting
    # next tokens txts[:, 1:]. Additionally, mask_loss[:, 1:] indicates which tokens
    # are part of the loss (e.g. prefix and padded tokens are not included).
    mask_loss = batch["mask_loss"][:, 1:]
    targets = jax.nn.one_hot(txts[:, 1:], text_logits.shape[-1])

    # Compute the loss per example. i.e. the mean of per token pplx.
    # Since each example has a different number of tokens we normalize it.
    token_pplx = jnp.sum(logp * targets, axis=-1)  # sum across vocab_size.
    example_loss = -jnp.sum(token_pplx * mask_loss, axis=-1)  # sum across seq_len.
    example_loss /= jnp.clip(jnp.sum(mask_loss, -1), 1)  # weight by num of tokens.

    # batch_loss: mean of per example loss.
    return jnp.mean(example_loss)

  loss, grads = jax.value_and_grad(loss_fn)(params)

  # Apply gradients to trainable params using SGD.
  def apply_grad(param, gradient, trainable):
    if not trainable: return param
    return param - learning_rate * gradient

  params = jax.tree_util.tree_map(apply_grad, params, grads, trainable_mask)

  return params, loss
