import json

query_file_name = "predictions_LLM_1-0.json"
predictions_file_name = "results/predictions_gt_predictions_LLM_1-0.json"

answer_file = "dataset/mimic_iv_cxr/valid/valid_answer.json"
question_file = "dataset/mimic_iv_cxr/valid/valid_data.json"

with open(query_file_name, "r") as f:
    parsed_result_gt = json.load(f)
    parsed_result_gt = {str(key): parsed_result_gt[key] for key in list(parsed_result_gt.keys())}

with open(predictions_file_name, "r") as f:
    executed_result = json.load(f)
    executed_result = {str(key): executed_result[key] for key in list(executed_result.keys())}

with open(answer_file, "r") as f:
    answers = json.load(f)
    answers = answers
parsed_result_answer = {str(item["id"]): item["answer"] for item in answers}

with open(question_file, "r") as f:
    questions = json.load(f)
parsed_questions = {str(item["id"]): item["question"] for item in questions}




correct_count_text = 0
wrong_count_text = 0
img_questions = 0
correct_count_image = 0
wrong_count_image = 0
# print executed result and answers side by side
for key in executed_result:
    
    if "func_vqa" in parsed_result_gt[key]:
        img_questions += 1
    answer = executed_result[key]
    truth = parsed_result_answer[key]
    # print(answer, truth, key, parsed_questions[key])

    if len(answer) != 1 or answer[0] == None:# or answer[0] == 0:
        answer = "null"

    if answer == "null":
        continue
    if "func_vqa" not in parsed_result_gt[key]:
        if answer == truth:
            correct_count_text += 1
        else:
            wrong_count_text += 1
    else:
        if answer == truth:
            correct_count_image += 1
        else:
            wrong_count_image += 1
            # print(answer, truth, key, parsed_questions[key])

print("Correct count:", correct_count_text)
print("Wrong count:", wrong_count_text)
print("Correct count image:", correct_count_image)
print("Wrong count image:", wrong_count_image)
print("Image questions:", img_questions)