import re
import sqlite3
import json
import os
import time
import numpy as np


table_path = 'mimic_iv/mimic_iv.sqlite'

def execute_sql(sql: str, db_path): # i altered this function to return true for func_vqa and remove tuple
        pattern = r'func_vqa\([^)]*\)'
        sql = re.sub(pattern, 'true', sql)
        con = sqlite3.connect(db_path)
        con.text_factory = lambda b: b.decode(errors="ignore")
        cur = con.cursor()
        result = cur.execute(sql).fetchall()
        for i in range(len(result)):
            if len(result[i]) == 1:
                result[i] = result[i][0]
        con.close()
        return result


def execute_sql_wrapper(key, sql, db_path, tag, skip_indicator='null'):
    assert tag in ['real', 'pred']
    if sql != skip_indicator:
        try:
            result = execute_sql(sql, db_path)
        except:
            if tag == 'pred':
                return (key, skip_indicator)
            result = 'error_'+tag
        result = process_answer(result)
        return (key, result)
    else:
        return (key, skip_indicator)

def execute_all(dict, tag):
    exec_result = {}
    for key in dict:
        sql = dict[key]
        exec_result[key] = execute_sql_wrapper(key, sql, table_path, tag)[-1]
    return exec_result

def process_answer(ans):
    if type(ans)==str:
        return ans
    else:
        return str(sorted([[process_item(c) for c in row] for row in ans])[:100]) # check only up to 100th record
    
def process_item(item):
    try:
        item = round(float(item),3)
    except:
        pass
    return str(item)