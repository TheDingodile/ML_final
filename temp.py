from src.execute_query import execute_sql
from src.experiment.post_processing import post_process_sql, post_process_answer
import pandas as pd
import json
from src.experiment.baseline import predict

silver_db_path = 'database/mimic_iv_cxr/silver/mimic_iv_cxr.db'

query_result = execute_sql("SELECT * FROM sqlite_master WHERE type='table'", silver_db_path)

print(pd.DataFrame(query_result))

with open('dataset/mimic_iv_cxr/train/train_data.json', 'r') as f:
    train_data = json.load(f) 

with open('dataset/mimic_iv_cxr/train/train_answer.json', 'r') as f:
    train_answer = json.load(f)

with open('dataset/mimic_iv_cxr/valid/valid_data.json', 'r') as f:
    valid_data = json.load(f)


print(len(train_data), len(valid_data))

example = train_data[2]

print(train_data[2])
print(execute_sql(post_process_sql(example['query']), silver_db_path))
print(post_process_answer(train_answer[2]['answer']))

valid_answer = predict(valid_data)
print(valid_answer[:5])