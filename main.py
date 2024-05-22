from __future__ import annotations
from dtu import Parameters, dtu, GPU
import wandb
from time import time as seconds
import jax
import numpy as np



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
        from big_vision_test import big_vision_test, update_fn
        from vqa_dataset import VQA_Dataset
        import big_vision.utils

        start = seconds()
        if (isServer): predictor_function, tokenizer, trainable_mask = big_vision_test(isServer=isServer)
        else: predictor_function, tokenizer, trainable_mask = None, None, None
        dataset = VQA_Dataset(split="train", isServer=isServer, tokenizer=tokenizer)
        data_iterator = dataset.train_data_iterator()
        sched_fn = big_vision.utils.create_learning_rate_schedule(total_steps=steps+1, base=lr, decay_type="cosine", warmup_percent=0.10)

        if (isServer):
            wandb.init(project="ML_healthcare", name=name)

        for step in range(1, steps + 1):
            examples = [next(data_iterator) for _ in range(batch_size)]
            batch = jax.tree.map(lambda *x: np.stack(x), *examples)
            learning_rate = sched_fn(step)
            params, loss = update_fn(params, batch, learning_rate)
            loss = jax.device_get(loss)


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