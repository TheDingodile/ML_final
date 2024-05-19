from src.execute_query import execute_sql
from src.experiment.post_processing import post_process_sql, post_process_answer
import pandas as pd
import json
from src.experiment.baseline import predict
import sqlite3

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


# print(len(train_data), len(valid_data))

# for i in range(20):
#     print(train_data[i]["question"])
#     print("   ")

print(train_data[0]["query"])
print(execute_sql(post_process_sql(train_data[0]["query"]), silver_db_path))
print(post_process_answer(train_answer[0]['answer']))

# valid_answer = predict(valid_data)
# print(valid_answer[:5])