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
    vqa_module_type: str = "yes"


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

        # with open("dataset/mimic_iv_cxr/train/train_data.json", "r") as f:
        #     gt_dataset = json.load(f)
        #     gt_dataset = gt_dataset

        # with open("dataset/mimic_iv_cxr/train/train_answer.json", "r") as f:
        #     answers = json.load(f)
        #     answers = answers

        # parsed_result_gt = {str(item["id"]): item["query"] for item in gt_dataset}
        # parsed_result_answer = {str(item["id"]): item["answer"] for item in answers}
        prediction_names = "predictions_LLM_1-0"
        with open(f"{prediction_names}.json", "r") as f:
            parsed_result_gt = json.load(f)
            parsed_result_gt = {str(key): parsed_result_gt[key] for key in list(parsed_result_gt.keys())}

        with open("dataset/mimic_iv_cxr/valid/valid_answer.json", "r") as f:
            answers = json.load(f)
            answers = answers
        parsed_result_answer = {str(item["id"]): item["answer"] for item in answers}
            



        executed_result = run_execution_for_gt_query(executor, parsed_result_gt, prediction_names)
        
        # with open("results/combined_results.json", "r") as f:
        #     executed_result = json.load(f)

        with open("dataset/mimic_iv_cxr/valid/valid_data.json", "r") as f:
            questions = json.load(f)
        parsed_questions = {str(item["id"]): item["question"] for item in questions}

        correct_count_text = 0
        wrong_count_text = 0
        correct_count_image = 0
        wrong_count_image = 0
        # print executed result and answers side by side
        for key in executed_result:
            answer = executed_result[key]
            truth = parsed_result_answer[key]
            if len(answer) != 1 or answer[0] == None or answer[0] == 0:
                answer = "null"

            if answer == "null":
                continue

            if "func_vqa" not in parsed_result_gt[key]:
                if answer == truth:
                    correct_count_text += 1
                else:
                    wrong_count_text += 1
                    print(answer, truth, key, parsed_questions[key])
            else:
                if answer == truth:
                    correct_count_image += 1
                else:
                    wrong_count_image += 1

        print("Correct count:", correct_count_text)
        print("Wrong count:", wrong_count_text)
        print("Correct count image:", correct_count_image)
        print("Wrong count image:", wrong_count_image)

        if (isServer): wandb.log({"accuracy": np.mean([1 if executed_result[key] == parsed_result_answer[key] else 0 for key in executed_result])})

Defaults.start()