import json

prediction_files = json.load(open("ensemble_predictions.json", "r"))
filter = json.load(open("results/predictions_gt_test_set09_fix-0.json", "r"))
query_file_name = "predictions_LLM_1-0_test.json"

with open(query_file_name, "r") as f:
    parsed_result_gt = json.load(f)
    parsed_result_gt = {str(key): parsed_result_gt[key] for key in list(parsed_result_gt.keys())}


# predict "null" if not all models agree, otherwise predict the answer
combined_predictions = []

for i in range(len(prediction_files)):
    if "func_vqa" in parsed_result_gt[str(i)] and not "true" in parsed_result_gt[str(i)][-6:]:
        if prediction_files[i]["answer"] != filter[str(i)]:
            # print(filter[str(i)])
            combined_predictions.append({"id": i, "answer": "null"})
        else:
            combined_predictions.append({"id": i, "answer": prediction_files[i]["answer"]})
    else:
        combined_predictions.append({"id": i, "answer": prediction_files[i]["answer"]})

img_questions = 0
for i, pred in enumerate(combined_predictions):
    if "func_vqa" in parsed_result_gt[str(i)]:
        # print(combined_predictions[i]["answer"])
        if pred["answer"] != "null":
            img_questions += 1
print(img_questions)
    




with open("filtered_predictions.json", "w") as f:
    json.dump(combined_predictions, f)

