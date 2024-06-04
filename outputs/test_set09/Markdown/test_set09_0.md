2024-06-04 16:56:23.488150: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.17.0
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_final/ML_final/wandb/run-20240604_165627-f8m6a2zy
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run test_set09-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/f8m6a2zy
2024-06-04 16:56:44.996577: W tensorflow/core/common_runtime/gpu/gpu_device.cc:2251] Cannot dlopen some GPU libraries. Please make sure the missing libraries mentioned above are installed properly if you would like to use GPU. Follow the guide at https://www.tensorflow.org/install/gpu for how to download and setup the required libraries for your platform.
Skipping registering GPU devices...
2024-06-04 16:56:45.678384: W external/xla/xla/service/gpu/nvptx_compiler.cc:760] The NVIDIA driver's CUDA version is 12.4 which is older than the ptxas CUDA version (12.5.40). Because the driver is older than the ptxas version, XLA is disabling parallel compilation, which may slow down compilation. You should update your NVIDIA driver or use the NVIDIA-provided CUDA forward compatibility packages.

Aborted!

<style>
c { color: #9cdcfe; font-family: 'Verdana', sans-serif;} /* VARIABLE */
d { color: #4EC9B0; font-family: 'Verdana', sans-serif;} /* CLASS */
e { color: #569cd6; font-family: 'Verdana', sans-serif;} /* BOOL */
f { color: #b5cea8; font-family: 'Verdana', sans-serif;} /* NUMBERS */
j { color: #ce9178; font-family: 'Verdana', sans-serif;} /* STRING */
k { font-family: 'Verdana', sans-serif;} /* SYMBOLS */
</style>

# Parameters

| PARAMETER         | TYPE              | VALUE             |
|-------------------|-------------------|-------------------|
| <c>name</c>       | <d>str</d>        | <j>"test_set09-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>3600</f>       |
| <c>vqa_module_type</c>| <d>str</d>        | <j>"custom"</j>   |
| <c>prediction_file_name</c>| <d>str</d>        | <j>"predictions_LLM_1-0_test"</j> |
| <c>threshold</c>  | <d>float</d>      | <f>0.9</f>        |
| <c>table_path</c> | <d>str</d>        | <j>"database/mimic_iv_cxr/gold"</j> |

# Output

```
sid_to_ipath_map loaded. (1616 entries)
Error executing query 1: Model only answers one image question SQLs
Error executing query 2: Model only answers one image question SQLs
Error executing query 3: Invalid expression / Unexpected token. Line 1, Col: 926.
  x-ray show any abnormality in the right atrium?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4: Model only answers one image question SQLs
Error executing query 5: Model only answers one image question SQLs
Error executing query 6: Model abstains from answering the question
Error executing query 9: Model only answers one image question SQLs
Error executing query 10: Invalid expression / Unexpected token. Line 1, Col: 618.
  _vqa("is a chest x-ray showing any abnormality?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 11: Expecting ). Line 1, Col: 827.
  etime('2105-12-31 23:59:00','-4 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 5
Error executing query 12: Model abstains from answering the question
Error executing query 14: Model abstains from answering the question
Error executing query 16: Model abstains from answering the question
Error executing query 18: Model only answers one image question SQLs
Error executing query 19: Invalid expression / Unexpected token. Line 1, Col: 719.
  func_vqa("is a chest x-ray showing any devices?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 20: Model abstains from answering the question
Error executing query 21: Model abstains from answering the question
Error executing query 22: Invalid expression / Unexpected token. Line 1, Col: 874.
  normality in the right atrium on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 23: Model abstains from answering the question
Error executing query 24: Invalid expression / Unexpected token. Line 1, Col: 990.
  .dischtime is not null order by admissions.admittime desc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 25: Invalid expression / Unexpected token. Line 1, Col: 622.
  ns.hadm_id from admissions where admissions.subject_id = 19457288 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 26: Model abstains from answering the question
Error executing query 27: Invalid expression / Unexpected token. Line 1, Col: 765.
  a("does a chest x-ray indicate any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 28: Invalid expression / Unexpected token. Line 1, Col: 851.
  x-ray reveal any abnormality in the right lung?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 29: Model abstains from answering the question
Error executing query 31: Invalid expression / Unexpected token. Line 1, Col: 790.
  criptions.starttime) >= datetime('2105-12-31 23:59:00','-40 month') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 32: Model only answers one image question SQLs
Error executing query 34: Invalid expression / Unexpected token. Line 1, Col: 981.
  e('%m',prescriptions.starttime) = '10' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of day') = datetime(t2.starttime,'start of day')
Error executing query 35: Model abstains from answering the question
Error executing query 36: Model abstains from answering the question
Error executing query 38: Model abstains from answering the question
Error executing query 39: Expecting ). Line 1, Col: 859.
  me('%Y',labevents.charttime) >= '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.itemid ) as t3 where t3.c1 = 3 )
Error executing query 40: Model only answers one image question SQLs
Error executing query 41: Model abstains from answering the question
Error executing query 42: Model only answers one image question SQLs
Error executing query 43: Model abstains from answering the question
Error executing query 44: Model abstains from answering the question
Error executing query 45: Invalid expression / Unexpected token. Line 1, Col: 946.
  cardiac pacer and wires in the left chest wall?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 47: Invalid expression / Unexpected token. Line 1, Col: 865.
   x-ray indicate any tubes/lines in the abdomen?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 49: Model only answers one image question SQLs
[False]
Error executing query 50: Model abstains from answering the question
Error executing query 51: Model abstains from answering the question
Error executing query 52: Invalid expression / Unexpected token. Line 1, Col: 784.
  escriptions.starttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 53: Model abstains from answering the question
Error executing query 55: Model abstains from answering the question
Error executing query 57: Model only answers one image question SQLs
Error executing query 59: Invalid expression / Unexpected token. Line 1, Col: 761.
  s a chest x-ray show any technical assessments?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 61: Model abstains from answering the question
Error executing query 62: Invalid expression / Unexpected token. Line 1, Col: 741.
  id = 18182458 ) and strftime('%Y',prescriptions.starttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 63: Invalid expression / Unexpected token. Line 1, Col: 953.
  ny abnormality in the right costophrenic angle?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 64: Model only answers one image question SQLs
Error executing query 66: Model abstains from answering the question
Error executing query 67: Model abstains from answering the question
Error executing query 68: Expecting ). Line 1, Col: 808.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 69: Model abstains from answering the question
Error executing query 71: Model only answers one image question SQLs
Error executing query 72: Model abstains from answering the question
Error executing query 73: Model only answers one image question SQLs
Error executing query 74: Model only answers one image question SQLs
Error executing query 75: Model abstains from answering the question
Error executing query 78: Model abstains from answering the question
Error executing query 79: Invalid expression / Unexpected token. Line 1, Col: 763.
  ',prescriptions.starttime) = '2105-07' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of day') = datetime(t2.starttime,'start of day')
Error executing query 80: near "(": syntax error
Error executing query 81: Model only answers one image question SQLs
Error executing query 84: Model abstains from answering the question
Error executing query 85: Model only answers one image question SQLs
Error executing query 87: Model only answers one image question SQLs
Error executing query 88: Model abstains from answering the question
Error executing query 90: Invalid expression / Unexpected token. Line 1, Col: 768.
  w any technical assessments in the mediastinum?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 92: Model only answers one image question SQLs
Error executing query 93: Invalid expression / Unexpected token. Line 1, Col: 1112.
  year','-1 year') and strftime('%m',procedures_icd.charttime) = '11' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t
Error executing query 94: Model abstains from answering the question
Error executing query 95: near "(": syntax error
Error executing query 98: Model only answers one image question SQLs
Error executing query 101: Model only answers one image question SQLs
Error executing query 103: Expecting ). Line 1, Col: 976.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
[False]
Error executing query 105: Model abstains from answering the question
Error executing query 108: Invalid expression / Unexpected token. Line 1, Col: 771.
  6526693 ) and strftime('%Y-%m',prescriptions.starttime) = '2102-02' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 110: Expecting ). Line 1, Col: 1039.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 111: Model only answers one image question SQLs
Error executing query 112: Model only answers one image question SQLs
Error executing query 114: Model only answers one image question SQLs
Error executing query 118: Model abstains from answering the question
Error executing query 119: Model abstains from answering the question
Error executing query 120: Model abstains from answering the question
Error executing query 121: Model abstains from answering the question
Error executing query 122: Expecting ). Line 1, Col: 950.
  %Y',prescriptions.starttime) >= '2103' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 4
Error executing query 123: Model only answers one image question SQLs
Error executing query 124: Model abstains from answering the question
Error executing query 125: Model abstains from answering the question
Error executing query 126: Model abstains from answering the question
Error executing query 127: Model only answers one image question SQLs
Error executing query 128: Model abstains from answering the question
Error executing query 130: Model abstains from answering the question
Error executing query 132: Model only answers one image question SQLs
Error executing query 133: Error tokenizing 't1.studydatetime) and datetime(t1.studydatetime,'
Error executing query 137: Model only answers one image question SQLs
Error executing query 139: Invalid expression / Unexpected token. Line 1, Col: 847.
   chest x-ray depicts any technical assessments?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 140: Invalid expression / Unexpected token. Line 1, Col: 1117.
  ecting infiltration in the right mid lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and date
Error executing query 142: Model abstains from answering the question
Error executing query 143: Invalid expression / Unexpected token. Line 1, Col: 890.
  omical findings in the left costophrenic angle?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 144: Model only answers one image question SQLs
Error executing query 145: Model abstains from answering the question
Error executing query 147: Invalid expression / Unexpected token. Line 1, Col: 731.
  _vqa("is a chest x-ray showing any abnormality?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 148: Model only answers one image question SQLs
Error executing query 153: Model abstains from answering the question
Error executing query 154: Model only answers one image question SQLs
Error executing query 155: Model only answers one image question SQLs
Error executing query 156: Model abstains from answering the question
Error executing query 158: Invalid expression / Unexpected token. Line 1, Col: 915.
  160511 ) and strftime('%Y-%m',procedures_icd.charttime) = '2105-11' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 159: Model abstains from answering the question
Error executing query 162: Model only answers one image question SQLs
Error executing query 163: Model abstains from answering the question
Error executing query 164: Invalid expression / Unexpected token. Line 1, Col: 895.
  vated hemidiaphragm in the right hemidiaphragm?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 167: Model abstains from answering the question
Error executing query 168: Model only answers one image question SQLs
Error executing query 169: Model abstains from answering the question
Error executing query 170: Model abstains from answering the question
Error executing query 173: Model abstains from answering the question
Error executing query 174: Model abstains from answering the question
Error executing query 175: Model abstains from answering the question
Error executing query 176: Invalid expression / Unexpected token. Line 1, Col: 852.
  as t2 where func_vqa("is enteric tube revealed?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 180: Model abstains from answering the question
Error executing query 181: Model abstains from answering the question
Error executing query 184: Model only answers one image question SQLs
Error executing query 185: Invalid expression / Unexpected token. Line 1, Col: 943.
  cedures_icd.charttime) = datetime('2105-12-31 23:59:00','-6 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 186: Expecting ). Line 1, Col: 841.
  %Y',prescriptions.starttime) >= '2100' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 189: Model only answers one image question SQLs
Error executing query 190: Model abstains from answering the question
Error executing query 191: Model abstains from answering the question
Error executing query 193: Invalid expression / Unexpected token. Line 1, Col: 624.
  ns.hadm_id from admissions where admissions.subject_id = 19371747 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 194: Model only answers one image question SQLs
Error executing query 195: Invalid expression / Unexpected token. Line 1, Col: 742.
  3336663 ) and strftime('%Y-%m',prescriptions.starttime) = '2105-11' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 196: Invalid expression / Unexpected token. Line 1, Col: 1006.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id
Error executing query 198: Invalid expression / Unexpected token. Line 1, Col: 1003.
  st x-ray shown any diseases in the mediastinum?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 199: Model abstains from answering the question
Error executing query 200: Model abstains from answering the question
Error executing query 201: Model abstains from answering the question
Error executing query 202: Invalid expression / Unexpected token. Line 1, Col: 853.
  ("is the chest x-ray depicting any tubes/lines?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 203: Invalid expression / Unexpected token. Line 1, Col: 664.
  ty in the cavoatrial junction on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 204: Model abstains from answering the question
Error executing query 205: Model only answers one image question SQLs
Error executing query 206: Model abstains from answering the question
Error executing query 208: Invalid expression / Unexpected token. Line 1, Col: 944.
  edures_icd.charttime) >= datetime('2105-12-31 23:59:00','-9 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 209: Invalid expression / Unexpected token. Line 1, Col: 823.
  eration of rectum and sphincter ani' ) ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id
Error executing query 210: Model abstains from answering the question
Error executing query 211: Model abstains from answering the question
Error executing query 212: Model abstains from answering the question
Error executing query 214: Model abstains from answering the question
Error executing query 215: Invalid expression / Unexpected token. Line 1, Col: 737.
  650925 ) and strftime('%Y-%m',prescriptions.starttime) >= '2103-02' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 216: Model abstains from answering the question
Error executing query 217: Invalid expression / Unexpected token. Line 1, Col: 987.
   year') = datetime('2105-12-31 23:59:00','start of year','-0 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 218: Invalid expression / Unexpected token. Line 1, Col: 640.
  indication of any abnormality on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 219: Model abstains from answering the question
Error executing query 220: Model abstains from answering the question
Error executing query 221: Invalid expression / Unexpected token. Line 1, Col: 920.
  70833 ) and strftime('%Y-%m',procedures_icd.charttime) >= '2102-08' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 225: Model only answers one image question SQLs
Error executing query 226: Model only answers one image question SQLs
Error executing query 227: Model abstains from answering the question
Error executing query 228: Invalid expression / Unexpected token. Line 1, Col: 903.
  noses_icd.charttime) >= datetime('2105-12-31 23:59:00','-86 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 230: Model abstains from answering the question
Error executing query 232: Model abstains from answering the question
Error executing query 233: Expecting ). Line 1, Col: 967.
  etime('2105-12-31 23:59:00','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 234: Invalid expression / Unexpected token. Line 1, Col: 791.
  chest x-ray indicate intra-aortic balloon pump?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 236: Model abstains from answering the question
Error executing query 239: Error tokenizing 't3.studydatetime) and datetime(t3.studydatetime,''
Error executing query 240: Invalid expression / Unexpected token. Line 1, Col: 919.
  9564280 ) and strftime('%Y-%m',diagnoses_icd.charttime) = '2104-02' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 241: Invalid expression / Unexpected token. Line 1, Col: 1027.
  ad/heart failure in the right hilar structures?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 242: Model only answers one image question SQLs
Error executing query 243: Model abstains from answering the question
Error executing query 244: Model only answers one image question SQLs
Error executing query 245: Model only answers one image question SQLs
Error executing query 246: Model only answers one image question SQLs
Error executing query 247: Expecting ). Line 1, Col: 779.
  dures_icd.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.icd_code ) as t3 where t3.c1 = 3 )
Error executing query 249: Model abstains from answering the question
Error executing query 250: Model abstains from answering the question
Error executing query 251: Model only answers one image question SQLs
Error executing query 252: Model only answers one image question SQLs
Error executing query 253: Invalid expression / Unexpected token. Line 1, Col: 883.
  unc_vqa("is cyst/bullae shown on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 254: Model abstains from answering the question
Error executing query 256: Required keyword: 'expressions' missing for <class 'sqlglot.expressions.Aliases'>. Line 1, Col: 503.
  ratory rate' and d_items.linksto = 'chartevents' ) order by chartevents.charttime desc limit 1 )  ( [4mselect[0m chartevents.valuenum from chartevents where chartevents.stay_id in ( select icustays.stay_id from i
Error executing query 257: Model abstains from answering the question
Error executing query 258: Invalid expression / Unexpected token. Line 1, Col: 789.
  _vqa("is the chest x-ray revealing any devices?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 259: Model abstains from answering the question
Error executing query 260: Model abstains from answering the question
Error executing query 261: Model only answers one image question SQLs
Error executing query 262: Model abstains from answering the question
Error executing query 266: Model only answers one image question SQLs
Error executing query 267: near "(": syntax error
Error executing query 268: Invalid expression / Unexpected token. Line 1, Col: 937.
  cedures_icd.charttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 269: Model abstains from answering the question
Error executing query 270: Model abstains from answering the question
Error executing query 271: Model abstains from answering the question
Error executing query 272: Invalid expression / Unexpected token. Line 1, Col: 897.
  d = 13336663 ) and strftime('%Y',diagnoses_icd.charttime) >= '2105' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 274: Model abstains from answering the question
Error executing query 275: Expecting ). Line 1, Col: 787.
  '%Y',prescriptions.starttime) = '2105' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 5
Error executing query 276: Model abstains from answering the question
Error executing query 278: Invalid expression / Unexpected token. Line 1, Col: 755.
  indication of any abnormality on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 280: Model only answers one image question SQLs
Error executing query 281: Model abstains from answering the question
Error executing query 283: Model abstains from answering the question
Error executing query 284: Model abstains from answering the question
Error executing query 286: Expecting ). Line 1, Col: 859.
  Y',procedures_icd.charttime) >= '2105' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 287: Model only answers one image question SQLs
Error executing query 288: Invalid expression / Unexpected token. Line 1, Col: 916.
   any abnormality in the right hilar structures?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 289: Invalid expression / Unexpected token. Line 1, Col: 873.
  c_vqa("does a chest x-ray show any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 290: Model abstains from answering the question
Error executing query 291: Model abstains from answering the question
Error executing query 293: Expecting ). Line 1, Col: 835.
  etime('2105-12-31 23:59:00','-5 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month') gro
Error executing query 295: Model abstains from answering the question
Error executing query 297: Invalid expression / Unexpected token. Line 1, Col: 902.
   = 13551252 ) and strftime('%Y',procedures_icd.charttime) >= '2105' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 299: Invalid expression / Unexpected token. Line 1, Col: 1113.
   x-ray indicate any abnormality in the trachea?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and
Error executing query 301: Model only answers one image question SQLs
Error executing query 302: Invalid expression / Unexpected token. Line 1, Col: 841.
  "has an x-ray indicated granulomatous diseases?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 304: Invalid expression / Unexpected token. Line 1, Col: 627.
  a("does a chest x-ray show any any abnormality?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 305: Invalid expression / Unexpected token. Line 1, Col: 991.
   year') = datetime('2105-12-31 23:59:00','start of year','-0 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 306: Model abstains from answering the question
Error executing query 308: Invalid expression / Unexpected token. Line 1, Col: 645.
  ns.hadm_id from admissions where admissions.subject_id = 14410216 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 310: Model only answers one image question SQLs
Error executing query 311: Model abstains from answering the question
Error executing query 312: Invalid expression / Unexpected token. Line 1, Col: 1085.
  st x-ray indicate any abnormality in the spine?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 313: Invalid expression / Unexpected token. Line 1, Col: 886.
  -ray demonstrated fluid overload/heart failure?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 314: Invalid expression / Unexpected token. Line 1, Col: 762.
  d = 11320106 ) and strftime('%Y',prescriptions.starttime) >= '2105' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 315: Model only answers one image question SQLs
Error executing query 316: Model abstains from answering the question
Error executing query 318: Model only answers one image question SQLs
Error executing query 319: Invalid expression / Unexpected token. Line 1, Col: 896.
  reveal infiltration in the right mid lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 320: near "(": syntax error
Error executing query 321: Model abstains from answering the question
Error executing query 322: Expecting ). Line 1, Col: 927.
  etime('2105-12-31 23:59:00','-3 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 5
Error executing query 323: Expecting ). Line 1, Col: 916.
  ime('%Y',labevents.charttime) = '2102' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.itemid ) as t3 where t3.c1 = 3 )
Error executing query 325: Model abstains from answering the question
Error executing query 328: Model only answers one image question SQLs
Error executing query 329: Model only answers one image question SQLs
Error executing query 332: Model abstains from answering the question
Error executing query 333: Model only answers one image question SQLs
Error executing query 334: Model abstains from answering the question
Error executing query 336: Model abstains from answering the question
Error executing query 338: Model abstains from answering the question
Error executing query 339: Model abstains from answering the question
Error executing query 340: Model abstains from answering the question
Error executing query 341: Invalid expression / Unexpected token. Line 1, Col: 929.
  _vqa("is any abnormality indicated on an x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 343: Model abstains from answering the question
Error executing query 346: Invalid expression / Unexpected token. Line 1, Col: 853.
  ay reveal any tubes/lines in the left shoulder?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 347: Model abstains from answering the question
Error executing query 348: Invalid expression / Unexpected token. Line 1, Col: 898.
  d = 17112656 ) and strftime('%Y',procedures_icd.charttime) = '2102' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 349: Model abstains from answering the question
Error executing query 350: Model only answers one image question SQLs
Error executing query 351: Expecting ). Line 1, Col: 905.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.itemid ) as t3 where t3.c1 = 5 )
Error executing query 352: Model abstains from answering the question
Error executing query 353: Expecting ). Line 1, Col: 977.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 355: Model abstains from answering the question
Error executing query 356: Model only answers one image question SQLs
Error executing query 357: Invalid expression / Unexpected token. Line 1, Col: 859.
  id = 13880645 ) and strftime('%Y',diagnoses_icd.charttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 358: Model only answers one image question SQLs
Error executing query 359: Model abstains from answering the question
Error executing query 360: Model abstains from answering the question
Error executing query 361: Model abstains from answering the question
Error executing query 364: Model only answers one image question SQLs
Error executing query 365: Model abstains from answering the question
Error executing query 366: Model abstains from answering the question
Error executing query 367: Model only answers one image question SQLs
Error executing query 368: Model abstains from answering the question
Error executing query 372: Model only answers one image question SQLs
Error executing query 375: Invalid expression / Unexpected token. Line 1, Col: 807.
  ray reveal any any devices in the right atrium?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 376: Model abstains from answering the question
Error executing query 378: Model abstains from answering the question
[False]
Error executing query 380: Model only answers one image question SQLs
Error executing query 383: Model abstains from answering the question
Error executing query 385: Model only answers one image question SQLs
Error executing query 386: Invalid expression / Unexpected token. Line 1, Col: 770.
  ns.hadm_id from admissions where admissions.subject_id = 12429112 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 387: Invalid expression / Unexpected token. Line 1, Col: 872.
  e pneumothorax in the right costophrenic angle?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 388: Model abstains from answering the question
Error executing query 389: Expecting ). Line 1, Col: 749.
  ogyevents.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.test_name ) as t3 where t3.c1 = 3
Error executing query 390: Model abstains from answering the question
Error executing query 391: Expecting ). Line 1, Col: 764.
  ogyevents.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.spec_type_desc ) as t3 where t3.c1 = 3
Error executing query 392: Model only answers one image question SQLs
Error executing query 393: Model abstains from answering the question
Error executing query 394: Model abstains from answering the question
Error executing query 395: Model only answers one image question SQLs
Error executing query 396: Invalid expression / Unexpected token. Line 1, Col: 901.
   pleural/parenchymal scarring on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 397: Model abstains from answering the question
Error executing query 400: Model abstains from answering the question
Error executing query 401: Expecting ). Line 1, Col: 845.
  ime('%Y',labevents.charttime) = '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 403: Model only answers one image question SQLs
Error executing query 404: Invalid expression / Unexpected token. Line 1, Col: 715.
  ("does a chest x-ray reveal any enlarged hilum?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 406: Model abstains from answering the question
Error executing query 407: Model abstains from answering the question
Error executing query 408: Invalid expression / Unexpected token. Line 1, Col: 847.
  id = 11350319 ) and strftime('%Y',diagnoses_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 409: Model only answers one image question SQLs
Error executing query 410: Model only answers one image question SQLs
Error executing query 411: Invalid expression / Unexpected token. Line 1, Col: 966.
   year','-0 year') and strftime('%m',prescriptions.starttime) = '01' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 412: Model abstains from answering the question
Error executing query 413: Invalid expression / Unexpected token. Line 1, Col: 900.
  d = 18728663 ) and strftime('%Y',procedures_icd.charttime) = '2100' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 415: Model abstains from answering the question
Error executing query 416: Model only answers one image question SQLs
Error executing query 417: Invalid expression / Unexpected token. Line 1, Col: 769.
  754359 ) and strftime('%Y-%m',prescriptions.starttime) >= '2105-09' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 419: Invalid expression / Unexpected token. Line 1, Col: 612.
  vqa("does a chest x-ray reveal any abnormality?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 420: Model abstains from answering the question
Error executing query 421: Model abstains from answering the question
Error executing query 422: Model abstains from answering the question
Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 126, in <module>
    Defaults.start()
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/dtu/__init__.py", line 235, in start
    cls.run(*args)
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 68, in run
    executed_result = run_execution_for_gt_query(executor, parsed_result_gt, name)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/NeuralSQL/execute_nsql.py", line 82, in run_execution_for_gt_query
    result = executor.execute_nsql(query)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/NeuralSQL/executor/nsql_executor.py", line 266, in execute_nsql
    return self._execute_select_query(query_root, nsql, tables)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/NeuralSQL/executor/nsql_executor.py", line 328, in _execute_select_query
    return self._execute_vqa_subquery(from_clause_node, query_root, nsql, tables)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/NeuralSQL/executor/nsql_executor.py", line 359, in _execute_vqa_subquery
    return self.execute_vqa_function_in_nsql(nsql, tables)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/NeuralSQL/executor/nsql_executor.py", line 192, in execute_vqa_function_in_nsql
    answer_batch = self._execute_vqa_function(image_batch=image_batch, question_batch=question_batch)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/NeuralSQL/executor/nsql_executor.py", line 121, in _execute_vqa_function
    answers = self.vqa_module(image_batch, question_batch)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/NeuralSQL/executor/visual_module/custom_vqa_module.py", line 83, in __call__
    text_logits, _ = self.model.apply({"params": self.params}, preprocessed_images, tokenized_questions[:, :-1], mask_ar[:, :-1], train=False)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/traceback_util.py", line 179, in reraise_with_filtered_traceback
    return fun(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/flax/linen/module.py", line 2226, in apply
    return apply(
           ^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/flax/core/scope.py", line 1101, in wrapper
    y = fn(root, *args, **kwargs)
        ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/flax/linen/module.py", line 3006, in scope_fn
    return fn(module.clone(parent=scope, _deep_clone=True), *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/flax/linen/module.py", line 701, in wrapped_module_method
    return self._call_wrapped_method(fun, args, kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/flax/linen/module.py", line 1233, in _call_wrapped_method
    y = run_fun(self, *args, **kwargs)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/big_vision/models/proj/paligemma/paligemma.py", line 151, in __call__
    _, out_llm = self._llm(x, mask=attn_mask, train=train)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/flax/linen/module.py", line 701, in wrapped_module_method
    return self._call_wrapped_method(fun, args, kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/flax/linen/module.py", line 1233, in _call_wrapped_method
    y = run_fun(self, *args, **kwargs)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/big_vision/models/proj/paligemma/gemma_bv.py", line 81, in __call__
    logits, out = self.model(
                  ^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/flax/linen/module.py", line 701, in wrapped_module_method
    return self._call_wrapped_method(fun, args, kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/flax/linen/module.py", line 1233, in _call_wrapped_method
    y = run_fun(self, *args, **kwargs)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/big_vision/models/ppp/gemma.py", line 452, in __call__
    x, unused_scan_arg = block(
                         ^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/flax/linen/transforms.py", line 378, in wrapped_fn
    ret = trafo_fn(module_scopes, *args, **kwargs)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/flax/core/lift.py", line 325, in wrapper
    y, out_variable_groups_xs_t = fn(
                                  ^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/flax/core/lift.py", line 1028, in inner
    broadcast_vars, (carry_vars, c), (ys, scan_vars) = scanned(
                                                       ^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/flax/core/axes_scan.py", line 165, in scan_fn
    c, ys = lax.scan(
            ^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/traceback_util.py", line 179, in reraise_with_filtered_traceback
    return fun(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/lax/control_flow/loops.py", line 288, in scan
    out = scan_p.bind(*consts, *in_flat,
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/lax/control_flow/loops.py", line 1280, in scan_bind
    return core.AxisPrimitive.bind(scan_p, *args, **params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/core.py", line 2789, in bind
    return self.bind_with_trace(top_trace, args, params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/core.py", line 391, in bind_with_trace
    out = trace.process_primitive(self, map(trace.full_raise, args), params)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/core.py", line 879, in process_primitive
    return primitive.impl(*tracers, **params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/dispatch.py", line 86, in apply_primitive
    outs = fun(*args)
           ^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/traceback_util.py", line 179, in reraise_with_filtered_traceback
    return fun(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/pjit.py", line 304, in cache_miss
    outs, out_flat, out_tree, args_flat, jaxpr, attrs_tracked = _python_pjit_helper(
                                                                ^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/pjit.py", line 181, in _python_pjit_helper
    out_flat = pjit_p.bind(*args_flat, **params)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/core.py", line 2789, in bind
    return self.bind_with_trace(top_trace, args, params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/core.py", line 391, in bind_with_trace
    out = trace.process_primitive(self, map(trace.full_raise, args), params)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/core.py", line 879, in process_primitive
    return primitive.impl(*tracers, **params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/pjit.py", line 1525, in _pjit_call_impl
    return xc._xla.pjit(
           ^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/pjit.py", line 1508, in call_impl_cache_miss
    out_flat, compiled = _pjit_call_impl_python(
                         ^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/pjit.py", line 1438, in _pjit_call_impl_python
    inline=inline, lowering_parameters=mlir.LoweringParameters()).compile()
                                                                  ^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/interpreters/pxla.py", line 2363, in compile
    executable = UnloadedMeshExecutable.from_hlo(
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/interpreters/pxla.py", line 2860, in from_hlo
    xla_executable = _cached_compilation(
                     ^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/interpreters/pxla.py", line 2678, in _cached_compilation
    xla_executable = compiler.compile_or_get_cached(
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/compiler.py", line 330, in compile_or_get_cached
    return _compile_and_write_cache(
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/compiler.py", line 501, in _compile_and_write_cache
    executable = backend_compile(
                 ^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/profiler.py", line 335, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/compiler.py", line 237, in backend_compile
    return backend.compile(built_c, compile_options=options)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
KeyboardInterrupt
Terminated

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21915972: <test_set09_0> in cluster <dcc> Exited

Job <test_set09_0> was submitted from host <n-62-30-2> by user <s183914> in cluster <dcc> at Tue Jun  4 15:47:55 2024
Job was executed on host(s) <4*n-62-11-14>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue Jun  4 16:56:15 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_final/ML_final> was used as the working directory.
Started at Tue Jun  4 16:56:15 2024
Terminated at Tue Jun  4 17:05:01 2024
Results reported at Tue Jun  4 17:05:01 2024

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 4
#BSUB -R "rusage[mem=16G]"
#BSUB -R "select[gpu32gb]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
module -s load python3
source ../project-env/bin/activate

python main.py $MYARGS
------------------------------------------------------------

TERM_OWNER: job killed by owner.
Exited with exit code 143.

Resource usage summary:

    CPU time :                                   533.00 sec.
    Max Memory :                                 8848 MB
    Average Memory :                             7123.67 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               56688.00 MB
    Max Swap :                                   -
    Max Processes :                              6
    Max Threads :                                67
    Run time :                                   527 sec.
    Turnaround time :                            4626 sec.

The output (if any) is above this job summary.
