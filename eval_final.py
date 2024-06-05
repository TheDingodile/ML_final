import json
import time
import re

name = "temp.json"

# query_file_name = "predictions_LLM_1-0.json"
# file_name = "predictions_gt_vision1valid09-0"
# answer_file = "dataset/mimic_iv_cxr/valid/valid_answer.json"
# question_file = "dataset/mimic_iv_cxr/valid/valid_data.json"

query_file_name = "predictions_LLM_1-0_test.json"
file_name = "predictions_gt_vision3test09-0"
answer_file = "dataset/mimic_iv_cxr/valid/valid_answer.json"
question_file = "dataset/mimic_iv_cxr/test/test_data.json"




predictions_file_name = f"results/{file_name}.json"
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
wrong_img_idxs = []
wrong_img_question = []
wrong_img_query = []


file_to_submit = []

for key in executed_result:
    
    if "func_vqa" in parsed_result_gt[key]:
        img_questions += 1
    answer = executed_result[key]
    truth = parsed_result_answer[key]



    if len(answer) != 1 or answer[0] == None:
        answer = "null"
    if "true" in parsed_result_gt[key][-6:] and answer[0] == 0:
        answer = "null"
    if "true" in parsed_result_gt[key][-5:]:
        answer = "null"
    # check if query contains more than 1 func_vqa
    if parsed_result_gt[key].count("func_vqa") > 1:
        answer = "null"

    # Only for text based questions
    if "func_vqa" not in parsed_result_gt[key] and answer[0] == 0:
        answer = "null"
    if "order by count(*) desc" in parsed_result_gt[key]:
        answer = "null"



    # if "func_vqa" in parsed_result_gt[key] and "t1 where func_vqa(" not in parsed_result_gt[key]:
    #     print(parsed_questions[key])
    #     print(parsed_result_gt[key])
    #     print(" ")
    #     time.sleep(1)

    file_to_submit.append({"id": int(key), "answer": answer})
    if answer == "null":
        continue


    if "func_vqa" not in parsed_result_gt[key]:
        if answer == truth:
            correct_count_text += 1
        else:
            wrong_count_text += 1
    else:
        print(key, answer, truth)
        print(parsed_questions[key])
        print(parsed_result_gt[key])
        print(" ")
        if answer == truth:
            correct_count_image += 1
        else:
            wrong_count_image += 1
            wrong_img_idxs.append(key)
            wrong_img_question.append(parsed_questions[key])
            wrong_img_query.append(parsed_result_gt[key])

# save the file
# with open(name, "w") as f:
#     json.dump(file_to_submit, f)


print("Correct count:", correct_count_text)
print("Wrong count:", wrong_count_text)
print("Correct count image:", correct_count_image)
print("Wrong count image:", wrong_count_image)
print("Image questions:", img_questions)
# for i in range(len(wrong_img_idxs)):
#     print(wrong_img_idxs[i], wrong_img_question[i], wrong_img_query[i])
#     print("   ")