2024-06-05 04:01:42.701188: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.17.0
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_final/ML_final/wandb/run-20240605_040146-zli9w0pa
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run vision1test09-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/zli9w0pa
2024-06-05 04:02:05.398636: W tensorflow/core/common_runtime/gpu/gpu_device.cc:2251] Cannot dlopen some GPU libraries. Please make sure the missing libraries mentioned above are installed properly if you would like to use GPU. Follow the guide at https://www.tensorflow.org/install/gpu for how to download and setup the required libraries for your platform.
Skipping registering GPU devices...
2024-06-05 04:02:06.566120: W external/xla/xla/service/gpu/nvptx_compiler.cc:760] The NVIDIA driver's CUDA version is 12.4 which is older than the ptxas CUDA version (12.5.40). Because the driver is older than the ptxas version, XLA is disabling parallel compilation, which may slow down compilation. You should update your NVIDIA driver or use the NVIDIA-provided CUDA forward compatibility packages.

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
| <c>name</c>       | <d>str</d>        | <j>"vision1test09-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>3600</f>       |
| <c>vqa_module_type</c>| <d>str</d>        | <j>"custom"</j>   |
| <c>prediction_file_name</c>| <d>str</d>        | <j>"predictions_LLM_1-0_test"</j> |
| <c>threshold</c>  | <d>float</d>      | <f>0.9</f>        |
| <c>table_path</c> | <d>str</d>        | <j>"database/mimic_iv_cxr/gold"</j> |
| <c>model_path_name</c>| <d>str</d>        | <j>"params_model_1-0"</j> |

# Output

```
sid_to_ipath_map loaded. (1616 entries)
Error executing query 1: Model only answers one image question SQLs
Error executing query 2: Model only answers one image question SQLs
Error executing query 3: Invalid expression / Unexpected token. Line 1, Col: 926.
  x-ray show any abnormality in the right atrium?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4: Model only answers one image question SQLs
Error executing query 5: Model only answers one image question SQLs
[True]
Error executing query 6: near "(": syntax error
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
Error executing query 50: Model abstains from answering the question
Error executing query 51: Model abstains from answering the question
Error executing query 52: Invalid expression / Unexpected token. Line 1, Col: 784.
  escriptions.starttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
[True]
Error executing query 53: near "(": syntax error
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
Error executing query 104: Model abstains from answering the question
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
[True]
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
[True]
Error executing query 211: Model abstains from answering the question
Error executing query 212: Model abstains from answering the question
[False]
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
[True]
Error executing query 271: Model abstains from answering the question
Error executing query 272: Invalid expression / Unexpected token. Line 1, Col: 897.
  d = 13336663 ) and strftime('%Y',diagnoses_icd.charttime) >= '2105' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
[True]
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
[False]
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
Error executing query 423: Model abstains from answering the question
Error executing query 424: Model only answers one image question SQLs
Error executing query 426: Invalid expression / Unexpected token. Line 1, Col: 967.
  cedures_icd.charttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 430: Model abstains from answering the question
Error executing query 431: Model abstains from answering the question
Error executing query 434: Invalid expression / Unexpected token. Line 1, Col: 621.
  a("does a chest x-ray show any any tubes/lines?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 435: Invalid expression / Unexpected token. Line 1, Col: 906.
  8946945 ) and strftime('%Y-%m',diagnoses_icd.charttime) = '2105-01' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 437: Model abstains from answering the question
Error executing query 438: Model only answers one image question SQLs
Error executing query 439: Model only answers one image question SQLs
Error executing query 440: Invalid expression / Unexpected token. Line 1, Col: 867.
  st x-ray depicting any abnormality in the neck?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 443: Model only answers one image question SQLs
Error executing query 444: Invalid expression / Unexpected token. Line 1, Col: 642.
  showing any diseases in the left hemidiaphragm?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 446: Invalid expression / Unexpected token. Line 1, Col: 722.
  id = 10063856 ) and strftime('%Y',prescriptions.starttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 447: Model abstains from answering the question
Error executing query 448: Model abstains from answering the question
Error executing query 452: Invalid expression / Unexpected token. Line 1, Col: 860.
  966115 ) and strftime('%Y-%m',diagnoses_icd.charttime) >= '2105-01' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 454: Model abstains from answering the question
Error executing query 455: Invalid expression / Unexpected token. Line 1, Col: 849.
  d = 11246165 ) and strftime('%Y',diagnoses_icd.charttime) >= '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 456: Invalid expression / Unexpected token. Line 1, Col: 849.
  c_vqa("does a chest x-ray show any tubes/lines?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 457: Invalid expression / Unexpected token. Line 1, Col: 728.
  d = 15790605 ) and strftime('%Y',prescriptions.starttime) >= '2103' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 458: Invalid expression / Unexpected token. Line 1, Col: 1079.
   year','-0 year') and strftime('%m',diagnoses_icd.charttime) = '09' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.
Error executing query 460: Model only answers one image question SQLs
Error executing query 463: Invalid expression / Unexpected token. Line 1, Col: 911.
  137553 ) and strftime('%Y-%m',procedures_icd.charttime) = '2103-11' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 465: Model only answers one image question SQLs
Error executing query 466: Expecting ). Line 1, Col: 914.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 467: Invalid expression / Unexpected token. Line 1, Col: 841.
  nc_vqa("does a chest x-ray reveal any diseases?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 470: Model abstains from answering the question
Error executing query 472: Model abstains from answering the question
Error executing query 473: Model only answers one image question SQLs
Error executing query 474: Model only answers one image question SQLs
Error executing query 475: Invalid expression / Unexpected token. Line 1, Col: 1020.
  n revealed in the aortic arch on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 476: Model abstains from answering the question
Error executing query 477: Invalid expression / Unexpected token. Line 1, Col: 913.
  etime('2105-12-31 23:59:00','-5 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
Error executing query 478: Expecting ). Line 1, Col: 815.
  ime('%Y',labevents.charttime) = '2103' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 482: Model abstains from answering the question
Error executing query 483: Model abstains from answering the question
Error executing query 484: Invalid expression / Unexpected token. Line 1, Col: 1109.
   func_vqa("does a chest x-ray reveal pneumonia?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 489: Model abstains from answering the question
Error executing query 493: Invalid expression / Unexpected token. Line 1, Col: 768.
  id = 13122104 ) and strftime('%Y',prescriptions.starttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 495: Invalid expression / Unexpected token. Line 1, Col: 1020.
  as t2 where func_vqa("is any diseases revealed?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 496: Invalid expression / Unexpected token. Line 1, Col: 1015.
  s.dischtime is not null order by admissions.admittime asc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 497: Model abstains from answering the question
Error executing query 498: Invalid expression / Unexpected token. Line 1, Col: 945.
  reveal any diseases in the right hemidiaphragm?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 501: Model abstains from answering the question
Error executing query 503: Model only answers one image question SQLs
Error executing query 505: Invalid expression / Unexpected token. Line 1, Col: 821.
   of any technical assessments on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 507: Model abstains from answering the question
Error executing query 508: Expecting ). Line 1, Col: 763.
  icrobiologyevents.charttime) >= '2103' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 512: Model abstains from answering the question
Error executing query 513: Model abstains from answering the question
Error executing query 514: Invalid expression / Unexpected token. Line 1, Col: 863.
  %Y',procedures_icd.charttime) = '2103' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 515: Model abstains from answering the question
Error executing query 516: Model only answers one image question SQLs
Error executing query 519: Model only answers one image question SQLs
Error executing query 520: Expecting ). Line 1, Col: 819.
  %Y',diagnoses_icd.charttime) >= '2105' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 528: Invalid expression / Unexpected token. Line 1, Col: 402.
  el = 'arterial blood pressure mean' and d_items.linksto = 'chartevents' ) and chartevents.valuenum  [4m107.0[0m and datetime(chartevents.charttime) = datetime('2105-12-31 23:59:00','-400 day')
Error executing query 529: Model only answers one image question SQLs
Error executing query 531: Invalid expression / Unexpected token. Line 1, Col: 828.
  ray indicate any any diseases in the left lung?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 532: Model only answers one image question SQLs
Error executing query 533: Model abstains from answering the question
Error executing query 534: Invalid expression / Unexpected token. Line 1, Col: 940.
  id = 16766035 ) and strftime('%Y',diagnoses_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 535: Model only answers one image question SQLs
Error executing query 536: Invalid expression / Unexpected token. Line 1, Col: 742.
  '%Y',prescriptions.starttime) = '2100' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id
Error executing query 542: Model abstains from answering the question
Error executing query 543: Model abstains from answering the question
Error executing query 545: Model abstains from answering the question
Error executing query 546: Model abstains from answering the question
Error executing query 549: Model abstains from answering the question
Error executing query 550: Model abstains from answering the question
Error executing query 552: Model abstains from answering the question
Error executing query 553: Model abstains from answering the question
Error executing query 554: Model only answers one image question SQLs
Error executing query 556: Invalid expression / Unexpected token. Line 1, Col: 814.
  escriptions.starttime) >= datetime('2105-12-31 23:59:00','-2 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 559: Model abstains from answering the question
Error executing query 560: Model abstains from answering the question
Error executing query 561: Model only answers one image question SQLs
Error executing query 563: near "(": syntax error
Error executing query 564: Model abstains from answering the question
Error executing query 566: Model abstains from answering the question
Error executing query 567: Invalid expression / Unexpected token. Line 1, Col: 947.
   shown any tubes/lines in the right chest wall?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 568: Model abstains from answering the question
Error executing query 570: Model abstains from answering the question
Error executing query 572: Model only answers one image question SQLs
Error executing query 573: Model abstains from answering the question
Error executing query 574: Invalid expression / Unexpected token. Line 1, Col: 976.
  x-ray indicate enlarged hilum in the left lung?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 575: Expecting ). Line 1, Col: 986.
  ar','-1 year') ) as t2 join admissions on t2.subject_id = admissions.subject_id where t2.charttime  [4madmissions[0m.admittime and datetime(admissions.admittime,'start of year') = datetime('2105-12-31 23:59:00','star
Error executing query 576: Model only answers one image question SQLs
Error executing query 581: Model abstains from answering the question
Error executing query 582: Model only answers one image question SQLs
Error executing query 586: Model only answers one image question SQLs
Error executing query 587: Invalid expression / Unexpected token. Line 1, Col: 927.
  any tubes/lines in the carina on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 591: Model only answers one image question SQLs
Error executing query 592: Model abstains from answering the question
Error executing query 595: Model abstains from answering the question
Error executing query 596: Model abstains from answering the question
Error executing query 597: Model abstains from answering the question
Error executing query 598: Model abstains from answering the question
Error executing query 599: Invalid expression / Unexpected token. Line 1, Col: 903.
   = 14661031 ) and strftime('%Y',procedures_icd.charttime) >= '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 600: Invalid expression / Unexpected token. Line 1, Col: 784.
  t x-ray detecting rotated in the left clavicle?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 602: Expecting ). Line 1, Col: 868.
  '%Y',prescriptions.starttime) = '2103' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 604: Model only answers one image question SQLs
Error executing query 605: Model abstains from answering the question
Error executing query 607: Invalid expression / Unexpected token. Line 1, Col: 871.
  indication of any abnormality on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 608: Model only answers one image question SQLs
Error executing query 609: Model only answers one image question SQLs
Error executing query 610: Model only answers one image question SQLs
Error executing query 611: Model abstains from answering the question
Error executing query 612: Model only answers one image question SQLs
Error executing query 613: Model abstains from answering the question
Error executing query 615: Model abstains from answering the question
Error executing query 619: Model only answers one image question SQLs
Error executing query 621: Model only answers one image question SQLs
Error executing query 622: Invalid expression / Unexpected token. Line 1, Col: 877.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id
Error executing query 623: Model abstains from answering the question
Error executing query 626: Model abstains from answering the question
Error executing query 628: near "(": syntax error
Error executing query 629: Invalid expression / Unexpected token. Line 1, Col: 966.
  hest x-ray depicting any technical assessments?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 631: Model abstains from answering the question
Error executing query 632: Model abstains from answering the question
Error executing query 633: Model only answers one image question SQLs
Error executing query 634: Model abstains from answering the question
Error executing query 637: Invalid expression / Unexpected token. Line 1, Col: 836.
  %Y',procedures_icd.charttime) = '2101' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
Error executing query 638: Model abstains from answering the question
Error executing query 640: Model abstains from answering the question
Error executing query 642: Invalid expression / Unexpected token. Line 1, Col: 934.
   where func_vqa("is any abnormality identified?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 643: Invalid expression / Unexpected token. Line 1, Col: 630.
  ns.hadm_id from admissions where admissions.subject_id = 17466107 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 644: Model abstains from answering the question
Error executing query 645: Invalid expression / Unexpected token. Line 1, Col: 792.
  id = 17049363 ) and strftime('%Y',prescriptions.starttime) = '2101' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 646: Model only answers one image question SQLs
Error executing query 648: near "(": syntax error
Error executing query 649: Invalid expression / Unexpected token. Line 1, Col: 943.
  a chest x-ray reveal any technical assessments?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 651: Model only answers one image question SQLs
Error executing query 652: Model only answers one image question SQLs
Error executing query 653: Model abstains from answering the question
Error executing query 655: Model only answers one image question SQLs
Error executing query 656: Model only answers one image question SQLs
[True]
Error executing query 657: Model abstains from answering the question
Error executing query 659: Model abstains from answering the question
Error executing query 662: Model abstains from answering the question
Error executing query 663: Model only answers one image question SQLs
Error executing query 664: Model abstains from answering the question
Error executing query 665: Model abstains from answering the question
Error executing query 666: Invalid expression / Unexpected token. Line 1, Col: 885.
  agnoses_icd.charttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 670: Invalid expression / Unexpected token. Line 1, Col: 802.
  ns.hadm_id from admissions where admissions.subject_id = 18476657 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 671: Invalid expression / Unexpected token. Line 1, Col: 974.
  indication of any tubes/lines on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 672: Model abstains from answering the question
Error executing query 673: Model abstains from answering the question
[True]
[True]
Error executing query 675: Invalid expression / Unexpected token. Line 1, Col: 855.
  %Y',procedures_icd.charttime) = '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 679: Model abstains from answering the question
Error executing query 680: Model abstains from answering the question
Error executing query 682: Invalid expression / Unexpected token. Line 1, Col: 891.
  id = 17766862 ) and strftime('%Y',diagnoses_icd.charttime) = '2101' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 683: Invalid expression / Unexpected token. Line 1, Col: 950.
  ocedures_icd.charttime) = datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 685: Model abstains from answering the question
Error executing query 687: Model only answers one image question SQLs
Error executing query 688: Model only answers one image question SQLs
Error executing query 690: Invalid expression / Unexpected token. Line 1, Col: 973.
   abnormality shown in the svc on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 691: Model only answers one image question SQLs
Error executing query 694: Model only answers one image question SQLs
Error executing query 695: Model abstains from answering the question
[True]
Error executing query 698: Model abstains from answering the question
Error executing query 699: Model only answers one image question SQLs
Error executing query 700: Expecting ). Line 1, Col: 1178.
  t 1 ) order by tb_cxr.studydatetime desc limit 1 ) ) ) order by tb_cxr.studydatetime desc limit 1 ) [4mas[0m
Error executing query 702: Invalid expression / Unexpected token. Line 1, Col: 1040.
  ny abnormality in the right costophrenic angle?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 703: Model only answers one image question SQLs
Error executing query 704: Model abstains from answering the question
Error executing query 705: Invalid expression / Unexpected token. Line 1, Col: 907.
  d = 19371747 ) and strftime('%Y',procedures_icd.charttime) = '2105' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 706: Model abstains from answering the question
Error executing query 707: Invalid expression / Unexpected token. Line 1, Col: 894.
  shown increased reticular markings/ild pattern?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 709: Model abstains from answering the question
Error executing query 710: Model abstains from answering the question
Error executing query 711: Model only answers one image question SQLs
Error executing query 713: Model abstains from answering the question
Error executing query 714: Invalid expression / Unexpected token. Line 1, Col: 943.
  cedures_icd.charttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 716: near "(": syntax error
Error executing query 718: Model abstains from answering the question
Error executing query 720: Model abstains from answering the question
Error executing query 721: Model abstains from answering the question
Error executing query 722: Model only answers one image question SQLs
Error executing query 723: Model abstains from answering the question
Error executing query 725: Model abstains from answering the question
Error executing query 726: Invalid expression / Unexpected token. Line 1, Col: 878.
  ray indicate any abnormality in the right lung?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 728: Model only answers one image question SQLs
Error executing query 731: Expecting ). Line 1, Col: 704.
  labevents.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.itemid ) as t3 where t3.c1 = 3 )
Error executing query 732: Model abstains from answering the question
Error executing query 733: Model abstains from answering the question
Error executing query 734: Model only answers one image question SQLs
Error executing query 735: Model abstains from answering the question
Error executing query 736: Model only answers one image question SQLs
Error executing query 737: Model abstains from answering the question
Error executing query 740: Model only answers one image question SQLs
Error executing query 741: Expecting ). Line 1, Col: 908.
  Y',procedures_icd.charttime) >= '2105' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.icd_code ) as t3 where t3.c1 = 3 )
Error executing query 742: Model abstains from answering the question
Error executing query 743: Expecting ). Line 1, Col: 781.
  ime('%Y',labevents.charttime) = '2103' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 745: Invalid expression / Unexpected token. Line 1, Col: 632.
  echnical assessments observed on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 746: Invalid expression / Unexpected token. Line 1, Col: 813.
  ns.hadm_id from admissions where admissions.subject_id = 12262788 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 747: Invalid expression / Unexpected token. Line 1, Col: 861.
   = 12822417 ) and strftime('%Y',procedures_icd.charttime) >= '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 748: Model only answers one image question SQLs
Error executing query 749: Model abstains from answering the question
Error executing query 750: Model abstains from answering the question
Error executing query 752: Invalid expression / Unexpected token. Line 1, Col: 727.
  id = 12930426 ) and strftime('%Y',prescriptions.starttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 753: Model abstains from answering the question
Error executing query 754: Model abstains from answering the question
Error executing query 755: Model only answers one image question SQLs
Error executing query 756: Model only answers one image question SQLs
Error executing query 758: Model only answers one image question SQLs
Error executing query 761: Model only answers one image question SQLs
Error executing query 762: Model only answers one image question SQLs
Error executing query 763: Invalid expression / Unexpected token. Line 1, Col: 929.
  dures_icd.charttime) >= datetime('2105-12-31 23:59:00','-68 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 764: Model abstains from answering the question
Error executing query 765: Invalid expression / Unexpected token. Line 1, Col: 864.
  ("is any abnormality revealed on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 766: Model abstains from answering the question
Error executing query 768: Model abstains from answering the question
Error executing query 769: Model abstains from answering the question
Error executing query 770: Expecting ). Line 1, Col: 1076.
  ar','-0 year') ) as t2 join admissions on t2.subject_id = admissions.subject_id where t2.charttime  [4madmissions[0m.admittime and datetime(admissions.admittime,'start of year') = datetime('2105-12-31 23:59:00','star
Error executing query 772: Model only answers one image question SQLs
Error executing query 773: Model only answers one image question SQLs
Error executing query 774: Model abstains from answering the question
Error executing query 775: Model only answers one image question SQLs
Error executing query 776: Invalid expression / Unexpected token. Line 1, Col: 920.
  agnoses_icd.charttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 779: Invalid expression / Unexpected token. Line 1, Col: 907.
  agnoses_icd.charttime) >= datetime('2105-12-31 23:59:00','-4 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 780: Model abstains from answering the question
Error executing query 782: Model only answers one image question SQLs
Error executing query 783: Invalid expression / Unexpected token. Line 1, Col: 926.
  dures_icd.charttime) >= datetime('2105-12-31 23:59:00','-16 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 784: Model abstains from answering the question
Error executing query 785: Model abstains from answering the question
Error executing query 788: Model only answers one image question SQLs
Error executing query 789: Model abstains from answering the question
Error executing query 791: Invalid expression / Unexpected token. Line 1, Col: 780.
  t x-ray demonstrated any technical assessments?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 792: Invalid expression / Unexpected token. Line 1, Col: 777.
  787238 ) and strftime('%Y-%m',prescriptions.starttime) >= '2104-03' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 793: Model abstains from answering the question
Error executing query 794: Model abstains from answering the question
Error executing query 795: Invalid expression / Unexpected token. Line 1, Col: 805.
  ns.hadm_id from admissions where admissions.subject_id = 12986647 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 797: Model abstains from answering the question
Error executing query 799: Model only answers one image question SQLs
Error executing query 800: Invalid expression / Unexpected token. Line 1, Col: 742.
  chest x-ray depicts any abnormality in the svc?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 801: Model only answers one image question SQLs
Error executing query 802: Invalid expression / Unexpected token. Line 1, Col: 995.
  wn copd/emphysema in the right upper lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 803: Model abstains from answering the question
Error executing query 804: Model only answers one image question SQLs
Error executing query 805: Model abstains from answering the question
Error executing query 807: Invalid expression / Unexpected token. Line 1, Col: 941.
  etime('2105-12-31 23:59:00','-4 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id
Error executing query 808: Required keyword: 'expression' missing for <class 'sqlglot.expressions.EQ'>. Line 1, Col: 1185.
  tetime('2105-12-31 23:59:00','start of year','-0 year') and strftime('%m',procedures_icd.charttime) [4m=[0m
Error executing query 809: Model abstains from answering the question
Error executing query 810: Invalid expression / Unexpected token. Line 1, Col: 890.
  cedures_icd.charttime) >= datetime('2105-12-31 23:59:00','-4 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 811: Model abstains from answering the question
Error executing query 812: Model abstains from answering the question
Error executing query 814: Invalid expression / Unexpected token. Line 1, Col: 619.
  where prescriptions.drug = 'ketorolac' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month')
Error executing query 815: Model only answers one image question SQLs
Error executing query 816: Model only answers one image question SQLs
Error executing query 817: Model only answers one image question SQLs
Error executing query 818: Model abstains from answering the question
Error executing query 819: Expecting ). Line 1, Col: 822.
  microbiologyevents.charttime) = '2103' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 820: Invalid expression / Unexpected token. Line 1, Col: 966.
  etime('2105-12-31 23:59:00','-4 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 821: Model abstains from answering the question
[True]
[True]
Error executing query 823: Model only answers one image question SQLs
Error executing query 824: near "(": syntax error
Error executing query 827: Model abstains from answering the question
Error executing query 828: Invalid expression / Unexpected token. Line 1, Col: 821.
  ns.hadm_id from admissions where admissions.subject_id = 17253958 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 830: Model abstains from answering the question
Error executing query 831: Model only answers one image question SQLs
Error executing query 834: Model abstains from answering the question
Error executing query 835: Model only answers one image question SQLs
Error executing query 836: Model abstains from answering the question
Error executing query 837: Model abstains from answering the question
Error executing query 838: Model abstains from answering the question
Error executing query 841: Invalid expression / Unexpected token. Line 1, Col: 986.
  nth') = datetime('2105-12-31 23:59:00','start of month','-1 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 844: Invalid expression / Unexpected token. Line 1, Col: 879.
  hnical assessments in the left lower lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 845: Invalid expression / Unexpected token. Line 1, Col: 654.
  ns.hadm_id from admissions where admissions.subject_id = 12844682 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 847: Expecting ). Line 1, Col: 1008.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month') gro
Error executing query 848: Model abstains from answering the question
Error executing query 849: Model abstains from answering the question
Error executing query 850: Model only answers one image question SQLs
Error executing query 852: Model abstains from answering the question
Error executing query 854: Model abstains from answering the question
Error executing query 855: Invalid expression / Unexpected token. Line 1, Col: 826.
  ',prescriptions.starttime) = '2104-12' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 d
Error executing query 856: Expecting ). Line 1, Col: 852.
  etime('2105-12-31 23:59:00','-3 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 857: Invalid expression / Unexpected token. Line 1, Col: 653.
  any any anatomical findings in the aortic arch?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 858: Invalid expression / Unexpected token. Line 1, Col: 1129.
  s in the left upper lung zone on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.chart
Error executing query 859: Expecting ). Line 1, Col: 918.
  time) = '2102' ) as t2 join admissions on t2.subject_id = admissions.subject_id where t2.charttime  [4madmissions[0m.admittime and strftime('%Y',admissions.admittime) = '2102' and datetime(admissions.admittime) betwe
Error executing query 860: Model abstains from answering the question
Error executing query 862: Invalid expression / Unexpected token. Line 1, Col: 970.
  s.dischtime is not null order by admissions.admittime asc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 863: Model only answers one image question SQLs
Error executing query 865: Model only answers one image question SQLs
Error executing query 867: Model abstains from answering the question
Error executing query 868: Model abstains from answering the question
Error executing query 869: Model abstains from answering the question
Error executing query 870: Model abstains from answering the question
Error executing query 871: Model abstains from answering the question
Error executing query 872: Expecting ). Line 1, Col: 822.
  microbiologyevents.charttime) = '2103' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 874: Invalid expression / Unexpected token. Line 1, Col: 723.
  id = 11982468 ) and strftime('%Y',prescriptions.starttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 875: Model only answers one image question SQLs
Error executing query 879: Model abstains from answering the question
Error executing query 880: Model abstains from answering the question
Error executing query 881: Invalid expression / Unexpected token. Line 1, Col: 731.
  qa("does the chest x-ray indicate any diseases?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 882: Invalid expression / Unexpected token. Line 1, Col: 723.
   a chest x-ray showing any anatomical findings?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 883: Invalid expression / Unexpected token. Line 1, Col: 915.
  t in the left upper lung zone on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 884: Model abstains from answering the question
Error executing query 886: Model abstains from answering the question
Error executing query 888: Model only answers one image question SQLs
[False]
[False]
Error executing query 891: Model only answers one image question SQLs
Error executing query 896: Model only answers one image question SQLs
Error executing query 897: Model abstains from answering the question
Error executing query 898: Model abstains from answering the question
Error executing query 900: Model abstains from answering the question
Error executing query 902: Invalid expression / Unexpected token. Line 1, Col: 977.
  cated in the right upper lung zone on an x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 903: Invalid expression / Unexpected token. Line 1, Col: 746.
  indication of any tubes/lines on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 904: Invalid expression / Unexpected token. Line 1, Col: 877.
  nc_vqa("is any diseases shown on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 905: Model abstains from answering the question
Error executing query 906: Model abstains from answering the question
Error executing query 910: Invalid expression / Unexpected token. Line 1, Col: 959.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 911: Model abstains from answering the question
Error executing query 912: Invalid expression / Unexpected token. Line 1, Col: 837.
  ow swan-ganz catheter in the upper mediastinum?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 913: Model abstains from answering the question
Error executing query 914: Invalid expression / Unexpected token. Line 1, Col: 887.
  c_vqa("does a chest x-ray indicate any devices?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 917: Invalid expression / Unexpected token. Line 1, Col: 885.
  any abnormality revealed in the right clavicle?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 918: Model abstains from answering the question
Error executing query 920: Model only answers one image question SQLs
Error executing query 921: Model abstains from answering the question
Error executing query 925: Required keyword: 'expressions' missing for <class 'sqlglot.expressions.Aliases'>. Line 1, Col: 397.
  d from d_labitems where d_labitems.label ='sodium' ) order by labevents.charttime desc limit 1 )  ( [4mselect[0m labevents.valuenum from labevents where labevents.hadm_id in ( select admissions.hadm_id from admis
Error executing query 926: Model only answers one image question SQLs
Error executing query 927: Model abstains from answering the question
Error executing query 929: Model abstains from answering the question
Error executing query 930: Model abstains from answering the question
Error executing query 931: Invalid expression / Unexpected token. Line 1, Col: 756.
  ns.hadm_id from admissions where admissions.subject_id = 10680329 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 932: Invalid expression / Unexpected token. Line 1, Col: 955.
  gnoses_icd.charttime) = datetime('2105-12-31 23:59:00','-39 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 933: Model only answers one image question SQLs
Error executing query 934: Model abstains from answering the question
Error executing query 935: Invalid expression / Unexpected token. Line 1, Col: 842.
  unc_vqa("is any anatomical findings identified?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 937: Invalid expression / Unexpected token. Line 1, Col: 789.
  ns.hadm_id from admissions where admissions.subject_id = 17011771 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 938: Model abstains from answering the question
Error executing query 940: Model abstains from answering the question
Error executing query 941: Model abstains from answering the question
Error executing query 942: Expecting ). Line 1, Col: 661.
  ogyevents.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 943: Model abstains from answering the question
Error executing query 944: Model abstains from answering the question
Error executing query 945: Model abstains from answering the question
Error executing query 946: Model abstains from answering the question
Error executing query 947: Model abstains from answering the question
Error executing query 948: Expecting ). Line 1, Col: 920.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 949: Model only answers one image question SQLs
Error executing query 950: Invalid expression / Unexpected token. Line 1, Col: 747.
  ay show any diseases in the left hemidiaphragm?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 952: Invalid expression / Unexpected token. Line 1, Col: 730.
  a("does a chest x-ray show any any abnormality?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 955: Model abstains from answering the question
Error executing query 956: Model only answers one image question SQLs
Error executing query 957: Invalid expression / Unexpected token. Line 1, Col: 615.
  ere prescriptions.drug = 'clopidogrel' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 958: Model abstains from answering the question
Error executing query 959: Model abstains from answering the question
Error executing query 960: Model abstains from answering the question
Error executing query 963: Model abstains from answering the question
Error executing query 964: Model abstains from answering the question
Error executing query 968: Model abstains from answering the question
Error executing query 969: Invalid expression / Unexpected token. Line 1, Col: 747.
  ns.hadm_id from admissions where admissions.subject_id = 15526304 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 970: Invalid expression / Unexpected token. Line 1, Col: 798.
   of any technical assessments on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 971: Model abstains from answering the question
Error executing query 974: Model abstains from answering the question
Error executing query 975: Model abstains from answering the question
Error executing query 976: Invalid expression / Unexpected token. Line 1, Col: 1023.
  e('%m',prescriptions.starttime) = '10' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id
Error executing query 978: Invalid expression / Unexpected token. Line 1, Col: 896.
  umes shown in the mediastinum on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 980: Model abstains from answering the question
Error executing query 981: Model only answers one image question SQLs
Error executing query 982: Model abstains from answering the question
Error executing query 983: Model abstains from answering the question
Error executing query 986: Model abstains from answering the question
Error executing query 987: Model only answers one image question SQLs
Error executing query 989: Model abstains from answering the question
Error executing query 992: Invalid expression / Unexpected token. Line 1, Col: 970.
  a chest x-ray show chest port in the left lung?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 993: Model only answers one image question SQLs
Error executing query 995: Invalid expression / Unexpected token. Line 1, Col: 620.
  qa("does a chest x-ray depicts any abnormality?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 996: Invalid expression / Unexpected token. Line 1, Col: 884.
  ny any tubes/lines in the left lower lung zone?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 998: Model abstains from answering the question
Error executing query 999: Invalid expression / Unexpected token. Line 1, Col: 976.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
Error executing query 1001: Invalid expression / Unexpected token. Line 1, Col: 827.
  scriptions.starttime) = datetime('2105-12-31 23:59:00','-38 month') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1004: Invalid expression / Unexpected token. Line 1, Col: 630.
  ns.hadm_id from admissions where admissions.subject_id = 15650925 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1005: Model abstains from answering the question
Error executing query 1006: Invalid expression / Unexpected token. Line 1, Col: 750.
  ed in the right mid lung zone on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 1007: Model only answers one image question SQLs
Error executing query 1008: Expecting ). Line 1, Col: 789.
  me('%Y',labevents.charttime) >= '2105' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 1009: Model abstains from answering the question
Error executing query 1010: Model abstains from answering the question
Error executing query 1011: Model abstains from answering the question
Error executing query 1012: Model abstains from answering the question
Error executing query 1014: Model abstains from answering the question
Error executing query 1015: Model abstains from answering the question
Error executing query 1016: Model abstains from answering the question
Error executing query 1020: Model only answers one image question SQLs
Error executing query 1021: Model abstains from answering the question
Error executing query 1023: Model abstains from answering the question
Error executing query 1024: Model abstains from answering the question
Error executing query 1025: Model abstains from answering the question
Error executing query 1026: Model only answers one image question SQLs
Error executing query 1027: Model abstains from answering the question
Error executing query 1029: Invalid expression / Unexpected token. Line 1, Col: 727.
  ny diseases revealed in the left hemidiaphragm?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 1030: Model abstains from answering the question
Error executing query 1033: Invalid expression / Unexpected token. Line 1, Col: 909.
  gnoses_icd.charttime) >= datetime('2105-12-31 23:59:00','-7 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1036: Model abstains from answering the question
Error executing query 1037: Model abstains from answering the question
Error executing query 1041: Model abstains from answering the question
Error executing query 1042: Model only answers one image question SQLs
Error executing query 1043: Model only answers one image question SQLs
Error executing query 1044: Model abstains from answering the question
Error executing query 1046: Model abstains from answering the question
Error executing query 1047: Model abstains from answering the question
Error executing query 1048: Model abstains from answering the question
Error executing query 1049: Model abstains from answering the question
Error executing query 1051: Invalid expression / Unexpected token. Line 1, Col: 865.
  nth') = datetime('2105-12-31 23:59:00','start of month','-0 month') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1052: Model abstains from answering the question
Error executing query 1053: Model abstains from answering the question
Error executing query 1055: near "(": syntax error
Error executing query 1056: Model only answers one image question SQLs
Error executing query 1057: Invalid expression / Unexpected token. Line 1, Col: 740.
  indication of any abnormality on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1058: Invalid expression / Unexpected token. Line 1, Col: 611.
  c_vqa("does a chest x-ray show any abnormality?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 1059: Model abstains from answering the question
Error executing query 1060: Model abstains from answering the question
Error executing query 1061: Invalid expression / Unexpected token. Line 1, Col: 989.
  etime('2105-12-31 23:59:00','-6 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id
Error executing query 1062: Model abstains from answering the question
Error executing query 1063: Model abstains from answering the question
Error executing query 1064: Model abstains from answering the question
Error executing query 1065: Expecting ). Line 1, Col: 825.
  etime('2105-12-31 23:59:00','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 5
Error executing query 1066: Model only answers one image question SQLs
Error executing query 1068: Model only answers one image question SQLs
Error executing query 1072: Invalid expression / Unexpected token. Line 1, Col: 818.
  escriptions.starttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
[False]
Error executing query 1076: Model abstains from answering the question
Error executing query 1078: Model abstains from answering the question
Error executing query 1081: Model abstains from answering the question
Error executing query 1083: Model abstains from answering the question
Error executing query 1084: Model only answers one image question SQLs
Error executing query 1085: Model abstains from answering the question
Error executing query 1086: Expecting ). Line 1, Col: 1048.
  ar','-1 year') ) as t2 join admissions on t2.subject_id = admissions.subject_id where t2.charttime  [4madmissions[0m.admittime and datetime(admissions.admittime,'start of year') = datetime('2105-12-31 23:59:00','star
Error executing query 1089: Invalid expression / Unexpected token. Line 1, Col: 956.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1092: Model abstains from answering the question
Error executing query 1093: Model abstains from answering the question
Error executing query 1094: Model abstains from answering the question
Error executing query 1095: Model abstains from answering the question
Error executing query 1097: Model abstains from answering the question
Error executing query 1098: Invalid expression / Unexpected token. Line 1, Col: 861.
  show any tubes/lines in the cardiac silhouette?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 1099: Model only answers one image question SQLs
Error executing query 1101: Model abstains from answering the question
Error executing query 1102: Model abstains from answering the question
Error executing query 1103: Model abstains from answering the question
Error executing query 1104: Invalid expression / Unexpected token. Line 1, Col: 754.
  ns.hadm_id from admissions where admissions.subject_id = 17466107 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1105: Model abstains from answering the question
Error executing query 1106: Model abstains from answering the question
Error executing query 1107: Model only answers one image question SQLs
Error executing query 1108: Model only answers one image question SQLs
Error executing query 1110: Model abstains from answering the question
Error executing query 1111: Model abstains from answering the question
Error executing query 1113: Model abstains from answering the question
Error executing query 1114: Model abstains from answering the question
Error executing query 1115: Model only answers one image question SQLs
Error executing query 1116: Model only answers one image question SQLs
Error executing query 1120: Model only answers one image question SQLs
Error executing query 1121: Model only answers one image question SQLs
Error executing query 1124: Model abstains from answering the question
Error executing query 1127: Invalid expression / Unexpected token. Line 1, Col: 908.
  23:59:00','start of month','-0 month') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id
Error executing query 1128: Invalid expression / Unexpected token. Line 1, Col: 770.
  trated any tubes/lines in the right chest wall?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 1129: Model abstains from answering the question
Error executing query 1130: Model only answers one image question SQLs
[True]
Error executing query 1132: Model abstains from answering the question
Error executing query 1133: Model only answers one image question SQLs
Error executing query 1134: Model abstains from answering the question
Error executing query 1135: Invalid expression / Unexpected token. Line 1, Col: 852.
  id = 13724767 ) and strftime('%Y',diagnoses_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1136: Model only answers one image question SQLs
Error executing query 1139: Model abstains from answering the question
Error executing query 1140: Model abstains from answering the question
Error executing query 1141: Model only answers one image question SQLs
Error executing query 1142: Model only answers one image question SQLs
Error executing query 1144: Model abstains from answering the question
Error executing query 1145: Model abstains from answering the question
Error executing query 1146: Model abstains from answering the question
Error executing query 1148: Model abstains from answering the question
Error executing query 1150: Invalid expression / Unexpected token. Line 1, Col: 756.
  hown in the upper mediastinum on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1152: Model abstains from answering the question
Error executing query 1158: Model only answers one image question SQLs
Error executing query 1159: Model abstains from answering the question
Error executing query 1162: Model abstains from answering the question
Error executing query 1164: Error tokenizing 'tetime(t1.charttime) and datetime(t1.charttime,'+'
Error executing query 1173: Invalid expression / Unexpected token. Line 1, Col: 894.
  n hydropneumothorax in the right mid lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1174: Model only answers one image question SQLs
Error executing query 1175: Model abstains from answering the question
Error executing query 1176: Invalid expression / Unexpected token. Line 1, Col: 900.
  wires in the right chest wall on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 1177: Model abstains from answering the question
Error executing query 1179: Invalid expression / Unexpected token. Line 1, Col: 931.
  agnoses_icd.charttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1180: Expecting ). Line 1, Col: 963.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1182: Model abstains from answering the question
Error executing query 1183: Model only answers one image question SQLs
Error executing query 1185: Invalid expression / Unexpected token. Line 1, Col: 795.
  escriptions.starttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 1186: Model only answers one image question SQLs
Error executing query 1187: Invalid expression / Unexpected token. Line 1, Col: 668.
  ns.hadm_id from admissions where admissions.subject_id = 16300198 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1190: Model abstains from answering the question
Error executing query 1191: Model abstains from answering the question
Error executing query 1192: near "(": syntax error
Error executing query 1193: Invalid expression / Unexpected token. Line 1, Col: 654.
  ns.hadm_id from admissions where admissions.subject_id = 15978979 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1194: Model abstains from answering the question
Error executing query 1198: Model abstains from answering the question
Error executing query 1199: Model only answers one image question SQLs
Error executing query 1200: Invalid expression / Unexpected token. Line 1, Col: 898.
  id = 14851188 ) and strftime('%Y',diagnoses_icd.charttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1203: Invalid expression / Unexpected token. Line 1, Col: 765.
  y anatomical findings in the right apical zone?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1205: near "(": syntax error
Error executing query 1208: Invalid expression / Unexpected token. Line 1, Col: 852.
  id = 14637230 ) and strftime('%Y',diagnoses_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1211: Model abstains from answering the question
Error executing query 1212: Model abstains from answering the question
Error executing query 1213: Model only answers one image question SQLs
Error executing query 1214: near "(": syntax error
Error executing query 1215: Model only answers one image question SQLs
Error executing query 1216: Model only answers one image question SQLs
Error executing query 1217: Model abstains from answering the question
Error executing query 1219: Model abstains from answering the question
Error executing query 1220: Model abstains from answering the question
Error executing query 1222: Invalid expression / Unexpected token. Line 1, Col: 932.
  agnoses_icd.charttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1223: Model only answers one image question SQLs
Error executing query 1224: Invalid expression / Unexpected token. Line 1, Col: 1080.
  reveal any diseases in the right mid lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 1226: Model abstains from answering the question
Error executing query 1227: Model abstains from answering the question
Error executing query 1228: Model abstains from answering the question
Error executing query 1229: Model abstains from answering the question
Error executing query 1231: Model abstains from answering the question
Error executing query 1233: Model abstains from answering the question
Error executing query 1234: Model abstains from answering the question
Error executing query 1236: Invalid expression / Unexpected token. Line 1, Col: 887.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 1237: Model abstains from answering the question
Error executing query 1238: Model only answers one image question SQLs
Error executing query 1239: Expecting ). Line 1, Col: 788.
  etime('2105-12-31 23:59:00','-5 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1241: Expecting ). Line 1, Col: 990.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1242: Model abstains from answering the question
Error executing query 1243: Expecting ). Line 1, Col: 730.
  '%Y',prescriptions.starttime) = '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month') gro
Error executing query 1244: Invalid expression / Unexpected token. Line 1, Col: 940.
  71014 ) and strftime('%Y-%m',procedures_icd.charttime) >= '2103-06' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1248: Invalid expression / Unexpected token. Line 1, Col: 767.
  %Y',prescriptions.starttime) >= '2101' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month')
Error executing query 1249: Model only answers one image question SQLs
Error executing query 1250: Model only answers one image question SQLs
Error executing query 1252: Model abstains from answering the question
Error executing query 1253: Model only answers one image question SQLs
Error executing query 1254: Model only answers one image question SQLs
Error executing query 1255: Invalid expression / Unexpected token. Line 1, Col: 814.
  ns.hadm_id from admissions where admissions.subject_id = 14851188 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1256: Model abstains from answering the question
Error executing query 1257: Expecting ). Line 1, Col: 778.
  '%Y',prescriptions.starttime) = '2103' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 3
Error executing query 1259: Model abstains from answering the question
Error executing query 1260: Invalid expression / Unexpected token. Line 1, Col: 915.
  mality in the left chest wall on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1261: Invalid expression / Unexpected token. Line 1, Col: 1136.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id
Error executing query 1262: Model only answers one image question SQLs
Error executing query 1263: Model abstains from answering the question
Error executing query 1264: Model abstains from answering the question
Error executing query 1265: Model abstains from answering the question
Error executing query 1266: Invalid expression / Unexpected token. Line 1, Col: 859.
  s.dischtime is not null order by admissions.admittime asc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1269: Model abstains from answering the question
Error executing query 1271: Invalid expression / Unexpected token. Line 1, Col: 890.
   func_vqa("does a chest x-ray show any devices?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 1273: Model abstains from answering the question
Error executing query 1274: Model abstains from answering the question
Error executing query 1275: Expecting ). Line 1, Col: 831.
  %Y',procedures_icd.charttime) = '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 1276: Model abstains from answering the question
Error executing query 1278: Model abstains from answering the question
Error executing query 1279: Model abstains from answering the question
Error executing query 1280: Model abstains from answering the question
Error executing query 1281: Model only answers one image question SQLs
Error executing query 1282: Model abstains from answering the question
Error executing query 1283: Model abstains from answering the question
Error executing query 1284: Model abstains from answering the question
Error executing query 1285: Model only answers one image question SQLs
Error executing query 1286: Model only answers one image question SQLs
Error executing query 1288: Model abstains from answering the question
Error executing query 1289: Model abstains from answering the question
Error executing query 1291: Model abstains from answering the question
Error executing query 1294: Model only answers one image question SQLs
Error executing query 1296: Model abstains from answering the question
Error executing query 1297: near "(": syntax error
Error executing query 1298: Model only answers one image question SQLs
Error executing query 1300: Invalid expression / Unexpected token. Line 1, Col: 791.
  ns.hadm_id from admissions where admissions.subject_id = 12429112 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1302: Invalid expression / Unexpected token. Line 1, Col: 880.
   shown in the left chest wall on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 1303: Model abstains from answering the question
Error executing query 1304: Invalid expression / Unexpected token. Line 1, Col: 990.
  picting any abnormality in the left chest wall?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1305: Model only answers one image question SQLs
Error executing query 1306: Invalid expression / Unexpected token. Line 1, Col: 864.
  ("is the chest x-ray revealing any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 1307: Model only answers one image question SQLs
Error executing query 1308: Model abstains from answering the question
Error executing query 1310: Model only answers one image question SQLs
Error executing query 1311: Model only answers one image question SQLs
Error executing query 1313: Model abstains from answering the question
Error executing query 1314: near "(": syntax error
Error executing query 1315: Expecting ). Line 1, Col: 914.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 1316: Model only answers one image question SQLs
Error executing query 1317: Model abstains from answering the question
Error executing query 1318: Invalid expression / Unexpected token. Line 1, Col: 870.
  %Y',diagnoses_icd.charttime) >= '2101' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
Error executing query 1319: Model abstains from answering the question
Error executing query 1320: Model abstains from answering the question
Error executing query 1321: Model only answers one image question SQLs
Error executing query 1324: Model abstains from answering the question
Error executing query 1325: Model abstains from answering the question
Error executing query 1326: Model only answers one image question SQLs
Error executing query 1328: Model only answers one image question SQLs
Error executing query 1333: Model only answers one image question SQLs
Error executing query 1334: Model abstains from answering the question
Error executing query 1336: Model abstains from answering the question
Error executing query 1337: Model abstains from answering the question
Error executing query 1339: Model abstains from answering the question
Error executing query 1341: Model abstains from answering the question
Error executing query 1343: Model abstains from answering the question
Error executing query 1345: Invalid expression / Unexpected token. Line 1, Col: 853.
  ("does a chest x-ray indicate subcutaneous air?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 1347: Model abstains from answering the question
Error executing query 1349: Model abstains from answering the question
Error executing query 1350: Invalid expression / Unexpected token. Line 1, Col: 636.
  ns.hadm_id from admissions where admissions.subject_id = 16178416 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 1351: Model only answers one image question SQLs
Error executing query 1352: Model abstains from answering the question
Error executing query 1353: Model abstains from answering the question
Error executing query 1354: Model abstains from answering the question
Error executing query 1355: Invalid expression / Unexpected token. Line 1, Col: 867.
  id = 19998497 ) and strftime('%Y',diagnoses_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1357: Model only answers one image question SQLs
Error executing query 1358: Invalid expression / Unexpected token. Line 1, Col: 756.
  ns.hadm_id from admissions where admissions.subject_id = 13724767 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1359: Model abstains from answering the question
Error executing query 1360: Model only answers one image question SQLs
Error executing query 1361: Invalid expression / Unexpected token. Line 1, Col: 943.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1362: Invalid expression / Unexpected token. Line 1, Col: 901.
  %Y',procedures_icd.charttime) = '2100' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
Error executing query 1363: Model abstains from answering the question
Error executing query 1364: Model only answers one image question SQLs
Error executing query 1365: Model abstains from answering the question
Error executing query 1366: Invalid expression / Unexpected token. Line 1, Col: 754.
  ay indicate any any abnormality in the abdomen?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1367: Model abstains from answering the question
Error executing query 1368: Invalid expression / Unexpected token. Line 1, Col: 973.
   year','-1 year') and strftime('%m',prescriptions.starttime) = '05' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1370: Model abstains from answering the question
Error executing query 1371: Model abstains from answering the question
Error executing query 1373: Model abstains from answering the question
Error executing query 1374: Model abstains from answering the question
Error executing query 1375: Model abstains from answering the question
Error executing query 1377: Invalid expression / Unexpected token. Line 1, Col: 790.
  r by admissions.admittime desc limit 1 ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 d
Error executing query 1380: Invalid expression / Unexpected token. Line 1, Col: 897.
  id = 16116913 ) and strftime('%Y',diagnoses_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1382: Model abstains from answering the question
Error executing query 1383: Model only answers one image question SQLs
Error executing query 1384: Expecting ). Line 1, Col: 900.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 1385: Model abstains from answering the question
Error executing query 1386: Model abstains from answering the question
Error executing query 1387: Model abstains from answering the question
Error executing query 1389: Model abstains from answering the question
Error executing query 1391: Model only answers one image question SQLs
Error executing query 1392: Model abstains from answering the question
Error executing query 1393: Invalid expression / Unexpected token. Line 1, Col: 771.
  dication of hydropneumothorax on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 1395: Invalid expression / Unexpected token. Line 1, Col: 857.
  5649581 ) and strftime('%Y-%m',diagnoses_icd.charttime) = '2105-10' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1396: Invalid expression / Unexpected token. Line 1, Col: 713.
  %Y',prescriptions.starttime) >= '2103' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month')
Error executing query 1397: Expecting ). Line 1, Col: 874.
  etime('2105-12-31 23:59:00','-5 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1399: Invalid expression / Unexpected token. Line 1, Col: 903.
  oes a chest x-ray show multiple masses/nodules?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 1402: Model abstains from answering the question
Error executing query 1403: Invalid expression / Unexpected token. Line 1, Col: 1004.
  ices in the upper mediastinum on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 1404: Model only answers one image question SQLs
Error executing query 1405: Expecting ). Line 1, Col: 888.
  etime('2105-12-31 23:59:00','-4 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.test_name ) as t3 where t3.c1 = 4
Error executing query 1406: Model abstains from answering the question
Error executing query 1407: Model abstains from answering the question
Error executing query 1408: Model abstains from answering the question
Error executing query 1409: Invalid expression / Unexpected token. Line 1, Col: 649.
  ed any tubes/lines in the left upper lung zone?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1412: Model abstains from answering the question
Error executing query 1413: Model abstains from answering the question
Error executing query 1414: Model abstains from answering the question
Error executing query 1415: Model abstains from answering the question
Error executing query 1416: Invalid expression / Unexpected token. Line 1, Col: 905.
  c_vqa("does a chest x-ray show any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 1417: Model abstains from answering the question
Error executing query 1418: Model only answers one image question SQLs
Error executing query 1419: Invalid expression / Unexpected token. Line 1, Col: 853.
  s a chest x-ray show any technical assessments?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1420: Model abstains from answering the question
Error executing query 1423: Model only answers one image question SQLs
Error executing query 1425: Model only answers one image question SQLs
Error executing query 1428: Model only answers one image question SQLs
Error executing query 1429: Model abstains from answering the question
Error executing query 1430: Model abstains from answering the question
Error executing query 1431: Model abstains from answering the question
Error executing query 1435: Invalid expression / Unexpected token. Line 1, Col: 886.
  x-ray show lung lesion in the left apical zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 1437: Expecting ). Line 1, Col: 802.
  microbiologyevents.charttime) = '2101' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1438: Model abstains from answering the question
Error executing query 1439: Model only answers one image question SQLs
Error executing query 1440: Invalid expression / Unexpected token. Line 1, Col: 865.
  anatomical findings in the right mid lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1441: Model only answers one image question SQLs
Error executing query 1443: Model only answers one image question SQLs
Error executing query 1444: Model abstains from answering the question
Error executing query 1447: Model abstains from answering the question
Error executing query 1448: Model only answers one image question SQLs
Error executing query 1449: Model abstains from answering the question
Error executing query 1450: Invalid expression / Unexpected token. Line 1, Col: 746.
  observed in the left shoulder on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1451: Model abstains from answering the question
Error executing query 1452: Model only answers one image question SQLs
Error executing query 1454: Invalid expression / Unexpected token. Line 1, Col: 788.
  ("is any abnormality observed on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1455: Expecting ). Line 1, Col: 732.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.starttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.starttime) and datetime(t1.starttime,'+2 m
Error executing query 1458: Expecting ). Line 1, Col: 903.
  etime('2105-12-31 23:59:00','-4 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.spec_type_desc ) as t3 where t3.c1 = 4
Error executing query 1461: Model abstains from answering the question
Error executing query 1463: Invalid expression / Unexpected token. Line 1, Col: 954.
   reveal pneumothorax in the left mid lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1465: Model abstains from answering the question
Error executing query 1469: near "(": syntax error
Error executing query 1471: Invalid expression / Unexpected token. Line 1, Col: 998.
  12873 ) and strftime('%Y-%m',procedures_icd.charttime) >= '2105-05' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and t1.hadm_id = t3.hadm_id
Error executing query 1472: Model abstains from answering the question
Error executing query 1473: Model only answers one image question SQLs
Error executing query 1474: Model only answers one image question SQLs
Error executing query 1475: Model abstains from answering the question
Error executing query 1476: Model abstains from answering the question
Error executing query 1477: Model only answers one image question SQLs
Error executing query 1478: Model only answers one image question SQLs
Error executing query 1481: Model abstains from answering the question
Error executing query 1482: Model abstains from answering the question
Error executing query 1483: Model abstains from answering the question
Error executing query 1487: Model only answers one image question SQLs
Error executing query 1488: Model only answers one image question SQLs
Error executing query 1490: Model abstains from answering the question
Error executing query 1493: Model only answers one image question SQLs
Error executing query 1494: Invalid expression / Unexpected token. Line 1, Col: 777.
  er by admissions.admittime asc limit 1 ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of day') = datetime(t2.starttime,'start of day')
Error executing query 1495: Invalid expression / Unexpected token. Line 1, Col: 861.
  .dischtime is not null order by admissions.admittime desc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1497: Invalid expression / Unexpected token. Line 1, Col: 961.
  indication of any abnormality on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 1499: Model abstains from answering the question
Error executing query 1500: Model only answers one image question SQLs
Error executing query 1501: Expecting ). Line 1, Col: 817.
  microbiologyevents.charttime) = '2101' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1502: Model abstains from answering the question
Error executing query 1503: Invalid expression / Unexpected token. Line 1, Col: 910.
  edures_icd.charttime) >= datetime('2105-12-31 23:59:00','-6 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1504: Invalid expression / Unexpected token. Line 1, Col: 762.
  c_vqa("has a chest x-ray shown any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 1505: Model abstains from answering the question
Error executing query 1506: Expecting ). Line 1, Col: 952.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1507: Model abstains from answering the question
Error executing query 1509: Invalid expression / Unexpected token. Line 1, Col: 1025.
  16528 ) and strftime('%Y-%m',procedures_icd.charttime) >= '2103-12' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and t1.hadm_id = t3.hadm_id
Error executing query 1510: Model only answers one image question SQLs
Error executing query 1512: Model abstains from answering the question
Error executing query 1513: Expecting ). Line 1, Col: 910.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month') gro
Error executing query 1514: Model only answers one image question SQLs
Error executing query 1515: Model abstains from answering the question
Error executing query 1516: Invalid expression / Unexpected token. Line 1, Col: 854.
  c_vqa("does a chest x-ray show any abnormality?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 1519: Model only answers one image question SQLs
Error executing query 1522: Model only answers one image question SQLs
Error executing query 1524: Model only answers one image question SQLs
Error executing query 1525: Model only answers one image question SQLs
Error executing query 1526: Invalid expression / Unexpected token. Line 1, Col: 934.
  cedures_icd.charttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1527: Model only answers one image question SQLs
Error executing query 1528: Invalid expression / Unexpected token. Line 1, Col: 896.
  y in the left lower lung zone on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 1529: Model abstains from answering the question
Error executing query 1531: Model abstains from answering the question
Error executing query 1534: Model abstains from answering the question
Error executing query 1535: Model abstains from answering the question
Error executing query 1536: Model abstains from answering the question
Error executing query 1540: Model abstains from answering the question
Error executing query 1541: Model only answers one image question SQLs
Error executing query 1543: Model abstains from answering the question
Error executing query 1544: Invalid expression / Unexpected token. Line 1, Col: 900.
  d = 16684992 ) and strftime('%Y',procedures_icd.charttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1546: Invalid expression / Unexpected token. Line 1, Col: 621.
   the chest x-ray indicate any low lung volumes?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1547: Invalid expression / Unexpected token. Line 1, Col: 802.
   x-ray reveal any pulmonary edema/hazy opacity?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1549: Invalid expression / Unexpected token. Line 1, Col: 938.
  etime('2105-12-31 23:59:00','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id
Error executing query 1551: Expecting ). Line 1, Col: 847.
  me('%Y',labevents.charttime) >= '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 1552: Model abstains from answering the question
Error executing query 1554: Invalid expression / Unexpected token. Line 1, Col: 652.
  ns.hadm_id from admissions where admissions.subject_id = 13833101 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1557: Invalid expression / Unexpected token. Line 1, Col: 809.
  cts any tubes/lines in the right hemidiaphragm?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1558: Model only answers one image question SQLs
Error executing query 1563: Invalid expression / Unexpected token. Line 1, Col: 900.
   a finding of any tubes/lines on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1565: Invalid expression / Unexpected token. Line 1, Col: 908.
  Y',procedures_icd.charttime) >= '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id
Error executing query 1566: Invalid expression / Unexpected token. Line 1, Col: 891.
  c_vqa("does a chest x-ray show any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 1567: Model only answers one image question SQLs
Error executing query 1568: Invalid expression / Unexpected token. Line 1, Col: 931.
  agnoses_icd.charttime) >= datetime('2105-12-31 23:59:00','-5 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1569: Model abstains from answering the question
Error executing query 1570: Model abstains from answering the question
Error executing query 1572: Invalid expression / Unexpected token. Line 1, Col: 873.
  etime('2105-12-31 23:59:00','-4 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id
Error executing query 1574: Model abstains from answering the question
Error executing query 1575: Model abstains from answering the question
Error executing query 1577: Model only answers one image question SQLs
Error executing query 1581: Model abstains from answering the question
Error executing query 1582: Model abstains from answering the question
Error executing query 1583: Model only answers one image question SQLs
Error executing query 1584: Model abstains from answering the question
Error executing query 1587: Model abstains from answering the question
Error executing query 1589: Model abstains from answering the question
Error executing query 1591: Model abstains from answering the question
Error executing query 1592: Model only answers one image question SQLs
Error executing query 1593: Invalid expression / Unexpected token. Line 1, Col: 938.
  etime('2105-12-31 23:59:00','-4 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id
Error executing query 1595: Model abstains from answering the question
Error executing query 1596: Model abstains from answering the question
Error executing query 1599: Model only answers one image question SQLs
Error executing query 1600: Model abstains from answering the question
Error executing query 1601: Invalid expression / Unexpected token. Line 1, Col: 853.
  est x-ray indicate spinal degenerative changes?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 1602: Invalid expression / Unexpected token. Line 1, Col: 970.
  c_vqa("does a chest x-ray show any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1603: Model only answers one image question SQLs
Error executing query 1604: Invalid expression / Unexpected token. Line 1, Col: 971.
   overload/heart failure shown on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 1605: Invalid expression / Unexpected token. Line 1, Col: 837.
  ns.hadm_id from admissions where admissions.subject_id = 10518993 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1606: Invalid expression / Unexpected token. Line 1, Col: 825.
  escriptions.starttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 1607: Invalid expression / Unexpected token. Line 1, Col: 728.
  d = 12930426 ) and strftime('%Y',prescriptions.starttime) >= '2103' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 1608: Model only answers one image question SQLs
Error executing query 1609: Invalid expression / Unexpected token. Line 1, Col: 1060.
  76036 ) and strftime('%Y-%m',procedures_icd.charttime) >= '2104-02' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and t1.hadm_id = t3.hadm_id
Error executing query 1611: Model abstains from answering the question
Error executing query 1612: Model abstains from answering the question
Error executing query 1613: Model abstains from answering the question
Error executing query 1615: Invalid expression / Unexpected token. Line 1, Col: 828.
  ny technical assessments indicated on an x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1616: Invalid expression / Unexpected token. Line 1, Col: 920.
  agnoses_icd.charttime) >= datetime('2105-12-31 23:59:00','-2 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1617: Model abstains from answering the question
Error executing query 1619: Model abstains from answering the question
Error executing query 1620: Model abstains from answering the question
Error executing query 1621: Model abstains from answering the question
Error executing query 1622: Model abstains from answering the question
Error executing query 1623: Model abstains from answering the question
Error executing query 1625: Expecting ). Line 1, Col: 771.
  '%Y',prescriptions.starttime) = '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 3
Error executing query 1626: Model only answers one image question SQLs
Error executing query 1627: Model abstains from answering the question
Error executing query 1628: Model abstains from answering the question
Error executing query 1630: Invalid expression / Unexpected token. Line 1, Col: 808.
  how any any abnormality in the left chest wall?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 1632: Invalid expression / Unexpected token. Line 1, Col: 870.
  _vqa("does a chest x-ray indicate any diseases?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1633: Required keyword: 'expressions' missing for <class 'sqlglot.expressions.Aliases'>. Line 1, Col: 505.
  ate' and d_items.linksto = 'chartevents' ) order by chartevents.charttime asc limit 1 offset 1 )  ( [4mselect[0m chartevents.valuenum from chartevents where chartevents.stay_id in ( select icustays.stay_id from i
Error executing query 1634: Model abstains from answering the question
[False]
Error executing query 1636: Model abstains from answering the question
Error executing query 1637: Invalid expression / Unexpected token. Line 1, Col: 792.
  re an indication of scoliosis on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1639: Model only answers one image question SQLs
Error executing query 1641: Invalid expression / Unexpected token. Line 1, Col: 941.
  func_vqa("does an x-ray reveal any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 1643: Model abstains from answering the question
Error executing query 1644: Model abstains from answering the question
Error executing query 1645: Model abstains from answering the question
Error executing query 1646: Invalid expression / Unexpected token. Line 1, Col: 940.
  y shown any abnormality in the left chest wall?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 1649: Model abstains from answering the question
Error executing query 1650: Model only answers one image question SQLs
Error executing query 1653: Model abstains from answering the question
Error executing query 1654: Model abstains from answering the question
Error executing query 1656: Model abstains from answering the question
Error executing query 1657: Invalid expression / Unexpected token. Line 1, Col: 856.
  c_vqa("does a chest x-ray show spinal fracture?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1658: Invalid expression / Unexpected token. Line 1, Col: 976.
   chest x-ray show pleural/parenchymal scarring?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1660: Model only answers one image question SQLs
Error executing query 1661: Model abstains from answering the question
Error executing query 1664: Model abstains from answering the question
Error executing query 1665: Expecting ). Line 1, Col: 787.
  labevents.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.itemid ) as t3 where t3.c1 = 5 )
Error executing query 1666: Model abstains from answering the question
Error executing query 1668: Model abstains from answering the question
Error executing query 1669: Invalid expression / Unexpected token. Line 1, Col: 767.
  ny anatomical findings in the right chest wall?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 1670: Model abstains from answering the question
Error executing query 1671: Model only answers one image question SQLs
Error executing query 1672: Model abstains from answering the question
Error executing query 1674: Invalid expression / Unexpected token. Line 1, Col: 922.
  gnoses_icd.charttime) >= datetime('2105-12-31 23:59:00','-2 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1675: Model abstains from answering the question
Error executing query 1676: Model abstains from answering the question
Error executing query 1677: Model abstains from answering the question
Error executing query 1679: Expecting ). Line 1, Col: 871.
  etime('2105-12-31 23:59:00','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1680: Model abstains from answering the question
Error executing query 1682: Model only answers one image question SQLs
Error executing query 1683: Invalid expression / Unexpected token. Line 1, Col: 928.
   consolidation in the right costophrenic angle?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 1684: Invalid expression / Unexpected token. Line 1, Col: 899.
  c_vqa("does a chest x-ray show any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 1686: Model abstains from answering the question
Error executing query 1687: Invalid expression / Unexpected token. Line 1, Col: 699.
  where admissions.subject_id = 13880645 ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id
Error executing query 1688: Model only answers one image question SQLs
Error executing query 1689: Model abstains from answering the question
Error executing query 1690: Invalid expression / Unexpected token. Line 1, Col: 940.
  551252 ) and strftime('%Y-%m',procedures_icd.charttime) = '2105-10' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1692: Model abstains from answering the question
Error executing query 1693: Invalid expression / Unexpected token. Line 1, Col: 744.
  id = 14661031 ) and strftime('%Y',prescriptions.starttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 1694: Model abstains from answering the question
Error executing query 1695: Model abstains from answering the question
Error executing query 1696: Model only answers one image question SQLs
Error executing query 1698: Model abstains from answering the question
Error executing query 1700: Model abstains from answering the question
Error executing query 1703: Invalid expression / Unexpected token. Line 1, Col: 956.
  edures_icd.charttime) >= datetime('2105-12-31 23:59:00','-7 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1704: Invalid expression / Unexpected token. Line 1, Col: 766.
  evealed any diseases in the left hemidiaphragm?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 1705: Model abstains from answering the question
Error executing query 1706: Model abstains from answering the question
Error executing query 1707: Model abstains from answering the question
Error executing query 1708: Invalid expression / Unexpected token. Line 1, Col: 917.
  cedures_icd.charttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1709: Model abstains from answering the question
Error executing query 1711: Model only answers one image question SQLs
Error executing query 1712: Model abstains from answering the question
[True]
[True]
Error executing query 1715: Model abstains from answering the question
Error executing query 1716: Invalid expression / Unexpected token. Line 1, Col: 995.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1718: Invalid expression / Unexpected token. Line 1, Col: 849.
  d = 15647220 ) and strftime('%Y',diagnoses_icd.charttime) >= '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1721: Expecting ). Line 1, Col: 856.
  microbiologyevents.charttime) = '2101' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.test_name ) as t3 where t3.c1 = 4
Error executing query 1723: Model only answers one image question SQLs
Error executing query 1725: Model abstains from answering the question
Error executing query 1726: Model only answers one image question SQLs
Error executing query 1727: Model abstains from answering the question
Error executing query 1729: Invalid expression / Unexpected token. Line 1, Col: 770.
  ray show superior mediastinal mass/enlargement?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 1732: Invalid expression / Unexpected token. Line 1, Col: 894.
  agnoses_icd.charttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1733: Model abstains from answering the question
Error executing query 1735: Model abstains from answering the question
Error executing query 1736: Model only answers one image question SQLs
Error executing query 1738: Invalid expression / Unexpected token. Line 1, Col: 890.
   = 16178416 ) and strftime('%Y',procedures_icd.charttime) >= '2102' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1739: Model abstains from answering the question
Error executing query 1740: Required keyword: 'expressions' missing for <class 'sqlglot.expressions.Aliases'>. Line 1, Col: 403.
   d_labitems where d_labitems.label = 'bicarbonate' ) order by labevents.charttime desc limit 1 )  ( [4mselect[0m labevents.valuenum from labevents where labevents.hadm_id in ( select admissions.hadm_id from admis
Error executing query 1741: Invalid expression / Unexpected token. Line 1, Col: 755.
  any any anatomical findings in the aortic arch?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1742: Model abstains from answering the question
Error executing query 1743: Model abstains from answering the question
Error executing query 1746: Model abstains from answering the question
Error executing query 1747: Model abstains from answering the question
Error executing query 1750: Model abstains from answering the question
Error executing query 1751: near "(": syntax error
Error executing query 1752: Model only answers one image question SQLs
Error executing query 1754: Model abstains from answering the question
Error executing query 1758: Model abstains from answering the question
Error executing query 1759: Invalid expression / Unexpected token. Line 1, Col: 644.
  ns.hadm_id from admissions where admissions.subject_id = 19096168 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 1760: Model abstains from answering the question
Error executing query 1761: Model abstains from answering the question
Error executing query 1762: Model only answers one image question SQLs
Error executing query 1763: Model abstains from answering the question
Error executing query 1765: Model abstains from answering the question
Error executing query 1766: Model only answers one image question SQLs
Error executing query 1767: Model only answers one image question SQLs
Error executing query 1768: Expecting ). Line 1, Col: 725.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.starttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 5
Error executing query 1769: Model abstains from answering the question
Error executing query 1771: Model abstains from answering the question
Error executing query 1772: Model abstains from answering the question
Error executing query 1773: Model abstains from answering the question
Error executing query 1775: Invalid expression / Unexpected token. Line 1, Col: 652.
   where prescriptions.drug = 'warfarin' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id
Error executing query 1777: Invalid expression / Unexpected token. Line 1, Col: 854.
  c_vqa("does a chest x-ray show any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 1778: Invalid expression / Unexpected token. Line 1, Col: 756.
  etime('2105-12-31 23:59:00','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month')
Error executing query 1779: Model only answers one image question SQLs
Error executing query 1780: Model abstains from answering the question
Error executing query 1781: Model only answers one image question SQLs
Error executing query 1784: Model only answers one image question SQLs
Error executing query 1785: Model abstains from answering the question
Error executing query 1786: Model abstains from answering the question
Error executing query 1787: Model abstains from answering the question
Error executing query 1788: Model abstains from answering the question
Error executing query 1789: Model only answers one image question SQLs
Error executing query 1790: Model abstains from answering the question
Error executing query 1792: Model abstains from answering the question
Error executing query 1794: Invalid expression / Unexpected token. Line 1, Col: 959.
   chest x-ray shown costophrenic angle blunting?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1795: Invalid expression / Unexpected token. Line 1, Col: 756.
  indication of any abnormality on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 1796: Model only answers one image question SQLs
Error executing query 1799: Model abstains from answering the question
Error executing query 1800: Invalid expression / Unexpected token. Line 1, Col: 1002.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1801: Invalid expression / Unexpected token. Line 1, Col: 618.
  _vqa("does a chest x-ray indicate any diseases?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 1802: Model abstains from answering the question
Error executing query 1806: Invalid expression / Unexpected token. Line 1, Col: 859.
  d = 12648153 ) and strftime('%Y',procedures_icd.charttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1810: Model abstains from answering the question
Error executing query 1811: Invalid expression / Unexpected token. Line 1, Col: 638.
  ns.hadm_id from admissions where admissions.subject_id = 12791659 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1812: Invalid expression / Unexpected token. Line 1, Col: 819.
  ns.hadm_id from admissions where admissions.subject_id = 13551252 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1813: Model abstains from answering the question
Error executing query 1814: Invalid expression / Unexpected token. Line 1, Col: 899.
  c_vqa("does a chest x-ray show any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1815: Model abstains from answering the question
Error executing query 1816: Model only answers one image question SQLs
Error executing query 1818: Invalid expression / Unexpected token. Line 1, Col: 849.
  id = 16289474 ) and strftime('%Y',diagnoses_icd.charttime) = '2102' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1821: Model only answers one image question SQLs
Error executing query 1822: Model only answers one image question SQLs
Error executing query 1823: Expecting ). Line 1, Col: 775.
  %Y',prescriptions.starttime) >= '2101' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month') gro
Error executing query 1824: near "(": syntax error
Error executing query 1826: Invalid expression / Unexpected token. Line 1, Col: 797.
  rescriptions.starttime) = datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 1827: Invalid expression / Unexpected token. Line 1, Col: 671.
  ns.hadm_id from admissions where admissions.subject_id = 18182458 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1830: Model abstains from answering the question
Error executing query 1834: Model only answers one image question SQLs
Error executing query 1838: Invalid expression / Unexpected token. Line 1, Col: 867.
  natomical findings in the left lower lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1839: Model abstains from answering the question
Error executing query 1840: Model only answers one image question SQLs
Error executing query 1841: Model abstains from answering the question
Error executing query 1842: Model abstains from answering the question
Error executing query 1843: Model abstains from answering the question
Error executing query 1845: Model abstains from answering the question
Error executing query 1847: Invalid expression / Unexpected token. Line 1, Col: 761.
  ns.hadm_id from admissions where admissions.subject_id = 16108338 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1852: Model only answers one image question SQLs
Error executing query 1853: Model only answers one image question SQLs
Error executing query 1854: Model abstains from answering the question
Error executing query 1855: Invalid expression / Unexpected token. Line 1, Col: 752.
  nc_vqa("has an x-ray revealed low lung volumes?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1856: Model only answers one image question SQLs
Error executing query 1857: Model abstains from answering the question
Error executing query 1858: Invalid expression / Unexpected token. Line 1, Col: 780.
  y depicting any tubes/lines in the mediastinum?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1859: Model abstains from answering the question
Error executing query 1860: Model only answers one image question SQLs
Error executing query 1861: Invalid expression / Unexpected token. Line 1, Col: 783.
  oad/heart failure in the right upper lung zone?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 1863: Model only answers one image question SQLs
Error executing query 1864: Model abstains from answering the question
Error executing query 1866: Model only answers one image question SQLs
Error executing query 1867: Model abstains from answering the question
Error executing query 1869: Model abstains from answering the question
Error executing query 1870: Invalid expression / Unexpected token. Line 1, Col: 852.
  d = 13655979 ) and strftime('%Y',procedures_icd.charttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1871: Model abstains from answering the question
Error executing query 1872: Model abstains from answering the question
Error executing query 1874: Model abstains from answering the question
Error executing query 1875: Model abstains from answering the question
Error executing query 1876: Model only answers one image question SQLs
Error executing query 1879: Model abstains from answering the question
Error executing query 1880: Model abstains from answering the question
Error executing query 1881: Model abstains from answering the question
Error executing query 1882: Model abstains from answering the question
Error executing query 1883: Invalid expression / Unexpected token. Line 1, Col: 1025.
  -ray show any tubes/lines in the left clavicle?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1884: Model abstains from answering the question
Error executing query 1885: Model only answers one image question SQLs
Error executing query 1888: Model abstains from answering the question
Error executing query 1889: Model only answers one image question SQLs
Error executing query 1891: Invalid expression / Unexpected token. Line 1, Col: 894.
   the right costophrenic angle on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1892: Model abstains from answering the question
Error executing query 1893: Model abstains from answering the question
Error executing query 1894: Model only answers one image question SQLs
Error executing query 1895: Model only answers one image question SQLs
Error executing query 1897: Model abstains from answering the question
Error executing query 1898: Model only answers one image question SQLs
Error executing query 1899: Model abstains from answering the question
Error executing query 1900: Invalid expression / Unexpected token. Line 1, Col: 977.
  ("is swan-ganz catheter shown on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1901: Model only answers one image question SQLs
Error executing query 1904: Model abstains from answering the question
Error executing query 1905: Invalid expression / Unexpected token. Line 1, Col: 760.
  id = 19966115 ) and strftime('%Y',prescriptions.starttime) = '2105' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 1906: Model only answers one image question SQLs
Error executing query 1908: Model abstains from answering the question
Error executing query 1910: Expecting ). Line 1, Col: 611.
  '%Y',prescriptions.starttime) = '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.starttime  [4mt2[0m.starttime and datetime(t1.starttime,'start of month') = datetime(t2.starttime,'start of month') gro
Error executing query 1911: Model abstains from answering the question
Error executing query 1912: Model abstains from answering the question
Error executing query 1914: Model only answers one image question SQLs
Error executing query 1915: Model abstains from answering the question
Error executing query 1916: Model only answers one image question SQLs
Error executing query 1917: Model abstains from answering the question
Error executing query 1918: Model abstains from answering the question
Error executing query 1920: Model only answers one image question SQLs
Error executing query 1923: Model abstains from answering the question
Error executing query 1924: Model abstains from answering the question
Error executing query 1925: Model abstains from answering the question
Error executing query 1926: Invalid expression / Unexpected token. Line 1, Col: 788.
  '%Y',diagnoses_icd.charttime) = '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
Error executing query 1928: Model abstains from answering the question
Error executing query 1929: Invalid expression / Unexpected token. Line 1, Col: 1013.
  te any tubes/lines in the left lower lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1931: Invalid expression / Unexpected token. Line 1, Col: 763.
  122104 ) and strftime('%Y-%m',prescriptions.starttime) >= '2104-10' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1932: Model only answers one image question SQLs
Error executing query 1934: Invalid expression / Unexpected token. Line 1, Col: 739.
  d = 16672541 ) and strftime('%Y',prescriptions.starttime) >= '2101' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 1935: Model only answers one image question SQLs
Error executing query 1936: Model abstains from answering the question
Error executing query 1937: Model abstains from answering the question
Error executing query 1938: Invalid expression / Unexpected token. Line 1, Col: 990.
  s a chest x-ray show any technical assessments?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 1939: Model abstains from answering the question
Error executing query 1940: Invalid expression / Unexpected token. Line 1, Col: 937.
  egmental collapse in the right lower lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1941: Model abstains from answering the question
Error executing query 1942: Model only answers one image question SQLs
Error executing query 1943: Model only answers one image question SQLs
Error executing query 1944: Invalid expression / Unexpected token. Line 1, Col: 756.
  t x-ray indicate any any technical assessments?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 1945: Invalid expression / Unexpected token. Line 1, Col: 637.
  _vqa("does a chest x-ray indicate any diseases?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 1946: Invalid expression / Unexpected token. Line 1, Col: 969.
  indicate lung cancer in the left mid lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1947: Model only answers one image question SQLs
Error executing query 1948: Model abstains from answering the question
Error executing query 1949: Expecting ). Line 1, Col: 969.
  d where prescriptions.drug = 'heparin' ) as t3 on t2.subject_id = t3.subject_id where t2.charttime  [4mt3[0m.starttime ) as t4 join patients on t4.subject_id = patients.subject_id
Error executing query 1951: Expecting ). Line 1, Col: 1003.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.itemid ) as t3 where t3.c1 = 5 )
Error executing query 1952: Invalid expression / Unexpected token. Line 1, Col: 661.
  ns.hadm_id from admissions where admissions.subject_id = 12876131 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1953: Model abstains from answering the question
Error executing query 1956: Model abstains from answering the question
Error executing query 1959: Model abstains from answering the question
Error executing query 1960: Model only answers one image question SQLs
Error executing query 1961: Model abstains from answering the question
Error executing query 1963: Invalid expression / Unexpected token. Line 1, Col: 763.
  e any hyperaeration in the right mid lung zone?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 1964: Model abstains from answering the question
Error executing query 1965: Model abstains from answering the question
Error executing query 1966: Model abstains from answering the question
Error executing query 1967: Invalid expression / Unexpected token. Line 1, Col: 747.
  d = 14881769 ) and strftime('%Y',prescriptions.starttime) >= '2100' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 1968: Model abstains from answering the question
Error executing query 1972: Invalid expression / Unexpected token. Line 1, Col: 919.
  cedures_icd.charttime) >= datetime('2105-12-31 23:59:00','-3 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1973: Model abstains from answering the question
Error executing query 1974: Model abstains from answering the question
Error executing query 1975: Model only answers one image question SQLs
Error executing query 1976: Model abstains from answering the question
Error executing query 1977: Model abstains from answering the question
Error executing query 1979: Invalid expression / Unexpected token. Line 1, Col: 734.
  ns.hadm_id from admissions where admissions.subject_id = 19096918 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1980: Model only answers one image question SQLs
Error executing query 1982: Expecting ). Line 1, Col: 980.
  ere prescriptions.drug = 'ondansetron' ) as t3 on t2.subject_id = t3.subject_id where t2.charttime  [4mt3[0m.starttime ) as t4 join patients on t4.subject_id = patients.subject_id
Error executing query 1984: Model only answers one image question SQLs
Error executing query 1985: Model only answers one image question SQLs
Error executing query 1986: Model abstains from answering the question
Error executing query 1987: Model only answers one image question SQLs
Error executing query 1988: Model abstains from answering the question
Error executing query 1990: Model only answers one image question SQLs
Error executing query 1992: Model abstains from answering the question
Error executing query 1994: Invalid expression / Unexpected token. Line 1, Col: 868.
  ication of swan-ganz catheter on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1995: Invalid expression / Unexpected token. Line 1, Col: 1049.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
[False]
[False]
Error executing query 1998: Model abstains from answering the question
Error executing query 1999: Model abstains from answering the question
Error executing query 2001: Model abstains from answering the question
Error executing query 2002: Model only answers one image question SQLs
Error executing query 2003: Model abstains from answering the question
Error executing query 2004: Model abstains from answering the question
Error executing query 2006: Model abstains from answering the question
Error executing query 2009: Invalid expression / Unexpected token. Line 1, Col: 996.
  ny abnormality in the trachea on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2011: Invalid expression / Unexpected token. Line 1, Col: 818.
  escriptions.starttime) >= datetime('2105-12-31 23:59:00','-2 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 2012: Invalid expression / Unexpected token. Line 1, Col: 985.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2013: Model abstains from answering the question
Error executing query 2015: Model only answers one image question SQLs
Error executing query 2018: Model abstains from answering the question
Error executing query 2020: Invalid expression / Unexpected token. Line 1, Col: 902.
  c_vqa("has a chest x-ray shown any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2021: Model only answers one image question SQLs
Error executing query 2022: Invalid expression / Unexpected token. Line 1, Col: 775.
  537002 ) and strftime('%Y-%m',prescriptions.starttime) >= '2103-11' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2023: Model abstains from answering the question
Error executing query 2024: Invalid expression / Unexpected token. Line 1, Col: 1019.
  atomical findings in the left hilar structures?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2025: Model abstains from answering the question
Error executing query 2026: Invalid expression / Unexpected token. Line 1, Col: 903.
  arged cardiac silhouette indicated on an x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2029: Expecting ). Line 1, Col: 936.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 2032: Invalid expression / Unexpected token. Line 1, Col: 734.
  a("does a chest x-ray indicate any abnormality?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2033: Invalid expression / Unexpected token. Line 1, Col: 628.
  qa("does a chest x-ray reveal any rib fracture?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2034: Invalid expression / Unexpected token. Line 1, Col: 889.
  s.dischtime is not null order by admissions.admittime asc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2035: Model abstains from answering the question
Error executing query 2036: Invalid expression / Unexpected token. Line 1, Col: 846.
  id = 16660935 ) and strftime('%Y',diagnoses_icd.charttime) = '2105' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2037: Model abstains from answering the question
Error executing query 2039: Invalid expression / Unexpected token. Line 1, Col: 383.
   where d_items.label = 'heart rate' and d_items.linksto = 'chartevents' ) and chartevents.valuenum  [4m86.0[0m and datetime(chartevents.charttime,'start of year') = datetime('2105-12-31 23:59:00','start of year
Error executing query 2041: Model abstains from answering the question
Error executing query 2043: Model abstains from answering the question
Error executing query 2044: Model abstains from answering the question
Error executing query 2047: Model only answers one image question SQLs
Error executing query 2049: Invalid expression / Unexpected token. Line 1, Col: 738.
  ns.hadm_id from admissions where admissions.subject_id = 19287866 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2051: Model abstains from answering the question
Error executing query 2052: Expecting ). Line 1, Col: 834.
  %Y',procedures_icd.charttime) = '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 2054: Model abstains from answering the question
Error executing query 2055: Model abstains from answering the question
Error executing query 2056: Model abstains from answering the question
Error executing query 2058: Model only answers one image question SQLs
Error executing query 2060: Model only answers one image question SQLs
Error executing query 2061: Model abstains from answering the question
Error executing query 2062: Model abstains from answering the question
Error executing query 2063: Invalid expression / Unexpected token. Line 1, Col: 939.
  gnoses_icd.charttime) = datetime('2105-12-31 23:59:00','-30 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2064: Model abstains from answering the question
Error executing query 2065: Model abstains from answering the question
Error executing query 2066: Model only answers one image question SQLs
Error executing query 2068: Model only answers one image question SQLs
Error executing query 2070: Model only answers one image question SQLs
Error executing query 2072: Invalid expression / Unexpected token. Line 1, Col: 754.
   shoulder osteoarthritis in the right shoulder?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 2073: Model abstains from answering the question
Error executing query 2075: Model abstains from answering the question
Error executing query 2077: Invalid expression / Unexpected token. Line 1, Col: 914.
  4851188 ) and strftime('%Y-%m',diagnoses_icd.charttime) = '2103-11' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2078: Model abstains from answering the question
Error executing query 2079: Model abstains from answering the question
Error executing query 2080: Model abstains from answering the question
Error executing query 2081: Model only answers one image question SQLs
Error executing query 2082: Model abstains from answering the question
Error executing query 2083: Model abstains from answering the question
Error executing query 2084: Model abstains from answering the question
Error executing query 2085: Model only answers one image question SQLs
Error executing query 2086: Invalid expression / Unexpected token. Line 1, Col: 736.
  d = 18011403 ) and strftime('%Y',prescriptions.starttime) >= '2102' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 2088: Invalid expression / Unexpected token. Line 1, Col: 944.
  led in the left mid lung zone on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2089: Model abstains from answering the question
Error executing query 2090: Model only answers one image question SQLs
Error executing query 2091: Invalid expression / Unexpected token. Line 1, Col: 751.
  ns.hadm_id from admissions where admissions.subject_id = 19969031 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2092: Expecting ). Line 1, Col: 768.
  '%Y',prescriptions.starttime) = '2100' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 3
Error executing query 2094: Model abstains from answering the question
Error executing query 2095: Model only answers one image question SQLs
Error executing query 2096: Model only answers one image question SQLs
Error executing query 2100: Invalid expression / Unexpected token. Line 1, Col: 983.
  noses_icd.charttime) >= datetime('2105-12-31 23:59:00','-30 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
[False]
Error executing query 2104: Model only answers one image question SQLs
Error executing query 2105: Model abstains from answering the question
Error executing query 2106: Model only answers one image question SQLs
Error executing query 2107: Model abstains from answering the question
Error executing query 2108: Model abstains from answering the question
Error executing query 2110: Model only answers one image question SQLs
Error executing query 2111: Model abstains from answering the question
Error executing query 2113: Model abstains from answering the question
Error executing query 2114: Model only answers one image question SQLs
Error executing query 2115: Invalid expression / Unexpected token. Line 1, Col: 752.
  func_vqa("does an x-ray reveal any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2119: Model abstains from answering the question
Error executing query 2120: Model abstains from answering the question
Error executing query 2124: Model abstains from answering the question
Error executing query 2125: Model abstains from answering the question
Error executing query 2127: Model abstains from answering the question
Error executing query 2128: Invalid expression / Unexpected token. Line 1, Col: 763.
  id = 18916144 ) and strftime('%Y',prescriptions.starttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 2133: Model only answers one image question SQLs
Error executing query 2135: Model abstains from answering the question
Error executing query 2137: Model only answers one image question SQLs
Error executing query 2138: Expecting ). Line 1, Col: 841.
  microbiologyevents.charttime) = '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.test_name ) as t3 where t3.c1 = 3
Error executing query 2140: Invalid expression / Unexpected token. Line 1, Col: 841.
   a chest x-ray show any abnormality in the svc?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2141: Model abstains from answering the question
Error executing query 2142: Model abstains from answering the question
Error executing query 2144: Model only answers one image question SQLs
Error executing query 2145: Invalid expression / Unexpected token. Line 1, Col: 916.
  echnical assessments revealed on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2146: Model abstains from answering the question
Error executing query 2147: Model abstains from answering the question
Error executing query 2148: Expecting ). Line 1, Col: 987.
  e prescriptions.drug = 'acetaminophen' ) as t3 on t2.subject_id = t3.subject_id where t2.charttime  [4mt3[0m.starttime ) as t4 join patients on t4.subject_id = patients.subject_id
Error executing query 2149: Model only answers one image question SQLs
Error executing query 2150: Expecting ). Line 1, Col: 749.
  %Y',prescriptions.starttime) >= '2101' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 2151: Model only answers one image question SQLs
Error executing query 2152: Expecting ). Line 1, Col: 897.
  %Y',procedures_icd.charttime) = '2101' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.icd_code ) as t3 where t3.c1 = 5 )
Error executing query 2154: Model only answers one image question SQLs
Error executing query 2157: Expecting ). Line 1, Col: 921.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 2158: Expecting ). Line 1, Col: 906.
  etime('2105-12-31 23:59:00','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
[False]
[False]
Error executing query 2160: Model abstains from answering the question
Error executing query 2163: Model only answers one image question SQLs
Error executing query 2168: Model only answers one image question SQLs
Error executing query 2169: Model only answers one image question SQLs
Error executing query 2170: Model only answers one image question SQLs
Error executing query 2172: Model abstains from answering the question
Error executing query 2173: Invalid expression / Unexpected token. Line 1, Col: 748.
  d = 15883826 ) and strftime('%Y',prescriptions.starttime) >= '2105' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 2174: Model only answers one image question SQLs
Error executing query 2176: Model only answers one image question SQLs
Error executing query 2177: Invalid expression / Unexpected token. Line 1, Col: 717.
  c_vqa("does a chest x-ray show any abnormality?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2178: Invalid expression / Unexpected token. Line 1, Col: 1027.
  agnoses_icd.charttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2179: Model abstains from answering the question
Error executing query 2180: Model only answers one image question SQLs
Error executing query 2181: Invalid expression / Unexpected token. Line 1, Col: 1041.
  n the left costophrenic angle on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2182: Expecting ). Line 1, Col: 905.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 2183: Model only answers one image question SQLs
Error executing query 2184: Model abstains from answering the question
Error executing query 2186: Invalid expression / Unexpected token. Line 1, Col: 633.
  ns.hadm_id from admissions where admissions.subject_id = 11212873 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2188: Invalid expression / Unexpected token. Line 1, Col: 744.
  ns.hadm_id from admissions where admissions.subject_id = 14294216 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2189: Model abstains from answering the question
Error executing query 2192: Invalid expression / Unexpected token. Line 1, Col: 895.
  n the left costophrenic angle on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2194: Invalid expression / Unexpected token. Line 1, Col: 748.
  1959746 ) and strftime('%Y-%m',prescriptions.starttime) = '2104-02' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2195: Model only answers one image question SQLs
Error executing query 2196: Invalid expression / Unexpected token. Line 1, Col: 753.
  ns.hadm_id from admissions where admissions.subject_id = 18787238 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2197: Invalid expression / Unexpected token. Line 1, Col: 1009.
  echnical assessments in the left mid lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2198: Invalid expression / Unexpected token. Line 1, Col: 760.
  y reveal vascular congestion in the right lung?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2199: Expecting ). Line 1, Col: 849.
  %Y',diagnoses_icd.charttime) >= '2105' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 2200: Invalid expression / Unexpected token. Line 1, Col: 758.
   any anatomical findings indicated on an x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2201: Expecting ). Line 1, Col: 896.
  '%Y',prescriptions.starttime) = '2101' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month') gro
[True]
Error executing query 2202: near "(": syntax error
Error executing query 2203: Invalid expression / Unexpected token. Line 1, Col: 953.
  cedures_icd.charttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2204: Invalid expression / Unexpected token. Line 1, Col: 839.
   = 12822417 ) and strftime('%Y',procedures_icd.charttime) >= '2105' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2207: Model only answers one image question SQLs
Error executing query 2210: Model abstains from answering the question
Error executing query 2211: Model only answers one image question SQLs
Error executing query 2214: Model abstains from answering the question
Error executing query 2215: Expecting ). Line 1, Col: 1011.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month') gro
Error executing query 2216: Model abstains from answering the question
Error executing query 2217: Model only answers one image question SQLs
Error executing query 2218: Model only answers one image question SQLs
Error executing query 2219: Model abstains from answering the question
Error executing query 2221: Invalid expression / Unexpected token. Line 1, Col: 905.
  pulmonary edema/hazy opacity in the right lung?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2222: Model abstains from answering the question
Error executing query 2225: Expecting ). Line 1, Col: 909.
  etime('2105-12-31 23:59:00','-3 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.test_name ) as t3 where t3.c1 = 5
Error executing query 2226: Model abstains from answering the question
Error executing query 2227: Expecting ). Line 1, Col: 923.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 2228: Model only answers one image question SQLs
Error executing query 2229: Model abstains from answering the question
Error executing query 2230: Model abstains from answering the question
Error executing query 2231: Model abstains from answering the question
Error executing query 2234: Model abstains from answering the question
Error executing query 2237: Expecting ). Line 1, Col: 977.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 2238: Expecting ). Line 1, Col: 608.
  %Y',prescriptions.starttime) >= '2101' ) as t2 on t1.subject_id = t2.subject_id where t1.starttime  [4mt2[0m.starttime and datetime(t1.starttime,'start of month') = datetime(t2.starttime,'start of month') gro
Error executing query 2239: Model abstains from answering the question
Error executing query 2240: Model only answers one image question SQLs
Error executing query 2241: Model abstains from answering the question
Error executing query 2242: Model abstains from answering the question
Error executing query 2248: Invalid expression / Unexpected token. Line 1, Col: 643.
  emonstrated any tubes/lines in the mediastinum?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2249: Expecting ). Line 1, Col: 867.
  etime('2105-12-31 23:59:00','-3 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 2250: Model only answers one image question SQLs
Error executing query 2251: Model abstains from answering the question
Error executing query 2252: Expecting ). Line 1, Col: 962.
   where prescriptions.drug = 'd5 1/2ns' ) as t3 on t2.subject_id = t3.subject_id where t2.charttime  [4mt3[0m.starttime ) as t4 join patients on t4.subject_id = patients.subject_id
Error executing query 2253: Model only answers one image question SQLs
Error executing query 2254: Invalid expression / Unexpected token. Line 1, Col: 934.
  agnoses_icd.charttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2259: Model abstains from answering the question
Error executing query 2260: Model abstains from answering the question
Error executing query 2261: Model abstains from answering the question
Error executing query 2263: Invalid expression / Unexpected token. Line 1, Col: 1033.
  s in the left lower lung zone on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2264: Model abstains from answering the question
Error executing query 2266: Expecting ). Line 1, Col: 802.
  ime('%Y',labevents.charttime) = '2103' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 2268: Invalid expression / Unexpected token. Line 1, Col: 646.
  ns.hadm_id from admissions where admissions.subject_id = 11461300 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 2269: Model abstains from answering the question
Error executing query 2270: Model only answers one image question SQLs
Error executing query 2271: Invalid expression / Unexpected token. Line 1, Col: 773.
  ns.hadm_id from admissions where admissions.subject_id = 18750620 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2272: Invalid expression / Unexpected token. Line 1, Col: 998.
  nth') = datetime('2105-12-31 23:59:00','start of month','-0 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2273: Model abstains from answering the question
Error executing query 2276: Model only answers one image question SQLs
Error executing query 2277: Model abstains from answering the question
Error executing query 2279: Invalid expression / Unexpected token. Line 1, Col: 910.
  noses_icd.charttime) >= datetime('2105-12-31 23:59:00','-15 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2280: Model abstains from answering the question
Error executing query 2281: Model abstains from answering the question
Error executing query 2286: Expecting ). Line 1, Col: 794.
  icrobiologyevents.charttime) >= '2103' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 2287: Invalid expression / Unexpected token. Line 1, Col: 766.
   any infiltration in the right upper lung zone?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 2288: Model abstains from answering the question
Error executing query 2289: Model only answers one image question SQLs
Error executing query 2296: Model only answers one image question SQLs
Error executing query 2297: Invalid expression / Unexpected token. Line 1, Col: 862.
  etime('2105-12-31 23:59:00','-3 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 2299: Model only answers one image question SQLs
Error executing query 2300: Invalid expression / Unexpected token. Line 1, Col: 818.
   any lung opacity in the left hilar structures?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2301: Model abstains from answering the question
Error executing query 2302: Invalid expression / Unexpected token. Line 1, Col: 976.
  dures_icd.charttime) >= datetime('2105-12-31 23:59:00','-17 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2303: Invalid expression / Unexpected token. Line 1, Col: 771.
  any abnormality in the left costophrenic angle?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2304: Invalid expression / Unexpected token. Line 1, Col: 1026.
  .dischtime is not null order by admissions.admittime desc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2305: Model abstains from answering the question
[True]
Error executing query 2306: near "(": syntax error
Error executing query 2308: Invalid expression / Unexpected token. Line 1, Col: 958.
   year') = datetime('2105-12-31 23:59:00','start of year','-0 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2311: Invalid expression / Unexpected token. Line 1, Col: 720.
  id = 13655979 ) and strftime('%Y',prescriptions.starttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 2315: Model abstains from answering the question
Error executing query 2319: Invalid expression / Unexpected token. Line 1, Col: 872.
  ns.hadm_id from admissions where admissions.subject_id = 10405915 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and t1.hadm_id = t3.hadm_id
Error executing query 2321: Model only answers one image question SQLs
Error executing query 2322: Model only answers one image question SQLs
Error executing query 2324: Invalid expression / Unexpected token. Line 1, Col: 848.
  '%Y',diagnoses_icd.charttime) = '2103' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 2325: Model abstains from answering the question
Error executing query 2326: Model only answers one image question SQLs
Error executing query 2329: Model only answers one image question SQLs
Error executing query 2330: Model only answers one image question SQLs
Error executing query 2332: Model abstains from answering the question
Error executing query 2333: Model abstains from answering the question
Error executing query 2335: Model only answers one image question SQLs
Error executing query 2337: Invalid expression / Unexpected token. Line 1, Col: 849.
  d = 13724767 ) and strftime('%Y',diagnoses_icd.charttime) >= '2102' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2340: Invalid expression / Unexpected token. Line 1, Col: 755.
  "is there a finding of hernia on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2341: Model abstains from answering the question
Error executing query 2343: Model abstains from answering the question
Error executing query 2345: Expecting ). Line 1, Col: 751.
  labevents.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 2346: Invalid expression / Unexpected token. Line 1, Col: 731.
  d = 12591968 ) and strftime('%Y',prescriptions.starttime) >= '2101' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 2347: Model only answers one image question SQLs
Error executing query 2349: Model abstains from answering the question
Error executing query 2350: Model abstains from answering the question
Error executing query 2351: Model only answers one image question SQLs
Error executing query 2352: Model abstains from answering the question
Error executing query 2353: Model abstains from answering the question
Error executing query 2354: Model only answers one image question SQLs
Error executing query 2356: Model only answers one image question SQLs
Error executing query 2358: Model abstains from answering the question
Error executing query 2360: Invalid expression / Unexpected token. Line 1, Col: 940.
  23:59:00','start of month','-0 month') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 d
Error executing query 2361: Model abstains from answering the question
Error executing query 2362: Model abstains from answering the question
Error executing query 2363: Model abstains from answering the question
Error executing query 2364: Model only answers one image question SQLs
Error executing query 2365: Model abstains from answering the question
Error executing query 2368: Model abstains from answering the question
Error executing query 2370: Model only answers one image question SQLs
Error executing query 2371: Model only answers one image question SQLs
Error executing query 2372: Model abstains from answering the question
Error executing query 2373: Model abstains from answering the question
Error executing query 2374: Model abstains from answering the question
Error executing query 2377: Invalid expression / Unexpected token. Line 1, Col: 930.
  t2 where func_vqa("is any abnormality revealed?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2378: Model abstains from answering the question
Error executing query 2380: Invalid expression / Unexpected token. Line 1, Col: 934.
  _vqa("is any abnormality indicated on an x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2381: Invalid expression / Unexpected token. Line 1, Col: 919.
  etime('2105-12-31 23:59:00','-5 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 2382: Invalid expression / Unexpected token. Line 1, Col: 783.
  ns.hadm_id from admissions where admissions.subject_id = 17964648 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2384: Model only answers one image question SQLs
Error executing query 2385: Invalid expression / Unexpected token. Line 1, Col: 893.
  84213 ) and strftime('%Y-%m',procedures_icd.charttime) >= '2102-10' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2390: Model only answers one image question SQLs
Error executing query 2391: Invalid expression / Unexpected token. Line 1, Col: 863.
  does the chest x-ray indicate any any diseases?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2392: Model abstains from answering the question
Error executing query 2393: Model abstains from answering the question
Error executing query 2394: Model only answers one image question SQLs
Error executing query 2395: Model abstains from answering the question
Error executing query 2397: Model abstains from answering the question
Error executing query 2398: Model abstains from answering the question
Error executing query 2399: Model abstains from answering the question
Error executing query 2401: Model abstains from answering the question
Error executing query 2402: Invalid expression / Unexpected token. Line 1, Col: 903.
  nth') = datetime('2105-12-31 23:59:00','start of month','-1 month') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2404: Model only answers one image question SQLs
Error executing query 2405: Model abstains from answering the question
Error executing query 2408: Model abstains from answering the question
Error executing query 2409: Invalid expression / Unexpected token. Line 1, Col: 869.
  %Y',procedures_icd.charttime) = '2102' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
Error executing query 2411: Invalid expression / Unexpected token. Line 1, Col: 995.
  ("is subclavian line revealed on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2413: Model only answers one image question SQLs
Error executing query 2414: Model only answers one image question SQLs
Error executing query 2416: Expecting ). Line 1, Col: 866.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 2417: Invalid expression / Unexpected token. Line 1, Col: 725.
  id = 10405915 ) and strftime('%Y',prescriptions.starttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 2419: Model only answers one image question SQLs
Error executing query 2420: Model only answers one image question SQLs
Error executing query 2421: Model only answers one image question SQLs
Error executing query 2422: Invalid expression / Unexpected token. Line 1, Col: 740.
  s.long_title = 'atrial fibrillation' ) ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id
Error executing query 2423: Expecting ). Line 1, Col: 985.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 2424: Model abstains from answering the question
Error executing query 2425: Invalid expression / Unexpected token. Line 1, Col: 905.
  .dischtime is not null order by admissions.admittime desc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2426: Invalid expression / Unexpected token. Line 1, Col: 769.
  unc_vqa("is a chest x-ray showing any diseases?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2427: Model abstains from answering the question
Error executing query 2428: Invalid expression / Unexpected token. Line 1, Col: 765.
  id = 13412512 ) and strftime('%Y',prescriptions.starttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 2429: Invalid expression / Unexpected token. Line 1, Col: 863.
   = 14771014 ) and strftime('%Y',procedures_icd.charttime) >= '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2430: Expecting ). Line 1, Col: 856.
  microbiologyevents.charttime) = '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.spec_type_desc ) as t3 where t3.c1 = 3
Error executing query 2433: Invalid expression / Unexpected token. Line 1, Col: 761.
  9969031 ) and strftime('%Y-%m',prescriptions.starttime) = '2105-06' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2434: Model abstains from answering the question
Error executing query 2436: Invalid expression / Unexpected token. Line 1, Col: 927.
  ocedures_icd.charttime) = datetime('2105-12-31 23:59:00','-2 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2437: Invalid expression / Unexpected token. Line 1, Col: 649.
  ns.hadm_id from admissions where admissions.subject_id = 18969313 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 2438: Model only answers one image question SQLs
Error executing query 2439: Invalid expression / Unexpected token. Line 1, Col: 734.
  has a chest x-ray demonstrated any abnormality?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2440: Model abstains from answering the question
Error executing query 2441: Model only answers one image question SQLs
Error executing query 2443: Invalid expression / Unexpected token. Line 1, Col: 910.
  2 where func_vqa("does a chest x-ray show picc?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2445: Model abstains from answering the question
Error executing query 2446: Invalid expression / Unexpected token. Line 1, Col: 822.
  nc_vqa("has a chest x-ray shown enlarged hilum?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2447: Model abstains from answering the question
Error executing query 2448: Model only answers one image question SQLs
Error executing query 2449: Model only answers one image question SQLs
Error executing query 2450: Model abstains from answering the question
Error executing query 2451: Model only answers one image question SQLs
Error executing query 2453: Model only answers one image question SQLs
Error executing query 2456: Model abstains from answering the question
Error executing query 2458: Model abstains from answering the question
Error executing query 2459: Invalid expression / Unexpected token. Line 1, Col: 763.
  x-ray showing any abnormality in the left lung?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 2462: Model abstains from answering the question
Error executing query 2463: Model abstains from answering the question
Error executing query 2466: Model abstains from answering the question
Error executing query 2467: Invalid expression / Unexpected token. Line 1, Col: 977.
  aled in the upper mediastinum on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2468: Model only answers one image question SQLs
Error executing query 2469: Model abstains from answering the question
Error executing query 2470: Model abstains from answering the question
Error executing query 2471: near "(": syntax error
Error executing query 2472: Model only answers one image question SQLs
Error executing query 2473: Model abstains from answering the question
Error executing query 2474: Expecting ). Line 1, Col: 924.
  etime('2105-12-31 23:59:00','-3 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.spec_type_desc ) as t3 where t3.c1 = 5
Error executing query 2475: Invalid expression / Unexpected token. Line 1, Col: 743.
  not otherwise specified) indicated on an x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2477: Invalid expression / Unexpected token. Line 1, Col: 935.
  any abnormality in the left costophrenic angle?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2478: Invalid expression / Unexpected token. Line 1, Col: 831.
  323860 ) and strftime('%Y-%m',diagnoses_icd.charttime) >= '2105-11' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2479: Model abstains from answering the question
Error executing query 2480: Model abstains from answering the question
Error executing query 2482: Invalid expression / Unexpected token. Line 1, Col: 651.
  ns.hadm_id from admissions where admissions.subject_id = 10518993 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2483: Model only answers one image question SQLs
Error executing query 2484: Model only answers one image question SQLs
Error executing query 2486: Invalid expression / Unexpected token. Line 1, Col: 903.
  466107 ) and strftime('%Y-%m',procedures_icd.charttime) = '2101-09' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2487: Invalid expression / Unexpected token. Line 1, Col: 766.
  352433 ) and strftime('%Y-%m',prescriptions.starttime) >= '2102-04' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2488: Model only answers one image question SQLs
Error executing query 2489: Model only answers one image question SQLs
Error executing query 2491: Model abstains from answering the question
Error executing query 2492: Model abstains from answering the question
Error executing query 2493: Invalid expression / Unexpected token. Line 1, Col: 926.
  ity shown in the right atrium on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2495: Model abstains from answering the question
Error executing query 2497: Model abstains from answering the question
Error executing query 2500: Model only answers one image question SQLs
Error executing query 2501: Invalid expression / Unexpected token. Line 1, Col: 794.
  ,prescriptions.starttime) >= '2105-09' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id
Error executing query 2502: Model abstains from answering the question
Error executing query 2503: Model abstains from answering the question
Error executing query 2504: Model only answers one image question SQLs
Error executing query 2505: Model abstains from answering the question
Error executing query 2506: Model abstains from answering the question
Error executing query 2510: Model abstains from answering the question
Error executing query 2511: Model abstains from answering the question
Error executing query 2512: Invalid expression / Unexpected token. Line 1, Col: 948.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
Error executing query 2513: Model abstains from answering the question
Error executing query 2514: Model abstains from answering the question
Error executing query 2515: Model only answers one image question SQLs
Error executing query 2516: Model only answers one image question SQLs
Error executing query 2517: Model only answers one image question SQLs
[False]
[False]
Error executing query 2523: Model only answers one image question SQLs
Error executing query 2524: Model abstains from answering the question
Error executing query 2525: Model abstains from answering the question
Error executing query 2526: Model only answers one image question SQLs
Error executing query 2527: Model abstains from answering the question
Error executing query 2529: Model abstains from answering the question
[False]
Error executing query 2532: Model abstains from answering the question
Error executing query 2533: near "(": syntax error
Error executing query 2534: Model abstains from answering the question
Error executing query 2535: Model abstains from answering the question
Error executing query 2536: Model only answers one image question SQLs
Error executing query 2537: Model abstains from answering the question
Error executing query 2541: Model abstains from answering the question
Error executing query 2542: Invalid expression / Unexpected token. Line 1, Col: 656.
  ns.hadm_id from admissions where admissions.subject_id = 18448597 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2543: Model abstains from answering the question
Error executing query 2544: Model abstains from answering the question
Error executing query 2546: Model abstains from answering the question
Error executing query 2547: Model abstains from answering the question
Error executing query 2549: Model abstains from answering the question
Error executing query 2550: Model only answers one image question SQLs
Error executing query 2552: Expecting ). Line 1, Col: 656.
  %Y',prescriptions.starttime) >= '2101' ) as t2 on t1.subject_id = t2.subject_id where t1.starttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 3
Error executing query 2554: Model only answers one image question SQLs
Error executing query 2555: Invalid expression / Unexpected token. Line 1, Col: 887.
  d = 12980071 ) and strftime('%Y',procedures_icd.charttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2556: Model abstains from answering the question
[False]
Error executing query 2558: Model abstains from answering the question
Error executing query 2559: Invalid expression / Unexpected token. Line 1, Col: 847.
  a("does a chest x-ray indicate any abnormality?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2560: Invalid expression / Unexpected token. Line 1, Col: 848.
  -ray reveal low lung volumes in the right lung?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2561: Invalid expression / Unexpected token. Line 1, Col: 747.
  unc_vqa("is any diseases indicated on an x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2563: Model abstains from answering the question
Error executing query 2564: Invalid expression / Unexpected token. Line 1, Col: 941.
   the right costophrenic angle on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2565: Model abstains from answering the question
Error executing query 2570: Model abstains from answering the question
Error executing query 2571: near "(": syntax error
Error executing query 2572: Invalid expression / Unexpected token. Line 1, Col: 913.
  noses_icd.charttime) >= datetime('2105-12-31 23:59:00','-29 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2574: Model abstains from answering the question
Error executing query 2575: Model only answers one image question SQLs
Error executing query 2576: Invalid expression / Unexpected token. Line 1, Col: 647.
  veal any abnormality in the left mid lung zone?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2578: Model only answers one image question SQLs
Error executing query 2579: Invalid expression / Unexpected token. Line 1, Col: 870.
   show pneumothorax in the left lower lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2581: Model abstains from answering the question
Error executing query 2582: Model abstains from answering the question
Error executing query 2583: Invalid expression / Unexpected token. Line 1, Col: 746.
  056668 ) and strftime('%Y-%m',prescriptions.starttime) >= '2104-02' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2584: Invalid expression / Unexpected token. Line 1, Col: 728.
  2798053 ) and strftime('%Y-%m',prescriptions.starttime) = '2105-07' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2585: Invalid expression / Unexpected token. Line 1, Col: 983.
  nth') = datetime('2105-12-31 23:59:00','start of month','-0 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2586: Invalid expression / Unexpected token. Line 1, Col: 733.
  '%Y',prescriptions.starttime) = '2105' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id
Error executing query 2588: Model abstains from answering the question
Error executing query 2590: Model abstains from answering the question
Error executing query 2593: Model abstains from answering the question
Error executing query 2597: Invalid expression / Unexpected token. Line 1, Col: 868.
  d = 11422357 ) and strftime('%Y',procedures_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2598: Model abstains from answering the question
Error executing query 2599: Model abstains from answering the question
Error executing query 2600: Invalid expression / Unexpected token. Line 1, Col: 855.
  .dischtime is not null order by admissions.admittime desc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2601: Model only answers one image question SQLs
Error executing query 2602: Model abstains from answering the question
Error executing query 2603: Model abstains from answering the question
Error executing query 2604: Invalid expression / Unexpected token. Line 1, Col: 1082.
  vealed any abnormality in the right chest wall?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2606: Model only answers one image question SQLs
Error executing query 2608: Invalid expression / Unexpected token. Line 1, Col: 758.
  unc_vqa("does a chest x-ray reveal any devices?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2609: Model only answers one image question SQLs
Error executing query 2610: Expecting ). Line 1, Col: 851.
  %Y',diagnoses_icd.charttime) >= '2105' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 2611: Model abstains from answering the question
Error executing query 2612: Model abstains from answering the question
Error executing query 2613: Model abstains from answering the question
Error executing query 2615: Expecting ). Line 1, Col: 857.
  Y',procedures_icd.charttime) >= '2105' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 2617: Model abstains from answering the question
Error executing query 2618: Invalid expression / Unexpected token. Line 1, Col: 920.
  etime('2105-12-31 23:59:00','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
Error executing query 2620: Model abstains from answering the question
Error executing query 2621: Model abstains from answering the question
Error executing query 2622: Model only answers one image question SQLs
Error executing query 2623: Model only answers one image question SQLs
Error executing query 2624: Model abstains from answering the question
Error executing query 2625: Invalid expression / Unexpected token. Line 1, Col: 1109.
  year','-0 year') and strftime('%m',procedures_icd.charttime) = '05' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime
Error executing query 2626: Model abstains from answering the question
Error executing query 2627: Model only answers one image question SQLs
Error executing query 2629: Model abstains from answering the question
Error executing query 2631: Model only answers one image question SQLs
Error executing query 2632: Invalid expression / Unexpected token. Line 1, Col: 856.
   chest x-ray show any abnormality in the spine?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2634: Model only answers one image question SQLs
Error executing query 2635: Model abstains from answering the question
Error executing query 2636: Invalid expression / Unexpected token. Line 1, Col: 882.
  Y',procedures_icd.charttime) >= '2101' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id
Error executing query 2637: Model abstains from answering the question
Error executing query 2640: Invalid expression / Unexpected token. Line 1, Col: 743.
  t x-ray indicate any any technical assessments?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2641: Model only answers one image question SQLs
Error executing query 2642: Model only answers one image question SQLs
Error executing query 2643: Model only answers one image question SQLs
[False]
Error executing query 2646: Model abstains from answering the question
Error executing query 2647: Model only answers one image question SQLs
Error executing query 2648: Model abstains from answering the question
Error executing query 2652: Model only answers one image question SQLs
Error executing query 2653: Model abstains from answering the question
Error executing query 2654: Invalid expression / Unexpected token. Line 1, Col: 837.
  n the left costophrenic angle on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2657: Model abstains from answering the question
Error executing query 2659: Model only answers one image question SQLs
Error executing query 2660: Invalid expression / Unexpected token. Line 1, Col: 383.
   where d_items.label = 'heart rate' and d_items.linksto = 'chartevents' ) and chartevents.valuenum  [4m75.0[0m and datetime(chartevents.charttime) >= datetime('2105-12-31 23:59:00','-75.0 day')
Error executing query 2661: Model only answers one image question SQLs
Error executing query 2662: Invalid expression / Unexpected token. Line 1, Col: 787.
  vqa("is a chest x-ray showing airspace opacity?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 2663: Invalid expression / Unexpected token. Line 1, Col: 921.
  ocedures_icd.charttime) = datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2665: Model only answers one image question SQLs
Error executing query 2666: Invalid expression / Unexpected token. Line 1, Col: 790.
  oad/heart failure in the right upper lung zone?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 2667: Model only answers one image question SQLs
Error executing query 2668: Model abstains from answering the question
Error executing query 2669: Model abstains from answering the question
Error executing query 2670: Model abstains from answering the question
Error executing query 2671: Model only answers one image question SQLs
Error executing query 2674: Invalid expression / Unexpected token. Line 1, Col: 974.
   x-ray detecting pneumothorax in the left lung?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2675: Invalid expression / Unexpected token. Line 1, Col: 929.
   anatomical findings in the left mid lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2676: Model abstains from answering the question
Error executing query 2677: Invalid expression / Unexpected token. Line 1, Col: 761.
  ns.hadm_id from admissions where admissions.subject_id = 12822417 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2679: Invalid expression / Unexpected token. Line 1, Col: 909.
  neumomediastinum in the right hilar structures?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2680: Model abstains from answering the question
Error executing query 2681: Invalid expression / Unexpected token. Line 1, Col: 763.
  y reveal superior mediastinal mass/enlargement?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2682: Model only answers one image question SQLs
Error executing query 2683: Model only answers one image question SQLs
Error executing query 2686: Model abstains from answering the question
Error executing query 2688: Model abstains from answering the question
Error executing query 2689: Model only answers one image question SQLs
Error executing query 2690: Invalid expression / Unexpected token. Line 1, Col: 670.
  ns.hadm_id from admissions where admissions.subject_id = 11636169 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2691: Model only answers one image question SQLs
Error executing query 2692: Invalid expression / Unexpected token. Line 1, Col: 839.
  id = 13551252 ) and strftime('%Y',diagnoses_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2693: Model abstains from answering the question
Error executing query 2694: Model only answers one image question SQLs
Error executing query 2696: Invalid expression / Unexpected token. Line 1, Col: 842.
  y technical assessments shown on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2698: Expecting ). Line 1, Col: 912.
  etime('2105-12-31 23:59:00','-3 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 5
Error executing query 2701: Model abstains from answering the question
Error executing query 2703: Model abstains from answering the question
Error executing query 2704: Model abstains from answering the question
Error executing query 2705: Model abstains from answering the question
Error executing query 2706: Invalid expression / Unexpected token. Line 1, Col: 754.
  0501557 ) and strftime('%Y-%m',prescriptions.starttime) = '2105-09' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2707: Model only answers one image question SQLs
Error executing query 2709: Invalid expression / Unexpected token. Line 1, Col: 971.
  ocedures_icd.charttime) = datetime('2105-12-31 23:59:00','-3 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2710: Invalid expression / Unexpected token. Line 1, Col: 943.
   = 13655979 ) and strftime('%Y',procedures_icd.charttime) >= '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2713: Expecting ). Line 1, Col: 752.
  %Y',prescriptions.starttime) >= '2102' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month') gro
Error executing query 2714: near "(": syntax error
Error executing query 2717: Invalid expression / Unexpected token. Line 1, Col: 734.
  icated any abnormality in the right chest wall?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2719: Model abstains from answering the question
Error executing query 2721: Invalid expression / Unexpected token. Line 1, Col: 884.
  d = 12006801 ) and strftime('%Y',procedures_icd.charttime) = '2105' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2723: Model abstains from answering the question
Error executing query 2724: Model only answers one image question SQLs
Error executing query 2726: Model abstains from answering the question
Error executing query 2727: Model abstains from answering the question
Error executing query 2728: Model abstains from answering the question
Error executing query 2729: Invalid expression / Unexpected token. Line 1, Col: 743.
  nc_vqa("does a chest x-ray reveal rib fracture?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2730: Model only answers one image question SQLs
Error executing query 2731: Model abstains from answering the question
Error executing query 2734: Invalid expression / Unexpected token. Line 1, Col: 931.
  agnoses_icd.charttime) = datetime('2105-12-31 23:59:00','-1 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2735: Model only answers one image question SQLs
Error executing query 2738: Model abstains from answering the question
Error executing query 2739: Model abstains from answering the question
Error executing query 2740: Model only answers one image question SQLs
Error executing query 2741: Expecting ). Line 1, Col: 788.
  etime('2105-12-31 23:59:00','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month') gro
Error executing query 2742: Expecting ). Line 1, Col: 873.
  %Y',prescriptions.starttime) >= '2103' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 2743: Invalid expression / Unexpected token. Line 1, Col: 866.
  own low lung volumes in the cardiac silhouette?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2744: Invalid expression / Unexpected token. Line 1, Col: 976.
  normality identified in the cardiac silhouette?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2745: Model only answers one image question SQLs
Error executing query 2746: Model abstains from answering the question
[True]
Error executing query 2747: near "(": syntax error
Error executing query 2749: Expecting ). Line 1, Col: 812.
  microbiologyevents.charttime) = '2102' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.test_name ) as t3 where t3.c1 = 4
Error executing query 2750: Invalid expression / Unexpected token. Line 1, Col: 780.
  ild pattern in the right lung on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2752: Model only answers one image question SQLs
Error executing query 2755: Model only answers one image question SQLs
Error executing query 2756: Invalid expression / Unexpected token. Line 1, Col: 962.
  ny indication of any diseases on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2757: Invalid expression / Unexpected token. Line 1, Col: 758.
  indication of any abnormality on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2758: Model abstains from answering the question
Error executing query 2759: Model only answers one image question SQLs
Error executing query 2760: Invalid expression / Unexpected token. Line 1, Col: 772.
  052988 ) and strftime('%Y-%m',prescriptions.starttime) >= '2102-07' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2761: Model only answers one image question SQLs
Error executing query 2762: Model abstains from answering the question
Error executing query 2765: Model only answers one image question SQLs
Error executing query 2766: Model abstains from answering the question
Error executing query 2767: Invalid expression / Unexpected token. Line 1, Col: 889.
  d = 19055351 ) and strftime('%Y',procedures_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2768: Model abstains from answering the question
Error executing query 2769: Model only answers one image question SQLs
Error executing query 2772: Model abstains from answering the question
Error executing query 2773: Invalid expression / Unexpected token. Line 1, Col: 787.
  ses in the cardiac silhouette on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2774: Model abstains from answering the question
Error executing query 2775: Model abstains from answering the question
Error executing query 2776: Model abstains from answering the question
Error executing query 2777: Model abstains from answering the question
Error executing query 2780: Model abstains from answering the question
Error executing query 2781: Invalid expression / Unexpected token. Line 1, Col: 654.
  ns.hadm_id from admissions where admissions.subject_id = 18501203 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 2782: Invalid expression / Unexpected token. Line 1, Col: 880.
  d = 15655083 ) and strftime('%Y',diagnoses_icd.charttime) >= '2105' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2783: Model abstains from answering the question
Error executing query 2786: Model abstains from answering the question
Error executing query 2787: Model abstains from answering the question
Error executing query 2790: Invalid expression / Unexpected token. Line 1, Col: 858.
  ndicated mass/nodule (not otherwise specified)?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2795: Expecting ). Line 1, Col: 880.
  ime) >= '2105' ) as t2 join admissions on t2.subject_id = admissions.subject_id where t2.charttime  [4madmissions[0m.admittime and strftime('%Y',admissions.admittime) >= '2105' and datetime(admissions.admittime) betw
[True]
Error executing query 2796: Model abstains from answering the question
Error executing query 2797: Invalid expression / Unexpected token. Line 1, Col: 760.
  lity in the right apical zone on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
[False]
Error executing query 2799: Model abstains from answering the question
Error executing query 2800: Model abstains from answering the question
[False]
Error executing query 2802: Model abstains from answering the question
Error executing query 2803: Model only answers one image question SQLs
Error executing query 2804: Model abstains from answering the question
Error executing query 2805: Model abstains from answering the question
Error executing query 2806: Model abstains from answering the question
Error executing query 2807: Model abstains from answering the question
Error executing query 2808: Model abstains from answering the question
Error executing query 2809: Model only answers one image question SQLs
Error executing query 2810: Invalid expression / Unexpected token. Line 1, Col: 905.
  vqa("does a chest x-ray reveal any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2811: Expecting ). Line 1, Col: 808.
  me('%Y',labevents.charttime) >= '2105' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 2812: Model abstains from answering the question
Error executing query 2813: Model abstains from answering the question
Error executing query 2814: Model abstains from answering the question
Error executing query 2815: Invalid expression / Unexpected token. Line 1, Col: 880.
  d = 15647220 ) and strftime('%Y',procedures_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2816: Model only answers one image question SQLs
Error executing query 2817: Model only answers one image question SQLs
Error executing query 2818: Model abstains from answering the question
Error executing query 2819: Model abstains from answering the question
Error executing query 2823: Expecting ). Line 1, Col: 894.
  %Y',procedures_icd.charttime) = '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 2826: Expecting ). Line 1, Col: 937.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 2831: Invalid expression / Unexpected token. Line 1, Col: 628.
   a chest x-ray showing cardiac pacer and wires?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2834: Model abstains from answering the question
Error executing query 2836: Model only answers one image question SQLs
Error executing query 2837: Invalid expression / Unexpected token. Line 1, Col: 619.
  ns.hadm_id from admissions where admissions.subject_id = 14771014 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2838: Model only answers one image question SQLs
Error executing query 2839: Invalid expression / Unexpected token. Line 1, Col: 765.
  -ray shown any devices in the right chest wall?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2840: Model abstains from answering the question
Error executing query 2844: Model only answers one image question SQLs
Error executing query 2845: Model only answers one image question SQLs
Error executing query 2846: Model abstains from answering the question
Error executing query 2848: Invalid expression / Unexpected token. Line 1, Col: 1043.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id
Error executing query 2849: Model abstains from answering the question
Error executing query 2851: Expecting ). Line 1, Col: 827.
  microbiologyevents.charttime) = '2102' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.spec_type_desc ) as t3 where t3.c1 = 4
Error executing query 2852: Model abstains from answering the question
Error executing query 2853: Invalid expression / Unexpected token. Line 1, Col: 854.
  id = 16672541 ) and strftime('%Y',diagnoses_icd.charttime) = '2101' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2854: Invalid expression / Unexpected token. Line 1, Col: 966.
  edures_icd.charttime) = datetime('2105-12-31 23:59:00','-26 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2856: Model abstains from answering the question
Error executing query 2857: Invalid expression / Unexpected token. Line 1, Col: 884.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 2859: Model abstains from answering the question
Error executing query 2861: Model abstains from answering the question
Error executing query 2863: Model abstains from answering the question
Error executing query 2864: Model abstains from answering the question
Error executing query 2865: Model abstains from answering the question
Error executing query 2866: Invalid expression / Unexpected token. Line 1, Col: 886.
   = 12215941 ) and strftime('%Y',procedures_icd.charttime) >= '2105' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2867: Model abstains from answering the question
Error executing query 2868: Model only answers one image question SQLs
Error executing query 2872: Invalid expression / Unexpected token. Line 1, Col: 875.
  ("is any abnormality revealed on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2873: Invalid expression / Unexpected token. Line 1, Col: 949.
  ny diseases revealed in the cardiac silhouette?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2874: near "(": syntax error
Error executing query 2875: Invalid expression / Unexpected token. Line 1, Col: 832.
  nc_vqa("is any diseases shown on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2877: Model only answers one image question SQLs
Error executing query 2878: Model only answers one image question SQLs
Error executing query 2880: Model abstains from answering the question
Error executing query 2881: Expecting ). Line 1, Col: 803.
  labevents.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.itemid ) as t3 where t3.c1 = 3 )
Error executing query 2882: Invalid expression / Unexpected token. Line 1, Col: 879.
  indication of any tubes/lines on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2883: Model abstains from answering the question
Error executing query 2884: Model only answers one image question SQLs
Error executing query 2885: Model abstains from answering the question
Error executing query 2886: Model abstains from answering the question
Error executing query 2887: Model abstains from answering the question
Error executing query 2888: Model only answers one image question SQLs
Error executing query 2889: Model abstains from answering the question
Error executing query 2890: Model only answers one image question SQLs
Error executing query 2891: Model abstains from answering the question
Error executing query 2892: Model abstains from answering the question
Error executing query 2893: Model abstains from answering the question
Error executing query 2895: Model abstains from answering the question
Error executing query 2897: Expecting ). Line 1, Col: 864.
  etime('2105-12-31 23:59:00','-3 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 3
Error executing query 2898: Expecting ). Line 1, Col: 944.
  etime('2105-12-31 23:59:00','-4 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.icd_code ) as t3 where t3.c1 = 5 )
Error executing query 2899: Model abstains from answering the question
Error executing query 2900: Invalid expression / Unexpected token. Line 1, Col: 1036.
   func_vqa("is any anatomical findings revealed?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2901: Model abstains from answering the question
Error executing query 2902: Model only answers one image question SQLs
Error executing query 2905: Invalid expression / Unexpected token. Line 1, Col: 792.
  indication of any abnormality on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2906: Model abstains from answering the question
Error executing query 2908: Model only answers one image question SQLs
Error executing query 2909: Model only answers one image question SQLs
Error executing query 2910: Model only answers one image question SQLs
Error executing query 2911: Invalid expression / Unexpected token. Line 1, Col: 790.
   x-ray indicate any any tubes/lines in the svc?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 2912: Model only answers one image question SQLs
Error executing query 2913: Model abstains from answering the question
Error executing query 2914: Model abstains from answering the question
Error executing query 2916: Model only answers one image question SQLs
Error executing query 2917: Model abstains from answering the question
Error executing query 2918: Model abstains from answering the question
Error executing query 2919: Model only answers one image question SQLs
Error executing query 2920: Model abstains from answering the question
Error executing query 2921: Expecting ). Line 1, Col: 958.
  '%Y',diagnoses_icd.charttime) = '2105' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 2924: Model abstains from answering the question
Error executing query 2926: Invalid expression / Unexpected token. Line 1, Col: 867.
  4972735 ) and strftime('%Y-%m',diagnoses_icd.charttime) = '2105-11' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2927: Model abstains from answering the question
Error executing query 2928: Invalid expression / Unexpected token. Line 1, Col: 861.
  id = 10501557 ) and strftime('%Y',diagnoses_icd.charttime) = '2105' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2930: Model only answers one image question SQLs
Error executing query 2932: Invalid expression / Unexpected token. Line 1, Col: 739.
  dicate infiltration in the right mid lung zone?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2933: Invalid expression / Unexpected token. Line 1, Col: 744.
  id = 14881769 ) and strftime('%Y',prescriptions.starttime) = '2100' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 2934: Invalid expression / Unexpected token. Line 1, Col: 919.
  cedures_icd.charttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2935: Model only answers one image question SQLs
Error executing query 2937: Model abstains from answering the question
Error executing query 2938: Invalid expression / Unexpected token. Line 1, Col: 841.
  e func_vqa("has an x-ray indicated bone lesion?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2939: Invalid expression / Unexpected token. Line 1, Col: 388.
  e d_items.label ='respiratory rate' and d_items.linksto = 'chartevents' ) and chartevents.valuenum  [4m21.0[0m and strftime('%Y-%m-%d',chartevents.charttime) = '2105-12-26'
Error executing query 2940: Model only answers one image question SQLs
Error executing query 2941: Model only answers one image question SQLs
Error executing query 2942: Model abstains from answering the question
Error executing query 2944: Model abstains from answering the question
Error executing query 2947: Model only answers one image question SQLs
Error executing query 2948: Model abstains from answering the question
Error executing query 2949: Model abstains from answering the question
[True]
Error executing query 2952: Model abstains from answering the question
Error executing query 2953: Invalid expression / Unexpected token. Line 1, Col: 773.
  052988 ) and strftime('%Y-%m',prescriptions.starttime) >= '2102-08' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2954: Model only answers one image question SQLs
Error executing query 2955: Invalid expression / Unexpected token. Line 1, Col: 950.
  indication of any tubes/lines on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 2956: Invalid expression / Unexpected token. Line 1, Col: 1003.
  nth') = datetime('2105-12-31 23:59:00','start of month','-1 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2959: Invalid expression / Unexpected token. Line 1, Col: 1071.
   any tubes/lines identified in the aortic arch?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2960: Model only answers one image question SQLs
Error executing query 2961: Model abstains from answering the question
Error executing query 2963: Model abstains from answering the question
Error executing query 2965: Model only answers one image question SQLs
Error executing query 2967: Model abstains from answering the question
Error executing query 2968: Expecting ). Line 1, Col: 898.
  time) = '2105' ) as t2 join admissions on t2.subject_id = admissions.subject_id where t2.charttime  [4madmissions[0m.admittime and strftime('%Y',admissions.admittime) = '2105' and datetime(admissions.admittime) betwe
Error executing query 2970: Invalid expression / Unexpected token. Line 1, Col: 883.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month')
Error executing query 2971: Model abstains from answering the question
[True]
Error executing query 2972: near "(": syntax error
Error executing query 2973: Model only answers one image question SQLs
Error executing query 2974: Invalid expression / Unexpected token. Line 1, Col: 730.
  id = 16881085 ) and strftime('%Y',prescriptions.starttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 2975: Model abstains from answering the question
Error executing query 2976: Model abstains from answering the question
Error executing query 2977: Model only answers one image question SQLs
Error executing query 2978: Invalid expression / Unexpected token. Line 1, Col: 788.
  led in the left mid lung zone on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2980: Model only answers one image question SQLs
Error executing query 2984: Model abstains from answering the question
Error executing query 2986: Model abstains from answering the question
Error executing query 2990: Expecting ). Line 1, Col: 991.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.icd_code ) as t3 where t3.c1 = 4 )
Error executing query 2991: Invalid expression / Unexpected token. Line 1, Col: 834.
  l any any abnormality in the upper mediastinum?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 2992: Invalid expression / Unexpected token. Line 1, Col: 883.
  2822417 ) and strftime('%Y-%m',diagnoses_icd.charttime) = '2105-05' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2993: Model abstains from answering the question
Error executing query 2994: Model only answers one image question SQLs
Error executing query 2995: Model abstains from answering the question
Error executing query 2996: Invalid expression / Unexpected token. Line 1, Col: 727.
   a chest x-ray showing any anatomical findings?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2997: Model abstains from answering the question
Error executing query 2998: Invalid expression / Unexpected token. Line 1, Col: 982.
   = 10993512 ) and strftime('%Y',procedures_icd.charttime) >= '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and t1.hadm_id = t3.hadm_id
Error executing query 3000: Model abstains from answering the question
Error executing query 3002: Model abstains from answering the question
Error executing query 3003: Invalid expression / Unexpected token. Line 1, Col: 759.
  ns.hadm_id from admissions where admissions.subject_id = 10104308 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3004: Model only answers one image question SQLs
Error executing query 3007: Model abstains from answering the question
Error executing query 3008: Model abstains from answering the question
Error executing query 3010: Model abstains from answering the question
Error executing query 3012: Model abstains from answering the question
Error executing query 3013: Expecting ). Line 1, Col: 650.
  '%Y',prescriptions.starttime) = '2105' ) as t2 on t1.subject_id = t2.subject_id where t1.starttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 5
Error executing query 3014: Invalid expression / Unexpected token. Line 1, Col: 755.
  vqa("is any abnormality shown on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3016: Invalid expression / Unexpected token. Line 1, Col: 1049.
   = 16476036 ) and strftime('%Y',procedures_icd.charttime) >= '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and t1.hadm_id = t3.hadm_id
Error executing query 3017: Model only answers one image question SQLs
Error executing query 3019: Model abstains from answering the question
Error executing query 3020: Model abstains from answering the question
Error executing query 3024: near "(": syntax error
Error executing query 3025: Model only answers one image question SQLs
Error executing query 3027: Invalid expression / Unexpected token. Line 1, Col: 898.
  id = 12648153 ) and strftime('%Y',diagnoses_icd.charttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3029: near "(": syntax error
Error executing query 3030: Invalid expression / Unexpected token. Line 1, Col: 786.
  hest x-ray indicate interstitial lung diseases?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 3031: Model only answers one image question SQLs
[False]
Error executing query 3032: near "(": syntax error
Error executing query 3033: Model abstains from answering the question
Error executing query 3034: Model abstains from answering the question
Error executing query 3037: Model only answers one image question SQLs
Error executing query 3038: Invalid expression / Unexpected token. Line 1, Col: 930.
  agnoses_icd.charttime) >= datetime('2105-12-31 23:59:00','-3 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3039: Model abstains from answering the question
Error executing query 3042: Invalid expression / Unexpected token. Line 1, Col: 881.
  howing lung opacity in the right mid lung zone?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3043: Invalid expression / Unexpected token. Line 1, Col: 842.
  unc_vqa("is any anatomical findings identified?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
[False]
Error executing query 3044: near "(": syntax error
Error executing query 3045: Model only answers one image question SQLs
Error executing query 3046: Model abstains from answering the question
Error executing query 3047: Invalid expression / Unexpected token. Line 1, Col: 972.
  ("is any abnormality revealed on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
[True]
Error executing query 3050: Invalid expression / Unexpected token. Line 1, Col: 785.
   func_vqa("does a chest x-ray indicate rotated?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 3051: Invalid expression / Unexpected token. Line 1, Col: 1035.
  dures_icd.charttime) >= datetime('2105-12-31 23:59:00','-10 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and t1.hadm_id = t3.hadm_id
Error executing query 3053: Invalid expression / Unexpected token. Line 1, Col: 882.
  ray shown any abnormality in the left shoulder?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3054: Model only answers one image question SQLs
Error executing query 3059: Model abstains from answering the question
Error executing query 3061: Model abstains from answering the question
Error executing query 3062: Model only answers one image question SQLs
Error executing query 3063: Expecting ). Line 1, Col: 967.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 3065: Model abstains from answering the question
Error executing query 3066: Model abstains from answering the question
Error executing query 3070: Model abstains from answering the question
Error executing query 3073: Model abstains from answering the question
Error executing query 3076: Invalid expression / Unexpected token. Line 1, Col: 911.
  d = 14420647 ) and strftime('%Y',diagnoses_icd.charttime) >= '2102' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3078: Model abstains from answering the question
Error executing query 3079: Invalid expression / Unexpected token. Line 1, Col: 752.
  strated any abnormality in the left chest wall?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 3081: Model only answers one image question SQLs
Error executing query 3082: Model abstains from answering the question
Error executing query 3083: Model abstains from answering the question
Error executing query 3084: Expecting ). Line 1, Col: 996.
  ar','-0 year') ) as t2 join admissions on t2.subject_id = admissions.subject_id where t2.charttime  [4madmissions[0m.admittime and datetime(admissions.admittime,'start of year') = datetime('2105-12-31 23:59:00','star
Error executing query 3085: Expecting ). Line 1, Col: 979.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 3087: Model abstains from answering the question
Error executing query 3089: Model abstains from answering the question
Error executing query 3090: Model only answers one image question SQLs
Error executing query 3091: Model only answers one image question SQLs
Error executing query 3092: Model abstains from answering the question
Error executing query 3093: Model abstains from answering the question
Error executing query 3095: Model only answers one image question SQLs
Error executing query 3096: Model abstains from answering the question
Error executing query 3097: Invalid expression / Unexpected token. Line 1, Col: 955.
  e('%m',prescriptions.starttime) = '04' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 d
Error executing query 3100: Model abstains from answering the question
Error executing query 3101: Model only answers one image question SQLs
Error executing query 3102: Model abstains from answering the question
Error executing query 3105: Model abstains from answering the question
Error executing query 3108: Invalid expression / Unexpected token. Line 1, Col: 761.
  d = 12843379 ) and strftime('%Y',prescriptions.starttime) >= '2101' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 3110: Model only answers one image question SQLs
Error executing query 3111: Model only answers one image question SQLs
Error executing query 3113: Model abstains from answering the question
Error executing query 3114: Expecting ). Line 1, Col: 901.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 3115: Model only answers one image question SQLs
Error executing query 3117: Error tokenizing 'ydatetime) and datetime(t3.studydatetime,'+2 mont'
Error executing query 3118: Model abstains from answering the question
Error executing query 3119: Invalid expression / Unexpected token. Line 1, Col: 748.
  d = 12255996 ) and strftime('%Y',prescriptions.starttime) >= '2103' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3120: Model only answers one image question SQLs
Error executing query 3121: Model abstains from answering the question
Error executing query 3122: Model only answers one image question SQLs
Error executing query 3124: Invalid expression / Unexpected token. Line 1, Col: 863.
  st x-ray detecting spinal degenerative changes?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3125: Invalid expression / Unexpected token. Line 1, Col: 699.
  ns.hadm_id from admissions where admissions.subject_id = 15528228 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 3126: Model abstains from answering the question
Error executing query 3127: Model only answers one image question SQLs
Error executing query 3128: Model abstains from answering the question
Error executing query 3130: Model abstains from answering the question
Error executing query 3131: Invalid expression / Unexpected token. Line 1, Col: 1106.
   year','-0 year') and strftime('%m',diagnoses_icd.charttime) = '08' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime)
Error executing query 3132: Model abstains from answering the question
Error executing query 3134: Model only answers one image question SQLs
Error executing query 3135: Model abstains from answering the question
Error executing query 3136: Invalid expression / Unexpected token. Line 1, Col: 1101.
   year') = datetime('2105-12-31 23:59:00','start of year','-0 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3137: near "(": syntax error
Error executing query 3138: Model abstains from answering the question
Error executing query 3139: Model only answers one image question SQLs
Error executing query 3141: Model only answers one image question SQLs
Error executing query 3142: Model abstains from answering the question
Error executing query 3143: Model only answers one image question SQLs
Error executing query 3144: Model abstains from answering the question
Error executing query 3145: Expecting ). Line 1, Col: 926.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 3147: Model abstains from answering the question
Error executing query 3148: Invalid expression / Unexpected token. Line 1, Col: 862.
  icate any abnormality in the upper mediastinum?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3150: Model only answers one image question SQLs
Error executing query 3151: Invalid expression / Unexpected token. Line 1, Col: 936.
  agnoses_icd.charttime) >= datetime('2105-12-31 23:59:00','-2 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3152: Invalid expression / Unexpected token. Line 1, Col: 868.
   anatomical findings revealed on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3153: Model abstains from answering the question
Error executing query 3154: Model abstains from answering the question
Error executing query 3156: Model abstains from answering the question
Error executing query 3158: Model abstains from answering the question
Error executing query 3160: Model only answers one image question SQLs
Error executing query 3162: Model only answers one image question SQLs
Error executing query 3163: Invalid expression / Unexpected token. Line 1, Col: 879.
  ot otherwise specified) shown on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3164: Invalid expression / Unexpected token. Line 1, Col: 940.
  as t2 where func_vqa("is any diseases revealed?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3165: Model only answers one image question SQLs
Error executing query 3166: Model abstains from answering the question
Error executing query 3167: Model abstains from answering the question
Error executing query 3169: Model abstains from answering the question
Error executing query 3170: Model only answers one image question SQLs
Error executing query 3171: Model abstains from answering the question
Error executing query 3172: Model abstains from answering the question
Error executing query 3173: Invalid expression / Unexpected token. Line 1, Col: 975.
   year') = datetime('2105-12-31 23:59:00','start of year','-0 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3174: Invalid expression / Unexpected token. Line 1, Col: 824.
  id = 10020740 ) and strftime('%Y',diagnoses_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3176: Invalid expression / Unexpected token. Line 1, Col: 871.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 3177: Model only answers one image question SQLs
Error executing query 3178: Model abstains from answering the question
Error executing query 3180: Model abstains from answering the question
Error executing query 3181: Model abstains from answering the question
Error executing query 3182: Model only answers one image question SQLs
Error executing query 3185: Model abstains from answering the question
Error executing query 3189: Expecting ). Line 1, Col: 1018.
  re prescriptions.drug = 'pantoprazole' ) as t3 on t2.subject_id = t3.subject_id where t2.charttime  [4mt3[0m.starttime ) as t4 join patients on t4.subject_id = patients.subject_id
Error executing query 3192: Model abstains from answering the question
Error executing query 3197: Model only answers one image question SQLs
Error executing query 3198: Model abstains from answering the question
Error executing query 3199: Model only answers one image question SQLs
Error executing query 3200: Model abstains from answering the question
Error executing query 3203: Model abstains from answering the question
Error executing query 3204: Model only answers one image question SQLs
Error executing query 3207: Model abstains from answering the question
Error executing query 3208: Model abstains from answering the question
Error executing query 3209: Model only answers one image question SQLs
Error executing query 3210: Invalid expression / Unexpected token. Line 1, Col: 946.
  ocedures_icd.charttime) = datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3211: Model abstains from answering the question
Error executing query 3213: Model abstains from answering the question
Error executing query 3216: Expecting ). Line 1, Col: 850.
  etime('2105-12-31 23:59:00','-4 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 3217: Model abstains from answering the question
Error executing query 3218: Model abstains from answering the question
Error executing query 3219: Invalid expression / Unexpected token. Line 1, Col: 761.
  d = 17267281 ) and strftime('%Y',prescriptions.starttime) >= '2105' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 3221: Invalid expression / Unexpected token. Line 1, Col: 729.
  d = 19949061 ) and strftime('%Y',prescriptions.starttime) >= '2104' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 3224: Model abstains from answering the question
Error executing query 3226: Invalid expression / Unexpected token. Line 1, Col: 861.
  est x-ray depicting any abnormality in the svc?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3227: Invalid expression / Unexpected token. Line 1, Col: 639.
  where admissions.subject_id = 15528228 ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 d
Error executing query 3228: Model abstains from answering the question
Error executing query 3229: Model only answers one image question SQLs
Error executing query 3231: Invalid expression / Unexpected token. Line 1, Col: 661.
  onsolidation in the left lung on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 3233: Invalid expression / Unexpected token. Line 1, Col: 750.
  any devices identified in the right chest wall?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3234: Model abstains from answering the question
Error executing query 3235: Model abstains from answering the question
Error executing query 3237: Invalid expression / Unexpected token. Line 1, Col: 917.
  ocedures_icd.charttime) = datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3238: Model abstains from answering the question
Error executing query 3239: Model only answers one image question SQLs
Error executing query 3241: Model abstains from answering the question
Error executing query 3242: Model abstains from answering the question
Error executing query 3243: Invalid expression / Unexpected token. Line 1, Col: 879.
  d = 17112656 ) and strftime('%Y',procedures_icd.charttime) = '2102' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3244: Model abstains from answering the question
Error executing query 3246: Model abstains from answering the question
Error executing query 3247: Model abstains from answering the question
Error executing query 3248: Invalid expression / Unexpected token. Line 1, Col: 796.
  echnical assessments observed on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3250: Model abstains from answering the question
Error executing query 3252: Model abstains from answering the question
Error executing query 3253: Model abstains from answering the question
Error executing query 3254: Invalid expression / Unexpected token. Line 1, Col: 819.
  x-ray indicate copd/emphysema in the left lung?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 3255: Model abstains from answering the question
Error executing query 3256: Expecting ). Line 1, Col: 828.
  etime('2105-12-31 23:59:00','-5 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month') gro
Error executing query 3257: Invalid expression / Unexpected token. Line 1, Col: 739.
  vqa("does a chest x-ray reveal any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3258: Invalid expression / Unexpected token. Line 1, Col: 882.
  d = 18476657 ) and strftime('%Y',procedures_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3260: Model abstains from answering the question
Error executing query 3261: Model only answers one image question SQLs
Error executing query 3262: Model only answers one image question SQLs
Error executing query 3263: Model abstains from answering the question
Error executing query 3264: Invalid expression / Unexpected token. Line 1, Col: 911.
  agnoses_icd.charttime) = datetime('2105-12-31 23:59:00','-3 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3266: Model abstains from answering the question
Error executing query 3267: Invalid expression / Unexpected token. Line 1, Col: 913.
  edures_icd.charttime) >= datetime('2105-12-31 23:59:00','-4 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3268: Model abstains from answering the question
Error executing query 3270: Model only answers one image question SQLs
Error executing query 3271: Invalid expression / Unexpected token. Line 1, Col: 960.
  cedures_icd.charttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3272: Model only answers one image question SQLs
Error executing query 3273: Model only answers one image question SQLs
Error executing query 3274: Model abstains from answering the question
Error executing query 3275: Model abstains from answering the question
Error executing query 3276: Model only answers one image question SQLs
Error executing query 3277: Model abstains from answering the question
Error executing query 3278: Model only answers one image question SQLs
Error executing query 3280: Model only answers one image question SQLs
Error executing query 3282: Model abstains from answering the question
Error executing query 3283: Model only answers one image question SQLs
Error executing query 3285: Invalid expression / Unexpected token. Line 1, Col: 800.
  escriptions.starttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 3286: Model abstains from answering the question
Error executing query 3289: Model abstains from answering the question
Error executing query 3290: Model abstains from answering the question
Error executing query 3291: Invalid expression / Unexpected token. Line 1, Col: 920.
  cedures_icd.charttime) >= datetime('2105-12-31 23:59:00','-5 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3296: Expecting ). Line 1, Col: 803.
  icrobiologyevents.charttime) >= '2101' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 3298: Model only answers one image question SQLs
Error executing query 3299: Model abstains from answering the question
Error executing query 3300: Invalid expression / Unexpected token. Line 1, Col: 860.
  qa("is pneumomediastinum indicated on an x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3302: Invalid expression / Unexpected token. Line 1, Col: 876.
  4420647 ) and strftime('%Y-%m',diagnoses_icd.charttime) = '2102-05' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3303: Invalid expression / Unexpected token. Line 1, Col: 907.
  2904315 ) and strftime('%Y-%m',diagnoses_icd.charttime) = '2104-11' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3306: Model only answers one image question SQLs
Error executing query 3307: Invalid expression / Unexpected token. Line 1, Col: 824.
  %Y',diagnoses_icd.charttime) >= '2103' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 3308: Model abstains from answering the question
Error executing query 3309: Invalid expression / Unexpected token. Line 1, Col: 815.
  ns.hadm_id from admissions where admissions.subject_id = 18551168 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3310: Expecting ). Line 1, Col: 859.
  etime('2105-12-31 23:59:00','-5 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 3312: Model abstains from answering the question
Error executing query 3313: Model abstains from answering the question
Error executing query 3318: Model abstains from answering the question
Error executing query 3319: Model only answers one image question SQLs
Error executing query 3320: Model only answers one image question SQLs
Error executing query 3322: Model abstains from answering the question
Error executing query 3323: Model abstains from answering the question
Error executing query 3324: Model abstains from answering the question
Error executing query 3325: Invalid expression / Unexpected token. Line 1, Col: 745.
  ns.hadm_id from admissions where admissions.subject_id = 14047359 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3327: Invalid expression / Unexpected token. Line 1, Col: 923.
  noses_icd.charttime) >= datetime('2105-12-31 23:59:00','-68 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3328: Model only answers one image question SQLs
Error executing query 3329: Model only answers one image question SQLs
Error executing query 3330: Model only answers one image question SQLs
Error executing query 3331: Model abstains from answering the question
Error executing query 3333: Model abstains from answering the question
Error executing query 3334: Model only answers one image question SQLs
Error executing query 3335: Invalid expression / Unexpected token. Line 1, Col: 759.
  id = 11422357 ) and strftime('%Y',prescriptions.starttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 3336: Model abstains from answering the question
Error executing query 3337: Model abstains from answering the question
Error executing query 3339: Invalid expression / Unexpected token. Line 1, Col: 788.
  rescriptions.starttime) = datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 3341: Invalid expression / Unexpected token. Line 1, Col: 851.
  how any anatomical findings in the aortic arch?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3343: Invalid expression / Unexpected token. Line 1, Col: 629.
  ns.hadm_id from admissions where admissions.subject_id = 15491652 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 3344: Invalid expression / Unexpected token. Line 1, Col: 627.
  a chest x-ray indicate vascular redistribution?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
[True]
Error executing query 3345: near "(": syntax error
Error executing query 3349: Invalid expression / Unexpected token. Line 1, Col: 757.
  ns.hadm_id from admissions where admissions.subject_id = 12957707 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3350: Model only answers one image question SQLs
Error executing query 3352: Model abstains from answering the question
Error executing query 3354: Model only answers one image question SQLs
Error executing query 3356: Model only answers one image question SQLs
Error executing query 3357: Model abstains from answering the question
Error executing query 3359: Invalid expression / Unexpected token. Line 1, Col: 947.
  s in the left lower lung zone on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3363: Invalid expression / Unexpected token. Line 1, Col: 865.
  id = 17964648 ) and strftime('%Y',diagnoses_icd.charttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3364: Invalid expression / Unexpected token. Line 1, Col: 934.
  '%Y',diagnoses_icd.charttime) = '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id
Error executing query 3366: Invalid expression / Unexpected token. Line 1, Col: 861.
  id = 15790605 ) and strftime('%Y',diagnoses_icd.charttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3368: Model abstains from answering the question
Error executing query 3369: Model abstains from answering the question
Error executing query 3370: Invalid expression / Unexpected token. Line 1, Col: 731.
  t x-ray indicate any any technical assessments?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3371: Invalid expression / Unexpected token. Line 1, Col: 1002.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3372: Model abstains from answering the question
Error executing query 3374: Model abstains from answering the question
Error executing query 3375: Invalid expression / Unexpected token. Line 1, Col: 987.
   year') = datetime('2105-12-31 23:59:00','start of year','-0 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3376: Model abstains from answering the question
Error executing query 3377: Model only answers one image question SQLs
Error executing query 3378: Model abstains from answering the question
Error executing query 3379: Model only answers one image question SQLs
Error executing query 3380: Model only answers one image question SQLs
Error executing query 3381: Invalid expression / Unexpected token. Line 1, Col: 762.
  ny diseases in the right lung on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 3382: Invalid expression / Unexpected token. Line 1, Col: 905.
  ny abnormality in the right costophrenic angle?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3383: Model abstains from answering the question
Error executing query 3384: Model abstains from answering the question
Error executing query 3385: Model only answers one image question SQLs
Error executing query 3386: Model abstains from answering the question
Error executing query 3387: Model only answers one image question SQLs
Error executing query 3388: Invalid expression / Unexpected token. Line 1, Col: 904.
  d = 11026054 ) and strftime('%Y',procedures_icd.charttime) = '2100' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3390: Invalid expression / Unexpected token. Line 1, Col: 1000.
  48597 ) and strftime('%Y-%m',procedures_icd.charttime) >= '2105-10' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and t1.hadm_id = t3.hadm_id
Error executing query 3391: Invalid expression / Unexpected token. Line 1, Col: 786.
  ns.hadm_id from admissions where admissions.subject_id = 18002691 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3396: Model abstains from answering the question
Error executing query 3397: Invalid expression / Unexpected token. Line 1, Col: 841.
  ns.hadm_id from admissions where admissions.subject_id = 18551168 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3398: Model abstains from answering the question
Error executing query 3400: Model abstains from answering the question
Error executing query 3401: Invalid expression / Unexpected token. Line 1, Col: 793.
  scriptions.starttime) = datetime('2105-12-31 23:59:00','-18 month') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3404: Invalid expression / Unexpected token. Line 1, Col: 1009.
  s.dischtime is not null order by admissions.admittime asc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3405: Model abstains from answering the question
Error executing query 3407: Model abstains from answering the question
Error executing query 3409: Model abstains from answering the question
Error executing query 3413: Model only answers one image question SQLs
Error executing query 3414: Invalid expression / Unexpected token. Line 1, Col: 1038.
   year') = datetime('2105-12-31 23:59:00','start of year','-0 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3415: Model abstains from answering the question
Error executing query 3417: Model only answers one image question SQLs
Error executing query 3418: Model abstains from answering the question
Error executing query 3419: Expecting ). Line 1, Col: 831.
  etime('2105-12-31 23:59:00','-5 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month') gro
Error executing query 3420: Model only answers one image question SQLs
Error executing query 3423: Invalid expression / Unexpected token. Line 1, Col: 847.
  ("is any abnormality observed on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 3424: Model abstains from answering the question
Error executing query 3426: Expecting ). Line 1, Col: 778.
  icrobiologyevents.charttime) >= '2103' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 3427: Model abstains from answering the question
Error executing query 3428: Invalid expression / Unexpected token. Line 1, Col: 903.
  indicate any diseases in the upper mediastinum?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3430: Invalid expression / Unexpected token. Line 1, Col: 945.
   shown breast/nipple shadows in the right lung?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3431: Model only answers one image question SQLs
Error executing query 3433: Model abstains from answering the question
Error executing query 3435: Required keyword: 'expressions' missing for <class 'sqlglot.expressions.Aliases'>. Line 1, Col: 406.
  labitems where d_labitems.label ='red blood cells' ) order by labevents.charttime desc limit 1 )  ( [4mselect[0m labevents.valuenum from labevents where labevents.hadm_id in ( select admissions.hadm_id from admis
Error executing query 3436: Model abstains from answering the question
Error executing query 3437: Model only answers one image question SQLs
Error executing query 3438: Model abstains from answering the question
Error executing query 3439: Model only answers one image question SQLs
Error executing query 3441: Model abstains from answering the question
Error executing query 3442: Model only answers one image question SQLs
[True]
Error executing query 3443: near "(": syntax error
Error executing query 3445: Model only answers one image question SQLs
Error executing query 3448: Expecting ). Line 1, Col: 735.
  %Y',prescriptions.starttime) >= '2103' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month') gro
Error executing query 3450: Model abstains from answering the question
Error executing query 3451: Invalid expression / Unexpected token. Line 1, Col: 760.
  y hydropneumothorax in the right mid lung zone?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3454: Invalid expression / Unexpected token. Line 1, Col: 885.
  %Y',procedures_icd.charttime) = '2105' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
Error executing query 3455: Invalid expression / Unexpected token. Line 1, Col: 962.
  e('%m',prescriptions.starttime) = '07' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of day') = datetime(t2.starttime,'start of day')
Error executing query 3456: Model abstains from answering the question
Error executing query 3457: Model abstains from answering the question
Error executing query 3458: Invalid expression / Unexpected token. Line 1, Col: 1004.
   year') = datetime('2105-12-31 23:59:00','start of year','-0 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3460: Model abstains from answering the question
Error executing query 3461: Invalid expression / Unexpected token. Line 1, Col: 882.
  156395 ) and strftime('%Y-%m',procedures_icd.charttime) = '2105-05' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3463: Invalid expression / Unexpected token. Line 1, Col: 742.
  vqa("does a chest x-ray reveal any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3464: Model abstains from answering the question
Error executing query 3465: Model abstains from answering the question
Error executing query 3466: Model only answers one image question SQLs
Error executing query 3468: Model only answers one image question SQLs
Error executing query 3469: Model abstains from answering the question
Error executing query 3470: Model abstains from answering the question
Error executing query 3471: Model abstains from answering the question
Error executing query 3472: Invalid expression / Unexpected token. Line 1, Col: 863.
  dicated any tubes/lines in the left chest wall?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3473: Model only answers one image question SQLs
Error executing query 3474: Model abstains from answering the question
Error executing query 3476: Invalid expression / Unexpected token. Line 1, Col: 1013.
  -ray show any abnormality in the left clavicle?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3477: Model only answers one image question SQLs
Error executing query 3478: Model abstains from answering the question
Error executing query 3481: Model abstains from answering the question
Error executing query 3482: Expecting ). Line 1, Col: 676.
  ogyevents.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 3483: Model only answers one image question SQLs
Error executing query 3484: Model abstains from answering the question
Error executing query 3485: Model abstains from answering the question
Error executing query 3486: Model abstains from answering the question
Error executing query 3488: Model abstains from answering the question
Error executing query 3490: Model abstains from answering the question
Error executing query 3491: Invalid expression / Unexpected token. Line 1, Col: 899.
   func_vqa("has a chest x-ray shown any devices?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3492: Model only answers one image question SQLs
Error executing query 3494: Model only answers one image question SQLs
Error executing query 3495: Model abstains from answering the question
Error executing query 3496: Model abstains from answering the question
Error executing query 3497: Invalid expression / Unexpected token. Line 1, Col: 898.
  cate any diseases in the left hilar structures?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3500: Invalid expression / Unexpected token. Line 1, Col: 963.
  etime('2105-12-31 23:59:00','-6 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 3501: Invalid expression / Unexpected token. Line 1, Col: 883.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 3502: Model abstains from answering the question
Error executing query 3503: Invalid expression / Unexpected token. Line 1, Col: 979.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3506: Model abstains from answering the question
Error executing query 3509: Model abstains from answering the question
Error executing query 3510: Invalid expression / Unexpected token. Line 1, Col: 865.
  975446 ) and strftime('%Y-%m',procedures_icd.charttime) = '2104-03' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3511: Invalid expression / Unexpected token. Line 1, Col: 617.
  ns.hadm_id from admissions where admissions.subject_id = 13209155 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3514: Model only answers one image question SQLs
Error executing query 3516: Model only answers one image question SQLs
Error executing query 3517: Model abstains from answering the question
Error executing query 3522: Invalid expression / Unexpected token. Line 1, Col: 944.
  cedures_icd.charttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3524: Model abstains from answering the question
Error executing query 3525: Model abstains from answering the question
Error executing query 3526: Invalid expression / Unexpected token. Line 1, Col: 814.
  ny copd/emphysema in the right upper lung zone?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 3528: Model abstains from answering the question
Error executing query 3529: Expecting ). Line 1, Col: 734.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.starttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.starttime) and datetime(t1.starttime,'+2 m
Error executing query 3530: Model only answers one image question SQLs
Error executing query 3531: Model only answers one image question SQLs
Error executing query 3532: Expecting ). Line 1, Col: 911.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 3533: Invalid expression / Unexpected token. Line 1, Col: 841.
  d = 17964648 ) and strftime('%Y',diagnoses_icd.charttime) >= '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3534: Model abstains from answering the question
Error executing query 3537: Model abstains from answering the question
Error executing query 3541: Invalid expression / Unexpected token. Line 1, Col: 788.
  scriptions.starttime) = datetime('2105-12-31 23:59:00','-20 month') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3543: Model abstains from answering the question
Error executing query 3544: Model abstains from answering the question
Error executing query 3545: Invalid expression / Unexpected token. Line 1, Col: 948.
  iagnoses_icd.charttime) = datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3546: Model only answers one image question SQLs
Error executing query 3547: Model abstains from answering the question
Error executing query 3549: Model only answers one image question SQLs
Error executing query 3551: Model abstains from answering the question
Error executing query 3554: Model only answers one image question SQLs
Error executing query 3555: Model abstains from answering the question
Error executing query 3556: Model only answers one image question SQLs
Error executing query 3557: Model abstains from answering the question
Error executing query 3558: Invalid expression / Unexpected token. Line 1, Col: 888.
  t x-ray detecting any abnormality in the spine?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3559: Expecting ). Line 1, Col: 743.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.starttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.starttime) and datetime(t1.starttime,'+2 m
Error executing query 3561: Model only answers one image question SQLs
Error executing query 3563: Model only answers one image question SQLs
Error executing query 3566: Model only answers one image question SQLs
Error executing query 3567: Model only answers one image question SQLs
Error executing query 3568: Model abstains from answering the question
Error executing query 3569: Model only answers one image question SQLs
Error executing query 3570: Model only answers one image question SQLs
Error executing query 3571: Model abstains from answering the question
Error executing query 3572: Model only answers one image question SQLs
[True]
Error executing query 3573: Model abstains from answering the question
Error executing query 3574: Model abstains from answering the question
Error executing query 3575: Model abstains from answering the question
Error executing query 3576: Model only answers one image question SQLs
Error executing query 3579: Model only answers one image question SQLs
Error executing query 3580: Invalid expression / Unexpected token. Line 1, Col: 967.
  e('%m',prescriptions.starttime) = '02' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of day') = datetime(t2.starttime,'start of day')
Error executing query 3581: Model abstains from answering the question
Error executing query 3584: Invalid expression / Unexpected token. Line 1, Col: 985.
  dures_icd.charttime) >= datetime('2105-12-31 23:59:00','-70 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3586: Invalid expression / Unexpected token. Line 1, Col: 871.
  _vqa("does a chest x-ray reveal copd/emphysema?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3587: Model only answers one image question SQLs
Error executing query 3588: Expecting ). Line 1, Col: 1171.
  er by admissions.admittime desc limit 1 ) order by tb_cxr.studydatetime desc limit 1 ) ) ) order by [4mtb_cx[0m
Error executing query 3591: Invalid expression / Unexpected token. Line 1, Col: 983.
  vqa("does the chest x-ray indicate cabg grafts?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3592: Invalid expression / Unexpected token. Line 1, Col: 954.
  does a chest x-ray show granulomatous diseases?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3593: Model abstains from answering the question
Error executing query 3595: Model abstains from answering the question
Error executing query 3596: Model abstains from answering the question
Error executing query 3599: Model abstains from answering the question
Error executing query 3601: Invalid expression / Unexpected token. Line 1, Col: 968.
  nth') = datetime('2105-12-31 23:59:00','start of month','-0 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3602: Model abstains from answering the question
Error executing query 3603: Invalid expression / Unexpected token. Line 1, Col: 840.
  id = 13368848 ) and strftime('%Y',diagnoses_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3604: Invalid expression / Unexpected token. Line 1, Col: 815.
  er by admissions.admittime asc limit 1 ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of day') = datetime(t2.starttime,'start of day')
Error executing query 3606: Invalid expression / Unexpected token. Line 1, Col: 766.
  etime('2105-12-31 23:59:00','-5 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 3607: Model abstains from answering the question
Error executing query 3608: Invalid expression / Unexpected token. Line 1, Col: 775.
  %Y',prescriptions.starttime) >= '2103' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month')
Error executing query 3610: Model abstains from answering the question
Error executing query 3612: Model only answers one image question SQLs
Error executing query 3616: Model abstains from answering the question
Error executing query 3617: Model only answers one image question SQLs
Error executing query 3619: Model only answers one image question SQLs
Error executing query 3622: Invalid expression / Unexpected token. Line 1, Col: 826.
  ng lung cancer in the right costophrenic angle?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3623: Model abstains from answering the question
Error executing query 3624: Model abstains from answering the question
Error executing query 3625: Invalid expression / Unexpected token. Line 1, Col: 971.
   year') = datetime('2105-12-31 23:59:00','start of year','-0 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3627: Model abstains from answering the question
Error executing query 3629: Model only answers one image question SQLs
Error executing query 3630: Model abstains from answering the question
Error executing query 3632: Model abstains from answering the question
Error executing query 3633: Model only answers one image question SQLs
Error executing query 3635: Model only answers one image question SQLs
Error executing query 3638: Model only answers one image question SQLs
Error executing query 3639: Invalid expression / Unexpected token. Line 1, Col: 750.
  %Y',prescriptions.starttime) >= '2102' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month')
Error executing query 3640: Invalid expression / Unexpected token. Line 1, Col: 728.
  d = 14665029 ) and strftime('%Y',prescriptions.starttime) >= '2103' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 3644: Invalid expression / Unexpected token. Line 1, Col: 862.
  c_vqa("does a chest x-ray show any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3645: Model only answers one image question SQLs
Error executing query 3647: Expecting ). Line 1, Col: 855.
  %Y',prescriptions.starttime) >= '2105' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 3650: Invalid expression / Unexpected token. Line 1, Col: 947.
  ocedures_icd.charttime) = datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3651: Expecting ). Line 1, Col: 978.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 3652: Model only answers one image question SQLs
Error executing query 3654: Model abstains from answering the question
Error executing query 3655: Model only answers one image question SQLs
Error executing query 3657: Invalid expression / Unexpected token. Line 1, Col: 797.
   mediastinal mass/enlargement on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3658: Model only answers one image question SQLs
Error executing query 3659: Model abstains from answering the question
Error executing query 3660: Invalid expression / Unexpected token. Line 1, Col: 869.
   year') = datetime('2105-12-31 23:59:00','start of year','-0 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3661: Invalid expression / Unexpected token. Line 1, Col: 789.
  %Y',diagnoses_icd.charttime) >= '2105' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
Error executing query 3662: Model abstains from answering the question
Error executing query 3663: Model only answers one image question SQLs
Error executing query 3669: Expecting ). Line 1, Col: 992.
  ar','-0 year') ) as t2 join admissions on t2.subject_id = admissions.subject_id where t2.charttime  [4madmissions[0m.admittime and datetime(admissions.admittime,'start of year') = datetime('2105-12-31 23:59:00','star
Error executing query 3671: Model only answers one image question SQLs
Error executing query 3672: Invalid expression / Unexpected token. Line 1, Col: 924.
  cedures_icd.charttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3673: Invalid expression / Unexpected token. Line 1, Col: 764.
  ',prescriptions.starttime) = '2103-10' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 d
Error executing query 3674: Model abstains from answering the question
[False]
Error executing query 3676: Model abstains from answering the question
Error executing query 3678: Invalid expression / Unexpected token. Line 1, Col: 896.
   as t2 where func_vqa("is any devices revealed?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3680: Invalid expression / Unexpected token. Line 1, Col: 993.
  agnoses_icd.charttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3681: Invalid expression / Unexpected token. Line 1, Col: 737.
  ns.hadm_id from admissions where admissions.subject_id = 18969313 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3682: near "(": syntax error
Error executing query 3683: Model only answers one image question SQLs
[True]
Error executing query 3684: Model abstains from answering the question
Error executing query 3687: Model abstains from answering the question
Error executing query 3688: Model abstains from answering the question
Error executing query 3689: Model abstains from answering the question
Error executing query 3690: Invalid expression / Unexpected token. Line 1, Col: 844.
  d = 18198385 ) and strftime('%Y',diagnoses_icd.charttime) >= '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3691: Model abstains from answering the question
Error executing query 3693: Model only answers one image question SQLs
Error executing query 3694: Model abstains from answering the question
Error executing query 3695: Model only answers one image question SQLs
Error executing query 3696: Model abstains from answering the question
Error executing query 3698: Model abstains from answering the question
Error executing query 3699: Model only answers one image question SQLs
Error executing query 3700: Expecting ). Line 1, Col: 851.
  me('%Y',labevents.charttime) >= '2101' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 3701: Invalid expression / Unexpected token. Line 1, Col: 846.
  id = 10667992 ) and strftime('%Y',diagnoses_icd.charttime) = '2105' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3703: Model abstains from answering the question
Error executing query 3706: Model abstains from answering the question
Error executing query 3709: Error tokenizing 't3.studydatetime) and datetime(t3.studydatetime,'
Error executing query 3710: Invalid expression / Unexpected token. Line 1, Col: 836.
  "does the chest x-ray indicate any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3711: Expecting ). Line 1, Col: 598.
  criptions.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month') gro
Error executing query 3712: Model only answers one image question SQLs
Error executing query 3713: Invalid expression / Unexpected token. Line 1, Col: 843.
  id = 19035431 ) and strftime('%Y',diagnoses_icd.charttime) = '2105' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3714: Invalid expression / Unexpected token. Line 1, Col: 845.
   = 18787238 ) and strftime('%Y',procedures_icd.charttime) >= '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3716: Model abstains from answering the question
Error executing query 3717: Expecting ). Line 1, Col: 1007.
  riptions.drug = '0.9% sodium chloride' ) as t3 on t2.subject_id = t3.subject_id where t2.charttime  [4mt3[0m.starttime ) as t4 join patients on t4.subject_id = patients.subject_id
Error executing query 3719: Model only answers one image question SQLs
Error executing query 3720: Model abstains from answering the question
Error executing query 3722: Model abstains from answering the question
Error executing query 3724: Model only answers one image question SQLs
Error executing query 3725: Expecting ). Line 1, Col: 758.
  labevents.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.itemid ) as t3 where t3.c1 = 5 )
Error executing query 3727: Model only answers one image question SQLs
Error executing query 3728: Invalid expression / Unexpected token. Line 1, Col: 745.
  s a chest x-ray show goiter in the mediastinum?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3729: Model abstains from answering the question
Error executing query 3730: Model only answers one image question SQLs
Error executing query 3733: Model only answers one image question SQLs
Error executing query 3734: Model only answers one image question SQLs
Error executing query 3735: Model abstains from answering the question
Error executing query 3739: Model abstains from answering the question
Error executing query 3740: Expecting ). Line 1, Col: 974.
  here prescriptions.drug = 'prednisone' ) as t3 on t2.subject_id = t3.subject_id where t2.charttime  [4mt3[0m.starttime ) as t4 join patients on t4.subject_id = patients.subject_id
Error executing query 3741: Invalid expression / Unexpected token. Line 1, Col: 816.
  criptions.starttime) >= datetime('2105-12-31 23:59:00','-64 month') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3742: Model abstains from answering the question
Error executing query 3743: Model abstains from answering the question
Error executing query 3744: Model only answers one image question SQLs
Error executing query 3746: Model only answers one image question SQLs
Error executing query 3747: Invalid expression / Unexpected token. Line 1, Col: 866.
   any abnormality in the right hilar structures?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3748: Model abstains from answering the question
Error executing query 3749: Invalid expression / Unexpected token. Line 1, Col: 774.
  _vqa("is any devices observed on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3750: Model only answers one image question SQLs
Error executing query 3751: Model only answers one image question SQLs
Error executing query 3754: Model only answers one image question SQLs
Error executing query 3756: Model abstains from answering the question
Error executing query 3757: Model abstains from answering the question
Error executing query 3758: Expecting ). Line 1, Col: 1166.
  mit 1 ) order by tb_cxr.studydatetime desc limit 1 ) ) ) order by tb_cxr.studydatetime desc limit 1 [4m)[0m
Error executing query 3759: Model abstains from answering the question
Error executing query 3761: Model only answers one image question SQLs
Error executing query 3762: Required keyword: 'expressions' missing for <class 'sqlglot.expressions.Aliases'>. Line 1, Col: 371.
  re d_labitems.label = 'lactate dehydrogenase (ld)' ) order by labevents.charttime desc limit 1 )  ( [4mselect[0m labevents.valuenum from labevents where labevents.hadm_id in ( select admissions.hadm_id from admis
Error executing query 3763: Model abstains from answering the question
Error executing query 3765: Model only answers one image question SQLs
Error executing query 3766: Model abstains from answering the question
Error executing query 3767: Model abstains from answering the question
Error executing query 3768: Model abstains from answering the question
Error executing query 3769: Invalid expression / Unexpected token. Line 1, Col: 737.
  id = 19989918 ) and strftime('%Y',prescriptions.starttime) = '2105' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 3770: Invalid expression / Unexpected token. Line 1, Col: 749.
  id = 12429112 ) and strftime('%Y',prescriptions.starttime) = '2105' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3771: Model abstains from answering the question
Error executing query 3773: Model abstains from answering the question
Error executing query 3774: Model only answers one image question SQLs
Error executing query 3775: Model only answers one image question SQLs
Error executing query 3776: Invalid expression / Unexpected token. Line 1, Col: 624.
  qa("has a chest x-ray demonstrated lung cancer?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 3777: Invalid expression / Unexpected token. Line 1, Col: 795.
  escriptions.starttime) >= datetime('2105-12-31 23:59:00','-4 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3778: Model abstains from answering the question
Error executing query 3779: Invalid expression / Unexpected token. Line 1, Col: 758.
  id = 11982468 ) and strftime('%Y',prescriptions.starttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 3781: Model abstains from answering the question
Error executing query 3782: Invalid expression / Unexpected token. Line 1, Col: 637.
  ns.hadm_id from admissions where admissions.subject_id = 11052292 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 3783: Model only answers one image question SQLs
Error executing query 3785: Model only answers one image question SQLs
Error executing query 3787: Expecting ). Line 1, Col: 624.
  criptions.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 3788: Model only answers one image question SQLs
Error executing query 3791: Invalid expression / Unexpected token. Line 1, Col: 826.
  c_vqa("does a chest x-ray show any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3792: Model only answers one image question SQLs
Error executing query 3793: Expecting ). Line 1, Col: 1213.
  time('2105-12-31 23:59:00','start of year','-1 year') and strftime('%m',procedures_icd.charttime) = [4m'11'[0m
Error executing query 3794: Invalid expression / Unexpected token. Line 1, Col: 796.
  etime('2105-12-31 23:59:00','-4 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id
Error executing query 3798: Model only answers one image question SQLs
Error executing query 3799: Model abstains from answering the question
Error executing query 3800: Model only answers one image question SQLs
Error executing query 3802: Invalid expression / Unexpected token. Line 1, Col: 652.
  ns.hadm_id from admissions where admissions.subject_id = 10104308 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 3803: Model abstains from answering the question
Error executing query 3805: Invalid expression / Unexpected token. Line 1, Col: 802.
  hest x-ray reveal fluid overload/heart failure?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 3806: Invalid expression / Unexpected token. Line 1, Col: 890.
  vqa("does a chest x-ray reveal any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3809: Model only answers one image question SQLs
Error executing query 3810: Model abstains from answering the question
Error executing query 3813: Invalid expression / Unexpected token. Line 1, Col: 860.
  c_vqa("does a chest x-ray show any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3814: Model only answers one image question SQLs
Error executing query 3815: Model abstains from answering the question
Error executing query 3818: Model only answers one image question SQLs
Error executing query 3821: Invalid expression / Unexpected token. Line 1, Col: 895.
  gnoses_icd.charttime) >= datetime('2105-12-31 23:59:00','-6 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3822: Model only answers one image question SQLs
Error executing query 3824: Model abstains from answering the question
Error executing query 3825: Model only answers one image question SQLs
Error executing query 3826: Model only answers one image question SQLs
Error executing query 3827: Model abstains from answering the question
Error executing query 3828: Model abstains from answering the question
Error executing query 3830: Model only answers one image question SQLs
Error executing query 3835: Model abstains from answering the question
Error executing query 3836: Model only answers one image question SQLs
Error executing query 3837: Model abstains from answering the question
Error executing query 3839: Model abstains from answering the question
Error executing query 3840: Invalid expression / Unexpected token. Line 1, Col: 817.
  rated any abnormality in the upper mediastinum?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 3842: Invalid expression / Unexpected token. Line 1, Col: 740.
  "does a chest x-ray reveal any any abnormality?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3843: Model abstains from answering the question
Error executing query 3844: Invalid expression / Unexpected token. Line 1, Col: 894.
   finding of pneumomediastinum on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3846: Model abstains from answering the question
Error executing query 3847: Model only answers one image question SQLs
Error executing query 3848: Invalid expression / Unexpected token. Line 1, Col: 844.
  ns.hadm_id from admissions where admissions.subject_id = 16776887 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
[True]
Error executing query 3852: Model abstains from answering the question
Error executing query 3853: Invalid expression / Unexpected token. Line 1, Col: 751.
  d = 13724767 ) and strftime('%Y',prescriptions.starttime) >= '2102' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 3854: Model only answers one image question SQLs
Error executing query 3855: Invalid expression / Unexpected token. Line 1, Col: 783.
  indicate mass/nodule (not otherwise specified)?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3857: Invalid expression / Unexpected token. Line 1, Col: 645.
  ns.hadm_id from admissions where admissions.subject_id = 11587177 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3858: Model only answers one image question SQLs
Error executing query 3860: Model abstains from answering the question
Error executing query 3861: Model abstains from answering the question
Error executing query 3864: Model abstains from answering the question
Error executing query 3865: Model only answers one image question SQLs
Error executing query 3866: Model abstains from answering the question
Error executing query 3869: Model abstains from answering the question
Error executing query 3872: Invalid expression / Unexpected token. Line 1, Col: 1003.
   year') = datetime('2105-12-31 23:59:00','start of year','-0 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3874: Model abstains from answering the question
Error executing query 3875: Model only answers one image question SQLs
Error executing query 3876: Model abstains from answering the question
Error executing query 3877: Model abstains from answering the question
Error executing query 3878: Model abstains from answering the question
Error executing query 3879: Model only answers one image question SQLs
Error executing query 3881: Model only answers one image question SQLs
Error executing query 3882: Model only answers one image question SQLs
Error executing query 3886: Model abstains from answering the question
Error executing query 3887: Model abstains from answering the question
Error executing query 3889: Invalid expression / Unexpected token. Line 1, Col: 695.
  %Y',prescriptions.starttime) >= '2103' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 3890: Model abstains from answering the question
Error executing query 3891: Model abstains from answering the question
Error executing query 3892: Invalid expression / Unexpected token. Line 1, Col: 775.
  %Y',prescriptions.starttime) >= '2102' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 3894: Model only answers one image question SQLs
Error executing query 3896: Expecting ). Line 1, Col: 996.
  '%Y',diagnoses_icd.charttime) = '2101' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 3898: Model only answers one image question SQLs
Error executing query 3899: Model abstains from answering the question
Error executing query 3900: Model only answers one image question SQLs
Error executing query 3901: Model abstains from answering the question
Error executing query 3902: Expecting ). Line 1, Col: 1026.
  d where prescriptions.drug = 'insulin' ) as t3 on t2.subject_id = t3.subject_id where t2.charttime  [4mt3[0m.starttime ) as t4 join patients on t4.subject_id = patients.subject_id
Error executing query 3904: Model abstains from answering the question
Error executing query 3906: Model abstains from answering the question
Error executing query 3907: Model only answers one image question SQLs
Error executing query 3908: near "(": syntax error
Error executing query 3909: Expecting ). Line 1, Col: 718.
  etime('2105-12-31 23:59:00','-4 year') ) as t2 on t1.subject_id = t2.subject_id where t1.starttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 4
Error executing query 3910: Expecting ). Line 1, Col: 739.
  noses_icd.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
[True]
Error executing query 3913: Model abstains from answering the question
Error executing query 3914: Invalid expression / Unexpected token. Line 1, Col: 760.
  echnical assessments in the cardiac silhouette?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3916: Expecting ). Line 1, Col: 700.
  ogyevents.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.test_name ) as t3 where t3.c1 = 3
Error executing query 3917: Model abstains from answering the question
Error executing query 3918: Model only answers one image question SQLs
Error executing query 3920: Model only answers one image question SQLs
Error executing query 3922: Invalid expression / Unexpected token. Line 1, Col: 735.
  ns.hadm_id from admissions where admissions.subject_id = 19096918 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3923: Model abstains from answering the question
Error executing query 3924: Invalid expression / Unexpected token. Line 1, Col: 569.
  ere prescriptions.drug = 'hydralazine' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month')
Error executing query 3925: Expecting ). Line 1, Col: 985.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 3927: Invalid expression / Unexpected token. Line 1, Col: 1017.
  a("does a chest x-ray indicate any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3931: Model abstains from answering the question
Error executing query 3932: Model abstains from answering the question
Error executing query 3935: Model abstains from answering the question
Error executing query 3936: Model abstains from answering the question
Error executing query 3937: Model abstains from answering the question
Error executing query 3940: Expecting ). Line 1, Col: 921.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 3941: Model abstains from answering the question
Error executing query 3943: Expecting ). Line 1, Col: 963.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 3944: Model abstains from answering the question
Error executing query 3945: Model only answers one image question SQLs
Error executing query 3946: Invalid expression / Unexpected token. Line 1, Col: 901.
  qa("does a chest x-ray indicate tortuous aorta?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3947: Model abstains from answering the question
Error executing query 3948: Model abstains from answering the question
Error executing query 3949: Expecting ). Line 1, Col: 892.
  %Y',procedures_icd.charttime) = '2100' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 3950: Model abstains from answering the question
Error executing query 3951: Invalid expression / Unexpected token. Line 1, Col: 723.
  ns.hadm_id from admissions where admissions.subject_id = 15179275 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3952: Model abstains from answering the question
Error executing query 3953: Model abstains from answering the question
Error executing query 3954: Model only answers one image question SQLs
Error executing query 3955: Model abstains from answering the question
Error executing query 3956: Model only answers one image question SQLs
Error executing query 3957: Model abstains from answering the question
Error executing query 3958: Invalid expression / Unexpected token. Line 1, Col: 748.
  ing lung cancer in the left costophrenic angle?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3959: Invalid expression / Unexpected token. Line 1, Col: 1048.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
Error executing query 3961: Invalid expression / Unexpected token. Line 1, Col: 880.
  id = 14010906 ) and strftime('%Y',diagnoses_icd.charttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3963: Model only answers one image question SQLs
Error executing query 3964: Model abstains from answering the question
Error executing query 3967: Model only answers one image question SQLs
Error executing query 3968: Model only answers one image question SQLs
Error executing query 3973: Model only answers one image question SQLs
Error executing query 3974: Model abstains from answering the question
Error executing query 3976: Model abstains from answering the question
Error executing query 3978: Model abstains from answering the question
Error executing query 3979: Model only answers one image question SQLs
Error executing query 3980: Model only answers one image question SQLs
Error executing query 3981: Invalid expression / Unexpected token. Line 1, Col: 988.
  ow airspace opacity in the right mid lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
[True]
Error executing query 3983: near "(": syntax error
Error executing query 3985: Model abstains from answering the question
Error executing query 3986: Model only answers one image question SQLs
Error executing query 3987: Model abstains from answering the question
Error executing query 3988: Model abstains from answering the question
Error executing query 3990: Model abstains from answering the question
Error executing query 3992: Model abstains from answering the question
[True]
Error executing query 3994: near "(": syntax error
Error executing query 3995: Invalid expression / Unexpected token. Line 1, Col: 950.
  e('%m',prescriptions.starttime) = '05' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of day') = datetime(t2.starttime,'start of day')
Error executing query 3996: Invalid expression / Unexpected token. Line 1, Col: 756.
  d in the left lower lung zone on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 3998: Model abstains from answering the question
Error executing query 3999: Model abstains from answering the question
Error executing query 4002: Model abstains from answering the question
Error executing query 4003: Model abstains from answering the question
Error executing query 4004: Model abstains from answering the question
Error executing query 4006: Invalid expression / Unexpected token. Line 1, Col: 840.
   where func_vqa("is any abnormality identified?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4007: Invalid expression / Unexpected token. Line 1, Col: 895.
  dures_icd.charttime) >= datetime('2105-12-31 23:59:00','-50 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4009: Model abstains from answering the question
Error executing query 4010: Expecting ). Line 1, Col: 508.
  criptions.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.starttime  [4mt2[0m.starttime and datetime(t1.starttime,'start of month') = datetime(t2.starttime,'start of month') gro
Error executing query 4011: Model only answers one image question SQLs
Error executing query 4012: Model abstains from answering the question
Error executing query 4013: Model abstains from answering the question
Error executing query 4015: Invalid expression / Unexpected token. Line 1, Col: 647.
  ns.hadm_id from admissions where admissions.subject_id = 12409604 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
[False]
Error executing query 4017: Invalid expression / Unexpected token. Line 1, Col: 984.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 4018: Model only answers one image question SQLs
Error executing query 4019: Invalid expression / Unexpected token. Line 1, Col: 1014.
  s.dischtime is not null order by admissions.admittime asc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4021: Model only answers one image question SQLs
Error executing query 4022: Model abstains from answering the question
Error executing query 4023: Model abstains from answering the question
Error executing query 4025: Model only answers one image question SQLs
Error executing query 4026: Invalid expression / Unexpected token. Line 1, Col: 881.
  d = 15528228 ) and strftime('%Y',procedures_icd.charttime) = '2105' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4027: Model abstains from answering the question
Error executing query 4029: Model abstains from answering the question
Error executing query 4030: Model abstains from answering the question
Error executing query 4032: Expecting ). Line 1, Col: 760.
  '%Y',prescriptions.starttime) = '2105' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 5
Error executing query 4034: Invalid expression / Unexpected token. Line 1, Col: 751.
  ns.hadm_id from admissions where admissions.subject_id = 17950066 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4035: Model only answers one image question SQLs
Error executing query 4036: Model abstains from answering the question
Error executing query 4037: Model only answers one image question SQLs
Error executing query 4038: Expecting ). Line 1, Col: 861.
  %Y',diagnoses_icd.charttime) >= '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 4039: Model abstains from answering the question
Error executing query 4040: Model only answers one image question SQLs
Error executing query 4041: Model abstains from answering the question
Error executing query 4043: Expecting ). Line 1, Col: 942.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 4044: Model only answers one image question SQLs
Error executing query 4046: Invalid expression / Unexpected token. Line 1, Col: 731.
  ns.hadm_id from admissions where admissions.subject_id = 15833469 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 4048: Expecting ). Line 1, Col: 724.
  dures_icd.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 4049: Expecting ). Line 1, Col: 879.
  Y',procedures_icd.charttime) >= '2105' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 4050: Invalid expression / Unexpected token. Line 1, Col: 1043.
  486932 ) and strftime('%Y-%m',procedures_icd.charttime) = '2103-02' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and t1.hadm_id = t3.hadm_id
Error executing query 4051: Model abstains from answering the question
Error executing query 4052: Model abstains from answering the question
Error executing query 4054: Model only answers one image question SQLs
Error executing query 4055: Invalid expression / Unexpected token. Line 1, Col: 748.
  id = 11843648 ) and strftime('%Y',prescriptions.starttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 4056: Model only answers one image question SQLs
Error executing query 4058: Invalid expression / Unexpected token. Line 1, Col: 891.
  5112603 ) and strftime('%Y-%m',diagnoses_icd.charttime) = '2104-03' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4059: Model abstains from answering the question
Error executing query 4066: Model only answers one image question SQLs
Error executing query 4067: Expecting ). Line 1, Col: 851.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 4068: Model abstains from answering the question
Error executing query 4069: Model abstains from answering the question
Error executing query 4070: Model abstains from answering the question
Error executing query 4071: Invalid expression / Unexpected token. Line 1, Col: 734.
  s the chest x-ray indicate any any abnormality?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4073: Invalid expression / Unexpected token. Line 1, Col: 990.
  lines in the left apical zone on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4074: Model abstains from answering the question
Error executing query 4075: Model abstains from answering the question
Error executing query 4076: Model abstains from answering the question
Error executing query 4078: Model abstains from answering the question
Error executing query 4081: Model abstains from answering the question
Error executing query 4082: Model abstains from answering the question
Error executing query 4083: near "(": syntax error
Error executing query 4085: Model abstains from answering the question
Error executing query 4088: Model abstains from answering the question
Error executing query 4089: Model only answers one image question SQLs
Error executing query 4090: Model abstains from answering the question
Error executing query 4092: Model only answers one image question SQLs
Error executing query 4093: near "(": syntax error
Error executing query 4094: Invalid expression / Unexpected token. Line 1, Col: 886.
  d = 12957707 ) and strftime('%Y',diagnoses_icd.charttime) >= '2105' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 4095: Model abstains from answering the question
Error executing query 4099: Invalid expression / Unexpected token. Line 1, Col: 659.
  ns.hadm_id from admissions where admissions.subject_id = 16178416 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4100: Invalid expression / Unexpected token. Line 1, Col: 760.
  veal any abnormality in the left hemidiaphragm?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4101: Invalid expression / Unexpected token. Line 1, Col: 909.
  d = 18002691 ) and strftime('%Y',procedures_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 4104: Invalid expression / Unexpected token. Line 1, Col: 846.
  indication of any abnormality on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4105: Model only answers one image question SQLs
Error executing query 4106: Invalid expression / Unexpected token. Line 1, Col: 1015.
  d = 12931948 ) and strftime('%Y',procedures_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and t1.hadm_id = t3.hadm_id
Error executing query 4112: Invalid expression / Unexpected token. Line 1, Col: 826.
  escriptions.starttime) >= datetime('2105-12-31 23:59:00','-5 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 4113: Model abstains from answering the question
Error executing query 4116: Model abstains from answering the question
Error executing query 4120: Model abstains from answering the question
Error executing query 4121: Model abstains from answering the question
Error executing query 4122: Invalid expression / Unexpected token. Line 1, Col: 1038.
  vqa("is airspace opacity indicated on an x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4123: Model abstains from answering the question
Error executing query 4125: Model abstains from answering the question
Error executing query 4127: Model abstains from answering the question
Error executing query 4128: Invalid expression / Unexpected token. Line 1, Col: 838.
  ns.hadm_id from admissions where admissions.subject_id = 13551252 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 4129: Model abstains from answering the question
Error executing query 4130: Invalid expression / Unexpected token. Line 1, Col: 799.
  c_vqa("has a chest x-ray shown any tubes/lines?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4132: Model abstains from answering the question
Error executing query 4133: Model abstains from answering the question
Error executing query 4134: Invalid expression / Unexpected token. Line 1, Col: 856.
  d = 15649581 ) and strftime('%Y',diagnoses_icd.charttime) >= '2105' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4135: Invalid expression / Unexpected token. Line 1, Col: 742.
  showing any anatomical findings in the abdomen?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4137: Model only answers one image question SQLs
Error executing query 4138: Model abstains from answering the question
Error executing query 4139: Invalid expression / Unexpected token. Line 1, Col: 785.
  553635 ) and strftime('%Y-%m',prescriptions.starttime) >= '2104-04' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4142: Model abstains from answering the question
Error executing query 4144: Invalid expression / Unexpected token. Line 1, Col: 903.
  78034 ) and strftime('%Y-%m',procedures_icd.charttime) >= '2105-03' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4146: Model abstains from answering the question
Error executing query 4147: Model only answers one image question SQLs
Error executing query 4148: Model abstains from answering the question
Error executing query 4149: Model only answers one image question SQLs
Error executing query 4150: Model abstains from answering the question
Error executing query 4151: Model abstains from answering the question
Error executing query 4152: Invalid expression / Unexpected token. Line 1, Col: 746.
  5729731 ) and strftime('%Y-%m',prescriptions.starttime) = '2102-08' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4153: Invalid expression / Unexpected token. Line 1, Col: 760.
  7460568 ) and strftime('%Y-%m',prescriptions.starttime) = '2105-09' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4154: Model only answers one image question SQLs
Error executing query 4155: Invalid expression / Unexpected token. Line 1, Col: 894.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 4157: Invalid expression / Unexpected token. Line 1, Col: 974.
  vqa("is any abnormality shown on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4159: Expecting ). Line 1, Col: 802.
  %Y',prescriptions.starttime) >= '2102' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 4160: Invalid expression / Unexpected token. Line 1, Col: 1036.
  edures_icd.charttime) >= datetime('2105-12-31 23:59:00','-5 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and t1.hadm_id = t3.hadm_id
Error executing query 4161: Model abstains from answering the question
Error executing query 4162: Model abstains from answering the question
Error executing query 4163: Model only answers one image question SQLs
Error executing query 4164: Model abstains from answering the question
Error executing query 4165: Model abstains from answering the question
Error executing query 4166: Model abstains from answering the question
Error executing query 4169: Invalid expression / Unexpected token. Line 1, Col: 886.
   an x-ray indicated any abnormality in the svc?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4172: Model abstains from answering the question
Error executing query 4175: Model only answers one image question SQLs
Error executing query 4176: Expecting ). Line 1, Col: 715.
  ogyevents.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.spec_type_desc ) as t3 where t3.c1 = 3
Error executing query 4178: Model only answers one image question SQLs
Error executing query 4179: Invalid expression / Unexpected token. Line 1, Col: 850.
   = 13724767 ) and strftime('%Y',procedures_icd.charttime) >= '2102' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4185: Model abstains from answering the question
Error executing query 4187: Model only answers one image question SQLs
Error executing query 4190: Invalid expression / Unexpected token. Line 1, Col: 839.
  vqa("does a chest x-ray reveal any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4191: Model only answers one image question SQLs
Error executing query 4193: Invalid expression / Unexpected token. Line 1, Col: 631.
  ns.hadm_id from admissions where admissions.subject_id = 13122104 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 4194: Model abstains from answering the question
Error executing query 4195: Model abstains from answering the question
Error executing query 4196: Model abstains from answering the question
Error executing query 4198: Invalid expression / Unexpected token. Line 1, Col: 662.
  emonstrated any abnormality in the aortic arch?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 4200: Model only answers one image question SQLs
Error executing query 4201: Model abstains from answering the question
Error executing query 4202: Model abstains from answering the question
Error executing query 4203: Model abstains from answering the question
Error executing query 4205: Model only answers one image question SQLs
Error executing query 4206: Model only answers one image question SQLs
Error executing query 4207: Model abstains from answering the question
Error executing query 4209: Invalid expression / Unexpected token. Line 1, Col: 863.
  nary edema/hazy opacity shown on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4210: Expecting ). Line 1, Col: 856.
  microbiologyevents.charttime) = '2101' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.test_name ) as t3 where t3.c1 = 4
Error executing query 4211: Model only answers one image question SQLs
Error executing query 4212: near "(": syntax error
Error executing query 4215: Model abstains from answering the question
Error executing query 4218: Invalid expression / Unexpected token. Line 1, Col: 991.
  ube in the cardiac silhouette on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 4222: Model only answers one image question SQLs
Error executing query 4223: near "(": syntax error
Error executing query 4224: Model only answers one image question SQLs
Error executing query 4228: Model abstains from answering the question
Error executing query 4229: Model abstains from answering the question
Error executing query 4230: Invalid expression / Unexpected token. Line 1, Col: 748.
  id = 11298578 ) and strftime('%Y',prescriptions.starttime) = '2102' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 4231: Model abstains from answering the question
Error executing query 4232: Model abstains from answering the question
Error executing query 4234: Model only answers one image question SQLs
Error executing query 4235: Model only answers one image question SQLs
Error executing query 4236: Model only answers one image question SQLs
Error executing query 4240: Model abstains from answering the question
Error executing query 4241: Model abstains from answering the question
Error executing query 4243: Invalid expression / Unexpected token. Line 1, Col: 812.
  ' ) ) as t2 where func_vqa("is picc identified?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4244: Invalid expression / Unexpected token. Line 1, Col: 1086.
   year','-0 year') and strftime('%m',diagnoses_icd.charttime) = '12' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t
Error executing query 4246: Model only answers one image question SQLs
Error executing query 4247: Model only answers one image question SQLs
Error executing query 4249: Invalid expression / Unexpected token. Line 1, Col: 745.
  ns.hadm_id from admissions where admissions.subject_id = 19096918 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4251: Model only answers one image question SQLs
Error executing query 4253: Model abstains from answering the question
Error executing query 4256: Model abstains from answering the question
Error executing query 4257: Model only answers one image question SQLs
Error executing query 4261: Model abstains from answering the question
Error executing query 4262: Model only answers one image question SQLs
Error executing query 4263: Invalid expression / Unexpected token. Line 1, Col: 892.
  agnoses_icd.charttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 4264: Model only answers one image question SQLs
Error executing query 4265: Model abstains from answering the question
Error executing query 4267: Model abstains from answering the question
Error executing query 4268: Model only answers one image question SQLs
Error executing query 4270: Invalid expression / Unexpected token. Line 1, Col: 762.
  st x-ray show bone lesion in the left shoulder?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4272: Model abstains from answering the question
Error executing query 4273: Model abstains from answering the question
Error executing query 4275: Model abstains from answering the question
Error executing query 4276: Model only answers one image question SQLs
Error executing query 4277: Model abstains from answering the question
Error executing query 4278: Expecting ). Line 1, Col: 969.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 4279: Model only answers one image question SQLs
Error executing query 4280: Model abstains from answering the question
Error executing query 4282: Model only answers one image question SQLs
Error executing query 4284: Model only answers one image question SQLs
Error executing query 4287: Model only answers one image question SQLs
Error executing query 4288: Invalid expression / Unexpected token. Line 1, Col: 895.
  any indication of cyst/bullae on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4289: Invalid expression / Unexpected token. Line 1, Col: 743.
  id = 14258856 ) and strftime('%Y',prescriptions.starttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 4290: Model only answers one image question SQLs
Error executing query 4291: Model only answers one image question SQLs
Error executing query 4292: Model only answers one image question SQLs
Error executing query 4293: Expecting ). Line 1, Col: 1130.
  ar','-1 year') ) as t2 join admissions on t2.subject_id = admissions.subject_id where t2.charttime  [4madmissions[0m.admittime and datetime(admissions.admittime,'start of year') = datetime('2105-12-31 23:59:00','star
Error executing query 4294: Model abstains from answering the question
Error executing query 4296: Model abstains from answering the question
Error executing query 4297: Model only answers one image question SQLs
Error executing query 4301: Invalid expression / Unexpected token. Line 1, Col: 904.
  ocedures_icd.charttime) = datetime('2105-12-31 23:59:00','-2 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 4303: Invalid expression / Unexpected token. Line 1, Col: 743.
  ns.hadm_id from admissions where admissions.subject_id = 12798053 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 4304: Model abstains from answering the question
Error executing query 4305: Model abstains from answering the question
Error executing query 4306: Invalid expression / Unexpected token. Line 1, Col: 725.
  vqa("is any abnormality shown on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4307: Model only answers one image question SQLs
Error executing query 4308: Invalid expression / Unexpected token. Line 1, Col: 763.
  ns.hadm_id from admissions where admissions.subject_id = 15125816 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4309: Model abstains from answering the question
Error executing query 4310: Model abstains from answering the question
Error executing query 4311: Error tokenizing 'ydatetime) and datetime(t3.studydatetime,'+2 mont'
Error executing query 4312: Expecting ). Line 1, Col: 890.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 4313: Model abstains from answering the question
Error executing query 4315: Invalid expression / Unexpected token. Line 1, Col: 781.
  y technical assessments shown on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4320: Invalid expression / Unexpected token. Line 1, Col: 1107.
  a/hazy opacity in the right costophrenic angle?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.char
Error executing query 4322: Expecting ). Line 1, Col: 987.
  ptions.drug = 'diphenoxylate-atropine' ) as t3 on t2.subject_id = t3.subject_id where t2.charttime  [4mt3[0m.starttime ) as t4 join patients on t4.subject_id = patients.subject_id
Error executing query 4323: Model abstains from answering the question
Error executing query 4324: Expecting ). Line 1, Col: 1032.
  where prescriptions.drug = 'torsemide' ) as t3 on t2.subject_id = t3.subject_id where t2.charttime  [4mt3[0m.starttime ) as t4 join patients on t4.subject_id = patients.subject_id
Error executing query 4325: Invalid expression / Unexpected token. Line 1, Col: 829.
  findings in the left clavicle on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 4326: Model abstains from answering the question
Error executing query 4327: Invalid expression / Unexpected token. Line 1, Col: 845.
  %Y',procedures_icd.charttime) = '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
Error executing query 4328: Invalid expression / Unexpected token. Line 1, Col: 651.
  ns.hadm_id from admissions where admissions.subject_id = 12839549 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 4331: Invalid expression / Unexpected token. Line 1, Col: 879.
  al any abnormality in the left upper lung zone?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 4332: Invalid expression / Unexpected token. Line 1, Col: 797.
  escriptions.starttime) = datetime('2105-12-31 23:59:00','-3 month') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4333: Model only answers one image question SQLs
Error executing query 4334: Invalid expression / Unexpected token. Line 1, Col: 1091.
   year','-0 year') and strftime('%m',diagnoses_icd.charttime) = '09' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4335: Model abstains from answering the question
Error executing query 4336: Model only answers one image question SQLs
Error executing query 4337: Invalid expression / Unexpected token. Line 1, Col: 929.
  "has an x-ray revealed any anatomical findings?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4338: Model abstains from answering the question
Error executing query 4339: Model abstains from answering the question
Error executing query 4340: Model abstains from answering the question
Error executing query 4341: Model only answers one image question SQLs
Error executing query 4343: Model abstains from answering the question
Error executing query 4344: Model only answers one image question SQLs
Error executing query 4345: Invalid expression / Unexpected token. Line 1, Col: 859.
  id = 12405140 ) and strftime('%Y',diagnoses_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 4346: Invalid expression / Unexpected token. Line 1, Col: 982.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
Error executing query 4347: Invalid expression / Unexpected token. Line 1, Col: 988.
   wires in the left chest wall on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 4348: Invalid expression / Unexpected token. Line 1, Col: 934.
  ny indication of pneumothorax on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4349: Model abstains from answering the question
Error executing query 4352: Model abstains from answering the question
Error executing query 4355: Model abstains from answering the question
Error executing query 4357: Model abstains from answering the question
Error executing query 4358: Model abstains from answering the question
Error executing query 4360: Model only answers one image question SQLs
Error executing query 4361: Model abstains from answering the question
Error executing query 4362: Model abstains from answering the question
Error executing query 4364: Invalid expression / Unexpected token. Line 1, Col: 910.
  ray reveal pneumomediastinum in the right lung?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4366: Model only answers one image question SQLs
Error executing query 4367: Model abstains from answering the question
Error executing query 4368: Model abstains from answering the question
Error executing query 4369: Model only answers one image question SQLs
Error executing query 4370: Model abstains from answering the question
Error executing query 4371: Model only answers one image question SQLs
Error executing query 4373: Model abstains from answering the question
Error executing query 4374: Model abstains from answering the question
Error executing query 4375: Model only answers one image question SQLs
Error executing query 4376: Model abstains from answering the question
Error executing query 4377: Model only answers one image question SQLs
Error executing query 4378: Model abstains from answering the question
Error executing query 4379: Invalid expression / Unexpected token. Line 1, Col: 625.
  ns.hadm_id from admissions where admissions.subject_id = 10284038 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 4381: Expecting ). Line 1, Col: 779.
  icrobiologyevents.charttime) >= '2103' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 4382: Invalid expression / Unexpected token. Line 1, Col: 858.
  2986647 ) and strftime('%Y-%m',diagnoses_icd.charttime) = '2105-07' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4385: Invalid expression / Unexpected token. Line 1, Col: 1119.
  an x-ray revealed any abnormality in the spine?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.char
Error executing query 4386: Invalid expression / Unexpected token. Line 1, Col: 1084.
  er and wires identified in the left chest wall?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4387: Model abstains from answering the question
Error executing query 4388: Model abstains from answering the question
Error executing query 4390: Invalid expression / Unexpected token. Line 1, Col: 905.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id
Error executing query 4393: Model only answers one image question SQLs
Error executing query 4394: Invalid expression / Unexpected token. Line 1, Col: 809.
  y indicate any abnormality in the right atrium?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 4395: Model only answers one image question SQLs
Error executing query 4397: Model abstains from answering the question
Error executing query 4399: Model abstains from answering the question
Error executing query 4400: Invalid expression / Unexpected token. Line 1, Col: 1019.
  etecting any tubes/lines in the right shoulder?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4401: Invalid expression / Unexpected token. Line 1, Col: 1013.
   year') = datetime('2105-12-31 23:59:00','start of year','-0 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 4402: Model abstains from answering the question
Error executing query 4405: Model abstains from answering the question
Error executing query 4406: Invalid expression / Unexpected token. Line 1, Col: 740.
  indication of any abnormality on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4408: near "(": syntax error
Error executing query 4409: Model only answers one image question SQLs
Error executing query 4411: Model only answers one image question SQLs
Error executing query 4412: Model only answers one image question SQLs
Error executing query 4413: Model abstains from answering the question
Error executing query 4414: Invalid expression / Unexpected token. Line 1, Col: 964.
  id = 17455506 ) and strftime('%Y',diagnoses_icd.charttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
[True]
[True]
Error executing query 4418: Invalid expression / Unexpected token. Line 1, Col: 777.
  /lines in the left chest wall on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4421: Model only answers one image question SQLs
Error executing query 4422: Model abstains from answering the question
Error executing query 4423: Model abstains from answering the question
Error executing query 4424: Model abstains from answering the question
Error executing query 4428: Invalid expression / Unexpected token. Line 1, Col: 721.
  qa("has a chest x-ray demonstrated bone lesion?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4429: Model only answers one image question SQLs
Error executing query 4430: Model only answers one image question SQLs
Error executing query 4432: Model abstains from answering the question
Error executing query 4433: Invalid expression / Unexpected token. Line 1, Col: 871.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 4434: Invalid expression / Unexpected token. Line 1, Col: 982.
  dures_icd.charttime) >= datetime('2105-12-31 23:59:00','-55 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
[True]
Error executing query 4435: Model abstains from answering the question
Error executing query 4436: Invalid expression / Unexpected token. Line 1, Col: 719.
  c_vqa("is a chest x-ray showing enlarged hilum?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4437: Model only answers one image question SQLs
Error executing query 4438: Model abstains from answering the question
Error executing query 4439: Invalid expression / Unexpected token. Line 1, Col: 865.
  d = 15696371 ) and strftime('%Y',procedures_icd.charttime) = '2101' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 4440: Model abstains from answering the question
Error executing query 4441: Invalid expression / Unexpected token. Line 1, Col: 765.
  g any abnormality in the right upper lung zone?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 4442: Model only answers one image question SQLs
Error executing query 4444: Model abstains from answering the question
Error executing query 4448: Invalid expression / Unexpected token. Line 1, Col: 1001.
  s.dischtime is not null order by admissions.admittime asc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4449: Model abstains from answering the question
Error executing query 4450: Model abstains from answering the question
Error executing query 4452: Model abstains from answering the question
Error executing query 4453: Model abstains from answering the question
Error executing query 4454: Model only answers one image question SQLs
Error executing query 4455: Invalid expression / Unexpected token. Line 1, Col: 721.
  ns.hadm_id from admissions where admissions.subject_id = 12822417 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4457: Model only answers one image question SQLs
Error executing query 4458: Model only answers one image question SQLs
Error executing query 4459: Model only answers one image question SQLs
Error executing query 4460: Invalid expression / Unexpected token. Line 1, Col: 766.
   'routine chest x-ray, so described' ) ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id
Error executing query 4461: Model only answers one image question SQLs
Error executing query 4462: Model abstains from answering the question
Error executing query 4463: Model only answers one image question SQLs
Error executing query 4464: Model abstains from answering the question
Error executing query 4465: Expecting ). Line 1, Col: 833.
  '%Y',diagnoses_icd.charttime) = '2103' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 4466: Model abstains from answering the question
Error executing query 4467: Model abstains from answering the question
Error executing query 4468: Invalid expression / Unexpected token. Line 1, Col: 657.
  ns.hadm_id from admissions where admissions.subject_id = 12843379 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 4469: Model only answers one image question SQLs
Error executing query 4470: Invalid expression / Unexpected token. Line 1, Col: 963.
  e('%m',prescriptions.starttime) = '12' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 d
Error executing query 4471: Model only answers one image question SQLs
Error executing query 4474: Model abstains from answering the question
Error executing query 4475: Invalid expression / Unexpected token. Line 1, Col: 761.
  ns.hadm_id from admissions where admissions.subject_id = 15790605 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4476: Model abstains from answering the question
Error executing query 4478: Model abstains from answering the question
Error executing query 4479: Model abstains from answering the question
Error executing query 4481: Invalid expression / Unexpected token. Line 1, Col: 886.
  etime('2105-12-31 23:59:00','-4 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 4482: Model abstains from answering the question
Error executing query 4483: Expecting ). Line 1, Col: 865.
  etime('2105-12-31 23:59:00','-4 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 4484: Model only answers one image question SQLs
Error executing query 4485: Model only answers one image question SQLs
Error executing query 4486: Invalid expression / Unexpected token. Line 1, Col: 929.
  ocedures_icd.charttime) = datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 4487: Model abstains from answering the question
Error executing query 4488: Invalid expression / Unexpected token. Line 1, Col: 1012.
   of any technical assessments on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4489: Model abstains from answering the question
Error executing query 4490: Model abstains from answering the question
Error executing query 4491: Model only answers one image question SQLs
Error executing query 4492: Model only answers one image question SQLs
Error executing query 4497: Model abstains from answering the question
Error executing query 4499: Model only answers one image question SQLs
Error executing query 4502: Model abstains from answering the question
Error executing query 4504: Model abstains from answering the question
Error executing query 4506: Invalid expression / Unexpected token. Line 1, Col: 795.
  rmittent, less than 6 hours per day' ) ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id
Error executing query 4507: Invalid expression / Unexpected token. Line 1, Col: 1025.
  hest x-ray show any abnormality in the abdomen?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4508: Invalid expression / Unexpected token. Line 1, Col: 775.
  unc_vqa("is any technical assessments revealed?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4512: Expecting ). Line 1, Col: 1070.
   year') order by tb_cxr.studydatetime desc limit 1 ) ) ) order by tb_cxr.studydatetime desc limit 1 [4m)[0m
Error executing query 4514: Model abstains from answering the question
Error executing query 4516: Invalid expression / Unexpected token. Line 1, Col: 815.
  escriptions.starttime) >= datetime('2105-12-31 23:59:00','-3 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 4519: Model abstains from answering the question
Error executing query 4520: Model abstains from answering the question
Error executing query 4521: Expecting ). Line 1, Col: 956.
  ime) >= '2103' ) as t2 join admissions on t2.subject_id = admissions.subject_id where t2.charttime  [4madmissions[0m.admittime and strftime('%Y',admissions.admittime) >= '2103' and datetime(admissions.admittime) betw
Error executing query 4522: Model abstains from answering the question
Error executing query 4523: Invalid expression / Unexpected token. Line 1, Col: 920.
   in the left hilar structures on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4524: Invalid expression / Unexpected token. Line 1, Col: 1028.
  ere a finding of any diseases on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4526: Model only answers one image question SQLs
Error executing query 4529: Invalid expression / Unexpected token. Line 1, Col: 803.
  ny indication of any diseases on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4531: Model abstains from answering the question
Error executing query 4532: Invalid expression / Unexpected token. Line 1, Col: 806.
  r by admissions.admittime desc limit 1 ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 d
Error executing query 4534: Model only answers one image question SQLs
Error executing query 4536: Model only answers one image question SQLs
Error executing query 4539: Model abstains from answering the question
Error executing query 4540: Invalid expression / Unexpected token. Line 1, Col: 888.
  depicts any technical assessments in the spine?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4541: Invalid expression / Unexpected token. Line 1, Col: 1010.
  ascular calcification in the upper mediastinum?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4542: Invalid expression / Unexpected token. Line 1, Col: 976.
  e('%m',prescriptions.starttime) = '12' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 d
Error executing query 4544: Model abstains from answering the question
Error executing query 4545: Model only answers one image question SQLs
Error executing query 4547: Model only answers one image question SQLs
Error executing query 4548: Model abstains from answering the question
Error executing query 4549: Model abstains from answering the question
Error executing query 4550: Model abstains from answering the question
Error executing query 4554: Model only answers one image question SQLs
Error executing query 4556: Invalid expression / Unexpected token. Line 1, Col: 847.
  528228 ) and strftime('%Y-%m',procedures_icd.charttime) = '2103-12' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4557: Model only answers one image question SQLs
Error executing query 4559: Invalid expression / Unexpected token. Line 1, Col: 644.
  ns.hadm_id from admissions where admissions.subject_id = 12250782 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4560: Model only answers one image question SQLs
Error executing query 4561: Expecting ). Line 1, Col: 901.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 4564: Invalid expression / Unexpected token. Line 1, Col: 743.
  ns.hadm_id from admissions where admissions.subject_id = 12876131 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4565: Model abstains from answering the question
Error executing query 4568: Invalid expression / Unexpected token. Line 1, Col: 954.
  ocedures_icd.charttime) = datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 4571: Invalid expression / Unexpected token. Line 1, Col: 1007.
  t x-ray detecting pulmonary edema/hazy opacity?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4572: Model abstains from answering the question
Error executing query 4573: Model abstains from answering the question
Error executing query 4575: Invalid expression / Unexpected token. Line 1, Col: 891.
   any abnormality in the spine on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4576: Model only answers one image question SQLs
Error executing query 4577: near "(": syntax error
Error executing query 4578: Model abstains from answering the question
Error executing query 4580: Model only answers one image question SQLs
Error executing query 4581: Model only answers one image question SQLs
Error executing query 4582: Invalid expression / Unexpected token. Line 1, Col: 849.
  d = 14410216 ) and strftime('%Y',diagnoses_icd.charttime) >= '2105' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 4583: Model abstains from answering the question
Error executing query 4587: Model abstains from answering the question
Error executing query 4588: Model only answers one image question SQLs
Correct count: 91
Wrong count: 1125
Correct count image: 24
Wrong count image: 60
Image questions: 2916
```
wandb: - 0.004 MB of 0.004 MB uploadedwandb: \ 0.004 MB of 0.004 MB uploadedwandb: | 0.004 MB of 0.004 MB uploadedwandb: / 0.009 MB of 0.424 MB uploaded (0.004 MB deduped)wandb: - 0.010 MB of 0.424 MB uploaded (0.004 MB deduped)wandb: \ 0.424 MB of 0.424 MB uploaded (0.004 MB deduped)wandb: 
wandb: Run history:
wandb: accuracy ▁
wandb: 
wandb: Run summary:
wandb: accuracy 0.02637
wandb: 
wandb: 🚀 View run vision1test09-0 at: https://wandb.ai/kobomao/ML_healthcare/runs/zli9w0pa
wandb: ⭐️ View project at: https://wandb.ai/kobomao/ML_healthcare
wandb: Synced 5 W&B file(s), 0 media file(s), 2 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20240605_040146-zli9w0pa/logs

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21919006: <vision1test09_0> in cluster <dcc> Done

Job <vision1test09_0> was submitted from host <n-62-27-22> by user <s183914> in cluster <dcc> at Tue Jun  4 19:48:22 2024
Job was executed on host(s) <4*n-62-20-15>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Jun  5 04:01:30 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_final/ML_final> was used as the working directory.
Started at Wed Jun  5 04:01:30 2024
Terminated at Wed Jun  5 05:19:51 2024
Results reported at Wed Jun  5 05:19:51 2024

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

Successfully completed.

Resource usage summary:

    CPU time :                                   4912.15 sec.
    Max Memory :                                 17265 MB
    Average Memory :                             12932.27 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               48271.00 MB
    Max Swap :                                   -
    Max Processes :                              6
    Max Threads :                                67
    Run time :                                   4701 sec.
    Turnaround time :                            34289 sec.

The output (if any) is above this job summary.

