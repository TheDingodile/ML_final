from __future__ import annotations
from dtu import Parameters, dtu, GPU
import wandb
from time import time as seconds
import numpy as np
import functools
import torch
import json
from NeuralSQL.executor.nsql_executor import NeuralSQLExecutor
from NeuralSQL.executor.sqlglot.executor import Table
from NeuralSQL.execute_nsql import run_execution_for_gt_query





@dtu
class Defaults(Parameters):
    name: str = "local"
    instances: int = 1
    GPU: None | GPU = None
    time: int = 3600

    name: str = "local"
    vqa_module_type: str = "custom"


    def run(self, name: str, isServer: bool, vqa_module_type: str) -> None:

        if (isServer):
            wandb.init(project="ML_healthcare", name=name)
        start = seconds()

        if (isServer): images_path = "../../../../../../../work1/s183914/ml_healthcare/resized_ratio_short_side_768"
        else: images_path = "ehrxqa-2024-ml4h/resized_ratio_short_side_768"

        executor = NeuralSQLExecutor(
            "database/mimic_iv_cxr/silver",
            images_path,
            vqa_module_type=vqa_module_type,

        )
        with open("dataset/mimic_iv_cxr/train/train_data.json", "r") as f:
            gt_dataset = json.load(f)
            gt_dataset = gt_dataset[:500]

        with open("dataset/mimic_iv_cxr/train/train_answer.json", "r") as f:
            answers = json.load(f)
            answers = answers[:500]

        parsed_result_gt = {str(item["id"]): item["query"] for item in gt_dataset}
        parsed_result_answer = {str(item["id"]): item["answer"] for item in answers}

        executed_result = run_execution_for_gt_query(executor, parsed_result_gt)

        print("Executed result")
        print(executed_result)
        print("Answer result")
        print(parsed_result_answer)


        if (isServer): wandb.log({"accuracy": np.mean([1 if executed_result[key] == parsed_result_answer[key] else 0 for key in executed_result])})

Defaults.start()