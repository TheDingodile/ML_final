import json

answer_files = ["predictions_gt_predictions_LLM_0-0.json", 
                "predictions_gt_predictions_LLM_1-0.json",
                ]

all_answer_files = []

for answer_file in answer_files:
    with open(f"results/{answer_file}", "r") as f:
        executed_result = json.load(f)
        all_answer_files.append(executed_result)

# loop through all keys in executed_result
combined_results = {}

for key in all_answer_files[0]:
    # check if all answers are the same for this key
    all_same = True
    for answer_file in all_answer_files:
        if answer_file[key] != all_answer_files[0][key]:
            all_same = False
            break
    if all_same:
        combined_results[key] = all_answer_files[0][key]
    else:
        combined_results[key] = "null"

# write combined results to file
with open("results/combined_results.json", "w") as f:
    json.dump(combined_results, f)