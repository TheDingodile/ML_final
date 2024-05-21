from __future__ import annotations
from dtu import Parameters, dtu, GPU
from paligemma import run_test
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
        start = seconds()
        if (isServer):
            wandb.init(project="ML_healthcare", name=name)
        
        if (isServer): path = "../../../../../../../work1/s183914/ml_healthcare"
        else: path = "ehrxqa-2024-ml4h"
    
        for i in range(10):
            question_text, answer, result = next(run_test(path))

            if (isServer): wandb.log({"question": question_text, "answer": answer, "result": result})
            else: print(question_text, answer, result)



Defaults.start()