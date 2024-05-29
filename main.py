from __future__ import annotations
from dtu import Parameters, dtu, GPU
import wandb
from time import time as seconds
import jax
import numpy as np
import jax.numpy as jnp
import functools
import torch
import big_vision.utils as bv_utils




@dtu
class Defaults(Parameters):
    name: str = "local"
    instances: int = 1
    GPU: None | GPU = None
    time: int = 3600

    name: str = "local"
    lr: float = 0.03
    batch_size: int = 8
    steps: int = 1000


    def run(self, name: str, isServer: bool, lr: float, batch_size: int, steps: int) -> None:
        # from paligemma import run_test
        from big_vision_test import big_vision_test
        from vqa_dataset import VQA_Dataset
        import big_vision.utils

        if (isServer): path = "../../../../../../../work1/s183914/ml_healthcare/models"
        else: path = "ehrxqa-2024-ml4h"

        if (isServer):
            wandb.init(project="ML_healthcare", name=name)
        start = seconds()
        if (isServer): predictor_function, tokenizer, trainable_mask, params, model, save_func = big_vision_test(isServer=isServer)
        else: predictor_function, tokenizer, trainable_mask, params, model, save_func = None, None, None, None, None, None
        dataset = VQA_Dataset(split="train", isServer=isServer, tokenizer=tokenizer)
        data_iterator = dataset.train_data_iterator()
        eval_data_iterator = dataset.eval_data_iterator()
        sched_fn = big_vision.utils.create_learning_rate_schedule(total_steps=steps+1, base=lr, decay_type="cosine", warmup_percent=0.0)

        save_func(params, f"{path}/params_{name}.npz")
        params = bv_utils.load_checkpoint_np(f"{path}/params_{name}.npz")

        @functools.partial(jax.jit, donate_argnums=(0,))
        def update_fn(params, batch, learning_rate):
            imgs, txts, mask_ar = batch["image"], batch["text"], batch["mask_ar"]

            def loss_fn(params):
                text_logits, _ = model.apply({"params": params}, imgs, txts[:, :-1], mask_ar[:, :-1], train=True)
                logp = jax.nn.log_softmax(text_logits, axis=-1)
                mask_loss = batch["mask_loss"][:, 1:]
                targets = jax.nn.one_hot(txts[:, 1:], text_logits.shape[-1])
                token_pplx = jnp.sum(logp * targets, axis=-1)
                example_loss = -jnp.sum(token_pplx * mask_loss, axis=-1)
                example_loss /= jnp.clip(jnp.sum(mask_loss, -1), 1)
                return jnp.mean(example_loss)
            loss, grads = jax.value_and_grad(loss_fn)(params)

            # Apply gradients to trainable params using SGD.
            def apply_grad(param, gradient, trainable):
                if not trainable: return param
                return param - learning_rate * gradient

            params = jax.tree_util.tree_map(apply_grad, params, grads, trainable_mask)

            return params, loss
    

        for step in range(1, steps + 1):
            examples = [next(data_iterator) for _ in range(batch_size)]
            batch = jax.tree.map(lambda *x: np.stack(x), *examples)
            learning_rate = sched_fn(step)
            # params, batch, learning_rate, model, trainable_mask
            params, loss = update_fn(params, batch, learning_rate)
            loss = jax.device_get(loss)


            if step % 10 == 0:
                # evaluate the model
                examples = [next(eval_data_iterator) for _ in range(batch_size)]
                batch = jax.tree.map(lambda *x: np.stack(x), *examples)
                imgs, txts, mask_ar = batch["image"], batch["text"], batch["mask_ar"]
                mask_loss = batch["mask_loss"][:, 1:]
                text_logits, _ = model.apply({"params": params}, imgs, txts[:, :-1], mask_ar[:, :-1], train=True)
                logp = jax.nn.log_softmax(text_logits, axis=-1)

                probs = jnp.exp(logp)
                max_probs = jnp.max(probs, axis=-1)
                argmax_probs = jnp.argmax(probs, axis=-1)

                for threshold in [0.9, 0.75, 0.55]:
                    # 3276 is token yes
                    # 956 is token no

                    abstain_filter = mask_loss * (max_probs > threshold)
                    predicted_tokens = abstain_filter * argmax_probs
                    # make sure either yes or no is predicted, otherwise make abstain_filter all 0
                    predicted_tokens_contain_yes = jnp.sum(predicted_tokens == 3276, axis=-1) > 0
                    predicted_tokens_contain_no = jnp.sum(predicted_tokens == 956, axis=-1) > 0
                    abstain_filter *= (predicted_tokens_contain_yes | predicted_tokens_contain_no)[:, None]


                    answer_rate = jnp.sum((jnp.sum(abstain_filter, axis=-1) == jnp.sum(mask_loss, axis=-1))) / batch_size
                    abstain_rate = 1 - answer_rate 

                    wrong_predictions = (argmax_probs != txts[:, 1:]) * abstain_filter
                    accuracy = 1 - jnp.sum(wrong_predictions) / batch_size



                    if (isServer): wandb.log({f"accuracy_{threshold}": accuracy, f"abstain_rate_{threshold}": abstain_rate})
                    else: print(f"accuracy_{threshold}: {accuracy:.4f}   abstain_rate_{threshold}: {abstain_rate:.4f}")


            # predictions = predictor_function({"params": params}, batch=batch, max_decode_len=64, sampler="greedy")
            # label = batch["text"]

            if (isServer): wandb.log({"step": step, "lr": learning_rate, "loss": loss})
            else: print(f"step: {step}   lr: {learning_rate:.5f}   loss: {loss:.4f}")
        



        # if (isServer): path = "../../../../../../../work1/s183914/ml_healthcare"
        # else: path = "ehrxqa-2024-ml4h"


        # iterator = run_test(path)
        # for i in range(100):
        #     question_text, answer, result = next(iterator)

        #     if (isServer): wandb.log({"question": question_text, "answer": answer, "result": result})
        #     else: print(question_text, answer, result)



Defaults.start()