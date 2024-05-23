from src.execute_query import execute_sql
from src.experiment.post_processing import post_process_sql, post_process_answer
import pandas as pd
import json
from src.experiment.baseline import predict
import sqlite3
from datetime import datetime

def is_datetime(string):
    """Check if the string can be converted to a datetime."""
    try:
        datetime.fromisoformat(string)
        return True
    except ValueError:
        return False
    

def is_number(string):
    """Check if the string represents a number."""
    try:
        float(string)
        return True
    except ValueError:
        return False
    

def filter_list(a):
    """Filter the list 'a' to contain only non-datetime, non-number strings and ensure it has at least one element."""
    filtered = [item for item in a if isinstance(item, str) and not is_datetime(item) and not is_number(item)]
    
    # Return the filtered list if it has at least one element, otherwise return an empty list
    return filtered if len(filtered) > 0 else []

silver_db_path = 'database/mimic_iv_cxr/silver/mimic_iv_cxr.db'

query_result = execute_sql("SELECT * FROM sqlite_master WHERE type='table'", silver_db_path)

# print(pd.DataFrame(query_result))

conn = sqlite3.connect(silver_db_path)
temper = pd.read_sql_query("SELECT * FROM TB_CXR;", conn)
# find where temper subject_id is 18679317
# print(temper[temper['subject_id'] == 18679317])

with open('dataset/mimic_iv_cxr/train/train_data.json', 'r') as f:
    train_data = json.load(f) 

with open('dataset/mimic_iv_cxr/train/train_answer.json', 'r') as f:
    train_answer = json.load(f)

with open('dataset/mimic_iv_cxr/valid/valid_data.json', 'r') as f:
    valid_data = json.load(f)


print(len(train_data), len(valid_data))

for i in range(20):
    print(train_data[i]["question"])
    print("   ")

# all_possible_answers = set()
# for i in range(1000):
#     # print(train_data[i]["question"])
#     # print(train_data[0]["query"])
#     # print(execute_sql(post_process_sql(train_data[i]["query"]), silver_db_path))
#     ans = post_process_answer(train_answer[i]['answer'])
#     # print(ans)
#     filtered_ans = filter_list(ans)
#     if len(filtered_ans) > 0:
#         # add all elements in filtered_ans to all_possible_answers
#         all_possible_answers.update(filtered_ans)

# all_possible_answers = list(all_possible_answers)


# # print(len(all_possible_answers), all_possible_answers)

# dummy_predictions = []
# for d in valid_data:
#     dummy_predictions.append({"id": d["id"], "answer": all_possible_answers})
# print(len(dummy_predictions))

# # save all_possible_answers to a json file
# with open('all_possible_answers.json', 'w') as f:
#     json.dump(all_possible_answers, f)

# # save dummy_predictions to a json file

# with open('dummy_predictions.json', 'w') as f:
#     json.dump(dummy_predictions, f)

# dummy_predictions2 = []

# for d in valid_data:
#     dummy_predictions2.append({"id": d["id"], "answer": [0]})

# with open('dummy_predictions2.json', 'w') as f:
#     json.dump(dummy_predictions2, f)

