import os
import re
import json

# custom package
from executor.nsql_executor import NeuralSQLExecutor
from executor.sqlglot.executor import Table


def post_process_sql(query):
    current_time = "2105-12-31 23:59:00"
    precomputed_dict = {
        "temperature": (35.5, 38.1),
        "sao2": (95.0, 100.0),
        "heart rate": (60.0, 100.0),
        "respiration": (12.0, 18.0),
        "systolic bp": (90.0, 120.0),
        "diastolic bp": (60.0, 90.0),
        "mean bp": (60.0, 110.0),
    }

    # Handle current_time
    query = query.replace("current_time", f"'{current_time}'")

    # Handle vital signs
    vital_lower_match = re.search("[ \n]+([a-zA-Z0-9_]+_lower)", query)
    vital_upper_match = re.search("[ \n]+([a-zA-Z0-9_]+_upper)", query)

    if vital_lower_match and vital_upper_match:
        vital_lower_expr = vital_lower_match.group(1)
        vital_upper_expr = vital_upper_match.group(1)
        vital_name_list = list(set(re.findall("([a-zA-Z0-9_]+)_lower", vital_lower_expr) + re.findall("([a-zA-Z0-9_]+)_upper", vital_upper_expr)))

        if len(vital_name_list) == 1:
            processed_vital_name = vital_name_list[0].replace("_", " ")
            if processed_vital_name in precomputed_dict:
                vital_range = precomputed_dict[processed_vital_name]
                query = query.replace(vital_lower_expr, str(vital_range[0])).replace(vital_upper_expr, str(vital_range[1]))

    # Handle etc.
    query = query.replace("''", "'").replace("< =", "<=")
    query = query.replace("%y", "%Y").replace("%j", "%J")
    query = query.replace("'", "'").replace("'", "'")
    query = query.replace("\u201c", '"').replace("\u201d", '"')

    return query


def post_process_answer(answer, round_digit=6, sorted_answer=False):
    assert isinstance(answer, list) or answer == "null"

    if answer == "null":
        return answer

    if not answer:
        assert answer == []
        return answer

    # Tuple data preprocessing
    if isinstance(answer[0], tuple):
        assert len(answer[0]) == 1  # NOTE: currently, only support single column output
        answer = [ans[0] for ans in answer]  # unpack tuple

    if isinstance(answer[0], float):
        # Float-type answer
        answer = [round(ans, round_digit) for ans in answer]  # round to specified digit
    elif isinstance(answer[0], str):
        # String-type answer
        if sorted_answer:
            answer = sorted(answer)

    return answer



def run_execution_for_gt_query(executor, parsed_result):
    executed_result = {}
    for idx, query in enumerate(parsed_result.values()):
        query = post_process_sql(query)
        try:
            result = executor.execute_nsql(query)
            if isinstance(result, Table):
                result = result.rows
            result = post_process_answer(result)
        except Exception as e:
            # raise
            # print(f"Error executing query {idx}: {e}")
            result = "null"  # NOTE: For NeuralSQL, we will abstain as "null" if the query execution fails
        executed_result[str(idx)] = result
        with open(os.path.join("results", "predictions_gt.json"), "w") as f:
            json.dump(executed_result, f, indent=4)
    return executed_result

# executor = NeuralSQLExecutor(
#     "database/mimic_iv_cxr/silver",
#     "ehrxqa-2024-ml4h/resized_ratio_short_side_768",
#     vqa_module_type="yes",

# )
# with open("dataset/mimic_iv_cxr/train/train_data.json", "r") as f:
#     gt_dataset = json.load(f)

# with open("dataset/mimic_iv_cxr/train/train_answer.json", "r") as f:
#     answers = json.load(f)

# gt_dataset = gt_dataset[:100]

# # for i in range(len(gt_dataset)):
# #     print(gt_dataset[i]["question"])

# parsed_result_gt = {str(item["id"]): item["query"] for item in gt_dataset}
# executed_result = run_execution_for_gt_query(executor, parsed_result_gt)
