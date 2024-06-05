import json

prediction_files = ["submission_vision1_09.json", "submission_vision3_09.json"]

parsed_results = [json.load(open(prediction_file, "r")) for prediction_file in prediction_files]


# predict "null" if not all models agree, otherwise predict the answer
combined_predictions = []

for i in range(len(parsed_results[0])):
    if parsed_results[0][i] == parsed_results[1][i]:
        combined_predictions.append({"id": i, "answer": parsed_results[0][i]["answer"]})
    else:
        combined_predictions.append({"id": i, "answer": "null"})

with open("ensemble_predictions.json", "w") as f:
    json.dump(combined_predictions, f)

# count amount of "null" predictions for first model

null_predictions = 0

for prediction in parsed_results[1]:
    if prediction["answer"] == "null":
        null_predictions += 1
print(f"Amount of 'null' predictions for first model: {null_predictions}")