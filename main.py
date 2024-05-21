from __future__ import annotations
from dtu import Parameters, dtu, GPU
import wandb
from time import time as seconds



@dtu
class Defaults(Parameters):
    name: str = "local"
    instances: int = 1
    GPU: None | GPU = None
    time: int = 3600

    name: str = "local"

    def run(self, name: str, isServer: bool) -> None:
        from paligemma import run_test
        start = seconds()
        if (isServer):
            wandb.init(project="ML_healthcare", name=name)
        
        if (isServer): path = "../../../../../../../work1/s183914/ml_healthcare"
        else: path = "ehrxqa-2024-ml4h"

        iterator = run_test(path)
        for i in range(100):
            question_text, answer, result = next(iterator)

            if (isServer): wandb.log({"question": question_text, "answer": answer, "result": result})
            else: print(question_text, answer, result)



Defaults.start()