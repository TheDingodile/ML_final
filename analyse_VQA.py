import json

with open('results/predictions_gt.json', 'r') as f:
    gt = json.load(f)

with open('dataset/mimic_iv_cxr/train/train_answer.json', 'r') as f:
    train_answer = json.load(f)

with open('dataset/mimic_iv_cxr/train/train_data.json', 'r') as f:
    train_data = json.load(f)

# print(train_answer)

for i in range(100):
    # check if func_vqa in train_data[i]['question'], only print if it is
    if "func_vqa" in train_data[i]['query']:
        # print(train_data[i]['question'])
        print(gt[str(i)], train_answer[i]['answer'])