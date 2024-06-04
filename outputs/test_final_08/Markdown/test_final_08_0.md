2024-06-04 13:19:49.973985: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.17.0
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_final/ML_final/wandb/run-20240604_131955-rwcoy6ck
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run test_final_08-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/rwcoy6ck
2024-06-04 13:20:12.036102: W tensorflow/core/common_runtime/gpu/gpu_device.cc:2251] Cannot dlopen some GPU libraries. Please make sure the missing libraries mentioned above are installed properly if you would like to use GPU. Follow the guide at https://www.tensorflow.org/install/gpu for how to download and setup the required libraries for your platform.
Skipping registering GPU devices...
2024-06-04 13:20:13.475085: W external/xla/xla/service/gpu/nvptx_compiler.cc:760] The NVIDIA driver's CUDA version is 12.4 which is older than the ptxas CUDA version (12.5.40). Because the driver is older than the ptxas version, XLA is disabling parallel compilation, which may slow down compilation. You should update your NVIDIA driver or use the NVIDIA-provided CUDA forward compatibility packages.

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
| <c>name</c>       | <d>str</d>        | <j>"test_final_08-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>3600</f>       |
| <c>vqa_module_type</c>| <d>str</d>        | <j>"custom"</j>   |
| <c>prediction_file_name</c>| <d>str</d>        | <j>"predictions_LLM_1-0"</j> |
| <c>threshold</c>  | <d>float</d>      | <f>0.8</f>        |

# Output

```
sid_to_ipath_map loaded. (1896 entries)
Error executing query 1: Invalid expression / Unexpected token. Line 1, Col: 651.
  ns.hadm_id from admissions where admissions.subject_id = 12252397 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 2: Model only answers one image question SQLs
Error executing query 3: Invalid expression / Unexpected token. Line 1, Col: 914.
  func_vqa("does a chest x-ray show any diseases?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 5: Model abstains from answering the question
Error executing query 9: Model abstains from answering the question
Error executing query 10: Model abstains from answering the question
Error executing query 11: Model abstains from answering the question
Error executing query 12: Model only answers one image question SQLs
Error executing query 14: Model only answers one image question SQLs
Error executing query 16: Model abstains from answering the question
Error executing query 17: Invalid expression / Unexpected token. Line 1, Col: 958.
  nth') = datetime('2105-12-31 23:59:00','start of month','-0 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 19: Model abstains from answering the question
Error executing query 23: Model abstains from answering the question
Error executing query 24: Model abstains from answering the question
Error executing query 25: Model abstains from answering the question
Error executing query 26: Invalid expression / Unexpected token. Line 1, Col: 821.
  escriptions.starttime) >= datetime('2105-12-31 23:59:00','-5 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 29: Model only answers one image question SQLs
Error executing query 33: Invalid expression / Unexpected token. Line 1, Col: 914.
  dures_icd.charttime) >= datetime('2105-12-31 23:59:00','-12 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 34: Model only answers one image question SQLs
Error executing query 35: Model only answers one image question SQLs
Error executing query 37: Model abstains from answering the question
Error executing query 40: Model abstains from answering the question
Error executing query 41: Invalid expression / Unexpected token. Line 1, Col: 779.
  aling copd/emphysema in the left mid lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 42: Invalid expression / Unexpected token. Line 1, Col: 777.
  _vqa("is a chest x-ray showing any abnormality?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 43: Model abstains from answering the question
Error executing query 44: Model abstains from answering the question
Error executing query 46: Model abstains from answering the question
Error executing query 50: Model abstains from answering the question
Error executing query 52: near "(": syntax error
Error executing query 53: Model only answers one image question SQLs
Error executing query 54: Invalid expression / Unexpected token. Line 1, Col: 746.
  st x-ray show any abnormality in the left lung?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 55: Model only answers one image question SQLs
Error executing query 56: Model abstains from answering the question
Error executing query 57: Model abstains from answering the question
Error executing query 59: Model only answers one image question SQLs
Error executing query 60: Model abstains from answering the question
Error executing query 61: Model abstains from answering the question
Error executing query 62: Model abstains from answering the question
Error executing query 64: Model only answers one image question SQLs
Error executing query 65: Model abstains from answering the question
Error executing query 66: Invalid expression / Unexpected token. Line 1, Col: 1103.
   year','-0 year') and strftime('%m',diagnoses_icd.charttime) = '09' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime
Error executing query 69: Expecting ). Line 1, Col: 1072.
  ar','-0 year') ) as t2 join admissions on t2.subject_id = admissions.subject_id where t2.charttime  [4madmissions[0m.admittime and datetime(admissions.admittime,'start of year') = datetime('2105-12-31 23:59:00','star
Error executing query 70: Model abstains from answering the question
Error executing query 71: Model only answers one image question SQLs
Error executing query 72: Model abstains from answering the question
Error executing query 74: Model only answers one image question SQLs
Error executing query 76: Model abstains from answering the question
Error executing query 78: Model abstains from answering the question
Error executing query 83: Model abstains from answering the question
Error executing query 85: Model abstains from answering the question
Error executing query 87: Model abstains from answering the question
Error executing query 88: Invalid expression / Unexpected token. Line 1, Col: 957.
  iagnoses_icd.charttime) = datetime('2105-12-31 23:59:00','-2 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 89: Invalid expression / Unexpected token. Line 1, Col: 652.
  ns.hadm_id from admissions where admissions.subject_id = 17198431 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 93: Model abstains from answering the question
Error executing query 94: Model only answers one image question SQLs
Error executing query 95: Expecting ). Line 1, Col: 859.
  etime('2105-12-31 23:59:00','-5 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 96: Model abstains from answering the question
Error executing query 98: Model abstains from answering the question
Error executing query 99: Model abstains from answering the question
Error executing query 100: Model abstains from answering the question
Error executing query 101: Invalid expression / Unexpected token. Line 1, Col: 760.
  w any spinal degenerative changes in the spine?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 102: Invalid expression / Unexpected token. Line 1, Col: 882.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 103: Invalid expression / Unexpected token. Line 1, Col: 949.
  380697 ) and strftime('%Y-%m',procedures_icd.charttime) = '2105-06' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 104: Model abstains from answering the question
Error executing query 105: Model abstains from answering the question
Error executing query 106: Expecting ). Line 1, Col: 898.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 107: Model abstains from answering the question
Error executing query 108: Invalid expression / Unexpected token. Line 1, Col: 1010.
   year') = datetime('2105-12-31 23:59:00','start of year','-0 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 110: Model abstains from answering the question
Error executing query 111: Expecting ). Line 1, Col: 719.
  ogyevents.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.test_name ) as t3 where t3.c1 = 5
Error executing query 112: Model abstains from answering the question
Error executing query 113: Model only answers one image question SQLs
Error executing query 114: Invalid expression / Unexpected token. Line 1, Col: 948.
  dicate clavicle fracture in the right clavicle?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 115: Model only answers one image question SQLs
Error executing query 116: Model only answers one image question SQLs
[False]
Error executing query 121: Invalid expression / Unexpected token. Line 1, Col: 891.
  d = 13888167 ) and strftime('%Y',procedures_icd.charttime) = '2105' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 122: Model only answers one image question SQLs
Error executing query 125: Model only answers one image question SQLs
Error executing query 128: Invalid expression / Unexpected token. Line 1, Col: 982.
   year') = datetime('2105-12-31 23:59:00','start of year','-0 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 130: Model abstains from answering the question
Error executing query 132: Invalid expression / Unexpected token. Line 1, Col: 845.
  qa("does a chest x-ray depicts any abnormality?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 133: Model abstains from answering the question
Error executing query 134: Model abstains from answering the question
Error executing query 137: Model abstains from answering the question
Error executing query 139: Invalid expression / Unexpected token. Line 1, Col: 757.
  ns.hadm_id from admissions where admissions.subject_id = 19385269 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 140: Model only answers one image question SQLs
Error executing query 141: Invalid expression / Unexpected token. Line 1, Col: 1065.
  cedures_icd.charttime) >= datetime('2105-12-31 23:59:00','-2 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and t1.hadm_id = t3.hadm_id
Error executing query 143: Model abstains from answering the question
Error executing query 144: Model abstains from answering the question
Error executing query 145: Model only answers one image question SQLs
Error executing query 146: Model only answers one image question SQLs
Error executing query 149: Model only answers one image question SQLs
Error executing query 150: Model abstains from answering the question
Error executing query 153: Model abstains from answering the question
Error executing query 155: Model only answers one image question SQLs
Error executing query 157: Invalid expression / Unexpected token. Line 1, Col: 871.
   where func_vqa("is any abnormality identified?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 158: Model abstains from answering the question
Error executing query 160: Invalid expression / Unexpected token. Line 1, Col: 994.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id
Error executing query 161: Model abstains from answering the question
Error executing query 162: Invalid expression / Unexpected token. Line 1, Col: 736.
  id = 18380697 ) and strftime('%Y',prescriptions.starttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 166: Model only answers one image question SQLs
Error executing query 167: Model abstains from answering the question
Error executing query 168: Invalid expression / Unexpected token. Line 1, Col: 938.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id
Error executing query 169: Model only answers one image question SQLs
Error executing query 170: Model abstains from answering the question
Error executing query 171: Model only answers one image question SQLs
Error executing query 172: Expecting ). Line 1, Col: 645.
  '%Y',prescriptions.starttime) = '2103' ) as t2 on t1.subject_id = t2.subject_id where t1.starttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 5
Error executing query 173: Model abstains from answering the question
Error executing query 175: Model abstains from answering the question
Error executing query 176: Model only answers one image question SQLs
Error executing query 177: Model abstains from answering the question
Error executing query 178: Invalid expression / Unexpected token. Line 1, Col: 876.
  s.dischtime is not null order by admissions.admittime asc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 179: Model only answers one image question SQLs
Error executing query 180: Model only answers one image question SQLs
Error executing query 181: Model abstains from answering the question
Error executing query 183: Model only answers one image question SQLs
Error executing query 184: Invalid expression / Unexpected token. Line 1, Col: 930.
  t x-ray show any abnormality in the right lung?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 186: Model abstains from answering the question
Error executing query 188: Invalid expression / Unexpected token. Line 1, Col: 829.
  iple masses/nodules in the right mid lung zone?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 189: Expecting ). Line 1, Col: 665.
  ogyevents.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 190: Invalid expression / Unexpected token. Line 1, Col: 887.
  id = 15467362 ) and strftime('%Y',diagnoses_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 192: Model abstains from answering the question
Error executing query 194: Model abstains from answering the question
Error executing query 195: Invalid expression / Unexpected token. Line 1, Col: 925.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 196: Invalid expression / Unexpected token. Line 1, Col: 758.
  y any abnormality in the right upper lung zone?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 197: Model abstains from answering the question
Error executing query 198: Model abstains from answering the question
Error executing query 199: Model only answers one image question SQLs
Error executing query 200: Model abstains from answering the question
Error executing query 202: Model abstains from answering the question
Error executing query 204: Invalid expression / Unexpected token. Line 1, Col: 935.
  agnoses_icd.charttime) >= datetime('2105-12-31 23:59:00','-2 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 207: Model abstains from answering the question
Error executing query 208: Model only answers one image question SQLs
Error executing query 209: Model only answers one image question SQLs
Error executing query 210: Expecting ). Line 1, Col: 852.
  etime('2105-12-31 23:59:00','-3 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 211: Invalid expression / Unexpected token. Line 1, Col: 960.
  dures_icd.charttime) >= datetime('2105-12-31 23:59:00','-33 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 212: Model abstains from answering the question
Error executing query 215: Expecting ). Line 1, Col: 953.
  '%Y',prescriptions.starttime) = '2100' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 5
[False]
Error executing query 217: Expecting ). Line 1, Col: 509.
  criptions.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.starttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.starttime) and datetime(t1.starttime,'+2 m
Error executing query 218: Invalid expression / Unexpected token. Line 1, Col: 731.
  id = 19970078 ) and strftime('%Y',prescriptions.starttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 219: Model only answers one image question SQLs
Error executing query 221: Model only answers one image question SQLs
Error executing query 222: Model abstains from answering the question
Error executing query 223: Model abstains from answering the question
Error executing query 224: Model only answers one image question SQLs
Error executing query 225: Error tokenizing 'in patients on t4.subject_id = patients.subject_i'
Error executing query 233: Invalid expression / Unexpected token. Line 1, Col: 620.
  _vqa("is any devices observed on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 235: Model abstains from answering the question
Error executing query 237: Model abstains from answering the question
Error executing query 238: Model abstains from answering the question
Error executing query 239: Model abstains from answering the question
Error executing query 240: Model abstains from answering the question
Error executing query 241: Model abstains from answering the question
Error executing query 242: Model abstains from answering the question
Error executing query 243: Model abstains from answering the question
Error executing query 244: Model only answers one image question SQLs
Error executing query 245: Model only answers one image question SQLs
Error executing query 246: Invalid expression / Unexpected token. Line 1, Col: 810.
  escriptions.starttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 247: Model only answers one image question SQLs
Error executing query 248: Model abstains from answering the question
Error executing query 249: Model abstains from answering the question
Error executing query 250: Model abstains from answering the question
Error executing query 252: Model abstains from answering the question
Error executing query 253: Model only answers one image question SQLs
Error executing query 254: near "(": syntax error
Error executing query 255: Invalid expression / Unexpected token. Line 1, Col: 746.
   observed in the right atrium on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 256: Model abstains from answering the question
Error executing query 257: Model only answers one image question SQLs
Error executing query 258: Model abstains from answering the question
Error executing query 259: Model abstains from answering the question
Error executing query 260: Model abstains from answering the question
Error executing query 261: Model abstains from answering the question
Error executing query 262: Invalid expression / Unexpected token. Line 1, Col: 903.
  vqa("is any abnormality shown on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 263: Model abstains from answering the question
Error executing query 265: Model only answers one image question SQLs
Error executing query 266: Model abstains from answering the question
Error executing query 267: Model abstains from answering the question
[False]
[False]
Error executing query 269: Model only answers one image question SQLs
Error executing query 270: Model only answers one image question SQLs
Error executing query 271: Model only answers one image question SQLs
Error executing query 272: Invalid expression / Unexpected token. Line 1, Col: 727.
  id = 11685699 ) and strftime('%Y',prescriptions.starttime) = '2105' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 273: Model only answers one image question SQLs
Error executing query 274: Expecting ). Line 1, Col: 904.
  etime('2105-12-31 23:59:00','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 275: Invalid expression / Unexpected token. Line 1, Col: 885.
  x-ray reveal bone lesion in the right clavicle?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 276: Model only answers one image question SQLs
Error executing query 278: Invalid expression / Unexpected token. Line 1, Col: 750.
  ns.hadm_id from admissions where admissions.subject_id = 17087118 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 280: Model abstains from answering the question
Error executing query 282: Model abstains from answering the question
Error executing query 284: Invalid expression / Unexpected token. Line 1, Col: 949.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
Error executing query 286: Model only answers one image question SQLs
Error executing query 287: Model abstains from answering the question
Error executing query 289: Invalid expression / Unexpected token. Line 1, Col: 759.
   calcified nodule in the right lower lung zone?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 290: Invalid expression / Unexpected token. Line 1, Col: 650.
  ns.hadm_id from admissions where admissions.subject_id = 15689544 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 291: Model abstains from answering the question
Error executing query 292: Model abstains from answering the question
Error executing query 294: Model only answers one image question SQLs
Error executing query 296: Model abstains from answering the question
Error executing query 297: Model only answers one image question SQLs
Error executing query 298: Model only answers one image question SQLs
Error executing query 299: Model abstains from answering the question
[False]
Error executing query 304: Invalid expression / Unexpected token. Line 1, Col: 848.
  d = 13411278 ) and strftime('%Y',procedures_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 305: Model abstains from answering the question
Error executing query 307: Expecting ). Line 1, Col: 898.
  %Y',prescriptions.starttime) >= '2103' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 5
Error executing query 309: Invalid expression / Unexpected token. Line 1, Col: 1025.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 311: Model only answers one image question SQLs
Error executing query 313: Model only answers one image question SQLs
Error executing query 315: Model abstains from answering the question
Error executing query 316: near "(": syntax error
Error executing query 317: Model abstains from answering the question
Error executing query 319: Model only answers one image question SQLs
Error executing query 321: Model only answers one image question SQLs
Error executing query 322: Model only answers one image question SQLs
Error executing query 323: Model only answers one image question SQLs
Error executing query 327: Model abstains from answering the question
Error executing query 328: Model only answers one image question SQLs
Error executing query 330: Model abstains from answering the question
Error executing query 331: Model only answers one image question SQLs
Error executing query 333: Invalid expression / Unexpected token. Line 1, Col: 1042.
   in the right lower lung zone on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 335: Model only answers one image question SQLs
Error executing query 336: Invalid expression / Unexpected token. Line 1, Col: 985.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 337: Model abstains from answering the question
Error executing query 338: Model only answers one image question SQLs
Error executing query 339: Expecting ). Line 1, Col: 824.
  etime('2105-12-31 23:59:00','-3 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 341: Model abstains from answering the question
Error executing query 343: Model abstains from answering the question
Error executing query 347: Model abstains from answering the question
Error executing query 348: Model abstains from answering the question
[False]
[False]
Error executing query 351: Invalid expression / Unexpected token. Line 1, Col: 733.
  unc_vqa("is a chest x-ray showing infiltration?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 352: Model only answers one image question SQLs
Error executing query 356: Model abstains from answering the question
Error executing query 357: Model only answers one image question SQLs
Error executing query 358: Model abstains from answering the question
Error executing query 359: Invalid expression / Unexpected token. Line 1, Col: 995.
   year') = datetime('2105-12-31 23:59:00','start of year','-0 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 360: Model only answers one image question SQLs
Error executing query 361: Model abstains from answering the question
Error executing query 363: Model abstains from answering the question
[True]
[True]
Error executing query 366: Invalid expression / Unexpected token. Line 1, Col: 764.
  etime('2105-12-31 23:59:00','-5 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 367: Invalid expression / Unexpected token. Line 1, Col: 735.
  ion of four or more vascular stents' ) ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 368: Model abstains from answering the question
Error executing query 369: Model only answers one image question SQLs
Error executing query 370: Model only answers one image question SQLs
Error executing query 372: Model only answers one image question SQLs
Error executing query 373: Model abstains from answering the question
Error executing query 374: Model only answers one image question SQLs
Error executing query 375: Model only answers one image question SQLs
Error executing query 376: Model only answers one image question SQLs
Error executing query 378: Model abstains from answering the question
Error executing query 379: Model abstains from answering the question
Error executing query 381: Expecting ). Line 1, Col: 883.
  %Y',procedures_icd.charttime) = '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.icd_code ) as t3 where t3.c1 = 5 )
Error executing query 383: Model only answers one image question SQLs
Error executing query 385: Invalid expression / Unexpected token. Line 1, Col: 936.
  agnoses_icd.charttime) = datetime('2105-12-31 23:59:00','-3 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 386: Model abstains from answering the question
Error executing query 387: Invalid expression / Unexpected token. Line 1, Col: 801.
  ray indicate any abnormality in the right lung?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 389: Model only answers one image question SQLs
Error executing query 391: Model only answers one image question SQLs
Error executing query 395: Model abstains from answering the question
Error executing query 397: Model abstains from answering the question
Error executing query 398: Model abstains from answering the question
Error executing query 400: Model only answers one image question SQLs
Error executing query 401: Model abstains from answering the question
Error executing query 405: Model abstains from answering the question
Error executing query 407: Model only answers one image question SQLs
[False]
[False]
Error executing query 409: Model abstains from answering the question
Error executing query 410: Model abstains from answering the question
Error executing query 412: Invalid expression / Unexpected token. Line 1, Col: 879.
   shoulder osteoarthritis in the right shoulder?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 413: Model abstains from answering the question
Error executing query 415: Model abstains from answering the question
Error executing query 416: Invalid expression / Unexpected token. Line 1, Col: 971.
  y reveal mass/nodule (not otherwise specified)?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 418: Expecting ). Line 1, Col: 780.
  dures_icd.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.icd_code ) as t3 where t3.c1 = 4 )
Error executing query 421: Model abstains from answering the question
Error executing query 423: Invalid expression / Unexpected token. Line 1, Col: 734.
  id = 10681061 ) and strftime('%Y',prescriptions.starttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 424: Model abstains from answering the question
Error executing query 425: Invalid expression / Unexpected token. Line 1, Col: 895.
  a("does a chest x-ray indicate any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 426: Model abstains from answering the question
Error executing query 427: Model only answers one image question SQLs
Error executing query 428: Model only answers one image question SQLs
Error executing query 429: Model abstains from answering the question
Error executing query 433: Model abstains from answering the question
Error executing query 435: Invalid expression / Unexpected token. Line 1, Col: 732.
  ns.hadm_id from admissions where admissions.subject_id = 15234578 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 437: Expecting ). Line 1, Col: 649.
  '%Y',prescriptions.starttime) = '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.starttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 5
Error executing query 438: Invalid expression / Unexpected token. Line 1, Col: 775.
  ns.hadm_id from admissions where admissions.subject_id = 15346117 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 439: Model abstains from answering the question
Error executing query 440: near "(": syntax error
Error executing query 441: Model abstains from answering the question
Error executing query 442: Model abstains from answering the question
Error executing query 443: Invalid expression / Unexpected token. Line 1, Col: 880.
  s.dischtime is not null order by admissions.admittime asc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 444: Invalid expression / Unexpected token. Line 1, Col: 841.
  ns.hadm_id from admissions where admissions.subject_id = 11131026 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 447: Expecting ). Line 1, Col: 786.
  ender = 'f' ) and admissions.age >= 60 ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 5
Error executing query 448: Model only answers one image question SQLs
Error executing query 449: Model only answers one image question SQLs
Error executing query 450: Model only answers one image question SQLs
Error executing query 452: Model only answers one image question SQLs
Error executing query 453: Model only answers one image question SQLs
Error executing query 454: Invalid expression / Unexpected token. Line 1, Col: 945.
  ocedures_icd.charttime) = datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 455: Model only answers one image question SQLs
Error executing query 457: Model only answers one image question SQLs
Error executing query 459: Model only answers one image question SQLs
Error executing query 460: Model abstains from answering the question
Error executing query 461: Expecting ). Line 1, Col: 794.
  of the jaws' ) ) as t2 join admissions on t2.subject_id = admissions.subject_id where t2.charttime  [4madmissions[0m.admittime and datetime(admissions.admittime) between datetime(t2.charttime) and datetime(t2.chartti
[False]
Error executing query 463: Invalid expression / Unexpected token. Line 1, Col: 895.
  id = 15584605 ) and strftime('%Y',diagnoses_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 464: Invalid expression / Unexpected token. Line 1, Col: 955.
  cedures_icd.charttime) = datetime('2105-12-31 23:59:00','-2 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 465: Invalid expression / Unexpected token. Line 1, Col: 863.
  e func_vqa("has an x-ray indicated lung lesion?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 466: Model abstains from answering the question
Error executing query 467: Model abstains from answering the question
Error executing query 468: Expecting ). Line 1, Col: 880.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 469: Model abstains from answering the question
Error executing query 470: Model abstains from answering the question
Error executing query 471: Model abstains from answering the question
Error executing query 472: Model only answers one image question SQLs
Error executing query 473: Invalid expression / Unexpected token. Line 1, Col: 962.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
Error executing query 474: Invalid expression / Unexpected token. Line 1, Col: 825.
  rated any diseases in the left upper lung zone?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 475: Model abstains from answering the question
Error executing query 477: Invalid expression / Unexpected token. Line 1, Col: 868.
   = 19896759 ) and strftime('%Y',procedures_icd.charttime) >= '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 478: Model only answers one image question SQLs
Error executing query 480: Model abstains from answering the question
Error executing query 482: Model abstains from answering the question
Error executing query 483: Model only answers one image question SQLs
Error executing query 485: Model abstains from answering the question
Error executing query 486: Model abstains from answering the question
Error executing query 487: Model only answers one image question SQLs
Error executing query 488: Model abstains from answering the question
Error executing query 490: Model only answers one image question SQLs
[False]
Error executing query 493: Model abstains from answering the question
Error executing query 494: Model abstains from answering the question
Error executing query 495: Model abstains from answering the question
Error executing query 496: Model only answers one image question SQLs
Error executing query 497: Expecting ). Line 1, Col: 896.
  etime('2105-12-31 23:59:00','-4 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.itemid ) as t3 where t3.c1 = 4 )
Error executing query 498: Model abstains from answering the question
Error executing query 499: Invalid expression / Unexpected token. Line 1, Col: 919.
  edures_icd.charttime) >= datetime('2105-12-31 23:59:00','-1 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 500: Invalid expression / Unexpected token. Line 1, Col: 918.
  t x-ray detecting pleural/parenchymal scarring?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 502: Invalid expression / Unexpected token. Line 1, Col: 895.
   indication of tortuous aorta on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 503: Model abstains from answering the question
Error executing query 506: near "(": syntax error
Error executing query 507: Model abstains from answering the question
Error executing query 508: Model abstains from answering the question
Error executing query 509: Model only answers one image question SQLs
Error executing query 510: Model abstains from answering the question
Error executing query 511: Model abstains from answering the question
Error executing query 512: Model abstains from answering the question
Error executing query 513: Model only answers one image question SQLs
Error executing query 514: Model abstains from answering the question
Error executing query 515: Model only answers one image question SQLs
Error executing query 516: Model only answers one image question SQLs
Error executing query 517: Model only answers one image question SQLs
Error executing query 518: Model abstains from answering the question
Error executing query 519: Model abstains from answering the question
Error executing query 520: Model abstains from answering the question
Error executing query 522: Model abstains from answering the question
Error executing query 525: Model only answers one image question SQLs
Error executing query 526: Model only answers one image question SQLs
Error executing query 527: Model only answers one image question SQLs
Error executing query 528: Invalid expression / Unexpected token. Line 1, Col: 904.
  vqa("is any abnormality shown on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 530: Invalid expression / Unexpected token. Line 1, Col: 881.
  566805 ) and strftime('%Y-%m',diagnoses_icd.charttime) >= '2104-09' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 533: Model only answers one image question SQLs
Error executing query 535: Model only answers one image question SQLs
Error executing query 536: Invalid expression / Unexpected token. Line 1, Col: 798.
  st x-ray indicate pleural/parenchymal scarring?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 537: Invalid expression / Unexpected token. Line 1, Col: 637.
  ns.hadm_id from admissions where admissions.subject_id = 17328792 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 538: Model only answers one image question SQLs
Error executing query 539: Model abstains from answering the question
Error executing query 540: Invalid expression / Unexpected token. Line 1, Col: 757.
  n pneumothorax in the right costophrenic angle?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 541: Model abstains from answering the question
Error executing query 542: Model only answers one image question SQLs
Error executing query 543: Model abstains from answering the question
Error executing query 544: Model abstains from answering the question
Error executing query 546: Model abstains from answering the question
Error executing query 548: Model abstains from answering the question
Error executing query 552: Model only answers one image question SQLs
Error executing query 553: Invalid expression / Unexpected token. Line 1, Col: 783.
  ns.hadm_id from admissions where admissions.subject_id = 14623286 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 554: Model only answers one image question SQLs
Error executing query 555: Model only answers one image question SQLs
Error executing query 556: Model abstains from answering the question
Error executing query 557: Invalid expression / Unexpected token. Line 1, Col: 917.
  a("does an x-ray reveal vascular calcification?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 558: Invalid expression / Unexpected token. Line 1, Col: 796.
  e any abnormality in the right lower lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 560: Model abstains from answering the question
Error executing query 561: Invalid expression / Unexpected token. Line 1, Col: 1031.
  s.dischtime is not null order by admissions.admittime asc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 565: Invalid expression / Unexpected token. Line 1, Col: 879.
  ng any abnormality in the left upper lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 566: Model abstains from answering the question
Error executing query 567: Model abstains from answering the question
Error executing query 568: Model abstains from answering the question
Error executing query 571: Model abstains from answering the question
Error executing query 572: Expecting ). Line 1, Col: 967.
  etime('2105-12-31 23:59:00','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 573: Model only answers one image question SQLs
Error executing query 576: Invalid expression / Unexpected token. Line 1, Col: 777.
  ns.hadm_id from admissions where admissions.subject_id = 18380697 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 577: Model abstains from answering the question
Error executing query 580: Model only answers one image question SQLs
Error executing query 581: Invalid expression / Unexpected token. Line 1, Col: 797.
  est x-ray indicate any any anatomical findings?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 582: Model abstains from answering the question
Error executing query 583: Model abstains from answering the question
Error executing query 585: Model abstains from answering the question
Error executing query 586: Model abstains from answering the question
Error executing query 588: Model abstains from answering the question
Error executing query 589: Model abstains from answering the question
Error executing query 591: near "(": syntax error
Error executing query 593: Model abstains from answering the question
Error executing query 594: Model abstains from answering the question
Error executing query 596: Invalid expression / Unexpected token. Line 1, Col: 880.
  .dischtime is not null order by admissions.admittime desc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 598: Expecting ). Line 1, Col: 971.
  %Y',diagnoses_icd.charttime) >= '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 599: Model abstains from answering the question
Error executing query 600: Model abstains from answering the question
Error executing query 601: Invalid expression / Unexpected token. Line 1, Col: 786.
  1468671 ) and strftime('%Y-%m',prescriptions.starttime) = '2102-01' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 602: Model abstains from answering the question
Error executing query 603: Model only answers one image question SQLs
Error executing query 604: Model only answers one image question SQLs
Error executing query 605: Model only answers one image question SQLs
Error executing query 608: Model abstains from answering the question
Error executing query 609: Model abstains from answering the question
Error executing query 610: Model only answers one image question SQLs
Error executing query 611: Model abstains from answering the question
Error executing query 612: Model abstains from answering the question
Error executing query 617: Invalid expression / Unexpected token. Line 1, Col: 892.
  d = 13506966 ) and strftime('%Y',procedures_icd.charttime) = '2105' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 620: Model abstains from answering the question
Error executing query 621: Model only answers one image question SQLs
Error executing query 622: Invalid expression / Unexpected token. Line 1, Col: 891.
  55097 ) and strftime('%Y-%m',procedures_icd.charttime) >= '2104-08' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 624: Model abstains from answering the question
Error executing query 625: Model abstains from answering the question
[False]
Error executing query 627: Invalid expression / Unexpected token. Line 1, Col: 913.
  id = 18380697 ) and strftime('%Y',diagnoses_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 629: Model abstains from answering the question
Error executing query 630: Invalid expression / Unexpected token. Line 1, Col: 859.
  a("does a chest x-ray indicate any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 631: Model only answers one image question SQLs
Error executing query 633: Expecting ). Line 1, Col: 1215.
  year') = datetime('2105-12-31 23:59:00','start of year','-0 year') and strftime('%m',procedures_icd.[4mchart[0m
Error executing query 634: Model abstains from answering the question
Error executing query 635: Model only answers one image question SQLs
Error executing query 636: Invalid expression / Unexpected token. Line 1, Col: 852.
  2140106 ) and strftime('%Y-%m',diagnoses_icd.charttime) = '2104-05' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 637: Invalid expression / Unexpected token. Line 1, Col: 777.
  g of any diseases in the neck on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 640: Model abstains from answering the question
Error executing query 641: Model only answers one image question SQLs
Error executing query 642: Model abstains from answering the question
Error executing query 643: Invalid expression / Unexpected token. Line 1, Col: 856.
  d = 16827631 ) and strftime('%Y',diagnoses_icd.charttime) >= '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 644: Model only answers one image question SQLs
Error executing query 645: Invalid expression / Unexpected token. Line 1, Col: 831.
  ("is the chest x-ray revealing any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 647: Invalid expression / Unexpected token. Line 1, Col: 813.
  rescriptions.starttime) = datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 648: Invalid expression / Unexpected token. Line 1, Col: 751.
   any anatomical findings in the right clavicle?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 649: Invalid expression / Unexpected token. Line 1, Col: 736.
  chest x-ray indicate any technical assessments?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 650: Model abstains from answering the question
Error executing query 651: Expecting ). Line 1, Col: 856.
  etime('2105-12-31 23:59:00','-3 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 652: Model abstains from answering the question
Error executing query 653: Invalid expression / Unexpected token. Line 1, Col: 891.
  func_vqa("does an x-ray reveal any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 654: Model abstains from answering the question
Error executing query 655: Model only answers one image question SQLs
Error executing query 656: Model abstains from answering the question
Error executing query 657: Invalid expression / Unexpected token. Line 1, Col: 726.
  qa("does a chest x-ray reveal any any diseases?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 659: Invalid expression / Unexpected token. Line 1, Col: 988.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 661: Model abstains from answering the question
Error executing query 662: Model abstains from answering the question
Error executing query 664: Model only answers one image question SQLs
Error executing query 665: Invalid expression / Unexpected token. Line 1, Col: 878.
  398283 ) and strftime('%Y-%m',procedures_icd.charttime) = '2104-08' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 666: Model only answers one image question SQLs
Error executing query 667: Model only answers one image question SQLs
Error executing query 668: Model only answers one image question SQLs
Error executing query 669: Model only answers one image question SQLs
Error executing query 670: Model abstains from answering the question
Error executing query 671: Invalid expression / Unexpected token. Line 1, Col: 749.
  id = 18136887 ) and strftime('%Y',prescriptions.starttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 672: Model abstains from answering the question
Error executing query 673: Model abstains from answering the question
Error executing query 674: Model abstains from answering the question
Error executing query 677: Model abstains from answering the question
Error executing query 678: Model abstains from answering the question
Error executing query 679: Model only answers one image question SQLs
Error executing query 680: Model only answers one image question SQLs
Error executing query 684: Model abstains from answering the question
Error executing query 685: Model abstains from answering the question
Error executing query 687: Invalid expression / Unexpected token. Line 1, Col: 769.
  how any any abnormality in the left chest wall?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 688: Model abstains from answering the question
Error executing query 690: Model abstains from answering the question
Error executing query 691: Model abstains from answering the question
Error executing query 693: Model abstains from answering the question
Error executing query 694: Model abstains from answering the question
Error executing query 695: Model abstains from answering the question
Error executing query 696: Model abstains from answering the question
Error executing query 699: Model only answers one image question SQLs
Error executing query 700: Invalid expression / Unexpected token. Line 1, Col: 973.
  nstrated any tubes/lines in the right shoulder?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 701: Invalid expression / Unexpected token. Line 1, Col: 660.
  ns.hadm_id from admissions where admissions.subject_id = 18044092 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 702: Model abstains from answering the question
Error executing query 703: Model abstains from answering the question
Error executing query 704: Invalid expression / Unexpected token. Line 1, Col: 632.
  ns.hadm_id from admissions where admissions.subject_id = 16807878 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 705: Expecting ). Line 1, Col: 674.
  ons.hadm_id where admissions.age >= 60 ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 4
Error executing query 706: Model only answers one image question SQLs
Error executing query 707: Model only answers one image question SQLs
Error executing query 708: Expecting ). Line 1, Col: 920.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 709: Model only answers one image question SQLs
Error executing query 711: Model abstains from answering the question
Error executing query 712: Model abstains from answering the question
Error executing query 713: Model only answers one image question SQLs
Error executing query 715: Model only answers one image question SQLs
Error executing query 717: Model only answers one image question SQLs
Error executing query 718: Model only answers one image question SQLs
Error executing query 719: Invalid expression / Unexpected token. Line 1, Col: 877.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 720: Model only answers one image question SQLs
Error executing query 724: Invalid expression / Unexpected token. Line 1, Col: 745.
  ns.hadm_id from admissions where admissions.subject_id = 10938464 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 726: Model abstains from answering the question
Error executing query 727: Model abstains from answering the question
Error executing query 728: Invalid expression / Unexpected token. Line 1, Col: 978.
  f costophrenic angle blunting on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 729: Model only answers one image question SQLs
Error executing query 732: Invalid expression / Unexpected token. Line 1, Col: 889.
  does a chest x-ray show elevated hemidiaphragm?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 733: Invalid expression / Unexpected token. Line 1, Col: 959.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id
Error executing query 734: Invalid expression / Unexpected token. Line 1, Col: 629.
  ns.hadm_id from admissions where admissions.subject_id = 16922420 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 735: Expecting ). Line 1, Col: 872.
  '%Y',diagnoses_icd.charttime) = '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 736: Model abstains from answering the question
Error executing query 737: Invalid expression / Unexpected token. Line 1, Col: 851.
  t x-ray indicate any abnormality in the carina?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 738: Invalid expression / Unexpected token. Line 1, Col: 875.
  431875 ) and strftime('%Y-%m',diagnoses_icd.charttime) >= '2103-12' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 739: Invalid expression / Unexpected token. Line 1, Col: 725.
  d = 12712004 ) and strftime('%Y',prescriptions.starttime) >= '2105' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 740: Model only answers one image question SQLs
Error executing query 743: Model abstains from answering the question
Error executing query 744: Invalid expression / Unexpected token. Line 1, Col: 1122.
  nth') = datetime('2105-12-31 23:59:00','start of month','-0 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and t1.hadm_id = t3.hadm_id
Error executing query 745: Model abstains from answering the question
Error executing query 746: Model abstains from answering the question
Error executing query 751: Model abstains from answering the question
Error executing query 752: Model abstains from answering the question
Error executing query 754: Invalid expression / Unexpected token. Line 1, Col: 716.
  ns.hadm_id from admissions where admissions.subject_id = 12408912 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 755: Expecting ). Line 1, Col: 918.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.test_name ) as t3 where t3.c1 = 3
Error executing query 756: Expecting ). Line 1, Col: 1031.
  olume ( dialysis/pheresis catheters )' ) as t3 on t2.subject_id = t3.subject_id where t2.charttime  [4mt3[0m.starttime ) as t4 join patients on t4.subject_id = patients.subject_id
Error executing query 757: Model abstains from answering the question
Error executing query 758: Model only answers one image question SQLs
Error executing query 759: Model abstains from answering the question
Error executing query 760: Expecting ). Line 1, Col: 970.
  ere prescriptions.drug = 'colesevelam' ) as t3 on t2.subject_id = t3.subject_id where t2.charttime  [4mt3[0m.starttime ) as t4 join patients on t4.subject_id = patients.subject_id
Error executing query 761: near "(": syntax error
Error executing query 762: Model abstains from answering the question
Error executing query 764: Invalid expression / Unexpected token. Line 1, Col: 1095.
  agnoses_icd.charttime) >= datetime('2105-12-31 23:59:00','-3 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 765: Model only answers one image question SQLs
Error executing query 766: Model only answers one image question SQLs
Error executing query 767: Invalid expression / Unexpected token. Line 1, Col: 927.
   anatomical findings in the left mid lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 768: Model only answers one image question SQLs
Error executing query 771: Model abstains from answering the question
Error executing query 773: Model abstains from answering the question
Error executing query 774: Model abstains from answering the question
Error executing query 775: Invalid expression / Unexpected token. Line 1, Col: 1005.
  _vqa("does a chest x-ray indicate any diseases?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 776: Invalid expression / Unexpected token. Line 1, Col: 883.
  any indication of any devices on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 778: Expecting ). Line 1, Col: 860.
  microbiologyevents.charttime) = '2103' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.test_name ) as t3 where t3.c1 = 5
Error executing query 779: Model only answers one image question SQLs
Error executing query 781: Expecting ). Line 1, Col: 870.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 782: Model abstains from answering the question
Error executing query 785: Invalid expression / Unexpected token. Line 1, Col: 767.
  ns.hadm_id from admissions where admissions.subject_id = 13119866 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 786: Expecting ). Line 1, Col: 833.
  me('%Y',labevents.charttime) >= '2105' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.itemid ) as t3 where t3.c1 = 5 )
Error executing query 788: Model only answers one image question SQLs
Error executing query 790: Model abstains from answering the question
Error executing query 793: Model abstains from answering the question
Error executing query 795: Expecting ). Line 1, Col: 895.
  etime('2105-12-31 23:59:00','-6 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 797: Invalid expression / Unexpected token. Line 1, Col: 913.
  s a chest x-ray show goiter in the mediastinum?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 798: Invalid expression / Unexpected token. Line 1, Col: 747.
  icate any abnormality in the right apical zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 799: Model abstains from answering the question
Error executing query 800: Model abstains from answering the question
Error executing query 801: Model abstains from answering the question
Error executing query 802: Invalid expression / Unexpected token. Line 1, Col: 882.
  ay indicate cardiac pacer and wires in the svc?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 803: Model abstains from answering the question
Error executing query 805: near "(": syntax error
Error executing query 806: Model abstains from answering the question
Error executing query 809: Model only answers one image question SQLs
Error executing query 810: Invalid expression / Unexpected token. Line 1, Col: 726.
   t2 where func_vqa("is tortuous aorta revealed?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 811: Model abstains from answering the question
Error executing query 812: Model abstains from answering the question
Error executing query 813: Model abstains from answering the question
Error executing query 814: Model abstains from answering the question
Error executing query 817: Expecting ). Line 1, Col: 852.
  ) and admissions.age between 50 and 59 ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 3
Error executing query 819: Model only answers one image question SQLs
Error executing query 820: Invalid expression / Unexpected token. Line 1, Col: 861.
  id = 17968028 ) and strftime('%Y',diagnoses_icd.charttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 821: Model abstains from answering the question
Error executing query 822: Model only answers one image question SQLs
Error executing query 823: Model only answers one image question SQLs
Error executing query 824: Model only answers one image question SQLs
Error executing query 825: Invalid expression / Unexpected token. Line 1, Col: 779.
  ns.hadm_id from admissions where admissions.subject_id = 16529186 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 827: Model abstains from answering the question
Error executing query 828: Expecting ). Line 1, Col: 672.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.starttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.starttime) and datetime(t1.starttime,'+2 m
Error executing query 829: Expecting ). Line 1, Col: 771.
  etime('2105-12-31 23:59:00','-4 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 830: Model only answers one image question SQLs
Error executing query 831: Invalid expression / Unexpected token. Line 1, Col: 768.
  ns.hadm_id from admissions where admissions.subject_id = 13411278 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 832: Model abstains from answering the question
Error executing query 833: Invalid expression / Unexpected token. Line 1, Col: 850.
  id = 10681061 ) and strftime('%Y',diagnoses_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 834: Model only answers one image question SQLs
Error executing query 836: Model only answers one image question SQLs
Error executing query 838: Invalid expression / Unexpected token. Line 1, Col: 893.
  echnical assessments revealed on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 839: Invalid expression / Unexpected token. Line 1, Col: 1016.
  ting any anatomical findings in the right lung?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 842: Model abstains from answering the question
Error executing query 844: Invalid expression / Unexpected token. Line 1, Col: 1018.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id
Error executing query 845: near "(": syntax error
Error executing query 846: Model only answers one image question SQLs
Error executing query 847: Model only answers one image question SQLs
[True]
Error executing query 850: Model abstains from answering the question
Error executing query 851: Expecting ). Line 1, Col: 885.
  dures_icd.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 852: Model abstains from answering the question
Error executing query 853: Expecting ). Line 1, Col: 958.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 3
Error executing query 854: Model abstains from answering the question
Error executing query 856: Model abstains from answering the question
Error executing query 857: Model only answers one image question SQLs
Error executing query 860: Model only answers one image question SQLs
Error executing query 861: Model only answers one image question SQLs
Error executing query 862: Model abstains from answering the question
Error executing query 864: Model abstains from answering the question
Error executing query 865: Invalid expression / Unexpected token. Line 1, Col: 853.
  nc_vqa("has an x-ray indicated any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 866: Model only answers one image question SQLs
Error executing query 867: Model abstains from answering the question
Error executing query 869: Model abstains from answering the question
Error executing query 871: Model abstains from answering the question
Error executing query 876: Model abstains from answering the question
Error executing query 877: Invalid expression / Unexpected token. Line 1, Col: 937.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
Error executing query 878: Invalid expression / Unexpected token. Line 1, Col: 885.
  agnoses_icd.charttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 879: Invalid expression / Unexpected token. Line 1, Col: 700.
  '%Y',prescriptions.starttime) = '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month')
Error executing query 881: Invalid expression / Unexpected token. Line 1, Col: 926.
  pneumonia revealed in the left upper lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 882: Model only answers one image question SQLs
Error executing query 883: Model only answers one image question SQLs
Error executing query 884: Model abstains from answering the question
Error executing query 887: Expecting ). Line 1, Col: 781.
  etime('2105-12-31 23:59:00','-3 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 890: Model abstains from answering the question
Error executing query 891: Invalid expression / Unexpected token. Line 1, Col: 737.
  831708 ) and strftime('%Y-%m',prescriptions.starttime) >= '2104-02' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 892: Model only answers one image question SQLs
Error executing query 893: Model abstains from answering the question
Error executing query 894: Model only answers one image question SQLs
Error executing query 897: Model abstains from answering the question
Error executing query 898: Invalid expression / Unexpected token. Line 1, Col: 936.
  gnoses_icd.charttime) = datetime('2105-12-31 23:59:00','-25 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
[True]
Error executing query 903: Invalid expression / Unexpected token. Line 1, Col: 861.
  segmental collapse in the left upper lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 904: Model only answers one image question SQLs
Error executing query 906: Invalid expression / Unexpected token. Line 1, Col: 1056.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 907: Model only answers one image question SQLs
Error executing query 911: Model abstains from answering the question
Error executing query 914: Model abstains from answering the question
Error executing query 915: Model only answers one image question SQLs
Error executing query 916: Model abstains from answering the question
Error executing query 917: Model abstains from answering the question
Error executing query 918: Model only answers one image question SQLs
Error executing query 919: Invalid expression / Unexpected token. Line 1, Col: 751.
   in the left hilar structures on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 920: Model abstains from answering the question
Error executing query 921: Invalid expression / Unexpected token. Line 1, Col: 970.
   year','-0 year') and strftime('%m',prescriptions.starttime) = '01' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 922: Model only answers one image question SQLs
Error executing query 924: Model abstains from answering the question
Error executing query 926: Model only answers one image question SQLs
Error executing query 927: Model only answers one image question SQLs
Error executing query 929: near "(": syntax error
Error executing query 930: Invalid expression / Unexpected token. Line 1, Col: 827.
  etime('2105-12-31 23:59:00','-5 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id
Error executing query 931: Invalid expression / Unexpected token. Line 1, Col: 647.
  t x-ray showing any abnormality in the abdomen?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 933: Model abstains from answering the question
Error executing query 934: Model only answers one image question SQLs
Error executing query 935: Model only answers one image question SQLs
Error executing query 936: Invalid expression / Unexpected token. Line 1, Col: 862.
  ny technical assessments indicated on an x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 939: Model abstains from answering the question
Error executing query 940: Model abstains from answering the question
Error executing query 941: Expecting ). Line 1, Col: 541.
  criptions.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.starttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 4
Error executing query 942: Model only answers one image question SQLs
Error executing query 943: Model abstains from answering the question
Error executing query 944: Invalid expression / Unexpected token. Line 1, Col: 759.
   anatomical findings in the left hemidiaphragm?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 946: Model abstains from answering the question
Error executing query 947: Model abstains from answering the question
Error executing query 949: Invalid expression / Unexpected token. Line 1, Col: 739.
  d = 12864997 ) and strftime('%Y',prescriptions.starttime) >= '2104' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 950: Model only answers one image question SQLs
Error executing query 951: Required keyword: 'expressions' missing for <class 'sqlglot.expressions.Aliases'>. Line 1, Col: 519.
  re systolic' and d_items.linksto = 'chartevents' ) order by chartevents.charttime desc limit 1 )  ( [4mselect[0m chartevents.valuenum from chartevents where chartevents.stay_id in ( select icustays.stay_id from i
Error executing query 952: Model abstains from answering the question
Error executing query 953: Invalid expression / Unexpected token. Line 1, Col: 869.
  23:59:00','start of month','-0 month') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 d
Error executing query 955: Invalid expression / Unexpected token. Line 1, Col: 769.
  ated any anatomical findings in the right lung?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 956: Expecting ). Line 1, Col: 792.
  ) and admissions.age between 30 and 39 ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 3
Error executing query 957: Invalid expression / Unexpected token. Line 1, Col: 992.
  x-ray reveal rotated in the cardiac silhouette?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 958: Model only answers one image question SQLs
Error executing query 960: Model abstains from answering the question
Error executing query 961: Expecting ). Line 1, Col: 796.
  dures_icd.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.icd_code ) as t3 where t3.c1 = 5 )
Error executing query 965: Model abstains from answering the question
Error executing query 966: Invalid expression / Unexpected token. Line 1, Col: 1007.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 967: Model abstains from answering the question
Error executing query 968: Model only answers one image question SQLs
Error executing query 969: Invalid expression / Unexpected token. Line 1, Col: 657.
   depicts any abnormality in the right shoulder?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 970: Model abstains from answering the question
Error executing query 971: Model only answers one image question SQLs
Error executing query 972: Invalid expression / Unexpected token. Line 1, Col: 832.
  c_vqa("does a chest x-ray show any tubes/lines?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 973: Model abstains from answering the question
Error executing query 975: Model abstains from answering the question
Error executing query 976: Expecting ). Line 1, Col: 784.
  me('%Y',labevents.charttime) >= '2101' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 977: Invalid expression / Unexpected token. Line 1, Col: 762.
  on of any anatomical findings on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 980: Expecting ). Line 1, Col: 791.
  microbiologyevents.charttime) = '2105' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 981: near "(": syntax error
Error executing query 982: Invalid expression / Unexpected token. Line 1, Col: 847.
  %Y',procedures_icd.charttime) = '2100' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 983: Invalid expression / Unexpected token. Line 1, Col: 835.
  es an x-ray reveal spinal degenerative changes?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 984: Invalid expression / Unexpected token. Line 1, Col: 756.
  089595 ) and strftime('%Y-%m',prescriptions.starttime) >= '2102-04' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
[False]
[False]
Error executing query 986: Model only answers one image question SQLs
Error executing query 987: Model only answers one image question SQLs
Error executing query 988: Model only answers one image question SQLs
Error executing query 989: Model abstains from answering the question
Error executing query 990: Model abstains from answering the question
Error executing query 991: Model only answers one image question SQLs
Error executing query 992: Model only answers one image question SQLs
Error executing query 993: Model only answers one image question SQLs
Error executing query 994: Model abstains from answering the question
Error executing query 995: Model only answers one image question SQLs
Error executing query 996: Model abstains from answering the question
Error executing query 997: Invalid expression / Unexpected token. Line 1, Col: 952.
   = 16484690 ) and strftime('%Y',procedures_icd.charttime) >= '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 998: Model abstains from answering the question
Error executing query 1000: Expecting ). Line 1, Col: 927.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1001: Model abstains from answering the question
Error executing query 1002: Model abstains from answering the question
Error executing query 1003: Model abstains from answering the question
Error executing query 1005: Invalid expression / Unexpected token. Line 1, Col: 918.
  c_vqa("has a chest x-ray shown any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1006: Model abstains from answering the question
Error executing query 1007: Invalid expression / Unexpected token. Line 1, Col: 885.
   the right costophrenic angle on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1008: Invalid expression / Unexpected token. Line 1, Col: 974.
  pleural/parenchymal scarring in the right lung?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 1010: Model only answers one image question SQLs
Error executing query 1011: Invalid expression / Unexpected token. Line 1, Col: 733.
  id = 16484690 ) and strftime('%Y',prescriptions.starttime) = '2102' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 1012: Model abstains from answering the question
Error executing query 1013: Expecting ). Line 1, Col: 868.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1014: Model abstains from answering the question
Error executing query 1015: Model abstains from answering the question
Error executing query 1016: Model abstains from answering the question
Error executing query 1017: Invalid expression / Unexpected token. Line 1, Col: 767.
  ns.hadm_id from admissions where admissions.subject_id = 11685699 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1018: Model abstains from answering the question
Error executing query 1020: Invalid expression / Unexpected token. Line 1, Col: 868.
  ere func_vqa("does an x-ray reveal lung cancer?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1021: Model only answers one image question SQLs
Error executing query 1022: Invalid expression / Unexpected token. Line 1, Col: 914.
  gnoses_icd.charttime) = datetime('2105-12-31 23:59:00','-15 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1023: Model abstains from answering the question
Error executing query 1024: Invalid expression / Unexpected token. Line 1, Col: 848.
   year') = datetime('2105-12-31 23:59:00','start of year','-0 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 1025: Model only answers one image question SQLs
Error executing query 1026: Model only answers one image question SQLs
Error executing query 1027: Model only answers one image question SQLs
Error executing query 1028: Model abstains from answering the question
Error executing query 1029: Expecting ). Line 1, Col: 734.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.starttime  [4mt2[0m.starttime and datetime(t1.starttime,'start of month') = datetime(t2.starttime,'start of month') gro
Error executing query 1030: Model only answers one image question SQLs
Error executing query 1031: Invalid expression / Unexpected token. Line 1, Col: 874.
  d = 17622334 ) and strftime('%Y',procedures_icd.charttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1032: Expecting ). Line 1, Col: 974.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 1033: Expecting ). Line 1, Col: 923.
  %Y',procedures_icd.charttime) = '2102' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.icd_code ) as t3 where t3.c1 = 4 )
Error executing query 1034: Model only answers one image question SQLs
Error executing query 1036: Model abstains from answering the question
Error executing query 1037: Model only answers one image question SQLs
Error executing query 1038: near "(": syntax error
Error executing query 1039: Model only answers one image question SQLs
Error executing query 1040: Model abstains from answering the question
Error executing query 1044: Invalid expression / Unexpected token. Line 1, Col: 993.
  lity in the right apical zone on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 1046: Model abstains from answering the question
[False]
Error executing query 1048: Model abstains from answering the question
Error executing query 1050: Model abstains from answering the question
Error executing query 1051: Model only answers one image question SQLs
Error executing query 1053: Model only answers one image question SQLs
Error executing query 1054: Model only answers one image question SQLs
Error executing query 1055: Model only answers one image question SQLs
Error executing query 1056: Invalid expression / Unexpected token. Line 1, Col: 727.
  ns.hadm_id from admissions where admissions.subject_id = 10032409 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1059: Expecting ). Line 1, Col: 635.
  '%Y',prescriptions.starttime) = '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.starttime  [4mt2[0m.starttime and datetime(t1.starttime,'start of month') = datetime(t2.starttime,'start of month') gro
Error executing query 1060: Model abstains from answering the question
Error executing query 1061: Expecting ). Line 1, Col: 908.
  time) = '2105' ) as t2 join admissions on t2.subject_id = admissions.subject_id where t2.charttime  [4madmissions[0m.admittime and strftime('%Y',admissions.admittime) = '2105' and datetime(admissions.admittime) betwe
Error executing query 1062: Model abstains from answering the question
Error executing query 1066: Model abstains from answering the question
Error executing query 1068: Model only answers one image question SQLs
Error executing query 1069: Invalid expression / Unexpected token. Line 1, Col: 790.
  a("does a chest x-ray show any any abnormality?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1070: Model abstains from answering the question
Error executing query 1071: Model only answers one image question SQLs
Error executing query 1072: Invalid expression / Unexpected token. Line 1, Col: 905.
  544660 ) and strftime('%Y-%m',procedures_icd.charttime) = '2103-02' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1073: Model abstains from answering the question
Error executing query 1075: Invalid expression / Unexpected token. Line 1, Col: 725.
  _vqa("has a chest x-ray shown prosthetic valve?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1076: Model only answers one image question SQLs
Error executing query 1077: Invalid expression / Unexpected token. Line 1, Col: 908.
  d = 13656933 ) and strftime('%Y',procedures_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1078: Model abstains from answering the question
Error executing query 1079: Model abstains from answering the question
Error executing query 1080: Model abstains from answering the question
Error executing query 1081: Expecting ). Line 1, Col: 900.
  %Y',procedures_icd.charttime) = '2100' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 1082: Model abstains from answering the question
Error executing query 1083: Invalid expression / Unexpected token. Line 1, Col: 733.
  id = 18291049 ) and strftime('%Y',prescriptions.starttime) = '2102' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 1085: Model only answers one image question SQLs
Error executing query 1087: Model only answers one image question SQLs
Error executing query 1088: Model abstains from answering the question
Error executing query 1089: Invalid expression / Unexpected token. Line 1, Col: 732.
  id = 10254956 ) and strftime('%Y',prescriptions.starttime) = '2105' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 1091: Expecting ). Line 1, Col: 706.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.starttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 3
Error executing query 1092: Model abstains from answering the question
Error executing query 1093: Model abstains from answering the question
Error executing query 1097: Model only answers one image question SQLs
Error executing query 1099: Model abstains from answering the question
Error executing query 1100: Invalid expression / Unexpected token. Line 1, Col: 751.
  ',prescriptions.starttime) = '2105-03' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 d
Error executing query 1101: Model abstains from answering the question
Error executing query 1102: Model abstains from answering the question
Error executing query 1103: Invalid expression / Unexpected token. Line 1, Col: 920.
  e chest x-ray revealing granulomatous diseases?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 1105: Invalid expression / Unexpected token. Line 1, Col: 996.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1107: Model abstains from answering the question
Error executing query 1108: Model abstains from answering the question
Error executing query 1112: Model abstains from answering the question
Error executing query 1113: Expecting ). Line 1, Col: 896.
  etime('2105-12-31 23:59:00','-3 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1117: Invalid expression / Unexpected token. Line 1, Col: 755.
  any any abnormality in the right mid lung zone?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1118: Invalid expression / Unexpected token. Line 1, Col: 844.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1120: Invalid expression / Unexpected token. Line 1, Col: 658.
  ns.hadm_id from admissions where admissions.subject_id = 10032409 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1121: Model abstains from answering the question
Error executing query 1122: Model abstains from answering the question
Error executing query 1123: Model abstains from answering the question
Error executing query 1124: Model only answers one image question SQLs
Error executing query 1125: Model abstains from answering the question
Error executing query 1126: Invalid expression / Unexpected token. Line 1, Col: 635.
  ns.hadm_id from admissions where admissions.subject_id = 17988477 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1127: Model abstains from answering the question
Error executing query 1129: Model abstains from answering the question
Error executing query 1131: Invalid expression / Unexpected token. Line 1, Col: 773.
  eft lower leg muscle, open approach' ) ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1132: Invalid expression / Unexpected token. Line 1, Col: 1092.
  dures_icd.charttime) >= datetime('2105-12-31 23:59:00','-12 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and t1.hadm_id = t3.hadm_id
Error executing query 1133: Required keyword: 'expressions' missing for <class 'sqlglot.expressions.Aliases'>. Line 1, Col: 410.
  tems where d_labitems.label = 'hemoglobin' ) order by labevents.charttime asc limit 1 offset 1 )  ( [4mselect[0m labevents.valuenum from labevents where labevents.hadm_id in ( select admissions.hadm_id from admis
Error executing query 1134: Model abstains from answering the question
Error executing query 1135: Invalid expression / Unexpected token. Line 1, Col: 854.
  nc_vqa("is a chest x-ray detecting any devices?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1136: Model only answers one image question SQLs
Error executing query 1137: Invalid expression / Unexpected token. Line 1, Col: 860.
  t x-ray showing any abnormality in the trachea?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 1139: Model abstains from answering the question
Error executing query 1141: Model abstains from answering the question
Error executing query 1143: Expecting ). Line 1, Col: 843.
  microbiologyevents.charttime) = '2105' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1144: Expecting ). Line 1, Col: 682.
  ogyevents.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 1146: Model abstains from answering the question
Error executing query 1149: Model abstains from answering the question
Error executing query 1150: Model only answers one image question SQLs
Error executing query 1151: Model abstains from answering the question
Error executing query 1152: Model only answers one image question SQLs
Error executing query 1153: Invalid expression / Unexpected token. Line 1, Col: 1005.
  iagnoses_icd.charttime) = datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1155: Model abstains from answering the question
Error executing query 1159: Model abstains from answering the question
Error executing query 1160: Expecting ). Line 1, Col: 679.
  ogyevents.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1161: Model abstains from answering the question
Error executing query 1162: Model only answers one image question SQLs
Error executing query 1163: Model abstains from answering the question
Error executing query 1164: Model abstains from answering the question
Error executing query 1165: Invalid expression / Unexpected token. Line 1, Col: 661.
  ns.hadm_id from admissions where admissions.subject_id = 12126708 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 1168: Model only answers one image question SQLs
Error executing query 1169: Model abstains from answering the question
Error executing query 1171: Model only answers one image question SQLs
Error executing query 1172: Model abstains from answering the question
Error executing query 1173: Model abstains from answering the question
Error executing query 1176: Model abstains from answering the question
Error executing query 1178: Invalid expression / Unexpected token. Line 1, Col: 728.
  id = 10160202 ) and strftime('%Y',prescriptions.starttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 1180: Model abstains from answering the question
Error executing query 1182: Invalid expression / Unexpected token. Line 1, Col: 817.
  escriptions.starttime) >= datetime('2105-12-31 23:59:00','-2 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 1183: Model only answers one image question SQLs
Error executing query 1184: Model abstains from answering the question
Error executing query 1187: Model only answers one image question SQLs
Error executing query 1188: Model abstains from answering the question
Error executing query 1190: Invalid expression / Unexpected token. Line 1, Col: 895.
  23:59:00','start of month','-0 month') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 d
Error executing query 1191: Model abstains from answering the question
Error executing query 1192: Model abstains from answering the question
Error executing query 1193: Model abstains from answering the question
Error executing query 1194: Model only answers one image question SQLs
Error executing query 1195: Model abstains from answering the question
Error executing query 1197: Model abstains from answering the question
Error executing query 1199: Model only answers one image question SQLs
Error executing query 1202: Model abstains from answering the question
Error executing query 1203: Model only answers one image question SQLs
Error executing query 1204: Model only answers one image question SQLs
Error executing query 1205: Model abstains from answering the question
Error executing query 1207: Required keyword: 'expression' missing for <class 'sqlglot.expressions.EQ'>. Line 1, Col: 1168.
  tetime('2105-12-31 23:59:00','start of year','-1 year') and strftime('%m',procedures_icd.charttime) [4m=[0m
Error executing query 1208: Invalid expression / Unexpected token. Line 1, Col: 934.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1209: Model abstains from answering the question
Error executing query 1212: Model abstains from answering the question
Error executing query 1215: Model abstains from answering the question
Error executing query 1218: Invalid expression / Unexpected token. Line 1, Col: 733.
  id = 17183305 ) and strftime('%Y',prescriptions.starttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1219: Invalid expression / Unexpected token. Line 1, Col: 738.
  id = 19606590 ) and strftime('%Y',prescriptions.starttime) = '2105' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 1220: Invalid expression / Unexpected token. Line 1, Col: 734.
  qa("does a chest x-ray depicts any abnormality?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 1221: Model abstains from answering the question
Error executing query 1223: Model only answers one image question SQLs
Error executing query 1224: Invalid expression / Unexpected token. Line 1, Col: 744.
  ns.hadm_id from admissions where admissions.subject_id = 14117444 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1226: Model only answers one image question SQLs
Error executing query 1229: Model abstains from answering the question
Error executing query 1230: Model only answers one image question SQLs
Error executing query 1231: Model only answers one image question SQLs
Error executing query 1232: Model only answers one image question SQLs
Error executing query 1233: Model abstains from answering the question
Error executing query 1234: Model abstains from answering the question
Error executing query 1235: Model abstains from answering the question
Error executing query 1236: Model abstains from answering the question
Error executing query 1237: Invalid expression / Unexpected token. Line 1, Col: 708.
  g_title = 'arterial catheterization' ) ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1238: Model only answers one image question SQLs
Error executing query 1239: Model only answers one image question SQLs
Error executing query 1240: Model only answers one image question SQLs
Error executing query 1242: Model abstains from answering the question
Error executing query 1243: Model abstains from answering the question
Error executing query 1245: Model only answers one image question SQLs
Error executing query 1246: Model only answers one image question SQLs
Error executing query 1247: Model abstains from answering the question
Error executing query 1248: Model only answers one image question SQLs
Error executing query 1249: Model only answers one image question SQLs
Error executing query 1251: Invalid expression / Unexpected token. Line 1, Col: 921.
  ated subclavian line in the cardiac silhouette?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1252: Model only answers one image question SQLs
Error executing query 1253: Model abstains from answering the question
Error executing query 1254: Model only answers one image question SQLs
Error executing query 1257: Model abstains from answering the question
Error executing query 1258: Invalid expression / Unexpected token. Line 1, Col: 400.
  bel = 'o2 saturation pulseoxymetry' and d_items.linksto = 'chartevents' ) and chartevents.valuenum  [4m97.0[0m and datetime(chartevents.charttime) = datetime('2105-12-31 23:59:00','-729 day')
Error executing query 1260: Invalid expression / Unexpected token. Line 1, Col: 937.
  8463717 ) and strftime('%Y-%m',diagnoses_icd.charttime) = '2105-12' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1261: Expecting ). Line 1, Col: 704.
  where admissions.age between 20 and 29 ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 3
Error executing query 1263: Model only answers one image question SQLs
Error executing query 1264: Model abstains from answering the question
Error executing query 1265: Model abstains from answering the question
Error executing query 1266: Model abstains from answering the question
Error executing query 1267: Model only answers one image question SQLs
Error executing query 1268: Invalid expression / Unexpected token. Line 1, Col: 768.
  ',prescriptions.starttime) = '2102-02' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id
Error executing query 1269: Invalid expression / Unexpected token. Line 1, Col: 912.
   a chest x-ray show interstitial lung diseases?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 1270: Model abstains from answering the question
Error executing query 1271: Model abstains from answering the question
Error executing query 1272: Model abstains from answering the question
Error executing query 1273: Model abstains from answering the question
Error executing query 1274: Model only answers one image question SQLs
Error executing query 1275: Model only answers one image question SQLs
Error executing query 1276: Model abstains from answering the question
Error executing query 1277: Model only answers one image question SQLs
Error executing query 1278: Model only answers one image question SQLs
Error executing query 1279: Model abstains from answering the question
Error executing query 1280: Model abstains from answering the question
Error executing query 1281: Invalid expression / Unexpected token. Line 1, Col: 928.
  etime('2105-12-31 23:59:00','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id
Error executing query 1283: Model abstains from answering the question
Error executing query 1284: Invalid expression / Unexpected token. Line 1, Col: 867.
  s an x-ray indicated any technical assessments?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 1286: Invalid expression / Unexpected token. Line 1, Col: 851.
  us catheter placement with guidance' ) ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
Error executing query 1287: Invalid expression / Unexpected token. Line 1, Col: 937.
  agnoses_icd.charttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1288: Model only answers one image question SQLs
Error executing query 1289: Model abstains from answering the question
Error executing query 1291: Expecting ). Line 1, Col: 828.
  etime('2105-12-31 23:59:00','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 1293: Model abstains from answering the question
Error executing query 1294: Model abstains from answering the question
Error executing query 1295: Model abstains from answering the question
Error executing query 1296: Model abstains from answering the question
Error executing query 1297: Model only answers one image question SQLs
Error executing query 1298: Invalid expression / Unexpected token. Line 1, Col: 984.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
Error executing query 1300: Model abstains from answering the question
Error executing query 1301: Model abstains from answering the question
Error executing query 1303: Invalid expression / Unexpected token. Line 1, Col: 905.
  agnoses_icd.charttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1305: Model abstains from answering the question
Error executing query 1306: Invalid expression / Unexpected token. Line 1, Col: 690.
  ns.hadm_id from admissions where admissions.subject_id = 16484690 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1307: Model abstains from answering the question
Error executing query 1308: Invalid expression / Unexpected token. Line 1, Col: 734.
  vqa("does a chest x-ray reveal any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
[False]
[False]
[True]
[True]
Error executing query 1315: Model abstains from answering the question
Error executing query 1317: Invalid expression / Unexpected token. Line 1, Col: 620.
  ns.hadm_id from admissions where admissions.subject_id = 19305006 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 1320: Expecting ). Line 1, Col: 843.
  microbiologyevents.charttime) = '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.test_name ) as t3 where t3.c1 = 3
Error executing query 1321: Model only answers one image question SQLs
Error executing query 1325: Model abstains from answering the question
Error executing query 1327: Model abstains from answering the question
Error executing query 1328: Expecting ). Line 1, Col: 894.
  etime('2105-12-31 23:59:00','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1329: Invalid expression / Unexpected token. Line 1, Col: 866.
  etime('2105-12-31 23:59:00','-3 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1330: Model only answers one image question SQLs
Error executing query 1331: Invalid expression / Unexpected token. Line 1, Col: 874.
  show hyperaeration in the left upper lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1333: Model only answers one image question SQLs
Error executing query 1334: Model only answers one image question SQLs
Error executing query 1336: Model abstains from answering the question
Error executing query 1337: Model abstains from answering the question
Error executing query 1338: Expecting ). Line 1, Col: 794.
  icrobiologyevents.charttime) >= '2102' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1339: Model only answers one image question SQLs
Error executing query 1340: Model abstains from answering the question
Error executing query 1341: Model abstains from answering the question
Error executing query 1342: Model only answers one image question SQLs
Error executing query 1347: Model abstains from answering the question
Error executing query 1348: Model only answers one image question SQLs
Error executing query 1349: Model abstains from answering the question
Error executing query 1350: Model abstains from answering the question
Error executing query 1351: Model abstains from answering the question
Error executing query 1352: Model only answers one image question SQLs
Error executing query 1354: Model only answers one image question SQLs
Error executing query 1355: Invalid expression / Unexpected token. Line 1, Col: 863.
  id = 11725800 ) and strftime('%Y',diagnoses_icd.charttime) = '2105' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1356: Model abstains from answering the question
Error executing query 1357: Invalid expression / Unexpected token. Line 1, Col: 812.
  ion of scoliosis in the spine on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 1358: Model abstains from answering the question
Error executing query 1359: Invalid expression / Unexpected token. Line 1, Col: 868.
  nth') = datetime('2105-12-31 23:59:00','start of month','-1 month') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1360: Model abstains from answering the question
Error executing query 1361: Model abstains from answering the question
Error executing query 1362: Model abstains from answering the question
Error executing query 1363: Model abstains from answering the question
Error executing query 1366: Invalid expression / Unexpected token. Line 1, Col: 860.
  id = 10578743 ) and strftime('%Y',diagnoses_icd.charttime) = '2105' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1367: Invalid expression / Unexpected token. Line 1, Col: 872.
  d = 15110303 ) and strftime('%Y',procedures_icd.charttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1369: Model abstains from answering the question
Error executing query 1370: Invalid expression / Unexpected token. Line 1, Col: 789.
   a chest x-ray reveal any mediastinal widening?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1371: Model only answers one image question SQLs
Error executing query 1372: Model abstains from answering the question
Error executing query 1374: Model abstains from answering the question
Error executing query 1375: Model only answers one image question SQLs
Error executing query 1377: Model only answers one image question SQLs
Error executing query 1380: Invalid expression / Unexpected token. Line 1, Col: 1010.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1383: Invalid expression / Unexpected token. Line 1, Col: 990.
  vealing any anatomical findings in the trachea?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
[False]
Error executing query 1386: Model abstains from answering the question
Error executing query 1387: Invalid expression / Unexpected token. Line 1, Col: 873.
  d = 15546321 ) and strftime('%Y',procedures_icd.charttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1389: Invalid expression / Unexpected token. Line 1, Col: 658.
  ray reveal any devices in the right chest wall?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1392: Model abstains from answering the question
Error executing query 1393: Invalid expression / Unexpected token. Line 1, Col: 875.
   airspace opacity in the left hilar structures?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1394: Invalid expression / Unexpected token. Line 1, Col: 955.
  etime('2105-12-31 23:59:00','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id
Error executing query 1396: Model abstains from answering the question
Error executing query 1398: Model only answers one image question SQLs
Error executing query 1399: Model abstains from answering the question
Error executing query 1400: Invalid expression / Unexpected token. Line 1, Col: 772.
  synthetic substitute, open approach' ) ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
Error executing query 1401: Model abstains from answering the question
Error executing query 1402: Model abstains from answering the question
Error executing query 1403: Invalid expression / Unexpected token. Line 1, Col: 900.
  indicated in the upper mediastinum on an x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1404: Model abstains from answering the question
Error executing query 1405: Model only answers one image question SQLs
Error executing query 1406: Model abstains from answering the question
Error executing query 1409: Model only answers one image question SQLs
Error executing query 1410: Model abstains from answering the question
Error executing query 1411: Invalid expression / Unexpected token. Line 1, Col: 754.
  qa("does a chest x-ray depicts any tubes/lines?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 1414: Model only answers one image question SQLs
Error executing query 1417: Model only answers one image question SQLs
Error executing query 1419: Model abstains from answering the question
Error executing query 1422: Invalid expression / Unexpected token. Line 1, Col: 730.
  a chest x-ray showing mediastinal displacement?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1423: Model abstains from answering the question
Error executing query 1425: Model abstains from answering the question
Error executing query 1428: Model abstains from answering the question
Error executing query 1429: Model abstains from answering the question
Error executing query 1430: Model only answers one image question SQLs
Error executing query 1433: Invalid expression / Unexpected token. Line 1, Col: 626.
  qa("does a chest x-ray depicts any abnormality?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1434: Model abstains from answering the question
Error executing query 1436: Model only answers one image question SQLs
Error executing query 1437: Model only answers one image question SQLs
Error executing query 1438: Model only answers one image question SQLs
Error executing query 1440: Invalid expression / Unexpected token. Line 1, Col: 737.
  6505791 ) and strftime('%Y-%m',prescriptions.starttime) = '2105-12' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1442: Invalid expression / Unexpected token. Line 1, Col: 809.
  eal any abnormality in the cavoatrial junction?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 1443: Model abstains from answering the question
Error executing query 1444: Model abstains from answering the question
Error executing query 1445: Expecting ). Line 1, Col: 873.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1446: Invalid expression / Unexpected token. Line 1, Col: 990.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1447: Invalid expression / Unexpected token. Line 1, Col: 978.
  cedures_icd.charttime) >= datetime('2105-12-31 23:59:00','-4 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1449: Model abstains from answering the question
Error executing query 1450: Model abstains from answering the question
Error executing query 1451: Invalid expression / Unexpected token. Line 1, Col: 735.
  ns.hadm_id from admissions where admissions.subject_id = 16484690 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1454: Invalid expression / Unexpected token. Line 1, Col: 739.
  d = 15981789 ) and strftime('%Y',prescriptions.starttime) >= '2105' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 1455: Invalid expression / Unexpected token. Line 1, Col: 853.
  r by admissions.admittime desc limit 1 ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of day') = datetime(t2.starttime,'start of day')
Error executing query 1456: Model only answers one image question SQLs
Error executing query 1457: Model abstains from answering the question
Error executing query 1458: Model abstains from answering the question
Error executing query 1460: Model abstains from answering the question
Error executing query 1461: Model abstains from answering the question
Error executing query 1462: Model abstains from answering the question
Error executing query 1463: Model abstains from answering the question
Error executing query 1464: Model only answers one image question SQLs
Error executing query 1465: Model only answers one image question SQLs
Error executing query 1466: Model abstains from answering the question
Error executing query 1467: Model abstains from answering the question
Error executing query 1469: Model abstains from answering the question
Error executing query 1470: Model abstains from answering the question
Error executing query 1471: Model abstains from answering the question
Error executing query 1474: Model abstains from answering the question
Error executing query 1475: Model abstains from answering the question
Error executing query 1477: Model abstains from answering the question
Error executing query 1478: Invalid expression / Unexpected token. Line 1, Col: 1016.
   = 18684692 ) and strftime('%Y',procedures_icd.charttime) >= '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and t1.hadm_id = t3.hadm_id
Error executing query 1479: Expecting ). Line 1, Col: 892.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1480: Model only answers one image question SQLs
Error executing query 1481: Model abstains from answering the question
Error executing query 1482: Expecting ). Line 1, Col: 921.
  etime('2105-12-31 23:59:00','-4 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1483: Expecting ). Line 1, Col: 977.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month') gro
Error executing query 1484: Model abstains from answering the question
Error executing query 1485: Model abstains from answering the question
Error executing query 1486: Model only answers one image question SQLs
Error executing query 1487: Model abstains from answering the question
Error executing query 1488: Model abstains from answering the question
Error executing query 1489: Model abstains from answering the question
Error executing query 1490: Model only answers one image question SQLs
Error executing query 1492: Invalid expression / Unexpected token. Line 1, Col: 891.
  ormality in the left shoulder on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1494: Model abstains from answering the question
Error executing query 1495: Model only answers one image question SQLs
[False]
[False]
Error executing query 1497: Model abstains from answering the question
Error executing query 1498: Invalid expression / Unexpected token. Line 1, Col: 872.
  id = 14097607 ) and strftime('%Y',diagnoses_icd.charttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
[False]
Error executing query 1501: Model only answers one image question SQLs
Error executing query 1504: Model only answers one image question SQLs
Error executing query 1505: Invalid expression / Unexpected token. Line 1, Col: 879.
   = 12864997 ) and strftime('%Y',procedures_icd.charttime) >= '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1506: Model only answers one image question SQLs
Error executing query 1508: Model abstains from answering the question
Error executing query 1509: Model abstains from answering the question
Error executing query 1511: Model abstains from answering the question
Error executing query 1513: Model abstains from answering the question
Error executing query 1516: Model abstains from answering the question
Error executing query 1518: Model only answers one image question SQLs
Error executing query 1519: Model abstains from answering the question
Error executing query 1521: Expecting ). Line 1, Col: 823.
  ime('%Y',labevents.charttime) = '2100' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.itemid ) as t3 where t3.c1 = 4 )
Error executing query 1522: Model abstains from answering the question
Error executing query 1524: Invalid expression / Unexpected token. Line 1, Col: 709.
  '%Y',prescriptions.starttime) = '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1528: Model abstains from answering the question
Error executing query 1531: near "(": syntax error
Error executing query 1533: Expecting ). Line 1, Col: 823.
  '%Y',diagnoses_icd.charttime) = '2105' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1534: Model abstains from answering the question
Error executing query 1535: Invalid expression / Unexpected token. Line 1, Col: 714.
  c_vqa("does a chest x-ray show any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1536: Required keyword: 'expressions' missing for <class 'sqlglot.expressions.Aliases'>. Line 1, Col: 461.
  ratory rate' and d_items.linksto = 'chartevents' ) order by chartevents.charttime desc limit 1 )  ( [4mselect[0m chartevents.valuenum from chartevents where chartevents.stay_id in ( select icustays.stay_id from i
Error executing query 1537: Invalid expression / Unexpected token. Line 1, Col: 991.
  a("does a chest x-ray indicate any tubes/lines?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 1539: Model abstains from answering the question
Error executing query 1540: Model abstains from answering the question
Error executing query 1541: Invalid expression / Unexpected token. Line 1, Col: 749.
  x-ray show any abnormality in the right atrium?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1543: Invalid expression / Unexpected token. Line 1, Col: 989.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1545: Model abstains from answering the question
Error executing query 1546: Model abstains from answering the question
Error executing query 1547: Model only answers one image question SQLs
Error executing query 1550: Invalid expression / Unexpected token. Line 1, Col: 987.
  nth') = datetime('2105-12-31 23:59:00','start of month','-1 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1551: Expecting ). Line 1, Col: 970.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.test_name ) as t3 where t3.c1 = 3
Error executing query 1554: Model abstains from answering the question
Error executing query 1556: Model abstains from answering the question
Error executing query 1557: Model abstains from answering the question
Error executing query 1558: Model abstains from answering the question
Error executing query 1561: Model only answers one image question SQLs
Error executing query 1563: Model abstains from answering the question
Error executing query 1564: Invalid expression / Unexpected token. Line 1, Col: 875.
  d = 16043637 ) and strftime('%Y',procedures_icd.charttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1566: Invalid expression / Unexpected token. Line 1, Col: 904.
  .dischtime is not null order by admissions.admittime desc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1568: Model abstains from answering the question
Error executing query 1571: Model abstains from answering the question
Error executing query 1572: Model abstains from answering the question
Error executing query 1573: Model abstains from answering the question
Error executing query 1575: Model abstains from answering the question
Error executing query 1576: Model abstains from answering the question
Error executing query 1577: Model abstains from answering the question
Error executing query 1578: Model abstains from answering the question
Error executing query 1579: Invalid expression / Unexpected token. Line 1, Col: 930.
  etime('2105-12-31 23:59:00','-4 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1580: Model abstains from answering the question
Error executing query 1582: Model only answers one image question SQLs
Error executing query 1584: Invalid expression / Unexpected token. Line 1, Col: 968.
  dures_icd.charttime) >= datetime('2105-12-31 23:59:00','-51 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1585: Model only answers one image question SQLs
Error executing query 1587: Model only answers one image question SQLs
Error executing query 1588: Model only answers one image question SQLs
Error executing query 1589: Model only answers one image question SQLs
Error executing query 1590: Model only answers one image question SQLs
Error executing query 1591: Model abstains from answering the question
Error executing query 1592: Model only answers one image question SQLs
Error executing query 1593: Model abstains from answering the question
Error executing query 1594: Invalid expression / Unexpected token. Line 1, Col: 995.
   year','-0 year') and strftime('%m',prescriptions.starttime) = '06' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1595: Invalid expression / Unexpected token. Line 1, Col: 858.
   year') = datetime('2105-12-31 23:59:00','start of year','-0 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 1596: Model only answers one image question SQLs
Error executing query 1598: Invalid expression / Unexpected token. Line 1, Col: 896.
   = 18246211 ) and strftime('%Y',procedures_icd.charttime) >= '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1600: Invalid expression / Unexpected token. Line 1, Col: 895.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id
Error executing query 1601: Model only answers one image question SQLs
Error executing query 1603: Invalid expression / Unexpected token. Line 1, Col: 1017.
  .dischtime is not null order by admissions.admittime desc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1604: Model abstains from answering the question
Error executing query 1606: Model abstains from answering the question
Error executing query 1609: Model abstains from answering the question
Error executing query 1610: Invalid expression / Unexpected token. Line 1, Col: 779.
  ns.hadm_id from admissions where admissions.subject_id = 13778342 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1611: Expecting ). Line 1, Col: 815.
  etime('2105-12-31 23:59:00','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 3
Error executing query 1612: Invalid expression / Unexpected token. Line 1, Col: 879.
  iagnoses_icd.charttime) = datetime('2105-12-31 23:59:00','-2 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1613: Model abstains from answering the question
Error executing query 1614: Model abstains from answering the question
Error executing query 1616: Model abstains from answering the question
Error executing query 1617: Model abstains from answering the question
Error executing query 1618: Model abstains from answering the question
Error executing query 1620: Invalid expression / Unexpected token. Line 1, Col: 760.
  d = 17598348 ) and strftime('%Y',prescriptions.starttime) >= '2104' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 1621: Invalid expression / Unexpected token. Line 1, Col: 851.
  2601162 ) and strftime('%Y-%m',diagnoses_icd.charttime) = '2105-05' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1622: Expecting ). Line 1, Col: 709.
  ogyevents.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.spec_type_desc ) as t3 where t3.c1 = 3
Error executing query 1623: Model abstains from answering the question
Error executing query 1624: Invalid expression / Unexpected token. Line 1, Col: 722.
  '%Y',prescriptions.starttime) = '2102' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id
Error executing query 1625: Model abstains from answering the question
Error executing query 1626: Model abstains from answering the question
Error executing query 1627: Invalid expression / Unexpected token. Line 1, Col: 849.
  442326 ) and strftime('%Y-%m',procedures_icd.charttime) = '2102-04' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1629: Model only answers one image question SQLs
Error executing query 1630: Invalid expression / Unexpected token. Line 1, Col: 942.
  etime('2105-12-31 23:59:00','-3 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1632: Invalid expression / Unexpected token. Line 1, Col: 731.
  d = 11184688 ) and strftime('%Y',prescriptions.starttime) >= '2105' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 1634: Model only answers one image question SQLs
Error executing query 1636: Model abstains from answering the question
Error executing query 1640: Model abstains from answering the question
[False]
[False]
Error executing query 1644: Model only answers one image question SQLs
Error executing query 1648: Model abstains from answering the question
Error executing query 1649: Model abstains from answering the question
Error executing query 1650: Expecting ). Line 1, Col: 801.
  microbiologyevents.charttime) = '2103' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 1651: Model abstains from answering the question
Error executing query 1652: Model abstains from answering the question
Error executing query 1654: Model only answers one image question SQLs
Error executing query 1655: Model abstains from answering the question
Error executing query 1656: Model abstains from answering the question
Error executing query 1659: Expecting ). Line 1, Col: 757.
  %Y',prescriptions.starttime) >= '2102' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1661: Model abstains from answering the question
Error executing query 1662: Model abstains from answering the question
Error executing query 1664: Model abstains from answering the question
Error executing query 1665: Model abstains from answering the question
Error executing query 1667: Invalid expression / Unexpected token. Line 1, Col: 954.
  ascular congestion in the left upper lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1669: Model only answers one image question SQLs
Error executing query 1670: Expecting ). Line 1, Col: 1211.
  limit 1 ) order by tb_cxr.studydatetime desc limit 1 ) ) ) order by tb_cxr.studydatetime desc limit [4m1[0m
Error executing query 1672: Model only answers one image question SQLs
Error executing query 1673: Model abstains from answering the question
Error executing query 1674: Model abstains from answering the question
Error executing query 1676: Model only answers one image question SQLs
Error executing query 1677: Model abstains from answering the question
Error executing query 1678: Model abstains from answering the question
Error executing query 1679: Model only answers one image question SQLs
Error executing query 1681: Model abstains from answering the question
Error executing query 1682: Model abstains from answering the question
Error executing query 1684: Invalid expression / Unexpected token. Line 1, Col: 825.
  rescriptions.starttime) = datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1686: Model abstains from answering the question
Error executing query 1687: Invalid expression / Unexpected token. Line 1, Col: 919.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
Error executing query 1688: Model only answers one image question SQLs
Error executing query 1689: Expecting ). Line 1, Col: 767.
  icrobiologyevents.charttime) >= '2101' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1690: near "(": syntax error
Error executing query 1691: Model abstains from answering the question
Error executing query 1692: Invalid expression / Unexpected token. Line 1, Col: 632.
  a("does a chest x-ray indicate any abnormality?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1694: Model only answers one image question SQLs
Error executing query 1695: Model abstains from answering the question
Error executing query 1696: Invalid expression / Unexpected token. Line 1, Col: 984.
  ng any abnormality in the left upper lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1697: Model only answers one image question SQLs
Error executing query 1698: Model abstains from answering the question
Error executing query 1700: Model abstains from answering the question
Error executing query 1701: Model abstains from answering the question
Error executing query 1702: Model abstains from answering the question
Error executing query 1703: Model abstains from answering the question
Error executing query 1704: Model only answers one image question SQLs
Error executing query 1705: Invalid expression / Unexpected token. Line 1, Col: 621.
  func_vqa("is a chest x-ray showing cyst/bullae?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1706: Model only answers one image question SQLs
Error executing query 1708: Model abstains from answering the question
Error executing query 1711: Model abstains from answering the question
Error executing query 1712: Model abstains from answering the question
Error executing query 1713: Model abstains from answering the question
Error executing query 1716: Model abstains from answering the question
Error executing query 1717: Invalid expression / Unexpected token. Line 1, Col: 1006.
  769040 ) and strftime('%Y-%m',procedures_icd.charttime) = '2102-03' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and t1.hadm_id = t3.hadm_id
Error executing query 1718: Model only answers one image question SQLs
Error executing query 1719: Model only answers one image question SQLs
Error executing query 1720: Model only answers one image question SQLs
Error executing query 1722: Invalid expression / Unexpected token. Line 1, Col: 870.
  ("is the chest x-ray depicting any tubes/lines?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1723: Model abstains from answering the question
Error executing query 1724: Model only answers one image question SQLs
Error executing query 1726: Model abstains from answering the question
Error executing query 1728: Model abstains from answering the question
Error executing query 1729: Model abstains from answering the question
Error executing query 1731: Invalid expression / Unexpected token. Line 1, Col: 851.
  c_vqa("is the chest x-ray revealing chest port?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1732: Model abstains from answering the question
Error executing query 1734: Model abstains from answering the question
Error executing query 1735: Model abstains from answering the question
Error executing query 1736: Model only answers one image question SQLs
Error executing query 1737: Model abstains from answering the question
Error executing query 1739: Model abstains from answering the question
Error executing query 1743: Model abstains from answering the question
Error executing query 1744: Model abstains from answering the question
Error executing query 1745: Model abstains from answering the question
Error executing query 1746: Invalid expression / Unexpected token. Line 1, Col: 850.
  vqa("is a chest x-ray detecting enlarged hilum?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1749: Model abstains from answering the question
Error executing query 1751: Model abstains from answering the question
Error executing query 1754: Model abstains from answering the question
Error executing query 1755: Invalid expression / Unexpected token. Line 1, Col: 782.
   func_vqa("does a chest x-ray show any devices?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 1758: Invalid expression / Unexpected token. Line 1, Col: 901.
  d = 18679317 ) and strftime('%Y',diagnoses_icd.charttime) >= '2105' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1763: Model abstains from answering the question
Error executing query 1765: Model only answers one image question SQLs
Error executing query 1766: Model abstains from answering the question
Error executing query 1768: Model abstains from answering the question
Error executing query 1769: Model only answers one image question SQLs
Error executing query 1770: Model only answers one image question SQLs
Error executing query 1771: Model abstains from answering the question
Error executing query 1775: Model only answers one image question SQLs
Error executing query 1777: Model abstains from answering the question
Error executing query 1779: Expecting ). Line 1, Col: 894.
  etime('2105-12-31 23:59:00','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1780: Model abstains from answering the question
Error executing query 1781: Model abstains from answering the question
Error executing query 1782: Invalid expression / Unexpected token. Line 1, Col: 667.
   in the left hilar structures on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
[True]
Error executing query 1784: Model abstains from answering the question
Error executing query 1785: Invalid expression / Unexpected token. Line 1, Col: 868.
  ting any tubes/lines in the left mid lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1787: Invalid expression / Unexpected token. Line 1, Col: 782.
  ns.hadm_id from admissions where admissions.subject_id = 19265525 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1788: Model only answers one image question SQLs
Error executing query 1789: Expecting ). Line 1, Col: 885.
  etime('2105-12-31 23:59:00','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 4
Error executing query 1790: Model abstains from answering the question
Error executing query 1791: Invalid expression / Unexpected token. Line 1, Col: 764.
  r by admissions.admittime desc limit 1 ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of day') = datetime(t2.starttime,'start of day')
Error executing query 1792: Model abstains from answering the question
Error executing query 1794: Model abstains from answering the question
Error executing query 1795: Model abstains from answering the question
Error executing query 1797: Model abstains from answering the question
Error executing query 1798: Invalid expression / Unexpected token. Line 1, Col: 858.
  d = 18961402 ) and strftime('%Y',diagnoses_icd.charttime) >= '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1801: Invalid expression / Unexpected token. Line 1, Col: 729.
  ns.hadm_id from admissions where admissions.subject_id = 11266631 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1802: Model only answers one image question SQLs
Error executing query 1803: Model abstains from answering the question
Error executing query 1804: Model abstains from answering the question
[True]
Error executing query 1807: Model only answers one image question SQLs
Error executing query 1808: Invalid expression / Unexpected token. Line 1, Col: 953.
   shown any abnormality in the right chest wall?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 1809: Model abstains from answering the question
Error executing query 1812: Invalid expression / Unexpected token. Line 1, Col: 854.
  nc_vqa("is a chest x-ray detecting any devices?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 1813: Invalid expression / Unexpected token. Line 1, Col: 938.
   = 14641317 ) and strftime('%Y',procedures_icd.charttime) >= '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1814: Model abstains from answering the question
Error executing query 1815: Model only answers one image question SQLs
Error executing query 1816: Model abstains from answering the question
Error executing query 1817: Model abstains from answering the question
Error executing query 1818: Model only answers one image question SQLs
Error executing query 1820: Invalid expression / Unexpected token. Line 1, Col: 880.
  23:59:00','start of month','-1 month') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of day') = datetime(t2.starttime,'start of day')
Error executing query 1821: Model only answers one image question SQLs
Error executing query 1823: Invalid expression / Unexpected token. Line 1, Col: 764.
  eveal lung cancer in the left hilar structures?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 1829: Invalid expression / Unexpected token. Line 1, Col: 731.
  est x-ray showing fluid overload/heart failure?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1831: Model abstains from answering the question
[False]
[False]
Error executing query 1836: Model abstains from answering the question
Error executing query 1837: Model abstains from answering the question
Error executing query 1838: Model only answers one image question SQLs
Error executing query 1840: Invalid expression / Unexpected token. Line 1, Col: 999.
  d = 15712372 ) and strftime('%Y',diagnoses_icd.charttime) >= '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1841: Model abstains from answering the question
Error executing query 1842: Model abstains from answering the question
Error executing query 1843: Model only answers one image question SQLs
Error executing query 1844: Invalid expression / Unexpected token. Line 1, Col: 924.
  d = 12907424 ) and strftime('%Y',procedures_icd.charttime) = '2100' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1847: Invalid expression / Unexpected token. Line 1, Col: 754.
  s a chest x-ray showing vascular calcification?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 1848: Invalid expression / Unexpected token. Line 1, Col: 923.
  qa("is a chest x-ray detecting any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
[False]
Error executing query 1850: Model abstains from answering the question
Error executing query 1851: Model only answers one image question SQLs
Error executing query 1852: Model only answers one image question SQLs
Error executing query 1854: Model abstains from answering the question
Error executing query 1857: Model abstains from answering the question
Error executing query 1858: Model only answers one image question SQLs
Error executing query 1859: Model abstains from answering the question
Error executing query 1861: Model abstains from answering the question
Error executing query 1863: Model only answers one image question SQLs
Error executing query 1865: Model abstains from answering the question
Error executing query 1866: Model abstains from answering the question
Error executing query 1867: Invalid expression / Unexpected token. Line 1, Col: 772.
  evealed in the right shoulder on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1868: Model abstains from answering the question
Error executing query 1870: Model only answers one image question SQLs
Error executing query 1871: Invalid expression / Unexpected token. Line 1, Col: 771.
  3710683 ) and strftime('%Y-%m',prescriptions.starttime) = '2105-08' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1873: Expecting ). Line 1, Col: 978.
  etime('2105-12-31 23:59:00','-3 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1874: Model abstains from answering the question
Error executing query 1876: Model abstains from answering the question
Error executing query 1877: Model abstains from answering the question
Error executing query 1878: Model only answers one image question SQLs
Error executing query 1881: Invalid expression / Unexpected token. Line 1, Col: 878.
  d = 18380697 ) and strftime('%Y',diagnoses_icd.charttime) >= '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1882: Model abstains from answering the question
Error executing query 1883: Model only answers one image question SQLs
Error executing query 1885: Expecting ). Line 1, Col: 826.
  microbiologyevents.charttime) = '2102' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1886: Model abstains from answering the question
Error executing query 1887: Invalid expression / Unexpected token. Line 1, Col: 825.
  enchymal scarring in the left hilar structures?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1888: Model only answers one image question SQLs
Error executing query 1889: Model only answers one image question SQLs
Error executing query 1891: Model only answers one image question SQLs
Error executing query 1892: Model abstains from answering the question
Error executing query 1894: Invalid expression / Unexpected token. Line 1, Col: 897.
  .dischtime is not null order by admissions.admittime desc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1896: Model abstains from answering the question
Error executing query 1897: Invalid expression / Unexpected token. Line 1, Col: 848.
  "does a chest x-ray reveal any any abnormality?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 1898: Invalid expression / Unexpected token. Line 1, Col: 728.
  vqa("does the chest x-ray indicate cabg grafts?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 1899: Model abstains from answering the question
Error executing query 1900: Model abstains from answering the question
Error executing query 1902: Model abstains from answering the question
Error executing query 1904: Model abstains from answering the question
Error executing query 1906: Model abstains from answering the question
Error executing query 1907: Expecting ). Line 1, Col: 773.
  icrobiologyevents.charttime) >= '2103' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
[False]
[False]
Error executing query 1910: Expecting ). Line 1, Col: 766.
  '%Y',prescriptions.starttime) = '2101' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 3
Error executing query 1912: Model only answers one image question SQLs
Error executing query 1913: Invalid expression / Unexpected token. Line 1, Col: 862.
  w shoulder osteoarthritis in the left clavicle?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1914: Model abstains from answering the question
Error executing query 1917: near "(": syntax error
Error executing query 1918: Model abstains from answering the question
Error executing query 1920: Invalid expression / Unexpected token. Line 1, Col: 887.
  etime('2105-12-31 23:59:00','-4 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1921: Model abstains from answering the question
Error executing query 1924: near "(": syntax error
Error executing query 1925: Model only answers one image question SQLs
Error executing query 1928: Invalid expression / Unexpected token. Line 1, Col: 817.
  re func_vqa("has an x-ray revealed cabg grafts?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1929: Model abstains from answering the question
Error executing query 1932: Model only answers one image question SQLs
Error executing query 1933: Model only answers one image question SQLs
Error executing query 1935: Model abstains from answering the question
Error executing query 1937: Invalid expression / Unexpected token. Line 1, Col: 775.
  ns.hadm_id from admissions where admissions.subject_id = 11553072 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1938: Model abstains from answering the question
Error executing query 1939: Model only answers one image question SQLs
Error executing query 1940: Model abstains from answering the question
Error executing query 1941: Invalid expression / Unexpected token. Line 1, Col: 882.
  iagnoses_icd.charttime) = datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1942: Model abstains from answering the question
Error executing query 1944: Model abstains from answering the question
Error executing query 1945: Model abstains from answering the question
Error executing query 1946: Model only answers one image question SQLs
Error executing query 1947: Model only answers one image question SQLs
[False]
Error executing query 1953: Model abstains from answering the question
Error executing query 1954: Model abstains from answering the question
Error executing query 1955: Model abstains from answering the question
[True]
Error executing query 1957: Model abstains from answering the question
Error executing query 1958: Invalid expression / Unexpected token. Line 1, Col: 908.
  al any abnormality in the left upper lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
[True]
Error executing query 1959: near "(": syntax error
Error executing query 1960: Model abstains from answering the question
Error executing query 1961: Model abstains from answering the question
Error executing query 1962: Model abstains from answering the question
Error executing query 1963: Model abstains from answering the question
Error executing query 1964: Model only answers one image question SQLs
Error executing query 1965: Invalid expression / Unexpected token. Line 1, Col: 783.
  escriptions.starttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 1966: Model abstains from answering the question
Error executing query 1967: Model abstains from answering the question
Error executing query 1968: Model abstains from answering the question
Error executing query 1969: Invalid expression / Unexpected token. Line 1, Col: 754.
  func_vqa("has a chest x-ray shown any diseases?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 1971: Model abstains from answering the question
Error executing query 1973: Expecting ). Line 1, Col: 928.
  etime('2105-12-31 23:59:00','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month') gro
Error executing query 1974: Model abstains from answering the question
Error executing query 1976: Model abstains from answering the question
Error executing query 1977: Invalid expression / Unexpected token. Line 1, Col: 838.
  d = 19025961 ) and strftime('%Y',procedures_icd.charttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1979: Model abstains from answering the question
Error executing query 1980: Model abstains from answering the question
Error executing query 1981: Expecting ). Line 1, Col: 712.
  ogyevents.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.test_name ) as t3 where t3.c1 = 4
Error executing query 1983: Model abstains from answering the question
Error executing query 1986: Invalid expression / Unexpected token. Line 1, Col: 887.
  "does an x-ray reveal any diseases in the neck?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 1987: Model only answers one image question SQLs
Error executing query 1989: Invalid expression / Unexpected token. Line 1, Col: 886.
  mality in the left chest wall on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1990: Invalid expression / Unexpected token. Line 1, Col: 762.
  319241 ) and strftime('%Y-%m',prescriptions.starttime) >= '2105-07' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1991: Model abstains from answering the question
Error executing query 1992: Model only answers one image question SQLs
Error executing query 1993: Model abstains from answering the question
Error executing query 1996: Model only answers one image question SQLs
Error executing query 1998: Expecting ). Line 1, Col: 692.
  criptions.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 4
Error executing query 1999: Invalid expression / Unexpected token. Line 1, Col: 869.
   = 17454400 ) and strftime('%Y',procedures_icd.charttime) >= '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2000: Model abstains from answering the question
Error executing query 2001: Model only answers one image question SQLs
Error executing query 2003: Invalid expression / Unexpected token. Line 1, Col: 938.
  nc_vqa("does a chest x-ray depicts any devices?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 2004: Expecting ). Line 1, Col: 903.
  %Y',diagnoses_icd.charttime) >= '2101' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 2008: Model only answers one image question SQLs
Error executing query 2009: Invalid expression / Unexpected token. Line 1, Col: 841.
  qa("is pleural effusion shown on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2010: Model abstains from answering the question
Error executing query 2011: Model only answers one image question SQLs
Error executing query 2012: Model abstains from answering the question
Error executing query 2013: Invalid expression / Unexpected token. Line 1, Col: 909.
  398915 ) and strftime('%Y-%m',procedures_icd.charttime) = '2104-10' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2015: Invalid expression / Unexpected token. Line 1, Col: 762.
  nstrated any abnormality in the right shoulder?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2016: Expecting ). Line 1, Col: 805.
  '%Y',prescriptions.starttime) = '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 3
Error executing query 2018: Model abstains from answering the question
Error executing query 2019: Model only answers one image question SQLs
Error executing query 2020: Model only answers one image question SQLs
Error executing query 2021: Model abstains from answering the question
Error executing query 2022: Model abstains from answering the question
Error executing query 2024: Invalid expression / Unexpected token. Line 1, Col: 909.
  ocedures_icd.charttime) = datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2025: Model abstains from answering the question
Error executing query 2026: Model abstains from answering the question
Error executing query 2027: Model abstains from answering the question
Error executing query 2028: Model abstains from answering the question
Error executing query 2031: Model abstains from answering the question
[False]
Error executing query 2037: Model only answers one image question SQLs
Error executing query 2038: Model only answers one image question SQLs
Error executing query 2039: Model only answers one image question SQLs
Error executing query 2040: Invalid expression / Unexpected token. Line 1, Col: 971.
  nc_vqa("does a chest x-ray show tortuous aorta?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2041: Model abstains from answering the question
Error executing query 2042: Model only answers one image question SQLs
Error executing query 2043: Invalid expression / Unexpected token. Line 1, Col: 906.
  re func_vqa("has an x-ray revealed any devices?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2045: Model abstains from answering the question
Error executing query 2046: Invalid expression / Unexpected token. Line 1, Col: 855.
  d = 17135436 ) and strftime('%Y',procedures_icd.charttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2048: Model only answers one image question SQLs
Error executing query 2049: Model only answers one image question SQLs
Error executing query 2050: Invalid expression / Unexpected token. Line 1, Col: 809.
  ',prescriptions.starttime) = '2101-05' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of day') = datetime(t2.starttime,'start of day')
Error executing query 2051: Expecting ). Line 1, Col: 1025.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 2052: Model only answers one image question SQLs
Error executing query 2054: Invalid expression / Unexpected token. Line 1, Col: 869.
  id = 18429309 ) and strftime('%Y',diagnoses_icd.charttime) = '2102' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2056: Expecting ). Line 1, Col: 845.
  etime('2105-12-31 23:59:00','-4 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 2059: Model abstains from answering the question
Error executing query 2060: Model abstains from answering the question
Error executing query 2061: Model abstains from answering the question
Error executing query 2062: Expecting ). Line 1, Col: 798.
  dures_icd.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.icd_code ) as t3 where t3.c1 = 4 )
Error executing query 2063: Model abstains from answering the question
Error executing query 2064: Model only answers one image question SQLs
Error executing query 2065: Expecting ). Line 1, Col: 784.
  microbiologyevents.charttime) = '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 2066: Model abstains from answering the question
Error executing query 2067: Invalid expression / Unexpected token. Line 1, Col: 843.
  id = 16419341 ) and strftime('%Y',diagnoses_icd.charttime) = '2101' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2068: Expecting ). Line 1, Col: 779.
  microbiologyevents.charttime) = '2101' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 2069: Model abstains from answering the question
Error executing query 2072: Model only answers one image question SQLs
Error executing query 2073: Invalid expression / Unexpected token. Line 1, Col: 916.
  es/lines in the left clavicle on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2074: Invalid expression / Unexpected token. Line 1, Col: 936.
  c_vqa("has a chest x-ray shown any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2075: Invalid expression / Unexpected token. Line 1, Col: 755.
   func_vqa("has a chest x-ray shown cabg grafts?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2076: Invalid expression / Unexpected token. Line 1, Col: 865.
  nc_vqa("has an x-ray indicated any tubes/lines?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2077: Model abstains from answering the question
Error executing query 2080: Model abstains from answering the question
Error executing query 2081: Invalid expression / Unexpected token. Line 1, Col: 747.
  ',prescriptions.starttime) = '2105-04' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of day') = datetime(t2.starttime,'start of day')
Error executing query 2083: Model abstains from answering the question
Error executing query 2085: Model only answers one image question SQLs
Error executing query 2089: Expecting ). Line 1, Col: 893.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 2090: Invalid expression / Unexpected token. Line 1, Col: 917.
  047039 ) and strftime('%Y-%m',procedures_icd.charttime) = '2105-04' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2091: Model abstains from answering the question
Error executing query 2093: Model abstains from answering the question
Error executing query 2096: Model abstains from answering the question
Error executing query 2097: Model abstains from answering the question
Error executing query 2098: Model abstains from answering the question
Error executing query 2100: Model abstains from answering the question
Error executing query 2101: Model abstains from answering the question
Error executing query 2102: Model only answers one image question SQLs
Error executing query 2104: Invalid expression / Unexpected token. Line 1, Col: 786.
  ns.hadm_id from admissions where admissions.subject_id = 14873669 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2105: Invalid expression / Unexpected token. Line 1, Col: 812.
  s any anatomical findings in the left clavicle?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2108: Model abstains from answering the question
Error executing query 2110: Model abstains from answering the question
Error executing query 2111: Invalid expression / Unexpected token. Line 1, Col: 631.
  t x-ray showing any diseases in the right lung?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 2112: Model abstains from answering the question
Error executing query 2114: Model abstains from answering the question
Error executing query 2115: Model only answers one image question SQLs
Error executing query 2116: Model only answers one image question SQLs
Error executing query 2117: Model abstains from answering the question
Error executing query 2119: Model abstains from answering the question
Error executing query 2120: Expecting ). Line 1, Col: 982.
  e prescriptions.drug = 'nortriptyline' ) as t3 on t2.subject_id = t3.subject_id where t2.charttime  [4mt3[0m.starttime ) as t4 join patients on t4.subject_id = patients.subject_id
Error executing query 2122: Model only answers one image question SQLs
Error executing query 2123: Model only answers one image question SQLs
Error executing query 2125: Model only answers one image question SQLs
Error executing query 2126: Model abstains from answering the question
Error executing query 2127: Model abstains from answering the question
Error executing query 2128: Model abstains from answering the question
Error executing query 2129: Model only answers one image question SQLs
Error executing query 2130: Model only answers one image question SQLs
Error executing query 2131: Model abstains from answering the question
Error executing query 2132: Model only answers one image question SQLs
Error executing query 2133: Invalid expression / Unexpected token. Line 1, Col: 1026.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2134: Expecting ). Line 1, Col: 1000.
  where prescriptions.drug = 'trazodone' ) as t3 on t2.subject_id = t3.subject_id where t2.charttime  [4mt3[0m.starttime ) as t4 join patients on t4.subject_id = patients.subject_id
Error executing query 2135: Model only answers one image question SQLs
Error executing query 2136: Model abstains from answering the question
Error executing query 2139: Model abstains from answering the question
Error executing query 2140: Model abstains from answering the question
Error executing query 2141: Model only answers one image question SQLs
Error executing query 2144: Model abstains from answering the question
Error executing query 2145: Model only answers one image question SQLs
Error executing query 2147: Model abstains from answering the question
Error executing query 2149: Model abstains from answering the question
Error executing query 2151: Invalid expression / Unexpected token. Line 1, Col: 886.
  .dischtime is not null order by admissions.admittime desc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2152: Model abstains from answering the question
Error executing query 2153: Invalid expression / Unexpected token. Line 1, Col: 868.
   = 19398915 ) and strftime('%Y',procedures_icd.charttime) >= '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2154: Invalid expression / Unexpected token. Line 1, Col: 744.
  ns.hadm_id from admissions where admissions.subject_id = 19311478 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2155: Invalid expression / Unexpected token. Line 1, Col: 996.
  d = 19022436 ) and strftime('%Y',procedures_icd.charttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and t1.hadm_id = t3.hadm_id
Error executing query 2157: Invalid expression / Unexpected token. Line 1, Col: 920.
  y show any abnormality in the right chest wall?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2159: Model abstains from answering the question
Error executing query 2160: Model only answers one image question SQLs
Error executing query 2161: Model abstains from answering the question
Error executing query 2162: Model abstains from answering the question
Error executing query 2164: Invalid expression / Unexpected token. Line 1, Col: 882.
  d = 12612379 ) and strftime('%Y',procedures_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2165: Model abstains from answering the question
Error executing query 2166: Model abstains from answering the question
Error executing query 2168: Invalid expression / Unexpected token. Line 1, Col: 740.
  975155 ) and strftime('%Y-%m',prescriptions.starttime) >= '2105-02' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2169: Model abstains from answering the question
Error executing query 2170: Expecting ). Line 1, Col: 843.
  etime('2105-12-31 23:59:00','-5 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 2171: Model abstains from answering the question
Error executing query 2173: Expecting ). Line 1, Col: 833.
  icrobiologyevents.charttime) >= '2105' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.spec_type_desc ) as t3 where t3.c1 = 3
Error executing query 2174: Invalid expression / Unexpected token. Line 1, Col: 720.
  c_vqa("does a chest x-ray show any tubes/lines?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 2175: Model only answers one image question SQLs
Error executing query 2176: Model abstains from answering the question
Error executing query 2177: Model abstains from answering the question
Error executing query 2178: Model abstains from answering the question
Error executing query 2179: Model abstains from answering the question
Error executing query 2181: Model abstains from answering the question
Error executing query 2182: Model abstains from answering the question
Error executing query 2183: Model abstains from answering the question
Error executing query 2186: Model abstains from answering the question
Error executing query 2188: Model abstains from answering the question
Error executing query 2189: Model abstains from answering the question
Error executing query 2191: Model only answers one image question SQLs
Error executing query 2192: Model abstains from answering the question
Error executing query 2195: Expecting ). Line 1, Col: 747.
  noses_icd.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 2196: Model only answers one image question SQLs
Error executing query 2197: Model abstains from answering the question
Error executing query 2205: Expecting ). Line 1, Col: 839.
  %Y',prescriptions.starttime) >= '2103' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 2206: Model only answers one image question SQLs
Error executing query 2207: Model abstains from answering the question
Error executing query 2208: Model abstains from answering the question
Error executing query 2209: Model only answers one image question SQLs
Error executing query 2212: Model abstains from answering the question
Error executing query 2213: Model abstains from answering the question
Error executing query 2214: Model abstains from answering the question
Error executing query 2217: Model only answers one image question SQLs
Error executing query 2218: Model abstains from answering the question
Error executing query 2219: Model abstains from answering the question
[False]
Error executing query 2222: Expecting ). Line 1, Col: 907.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 2223: Model abstains from answering the question
Error executing query 2224: Model abstains from answering the question
Error executing query 2226: Model abstains from answering the question
Error executing query 2227: Model only answers one image question SQLs
Error executing query 2228: Invalid expression / Unexpected token. Line 1, Col: 841.
  d = 17598348 ) and strftime('%Y',diagnoses_icd.charttime) >= '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2230: Model abstains from answering the question
Error executing query 2231: Invalid expression / Unexpected token. Line 1, Col: 955.
  nth') = datetime('2105-12-31 23:59:00','start of month','-0 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2235: Invalid expression / Unexpected token. Line 1, Col: 739.
  ',prescriptions.starttime) = '2101-05' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of day') = datetime(t2.starttime,'start of day')
Error executing query 2236: Model abstains from answering the question
Error executing query 2237: Model abstains from answering the question
Error executing query 2238: Model abstains from answering the question
Error executing query 2239: Model only answers one image question SQLs
Error executing query 2240: Model abstains from answering the question
Error executing query 2241: Model only answers one image question SQLs
Error executing query 2242: Invalid expression / Unexpected token. Line 1, Col: 871.
  y technical assessments shown on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2243: Model abstains from answering the question
Error executing query 2244: Model abstains from answering the question
Error executing query 2245: Invalid expression / Unexpected token. Line 1, Col: 851.
  ted any technical assessments in the left lung?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2247: Model abstains from answering the question
Error executing query 2248: Model abstains from answering the question
Error executing query 2249: Model only answers one image question SQLs
Error executing query 2250: Invalid expression / Unexpected token. Line 1, Col: 970.
   year','-1 year') and strftime('%m',prescriptions.starttime) = '04' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2251: Model abstains from answering the question
Error executing query 2252: Invalid expression / Unexpected token. Line 1, Col: 654.
  lar calcification in the left hilar structures?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 2253: Model only answers one image question SQLs
Error executing query 2256: Model abstains from answering the question
[False]
Error executing query 2262: Invalid expression / Unexpected token. Line 1, Col: 880.
  etime('2105-12-31 23:59:00','-4 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
Error executing query 2263: Expecting ). Line 1, Col: 969.
  where prescriptions.drug = 'ezetimibe' ) as t3 on t2.subject_id = t3.subject_id where t2.charttime  [4mt3[0m.starttime ) as t4 join patients on t4.subject_id = patients.subject_id
Error executing query 2264: Model only answers one image question SQLs
Error executing query 2265: Invalid expression / Unexpected token. Line 1, Col: 704.
  '%Y',prescriptions.starttime) = '2102' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month')
Error executing query 2266: Model abstains from answering the question
Error executing query 2267: Model abstains from answering the question
Error executing query 2269: Model only answers one image question SQLs
Error executing query 2271: Invalid expression / Unexpected token. Line 1, Col: 952.
  c_vqa("is a chest x-ray detecting any diseases?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2272: Model abstains from answering the question
Error executing query 2273: Model abstains from answering the question
Error executing query 2274: Model only answers one image question SQLs
Error executing query 2275: Model abstains from answering the question
Error executing query 2276: Model only answers one image question SQLs
Error executing query 2277: Invalid expression / Unexpected token. Line 1, Col: 923.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 2279: Model abstains from answering the question
Error executing query 2280: Model abstains from answering the question
[True]
Error executing query 2281: near "(": syntax error
Error executing query 2284: Expecting ). Line 1, Col: 986.
   prescriptions.drug = 'nystatin cream' ) as t3 on t2.subject_id = t3.subject_id where t2.charttime  [4mt3[0m.starttime ) as t4 join patients on t4.subject_id = patients.subject_id
Error executing query 2285: Model abstains from answering the question
Error executing query 2286: Expecting ). Line 1, Col: 881.
  '%Y',diagnoses_icd.charttime) = '2101' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 2287: Model only answers one image question SQLs
Error executing query 2288: Model abstains from answering the question
Error executing query 2291: Invalid expression / Unexpected token. Line 1, Col: 757.
  est x-ray shown any diseases in the right lung?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2296: Model abstains from answering the question
Error executing query 2297: Invalid expression / Unexpected token. Line 1, Col: 926.
  agnoses_icd.charttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2298: Invalid expression / Unexpected token. Line 1, Col: 741.
  ns.hadm_id from admissions where admissions.subject_id = 13917190 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2299: Model abstains from answering the question
Error executing query 2300: Invalid expression / Unexpected token. Line 1, Col: 834.
  raeration identified in the left mid lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2304: Model abstains from answering the question
Error executing query 2305: Model abstains from answering the question
Error executing query 2306: Model abstains from answering the question
Error executing query 2307: Model abstains from answering the question
Error executing query 2308: Model only answers one image question SQLs
Error executing query 2309: Model abstains from answering the question
Error executing query 2311: Model abstains from answering the question
Error executing query 2312: Invalid expression / Unexpected token. Line 1, Col: 884.
  id = 15346117 ) and strftime('%Y',diagnoses_icd.charttime) = '2105' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2313: Model abstains from answering the question
Error executing query 2315: Expecting ). Line 1, Col: 1034.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 2317: Model only answers one image question SQLs
Error executing query 2318: Model only answers one image question SQLs
Error executing query 2319: Model abstains from answering the question
Error executing query 2320: Model abstains from answering the question
Error executing query 2321: Model only answers one image question SQLs
Error executing query 2322: Model abstains from answering the question
Error executing query 2324: Model abstains from answering the question
Error executing query 2325: Model abstains from answering the question
Error executing query 2326: Model abstains from answering the question
Error executing query 2327: Invalid expression / Unexpected token. Line 1, Col: 931.
  vqa("is the chest x-ray revealing any diseases?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2328: Model abstains from answering the question
Error executing query 2330: Model abstains from answering the question
Error executing query 2332: Model abstains from answering the question
Error executing query 2334: Model only answers one image question SQLs
Error executing query 2335: Model only answers one image question SQLs
Error executing query 2337: near "(": syntax error
Error executing query 2338: Model abstains from answering the question
Error executing query 2339: Model abstains from answering the question
Error executing query 2341: Model abstains from answering the question
Error executing query 2342: Model only answers one image question SQLs
Error executing query 2343: Model abstains from answering the question
Error executing query 2345: Model abstains from answering the question
Error executing query 2346: Expecting ). Line 1, Col: 1017.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 2347: Invalid expression / Unexpected token. Line 1, Col: 759.
  teric tube in the mediastinum on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2349: Model only answers one image question SQLs
Error executing query 2350: Model only answers one image question SQLs
Error executing query 2351: Model abstains from answering the question
Error executing query 2353: Invalid expression / Unexpected token. Line 1, Col: 892.
  id = 14734513 ) and strftime('%Y',diagnoses_icd.charttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2354: Model only answers one image question SQLs
Error executing query 2355: Model abstains from answering the question
Error executing query 2356: Model abstains from answering the question
Error executing query 2357: Invalid expression / Unexpected token. Line 1, Col: 955.
   any tubes/lines in the right hilar structures?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2358: Model abstains from answering the question
Error executing query 2359: Model abstains from answering the question
Error executing query 2361: Model only answers one image question SQLs
Error executing query 2362: Model only answers one image question SQLs
Error executing query 2363: Model only answers one image question SQLs
Error executing query 2364: Invalid expression / Unexpected token. Line 1, Col: 829.
  id = 19540373 ) and strftime('%Y',diagnoses_icd.charttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2365: Invalid expression / Unexpected token. Line 1, Col: 584.
  where prescriptions.drug ='mesalamine' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month')
Error executing query 2366: Model abstains from answering the question
Error executing query 2367: Model abstains from answering the question
Error executing query 2369: Model only answers one image question SQLs
Error executing query 2371: Model abstains from answering the question
Error executing query 2372: Model abstains from answering the question
Error executing query 2373: Model only answers one image question SQLs
Error executing query 2374: Model abstains from answering the question
Error executing query 2375: Model abstains from answering the question
Error executing query 2377: Invalid expression / Unexpected token. Line 1, Col: 884.
  icated in the left lower lung zone on an x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2379: Model abstains from answering the question
Error executing query 2380: Model abstains from answering the question
[True]
Error executing query 2383: Model only answers one image question SQLs
Error executing query 2384: Model abstains from answering the question
Error executing query 2386: Invalid expression / Unexpected token. Line 1, Col: 858.
  4566423 ) and strftime('%Y-%m',diagnoses_icd.charttime) = '2101-12' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2387: Model only answers one image question SQLs
Error executing query 2388: Invalid expression / Unexpected token. Line 1, Col: 928.
  iagnoses_icd.charttime) = datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2390: Invalid expression / Unexpected token. Line 1, Col: 884.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 2392: Model abstains from answering the question
Error executing query 2393: Invalid expression / Unexpected token. Line 1, Col: 406.
  'arterial blood pressure diastolic' and d_items.linksto = 'chartevents' ) and chartevents.valuenum  [4m52.0[0m and strftime('%Y-%m-%d',chartevents.charttime) >= '2105-12-15'
Error executing query 2399: Model only answers one image question SQLs
Error executing query 2400: Model only answers one image question SQLs
Error executing query 2401: Model abstains from answering the question
Error executing query 2402: Model only answers one image question SQLs
Error executing query 2403: Model abstains from answering the question
Error executing query 2405: Model only answers one image question SQLs
Error executing query 2406: Expecting ). Line 1, Col: 920.
  '%Y',prescriptions.starttime) = '2100' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 3
Error executing query 2408: Model abstains from answering the question
Error executing query 2409: Invalid expression / Unexpected token. Line 1, Col: 763.
  id = 16517135 ) and strftime('%Y',prescriptions.starttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 2410: Invalid expression / Unexpected token. Line 1, Col: 973.
  e('%m',prescriptions.starttime) = '01' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 d
Error executing query 2411: Model abstains from answering the question
Error executing query 2412: Invalid expression / Unexpected token. Line 1, Col: 865.
  id = 19101176 ) and strftime('%Y',diagnoses_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2413: Model abstains from answering the question
Error executing query 2414: Model only answers one image question SQLs
Error executing query 2415: Model only answers one image question SQLs
Error executing query 2416: Model only answers one image question SQLs
Error executing query 2418: Model only answers one image question SQLs
Error executing query 2419: Model only answers one image question SQLs
Error executing query 2420: Model abstains from answering the question
Error executing query 2422: Model only answers one image question SQLs
Error executing query 2424: Error tokenizing 'missions where admissions.subject_id = (picc)' ) '
Error executing query 2426: Model only answers one image question SQLs
Error executing query 2427: Model abstains from answering the question
Error executing query 2429: Model abstains from answering the question
Error executing query 2430: Invalid expression / Unexpected token. Line 1, Col: 717.
  unc_vqa("has an x-ray revealed any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2431: Model abstains from answering the question
Error executing query 2433: Model abstains from answering the question
Error executing query 2434: Invalid expression / Unexpected token. Line 1, Col: 879.
  atchy atelectasis in the left hilar structures?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2436: Model only answers one image question SQLs
Error executing query 2437: Required keyword: 'expressions' missing for <class 'sqlglot.expressions.Aliases'>. Line 1, Col: 362.
  items where d_labitems.label = 'white blood cells' ) order by labevents.charttime desc limit 1 )  ( [4mselect[0m labevents.valuenum from labevents where labevents.hadm_id in ( select admissions.hadm_id from admis
Error executing query 2439: Model abstains from answering the question
Error executing query 2440: Invalid expression / Unexpected token. Line 1, Col: 737.
  func_vqa("is any devices indicated on an x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2441: Invalid expression / Unexpected token. Line 1, Col: 1022.
  15999 ) and strftime('%Y-%m',procedures_icd.charttime) >= '2102-09' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and t1.hadm_id = t3.hadm_id
Error executing query 2442: Model only answers one image question SQLs
Error executing query 2443: Invalid expression / Unexpected token. Line 1, Col: 964.
  w any anatomical findings in the left clavicle?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2444: Expecting ). Line 1, Col: 862.
  %Y',procedures_icd.charttime) = '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
[False]
Error executing query 2447: Model abstains from answering the question
Error executing query 2450: Model abstains from answering the question
Error executing query 2451: Expecting ). Line 1, Col: 964.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 2452: Model only answers one image question SQLs
Error executing query 2453: Error tokenizing '3.studydatetime) and datetime(t3.studydatetime,'+'
Error executing query 2454: Model only answers one image question SQLs
Error executing query 2455: Required keyword: 'expressions' missing for <class 'sqlglot.expressions.Aliases'>. Line 1, Col: 528.
  lic' and d_items.linksto = 'chartevents' ) order by chartevents.charttime asc limit 1 offset 1 )  ( [4mselect[0m chartevents.valuenum from chartevents where chartevents.stay_id in ( select icustays.stay_id from i
Error executing query 2458: Model only answers one image question SQLs
Error executing query 2459: Model only answers one image question SQLs
Error executing query 2460: Invalid expression / Unexpected token. Line 1, Col: 745.
  t x-ray depicts any diseases in the right lung?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2461: Model only answers one image question SQLs
Error executing query 2463: Expecting ). Line 1, Col: 885.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 2464: Model abstains from answering the question
Error executing query 2466: Invalid expression / Unexpected token. Line 1, Col: 983.
  edures_icd.charttime) = datetime('2105-12-31 23:59:00','-46 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2467: Model abstains from answering the question
Error executing query 2468: Model abstains from answering the question
Error executing query 2469: Model only answers one image question SQLs
Error executing query 2471: Model only answers one image question SQLs
Error executing query 2475: Model abstains from answering the question
Error executing query 2478: Model only answers one image question SQLs
Error executing query 2482: Invalid expression / Unexpected token. Line 1, Col: 638.
  ality observed in the trachea on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2483: Model abstains from answering the question
Error executing query 2486: Model abstains from answering the question
Error executing query 2487: Model abstains from answering the question
Error executing query 2488: Model abstains from answering the question
Error executing query 2489: Expecting ). Line 1, Col: 722.
  labevents.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.itemid ) as t3 where t3.c1 = 3 )
Error executing query 2490: Model only answers one image question SQLs
Error executing query 2491: Invalid expression / Unexpected token. Line 1, Col: 947.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 2493: Model only answers one image question SQLs
Error executing query 2494: Model abstains from answering the question
Error executing query 2495: Model abstains from answering the question
Error executing query 2497: Invalid expression / Unexpected token. Line 1, Col: 643.
  ns.hadm_id from admissions where admissions.subject_id = 10006692 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 2498: Model only answers one image question SQLs
Error executing query 2499: Model only answers one image question SQLs
Error executing query 2500: Model abstains from answering the question
Error executing query 2503: Invalid expression / Unexpected token. Line 1, Col: 799.
  escriptions.starttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 2504: Model abstains from answering the question
Error executing query 2508: Model only answers one image question SQLs
Error executing query 2509: Model abstains from answering the question
Error executing query 2510: Model abstains from answering the question
Error executing query 2511: Model only answers one image question SQLs
Error executing query 2514: Model abstains from answering the question
Error executing query 2515: Model abstains from answering the question
Error executing query 2516: Model abstains from answering the question
Error executing query 2517: near "(": syntax error
Error executing query 2518: Model abstains from answering the question
Error executing query 2519: Invalid expression / Unexpected token. Line 1, Col: 884.
  d = 18291049 ) and strftime('%Y',procedures_icd.charttime) = '2102' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2520: Model abstains from answering the question
Error executing query 2521: near "(": syntax error
Error executing query 2522: Invalid expression / Unexpected token. Line 1, Col: 643.
  ns.hadm_id from admissions where admissions.subject_id = 10938464 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2524: Expecting ). Line 1, Col: 672.
  '%Y',prescriptions.starttime) = '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.starttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 3
Error executing query 2525: Model only answers one image question SQLs
Error executing query 2528: Invalid expression / Unexpected token. Line 1, Col: 895.
  func_vqa("does a chest x-ray reveal aspiration?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2529: Invalid expression / Unexpected token. Line 1, Col: 880.
  d = 18153920 ) and strftime('%Y',procedures_icd.charttime) = '2102' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2533: Invalid expression / Unexpected token. Line 1, Col: 805.
  t x-ray indicate any abnormality in the carina?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2534: Model abstains from answering the question
Error executing query 2535: near "(": syntax error
Error executing query 2536: Model abstains from answering the question
Error executing query 2537: Model abstains from answering the question
Error executing query 2539: Model only answers one image question SQLs
Error executing query 2541: Model abstains from answering the question
Error executing query 2542: Model abstains from answering the question
Error executing query 2543: Invalid expression / Unexpected token. Line 1, Col: 855.
  veal any diseases in the left hilar structures?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2544: Model abstains from answering the question
Error executing query 2547: Model abstains from answering the question
Error executing query 2548: Invalid expression / Unexpected token. Line 1, Col: 902.
  _vqa("is spinal fracture indicated on an x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2549: Model only answers one image question SQLs
Error executing query 2550: Expecting ). Line 1, Col: 618.
  criptions.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 2553: Model abstains from answering the question
Error executing query 2554: Model only answers one image question SQLs
Error executing query 2556: Invalid expression / Unexpected token. Line 1, Col: 908.
  cedures_icd.charttime) >= datetime('2105-12-31 23:59:00','-2 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2558: Model abstains from answering the question
Error executing query 2559: Invalid expression / Unexpected token. Line 1, Col: 1006.
  s.dischtime is not null order by admissions.admittime asc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2563: Model abstains from answering the question
Error executing query 2564: Model only answers one image question SQLs
Error executing query 2565: Model abstains from answering the question
Error executing query 2566: Model only answers one image question SQLs
Error executing query 2568: Model only answers one image question SQLs
Error executing query 2569: Invalid expression / Unexpected token. Line 1, Col: 971.
  agnoses_icd.charttime) >= datetime('2105-12-31 23:59:00','-6 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2570: Invalid expression / Unexpected token. Line 1, Col: 655.
   any any tubes/lines in the left mid lung zone?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 2572: Invalid expression / Unexpected token. Line 1, Col: 912.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 2573: Invalid expression / Unexpected token. Line 1, Col: 723.
  ns.hadm_id from admissions where admissions.subject_id = 11194078 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2574: Model abstains from answering the question
Error executing query 2575: Model abstains from answering the question
Error executing query 2576: Model abstains from answering the question
Error executing query 2578: Model abstains from answering the question
Error executing query 2579: Model abstains from answering the question
Error executing query 2580: Invalid expression / Unexpected token. Line 1, Col: 841.
  d = 13861581 ) and strftime('%Y',procedures_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2581: Model abstains from answering the question
Error executing query 2582: Model abstains from answering the question
Error executing query 2583: Model abstains from answering the question
Error executing query 2584: Model abstains from answering the question
Error executing query 2585: Model abstains from answering the question
Error executing query 2586: Invalid expression / Unexpected token. Line 1, Col: 1140.
   year','-1 year') and strftime('%m',diagnoses_icd.charttime) = '04' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydate
Error executing query 2587: Invalid expression / Unexpected token. Line 1, Col: 761.
  d = 15346117 ) and strftime('%Y',prescriptions.starttime) >= '2105' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 2589: Model abstains from answering the question
Error executing query 2590: Required keyword: 'expressions' missing for <class 'sqlglot.expressions.Aliases'>. Line 1, Col: 353.
  rom d_labitems where d_labitems.label ='magnesium' ) order by labevents.charttime desc limit 1 )  ( [4mselect[0m labevents.valuenum from labevents where labevents.hadm_id in ( select admissions.hadm_id from admis
Error executing query 2591: Expecting ). Line 1, Col: 839.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 2592: Model only answers one image question SQLs
Error executing query 2593: Model abstains from answering the question
Error executing query 2595: Model only answers one image question SQLs
Error executing query 2596: Invalid expression / Unexpected token. Line 1, Col: 640.
  hest x-ray reveal fluid overload/heart failure?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 2597: Model only answers one image question SQLs
Error executing query 2598: Invalid expression / Unexpected token. Line 1, Col: 739.
  s a chest x-ray reveal any anatomical findings?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2599: Invalid expression / Unexpected token. Line 1, Col: 737.
  has a chest x-ray demonstrated any abnormality?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 2600: Model abstains from answering the question
Error executing query 2601: Invalid expression / Unexpected token. Line 1, Col: 748.
  %Y',prescriptions.starttime) >= '2101' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month')
Error executing query 2602: Invalid expression / Unexpected token. Line 1, Col: 775.
  ,prescriptions.starttime) >= '2104-08' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id
Error executing query 2603: Invalid expression / Unexpected token. Line 1, Col: 864.
  '%Y',diagnoses_icd.charttime) = '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
Error executing query 2605: Model abstains from answering the question
Error executing query 2606: Model abstains from answering the question
Error executing query 2608: Model only answers one image question SQLs
Error executing query 2609: Invalid expression / Unexpected token. Line 1, Col: 877.
  icate any tubes/lines in the upper mediastinum?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 2610: Model abstains from answering the question
Error executing query 2613: Model abstains from answering the question
Error executing query 2615: Model abstains from answering the question
Error executing query 2616: Model abstains from answering the question
Error executing query 2618: Model only answers one image question SQLs
Error executing query 2619: Invalid expression / Unexpected token. Line 1, Col: 844.
  ime('2105-12-31 23:59:00','-92 month') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 d
Error executing query 2620: Model only answers one image question SQLs
Error executing query 2621: Invalid expression / Unexpected token. Line 1, Col: 841.
   func_vqa("does a chest x-ray show any devices?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2622: Model abstains from answering the question
Error executing query 2624: Invalid expression / Unexpected token. Line 1, Col: 787.
  s the chest x-ray indicate any any abnormality?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 2625: Model abstains from answering the question
Error executing query 2627: Model only answers one image question SQLs
Error executing query 2628: Invalid expression / Unexpected token. Line 1, Col: 960.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
Error executing query 2629: Invalid expression / Unexpected token. Line 1, Col: 965.
  cedures_icd.charttime) >= datetime('2105-12-31 23:59:00','-4 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2630: Expecting ). Line 1, Col: 989.
  ions.drug = 'artificial tear ointment' ) as t3 on t2.subject_id = t3.subject_id where t2.charttime  [4mt3[0m.starttime ) as t4 join patients on t4.subject_id = patients.subject_id
Error executing query 2631: Model abstains from answering the question
Error executing query 2633: Model only answers one image question SQLs
Error executing query 2634: Model abstains from answering the question
Error executing query 2637: Model abstains from answering the question
Error executing query 2638: Model abstains from answering the question
Error executing query 2640: Model abstains from answering the question
Error executing query 2641: Invalid expression / Unexpected token. Line 1, Col: 727.
  d = 16566006 ) and strftime('%Y',prescriptions.starttime) >= '2105' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 2642: Model abstains from answering the question
Error executing query 2644: Model only answers one image question SQLs
Error executing query 2645: Model abstains from answering the question
Error executing query 2646: Model only answers one image question SQLs
Error executing query 2647: Invalid expression / Unexpected token. Line 1, Col: 1014.
  nth') = datetime('2105-12-31 23:59:00','start of month','-0 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2648: Invalid expression / Unexpected token. Line 1, Col: 748.
  ns.hadm_id from admissions where admissions.subject_id = 12974480 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2649: Expecting ). Line 1, Col: 1008.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 2650: Invalid expression / Unexpected token. Line 1, Col: 730.
  c_vqa("is hyperaeration shown on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2651: Model abstains from answering the question
Error executing query 2652: Invalid expression / Unexpected token. Line 1, Col: 837.
  as t2 where func_vqa("is any diseases revealed?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2654: Invalid expression / Unexpected token. Line 1, Col: 829.
   func_vqa("does a chest x-ray show lung lesion?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2656: Model only answers one image question SQLs
Error executing query 2657: Model abstains from answering the question
Error executing query 2658: Model abstains from answering the question
Error executing query 2661: Model only answers one image question SQLs
Error executing query 2663: Invalid expression / Unexpected token. Line 1, Col: 873.
  te any tubes/lines in the left lower lung zone?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2666: Model abstains from answering the question
Error executing query 2667: Required keyword: 'expressions' missing for <class 'sqlglot.expressions.Aliases'>. Line 1, Col: 396.
  id from d_labitems where d_labitems.label = 'pco2' ) order by labevents.charttime desc limit 1 )  ( [4mselect[0m labevents.valuenum from labevents where labevents.hadm_id in ( select admissions.hadm_id from admis
Error executing query 2668: Model abstains from answering the question
Error executing query 2669: Model abstains from answering the question
Error executing query 2672: Model abstains from answering the question
Error executing query 2673: Model only answers one image question SQLs
Error executing query 2674: Model abstains from answering the question
Error executing query 2675: Invalid expression / Unexpected token. Line 1, Col: 736.
  855132 ) and strftime('%Y-%m',prescriptions.starttime) >= '2105-04' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2676: Invalid expression / Unexpected token. Line 1, Col: 742.
  id = 17445268 ) and strftime('%Y',prescriptions.starttime) = '2105' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 2679: Model abstains from answering the question
Error executing query 2680: Model only answers one image question SQLs
Error executing query 2682: Model abstains from answering the question
Error executing query 2683: Model abstains from answering the question
Error executing query 2684: Model abstains from answering the question
Error executing query 2685: Model abstains from answering the question
Error executing query 2687: Model only answers one image question SQLs
[True]
Error executing query 2689: Invalid expression / Unexpected token. Line 1, Col: 695.
  68425 and admissions.dischtime is null ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 d
Error executing query 2690: Model abstains from answering the question
Error executing query 2692: Expecting ). Line 1, Col: 884.
  time) = '2105' ) as t2 join admissions on t2.subject_id = admissions.subject_id where t2.charttime  [4madmissions[0m.admittime and strftime('%Y',admissions.admittime) = '2105' and datetime(t2.charttime,'start of mont
Error executing query 2693: Model abstains from answering the question
Error executing query 2694: Invalid expression / Unexpected token. Line 1, Col: 759.
  ns.hadm_id from admissions where admissions.subject_id = 17914007 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2695: Expecting ). Line 1, Col: 818.
  etime('2105-12-31 23:59:00','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month') gro
Error executing query 2696: Model abstains from answering the question
Error executing query 2699: Invalid expression / Unexpected token. Line 1, Col: 627.
  ere prescriptions.drug = 'ondansetron' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id
Error executing query 2700: Invalid expression / Unexpected token. Line 1, Col: 720.
   func_vqa("has a chest x-ray shown any devices?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2702: Model abstains from answering the question
Error executing query 2703: Invalid expression / Unexpected token. Line 1, Col: 906.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
Error executing query 2705: Model only answers one image question SQLs
Error executing query 2706: Model abstains from answering the question
Error executing query 2707: Invalid expression / Unexpected token. Line 1, Col: 748.
   in the right lower lung zone on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2708: Invalid expression / Unexpected token. Line 1, Col: 864.
  23:59:00','start of month','-0 month') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 d
[True]
[True]
Error executing query 2710: Invalid expression / Unexpected token. Line 1, Col: 940.
  agnoses_icd.charttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2711: Invalid expression / Unexpected token. Line 1, Col: 722.
  vqa("is any diseases observed on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2714: Model abstains from answering the question
Error executing query 2716: Invalid expression / Unexpected token. Line 1, Col: 750.
  id = 15700387 ) and strftime('%Y',prescriptions.starttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 2717: Model abstains from answering the question
Error executing query 2718: Model only answers one image question SQLs
Error executing query 2719: Model abstains from answering the question
Error executing query 2722: Invalid expression / Unexpected token. Line 1, Col: 894.
  vqa("does a chest x-ray reveal any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2723: Invalid expression / Unexpected token. Line 1, Col: 998.
  s.dischtime is not null order by admissions.admittime asc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2724: Model abstains from answering the question
Error executing query 2726: Invalid expression / Unexpected token. Line 1, Col: 878.
  ranulomatous diseases in the right apical zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
[False]
Error executing query 2728: Model abstains from answering the question
Error executing query 2729: Invalid expression / Unexpected token. Line 1, Col: 909.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
Error executing query 2733: Model only answers one image question SQLs
Error executing query 2735: Invalid expression / Unexpected token. Line 1, Col: 952.
  etime('2105-12-31 23:59:00','-4 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id
Error executing query 2740: Model abstains from answering the question
Error executing query 2741: Model only answers one image question SQLs
Error executing query 2742: Model abstains from answering the question
Error executing query 2743: Model only answers one image question SQLs
Error executing query 2744: Model abstains from answering the question
[False]
[False]
Error executing query 2746: Model only answers one image question SQLs
Error executing query 2747: Invalid expression / Unexpected token. Line 1, Col: 785.
  d = 18044092 ) and strftime('%Y',prescriptions.starttime) >= '2105' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 2748: Invalid expression / Unexpected token. Line 1, Col: 807.
  a chest x-ray show any vascular redistribution?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 2749: Model only answers one image question SQLs
Error executing query 2751: Invalid expression / Unexpected token. Line 1, Col: 756.
  8463717 ) and strftime('%Y-%m',prescriptions.starttime) = '2105-05' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2752: Model only answers one image question SQLs
Error executing query 2753: Model only answers one image question SQLs
Error executing query 2754: Model only answers one image question SQLs
Error executing query 2757: Model abstains from answering the question
Error executing query 2758: Invalid expression / Unexpected token. Line 1, Col: 719.
  c_vqa("does a chest x-ray show any abnormality?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2759: Model abstains from answering the question
Error executing query 2760: Invalid expression / Unexpected token. Line 1, Col: 845.
  escriptions.starttime) >= datetime('2105-12-31 23:59:00','-2 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 2761: Model abstains from answering the question
Error executing query 2762: Invalid expression / Unexpected token. Line 1, Col: 894.
  d = 15110303 ) and strftime('%Y',procedures_icd.charttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2764: Invalid expression / Unexpected token. Line 1, Col: 746.
  indication of any abnormality on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2766: Model only answers one image question SQLs
Error executing query 2771: Invalid expression / Unexpected token. Line 1, Col: 729.
  _vqa("does a chest x-ray show pleural effusion?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 2772: Model abstains from answering the question
Error executing query 2773: Model only answers one image question SQLs
Error executing query 2774: Model abstains from answering the question
Error executing query 2776: Model abstains from answering the question
Error executing query 2777: Model abstains from answering the question
Error executing query 2778: Invalid expression / Unexpected token. Line 1, Col: 648.
  ns.hadm_id from admissions where admissions.subject_id = 18153920 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2780: Error tokenizing 'udydatetime) and datetime(t3.studydatetime,'+2 da'
Error executing query 2781: Invalid expression / Unexpected token. Line 1, Col: 782.
  escriptions.starttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 2782: Model only answers one image question SQLs
Error executing query 2783: Model only answers one image question SQLs
Error executing query 2784: Invalid expression / Unexpected token. Line 1, Col: 856.
  %Y',procedures_icd.charttime) = '2100' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 2786: Model only answers one image question SQLs
Error executing query 2788: Model abstains from answering the question
Error executing query 2789: Model abstains from answering the question
Error executing query 2790: Model only answers one image question SQLs
Error executing query 2793: Expecting ). Line 1, Col: 985.
  ug = 'gastropoate meglumine & sodium)' ) as t3 on t2.subject_id = t3.subject_id where t2.charttime  [4mt3[0m.starttime ) as t4 join patients on t4.subject_id = patients.subject_id
Error executing query 2794: Model abstains from answering the question
Error executing query 2796: Expecting ). Line 1, Col: 812.
  microbiologyevents.charttime) = '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 2797: Invalid expression / Unexpected token. Line 1, Col: 951.
  cedures_icd.charttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2798: Model only answers one image question SQLs
Error executing query 2799: Model abstains from answering the question
Error executing query 2801: Model only answers one image question SQLs
[False]
[False]
Error executing query 2803: Model abstains from answering the question
Error executing query 2809: Model only answers one image question SQLs
Error executing query 2810: Invalid expression / Unexpected token. Line 1, Col: 770.
  9994730 ) and strftime('%Y-%m',prescriptions.starttime) = '2105-09' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2812: Model only answers one image question SQLs
Error executing query 2813: Model abstains from answering the question
Error executing query 2814: Model abstains from answering the question
Error executing query 2815: Model only answers one image question SQLs
Error executing query 2816: Model abstains from answering the question
Error executing query 2817: Model abstains from answering the question
Error executing query 2818: Model only answers one image question SQLs
Error executing query 2819: Invalid expression / Unexpected token. Line 1, Col: 996.
   year') = datetime('2105-12-31 23:59:00','start of year','-0 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2820: Model abstains from answering the question
Error executing query 2821: Model only answers one image question SQLs
Error executing query 2822: Model abstains from answering the question
Error executing query 2823: Model abstains from answering the question
Error executing query 2824: Model abstains from answering the question
Error executing query 2825: Invalid expression / Unexpected token. Line 1, Col: 956.
  cedures_icd.charttime) >= datetime('2105-12-31 23:59:00','-2 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2827: Model only answers one image question SQLs
Error executing query 2829: Invalid expression / Unexpected token. Line 1, Col: 967.
   year') = datetime('2105-12-31 23:59:00','start of year','-0 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2830: Invalid expression / Unexpected token. Line 1, Col: 712.
  %Y',prescriptions.starttime) >= '2100' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month')
Error executing query 2833: Model abstains from answering the question
Error executing query 2834: Invalid expression / Unexpected token. Line 1, Col: 383.
   where d_items.label = 'heart rate' and d_items.linksto = 'chartevents' ) and chartevents.valuenum  [4m99.0[0m and datetime(chartevents.charttime,'start of year') = datetime('2105-12-31 23:59:00','start of year
Error executing query 2836: Model abstains from answering the question
Error executing query 2837: Invalid expression / Unexpected token. Line 1, Col: 851.
  nth') = datetime('2105-12-31 23:59:00','start of month','-1 month') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2838: Model only answers one image question SQLs
Error executing query 2839: Model abstains from answering the question
Error executing query 2840: Model only answers one image question SQLs
Error executing query 2844: Model abstains from answering the question
Error executing query 2845: Model abstains from answering the question
Error executing query 2848: Model abstains from answering the question
Error executing query 2849: Model only answers one image question SQLs
Error executing query 2850: Model abstains from answering the question
Error executing query 2851: Model only answers one image question SQLs
Error executing query 2852: Invalid expression / Unexpected token. Line 1, Col: 913.
   = 19686680 ) and strftime('%Y',procedures_icd.charttime) >= '2100' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2855: Invalid expression / Unexpected token. Line 1, Col: 990.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2856: Model only answers one image question SQLs
Error executing query 2857: Model only answers one image question SQLs
Error executing query 2858: Invalid expression / Unexpected token. Line 1, Col: 772.
  tchy atelectasis in the right hilar structures?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 2859: Model abstains from answering the question
Error executing query 2860: Model abstains from answering the question
Error executing query 2861: Model only answers one image question SQLs
Error executing query 2862: Model abstains from answering the question
Error executing query 2863: Invalid expression / Unexpected token. Line 1, Col: 836.
  %Y',diagnoses_icd.charttime) >= '2105' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id
Error executing query 2864: Model abstains from answering the question
Error executing query 2865: Invalid expression / Unexpected token. Line 1, Col: 935.
  iagnoses_icd.charttime) = datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2866: Model abstains from answering the question
Error executing query 2869: Model abstains from answering the question
Error executing query 2870: Expecting ). Line 1, Col: 818.
  icrobiologyevents.charttime) >= '2105' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.test_name ) as t3 where t3.c1 = 3
Error executing query 2871: Invalid expression / Unexpected token. Line 1, Col: 883.
  5110303 ) and strftime('%Y-%m',diagnoses_icd.charttime) = '2103-10' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2873: Model abstains from answering the question
Error executing query 2874: Model abstains from answering the question
Error executing query 2875: Model abstains from answering the question
Error executing query 2878: Model abstains from answering the question
[False]
Error executing query 2880: Model only answers one image question SQLs
Error executing query 2881: Invalid expression / Unexpected token. Line 1, Col: 781.
  etime('2105-12-31 23:59:00','-5 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month')
Error executing query 2882: Model only answers one image question SQLs
Error executing query 2883: Invalid expression / Unexpected token. Line 1, Col: 1051.
  ("is the chest x-ray depicting any tubes/lines?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2884: Model abstains from answering the question
Error executing query 2885: Model abstains from answering the question
Error executing query 2887: Model only answers one image question SQLs
Error executing query 2889: Model abstains from answering the question
Error executing query 2890: Model abstains from answering the question
Error executing query 2891: Model abstains from answering the question
Error executing query 2892: Model abstains from answering the question
Error executing query 2893: Model only answers one image question SQLs
Error executing query 2894: Model only answers one image question SQLs
Error executing query 2895: Model abstains from answering the question
Error executing query 2897: Model abstains from answering the question
Error executing query 2898: Expecting ). Line 1, Col: 785.
  %Y',prescriptions.starttime) >= '2105' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 2899: Model only answers one image question SQLs
Error executing query 2902: Model only answers one image question SQLs
Error executing query 2903: Model abstains from answering the question
Error executing query 2904: Model only answers one image question SQLs
Error executing query 2907: Model abstains from answering the question
Error executing query 2909: Model abstains from answering the question
Error executing query 2910: Model abstains from answering the question
Error executing query 2911: Invalid expression / Unexpected token. Line 1, Col: 922.
  ting any tubes/lines in the cardiac silhouette?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2914: Model abstains from answering the question
Error executing query 2916: Invalid expression / Unexpected token. Line 1, Col: 872.
  "is alveolar hemorrhage shown on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2917: Invalid expression / Unexpected token. Line 1, Col: 896.
  leural effusion in the left costophrenic angle?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2918: Invalid expression / Unexpected token. Line 1, Col: 755.
  d = 18503972 ) and strftime('%Y',prescriptions.starttime) >= '2104' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2920: Model abstains from answering the question
Error executing query 2921: Invalid expression / Unexpected token. Line 1, Col: 738.
  d = 13656933 ) and strftime('%Y',prescriptions.starttime) >= '2104' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 2923: Model abstains from answering the question
Error executing query 2924: Invalid expression / Unexpected token. Line 1, Col: 920.
  oes a chest x-ray show any anatomical findings?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2925: Invalid expression / Unexpected token. Line 1, Col: 961.
  w any technical assessments in the mediastinum?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2928: Invalid expression / Unexpected token. Line 1, Col: 956.
  f spinal degenerative changes on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 2929: Invalid expression / Unexpected token. Line 1, Col: 805.
   x-ray indicate any abnormality in the abdomen?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2931: Model only answers one image question SQLs
Error executing query 2932: Model abstains from answering the question
Error executing query 2933: Model only answers one image question SQLs
Error executing query 2934: Model abstains from answering the question
Error executing query 2938: Error tokenizing 'tetime(t1.charttime) and datetime(t1.charttime,'+'
Error executing query 2939: Model only answers one image question SQLs
Error executing query 2942: Model abstains from answering the question
Error executing query 2943: Model only answers one image question SQLs
Error executing query 2944: Invalid expression / Unexpected token. Line 1, Col: 1013.
  s.dischtime is not null order by admissions.admittime asc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 2946: Model abstains from answering the question
Error executing query 2948: Invalid expression / Unexpected token. Line 1, Col: 658.
  city in the right apical zone on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 2949: Invalid expression / Unexpected token. Line 1, Col: 752.
  chest x-ray reveal any any anatomical findings?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 2950: Expecting ). Line 1, Col: 832.
  etime('2105-12-31 23:59:00','-5 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 2951: Model abstains from answering the question
Error executing query 2952: Model abstains from answering the question
Error executing query 2954: Model only answers one image question SQLs
Error executing query 2956: Model abstains from answering the question
Error executing query 2957: Model only answers one image question SQLs
Error executing query 2958: Model abstains from answering the question
Error executing query 2960: Model abstains from answering the question
Error executing query 2961: Model abstains from answering the question
Error executing query 2962: Expecting ). Line 1, Col: 945.
  etime('2105-12-31 23:59:00','-6 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
[False]
[False]
Error executing query 2964: Model abstains from answering the question
Error executing query 2965: Model abstains from answering the question
Error executing query 2967: Invalid expression / Unexpected token. Line 1, Col: 948.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 2969: Model abstains from answering the question
Error executing query 2970: Model only answers one image question SQLs
Error executing query 2971: Model abstains from answering the question
Error executing query 2972: Invalid expression / Unexpected token. Line 1, Col: 746.
  id = 12637733 ) and strftime('%Y',prescriptions.starttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 2973: Model abstains from answering the question
Error executing query 2974: Model abstains from answering the question
Error executing query 2976: Model abstains from answering the question
Error executing query 2977: Model abstains from answering the question
Error executing query 2982: Model only answers one image question SQLs
Error executing query 2986: Expecting ). Line 1, Col: 874.
  etime('2105-12-31 23:59:00','-3 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 2987: Model abstains from answering the question
Error executing query 2988: Model abstains from answering the question
Error executing query 2989: Invalid expression / Unexpected token. Line 1, Col: 813.
  id = 15898931 ) and strftime('%Y',diagnoses_icd.charttime) = '2102' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 2990: Model abstains from answering the question
[False]
[False]
Error executing query 2992: Model only answers one image question SQLs
Error executing query 2994: Model abstains from answering the question
Error executing query 2996: Model abstains from answering the question
Error executing query 2997: Invalid expression / Unexpected token. Line 1, Col: 728.
  id = 18487097 ) and strftime('%Y',prescriptions.starttime) = '2101' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 2999: Model abstains from answering the question
Error executing query 3000: Model abstains from answering the question
Error executing query 3002: Invalid expression / Unexpected token. Line 1, Col: 892.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id
Error executing query 3003: Model only answers one image question SQLs
Error executing query 3005: Model abstains from answering the question
Error executing query 3006: Invalid expression / Unexpected token. Line 1, Col: 718.
  func_vqa("is a chest x-ray showing any devices?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3007: Invalid expression / Unexpected token. Line 1, Col: 906.
  ay revealed pleural effusion in the right lung?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3008: Model abstains from answering the question
Error executing query 3009: Model only answers one image question SQLs
Error executing query 3011: Model abstains from answering the question
Error executing query 3012: Model only answers one image question SQLs
Error executing query 3014: Model abstains from answering the question
Error executing query 3015: Invalid expression / Unexpected token. Line 1, Col: 835.
  id = 12070314 ) and strftime('%Y',diagnoses_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3016: Invalid expression / Unexpected token. Line 1, Col: 840.
  etime('2105-12-31 23:59:00','-4 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 3020: Model only answers one image question SQLs
Error executing query 3021: Model abstains from answering the question
Error executing query 3022: Model abstains from answering the question
Error executing query 3024: Model abstains from answering the question
Error executing query 3025: Invalid expression / Unexpected token. Line 1, Col: 875.
  d = 18153920 ) and strftime('%Y',procedures_icd.charttime) = '2102' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3026: Model abstains from answering the question
Error executing query 3027: Model abstains from answering the question
Error executing query 3028: Model only answers one image question SQLs
Error executing query 3029: Model only answers one image question SQLs
Error executing query 3030: Model only answers one image question SQLs
Error executing query 3031: Model abstains from answering the question
Error executing query 3032: Model only answers one image question SQLs
Error executing query 3033: Model only answers one image question SQLs
Error executing query 3034: Model abstains from answering the question
Error executing query 3036: Invalid expression / Unexpected token. Line 1, Col: 757.
  id = 12070314 ) and strftime('%Y',prescriptions.starttime) = '2102' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 3038: Model abstains from answering the question
Error executing query 3040: Model only answers one image question SQLs
Error executing query 3042: Model abstains from answering the question
Error executing query 3045: Model abstains from answering the question
Error executing query 3046: Model only answers one image question SQLs
Error executing query 3047: Invalid expression / Unexpected token. Line 1, Col: 847.
  d = 18443840 ) and strftime('%Y',diagnoses_icd.charttime) >= '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3048: Model abstains from answering the question
Error executing query 3049: Invalid expression / Unexpected token. Line 1, Col: 821.
  ns.hadm_id from admissions where admissions.subject_id = 15764474 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3050: Invalid expression / Unexpected token. Line 1, Col: 842.
  id = 12177956 ) and strftime('%Y',diagnoses_icd.charttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3054: Expecting ). Line 1, Col: 837.
  '%Y',diagnoses_icd.charttime) = '2103' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 3056: Model only answers one image question SQLs
Error executing query 3059: Model abstains from answering the question
Error executing query 3061: Model abstains from answering the question
Error executing query 3062: Model only answers one image question SQLs
Error executing query 3064: Model abstains from answering the question
[True]
Error executing query 3066: Expecting ). Line 1, Col: 839.
  etime('2105-12-31 23:59:00','-4 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 3067: Model only answers one image question SQLs
Error executing query 3069: Model abstains from answering the question
Error executing query 3071: Model abstains from answering the question
Error executing query 3072: Model abstains from answering the question
Error executing query 3073: near "(": syntax error
Error executing query 3076: Model abstains from answering the question
Error executing query 3077: Invalid expression / Unexpected token. Line 1, Col: 849.
  hest x-ray showing costophrenic angle blunting?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3078: Model abstains from answering the question
Error executing query 3079: Model abstains from answering the question
Error executing query 3080: Invalid expression / Unexpected token. Line 1, Col: 815.
  ns.hadm_id from admissions where admissions.subject_id = 11211421 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3081: Model only answers one image question SQLs
Error executing query 3082: Model only answers one image question SQLs
Error executing query 3086: Invalid expression / Unexpected token. Line 1, Col: 866.
  d = 14431875 ) and strftime('%Y',procedures_icd.charttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3089: Model abstains from answering the question
Error executing query 3090: Invalid expression / Unexpected token. Line 1, Col: 949.
  agnoses_icd.charttime) >= datetime('2105-12-31 23:59:00','-2 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3091: Model abstains from answering the question
Error executing query 3092: Model only answers one image question SQLs
Error executing query 3093: Model only answers one image question SQLs
Error executing query 3094: Model abstains from answering the question
Error executing query 3095: Model only answers one image question SQLs
Error executing query 3099: Invalid expression / Unexpected token. Line 1, Col: 887.
   func_vqa("has a chest x-ray shown any devices?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3100: Model abstains from answering the question
Error executing query 3101: Model only answers one image question SQLs
Error executing query 3103: Model only answers one image question SQLs
Error executing query 3104: Model abstains from answering the question
Error executing query 3105: Model abstains from answering the question
Error executing query 3108: Model abstains from answering the question
Error executing query 3109: Model abstains from answering the question
Error executing query 3112: Model abstains from answering the question
Error executing query 3113: Expecting ). Line 1, Col: 848.
  etime('2105-12-31 23:59:00','-3 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 3117: Model only answers one image question SQLs
Error executing query 3120: Model abstains from answering the question
Error executing query 3121: Model only answers one image question SQLs
Error executing query 3122: Invalid expression / Unexpected token. Line 1, Col: 995.
  e('%m',prescriptions.starttime) = '12' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id
Error executing query 3123: Model abstains from answering the question
Error executing query 3124: Model abstains from answering the question
Error executing query 3125: Model only answers one image question SQLs
Error executing query 3126: Invalid expression / Unexpected token. Line 1, Col: 956.
  _vqa("does a chest x-ray indicate any diseases?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3127: Model abstains from answering the question
Error executing query 3128: Model abstains from answering the question
Error executing query 3129: Model only answers one image question SQLs
Error executing query 3130: Model abstains from answering the question
Error executing query 3132: Expecting ). Line 1, Col: 1153.
  mit 1 ) order by tb_cxr.studydatetime desc limit 1 ) ) ) order by tb_cxr.studydatetime desc limit 1 [4m)[0m
Error executing query 3135: Model abstains from answering the question
Error executing query 3138: Model abstains from answering the question
Error executing query 3139: Model abstains from answering the question
Error executing query 3140: Model abstains from answering the question
Error executing query 3141: Model abstains from answering the question
Error executing query 3143: Model only answers one image question SQLs
[True]
Error executing query 3145: Model abstains from answering the question
Error executing query 3146: Model abstains from answering the question
Error executing query 3147: Model abstains from answering the question
Error executing query 3149: Model only answers one image question SQLs
Error executing query 3150: Model only answers one image question SQLs
Error executing query 3153: Model only answers one image question SQLs
Error executing query 3155: Invalid expression / Unexpected token. Line 1, Col: 911.
  agnoses_icd.charttime) >= datetime('2105-12-31 23:59:00','-2 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3156: Invalid expression / Unexpected token. Line 1, Col: 761.
  any abnormality in the left costophrenic angle?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3157: Invalid expression / Unexpected token. Line 1, Col: 884.
  ns.hadm_id from admissions where admissions.subject_id = 17620765 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and t1.hadm_id = t3.hadm_id
Error executing query 3158: Model abstains from answering the question
Error executing query 3159: Invalid expression / Unexpected token. Line 1, Col: 895.
  vqa("does a chest x-ray reveal any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3160: Invalid expression / Unexpected token. Line 1, Col: 855.
   = 10827632 ) and strftime('%Y',procedures_icd.charttime) >= '2102' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3161: Model only answers one image question SQLs
Error executing query 3164: Invalid expression / Unexpected token. Line 1, Col: 967.
   in the right lower lung zone on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3165: Model only answers one image question SQLs
Error executing query 3166: Invalid expression / Unexpected token. Line 1, Col: 873.
  %Y',procedures_icd.charttime) = '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
Error executing query 3168: Model abstains from answering the question
Error executing query 3170: Invalid expression / Unexpected token. Line 1, Col: 905.
  502354 ) and strftime('%Y-%m',diagnoses_icd.charttime) >= '2105-11' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3171: Model abstains from answering the question
Error executing query 3172: Model abstains from answering the question
Error executing query 3176: Model abstains from answering the question
Error executing query 3177: Model only answers one image question SQLs
Error executing query 3178: Expecting ). Line 1, Col: 933.
  etime('2105-12-31 23:59:00','-5 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 3179: Model abstains from answering the question
Error executing query 3180: Model only answers one image question SQLs
Error executing query 3181: Model abstains from answering the question
Error executing query 3182: Expecting ). Line 1, Col: 988.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 3184: Model abstains from answering the question
Error executing query 3190: Model only answers one image question SQLs
Error executing query 3191: Invalid expression / Unexpected token. Line 1, Col: 764.
  how any clavicle fracture in the left clavicle?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 3192: Model only answers one image question SQLs
Error executing query 3193: Invalid expression / Unexpected token. Line 1, Col: 872.
  cate any anatomical findings in the right lung?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3194: Model only answers one image question SQLs
Error executing query 3197: Model abstains from answering the question
Error executing query 3200: Expecting ). Line 1, Col: 876.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.itemid ) as t3 where t3.c1 = 4 )
Error executing query 3201: Invalid expression / Unexpected token. Line 1, Col: 845.
  obar/segmental collapse shown on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3202: Model abstains from answering the question
Error executing query 3203: Model abstains from answering the question
Error executing query 3204: Model only answers one image question SQLs
Error executing query 3205: Model abstains from answering the question
Error executing query 3206: Invalid expression / Unexpected token. Line 1, Col: 742.
  _vqa("is a chest x-ray showing any tubes/lines?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3208: Model abstains from answering the question
Error executing query 3210: Model abstains from answering the question
Error executing query 3212: Expecting ). Line 1, Col: 773.
  '%Y',prescriptions.starttime) = '2102' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
[False]
Error executing query 3213: Model abstains from answering the question
Error executing query 3216: Invalid expression / Unexpected token. Line 1, Col: 731.
  _vqa("is a chest x-ray showing any abnormality?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3217: Invalid expression / Unexpected token. Line 1, Col: 655.
  ns.hadm_id from admissions where admissions.subject_id = 10578743 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3218: Model abstains from answering the question
Error executing query 3219: Invalid expression / Unexpected token. Line 1, Col: 1022.
  ocedures_icd.charttime) = datetime('2105-12-31 23:59:00','-3 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3221: Model only answers one image question SQLs
Error executing query 3222: Expecting ). Line 1, Col: 734.
  noses_icd.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
[False]
Error executing query 3225: Model abstains from answering the question
Error executing query 3227: Model abstains from answering the question
Error executing query 3228: Invalid expression / Unexpected token. Line 1, Col: 818.
  riptions.starttime) >= datetime('2105-12-31 23:59:00','-108 month') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3229: Model abstains from answering the question
Error executing query 3231: Invalid expression / Unexpected token. Line 1, Col: 829.
  s any technical assessments in the mediastinum?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3232: Model only answers one image question SQLs
Error executing query 3233: Model only answers one image question SQLs
Error executing query 3234: Model abstains from answering the question
Error executing query 3235: Model only answers one image question SQLs
Error executing query 3236: Model abstains from answering the question
Error executing query 3237: Model only answers one image question SQLs
Error executing query 3238: Invalid expression / Unexpected token. Line 1, Col: 966.
  cedures_icd.charttime) >= datetime('2105-12-31 23:59:00','-2 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3239: Model only answers one image question SQLs
Error executing query 3240: Model only answers one image question SQLs
Error executing query 3241: Model abstains from answering the question
Error executing query 3242: Model abstains from answering the question
Error executing query 3243: Invalid expression / Unexpected token. Line 1, Col: 703.
  _title = 'other irrigation of wound' ) ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
Error executing query 3246: Model abstains from answering the question
Error executing query 3247: Invalid expression / Unexpected token. Line 1, Col: 622.
  vqa("does a chest x-ray reveal any tubes/lines?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 3248: Model only answers one image question SQLs
Error executing query 3249: Model abstains from answering the question
Error executing query 3253: Model abstains from answering the question
Error executing query 3254: Model only answers one image question SQLs
Error executing query 3255: Invalid expression / Unexpected token. Line 1, Col: 1044.
  d = 17598348 ) and strftime('%Y',procedures_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and t1.hadm_id = t3.hadm_id
Error executing query 3256: Invalid expression / Unexpected token. Line 1, Col: 851.
  vqa("does a chest x-ray reveal any abnormality?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3257: Model abstains from answering the question
Error executing query 3259: Invalid expression / Unexpected token. Line 1, Col: 628.
  ns.hadm_id from admissions where admissions.subject_id = 13461731 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 3260: Invalid expression / Unexpected token. Line 1, Col: 872.
  id = 10032409 ) and strftime('%Y',diagnoses_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3262: Model abstains from answering the question
Error executing query 3263: Model only answers one image question SQLs
Error executing query 3266: Model abstains from answering the question
Error executing query 3268: Model abstains from answering the question
Error executing query 3269: Invalid expression / Unexpected token. Line 1, Col: 926.
  ty in the right mid lung zone on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3270: Model abstains from answering the question
Error executing query 3271: Model abstains from answering the question
Error executing query 3272: Model abstains from answering the question
Error executing query 3274: Model only answers one image question SQLs
Error executing query 3275: Invalid expression / Unexpected token. Line 1, Col: 865.
  ments indicated in the left breast on an x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3276: Model abstains from answering the question
Error executing query 3277: Invalid expression / Unexpected token. Line 1, Col: 752.
  physema revealed in the right hilar structures?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3278: Invalid expression / Unexpected token. Line 1, Col: 745.
   show any diseases in the left upper lung zone?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3279: Model abstains from answering the question
Error executing query 3280: Model abstains from answering the question
Error executing query 3282: Model only answers one image question SQLs
Error executing query 3284: Model only answers one image question SQLs
Error executing query 3285: Model only answers one image question SQLs
Error executing query 3286: Model abstains from answering the question
Error executing query 3287: Model abstains from answering the question
Error executing query 3288: Model abstains from answering the question
Error executing query 3289: Model abstains from answering the question
Error executing query 3290: Model abstains from answering the question
Error executing query 3292: Model abstains from answering the question
Error executing query 3295: Model only answers one image question SQLs
Error executing query 3296: Model abstains from answering the question
Error executing query 3298: Model abstains from answering the question
Error executing query 3300: Model only answers one image question SQLs
Error executing query 3301: Model abstains from answering the question
Error executing query 3303: Invalid expression / Unexpected token. Line 1, Col: 861.
  d = 13895041 ) and strftime('%Y',diagnoses_icd.charttime) >= '2102' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3304: Invalid expression / Unexpected token. Line 1, Col: 751.
  ns.hadm_id from admissions where admissions.subject_id = 16200419 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3307: Model abstains from answering the question
Error executing query 3309: Model abstains from answering the question
Error executing query 3310: Model abstains from answering the question
Error executing query 3314: Model only answers one image question SQLs
Error executing query 3316: Model abstains from answering the question
Error executing query 3317: Model abstains from answering the question
Error executing query 3319: Model abstains from answering the question
Error executing query 3320: Invalid expression / Unexpected token. Line 1, Col: 996.
  c_vqa("does a chest x-ray show any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3322: Model abstains from answering the question
Error executing query 3323: Model only answers one image question SQLs
Error executing query 3325: Model abstains from answering the question
Error executing query 3326: Invalid expression / Unexpected token. Line 1, Col: 884.
   x-ray detecting tracheostomy tube in the neck?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3328: Model abstains from answering the question
Error executing query 3330: Invalid expression / Unexpected token. Line 1, Col: 1025.
   year') = datetime('2105-12-31 23:59:00','start of year','-0 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3331: Model only answers one image question SQLs
Error executing query 3332: Model only answers one image question SQLs
Error executing query 3333: Invalid expression / Unexpected token. Line 1, Col: 383.
   where d_items.label = 'heart rate' and d_items.linksto = 'chartevents' ) and chartevents.valuenum  [4m85.0[0m and datetime(chartevents.charttime) >= datetime('2105-12-31 23:59:00','-153 month')
Error executing query 3334: Model only answers one image question SQLs
Error executing query 3335: Expecting ). Line 1, Col: 780.
  '%Y',prescriptions.starttime) = '2103' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 4
Error executing query 3336: Invalid expression / Unexpected token. Line 1, Col: 803.
  ns.hadm_id from admissions where admissions.subject_id = 13855132 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3338: Model only answers one image question SQLs
Error executing query 3339: Invalid expression / Unexpected token. Line 1, Col: 894.
  tecting any abnormality in the left chest wall?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3341: Invalid expression / Unexpected token. Line 1, Col: 913.
  iagnoses_icd.charttime) = datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3342: Invalid expression / Unexpected token. Line 1, Col: 740.
  id = 16419341 ) and strftime('%Y',prescriptions.starttime) = '2101' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 3343: Model abstains from answering the question
Error executing query 3344: Model abstains from answering the question
Error executing query 3345: Invalid expression / Unexpected token. Line 1, Col: 761.
  ns.hadm_id from admissions where admissions.subject_id = 14835886 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3346: Model abstains from answering the question
Error executing query 3348: Model abstains from answering the question
Error executing query 3349: Expecting ). Line 1, Col: 934.
  00','-3 year') ) as t2 join admissions on t2.subject_id = admissions.subject_id where t2.charttime  [4madmissions[0m.admittime and datetime(admissions.admittime) >= datetime('2105-12-31 23:59:00','-3 year') and datet
Error executing query 3350: Model only answers one image question SQLs
Error executing query 3352: Invalid expression / Unexpected token. Line 1, Col: 919.
  rmality revealed in the spine on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3353: Model only answers one image question SQLs
Error executing query 3354: Model only answers one image question SQLs
Error executing query 3355: Model only answers one image question SQLs
Error executing query 3358: Model only answers one image question SQLs
Error executing query 3360: Model only answers one image question SQLs
Error executing query 3361: Model abstains from answering the question
Error executing query 3364: Model abstains from answering the question
Error executing query 3365: Model only answers one image question SQLs
Error executing query 3368: Invalid expression / Unexpected token. Line 1, Col: 970.
  cedures_icd.charttime) >= datetime('2105-12-31 23:59:00','-3 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3369: Model only answers one image question SQLs
Error executing query 3370: Model abstains from answering the question
Error executing query 3371: Model abstains from answering the question
Error executing query 3372: Invalid expression / Unexpected token. Line 1, Col: 852.
  _vqa("does a chest x-ray show pleural effusion?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3376: Model only answers one image question SQLs
Error executing query 3378: Model abstains from answering the question
Error executing query 3379: Invalid expression / Unexpected token. Line 1, Col: 918.
  t x-ray indicate any diseases in the left lung?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3380: Model abstains from answering the question
Error executing query 3382: Invalid expression / Unexpected token. Line 1, Col: 642.
  ns.hadm_id from admissions where admissions.subject_id = 17975155 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 3383: Invalid expression / Unexpected token. Line 1, Col: 615.
  where prescriptions.drug = 'diltiazem' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 3384: Model only answers one image question SQLs
Error executing query 3386: Expecting ). Line 1, Col: 871.
  etime('2105-12-31 23:59:00','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 3389: Expecting ). Line 1, Col: 902.
  %Y',prescriptions.starttime) >= '2102' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 4
Error executing query 3390: Model only answers one image question SQLs
Error executing query 3391: Expecting ). Line 1, Col: 974.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 3392: Invalid expression / Unexpected token. Line 1, Col: 623.
  ns.hadm_id from admissions where admissions.subject_id = 12139817 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 3395: Model only answers one image question SQLs
Error executing query 3398: Invalid expression / Unexpected token. Line 1, Col: 671.
  ns.hadm_id from admissions where admissions.subject_id = 15689544 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3401: Model abstains from answering the question
Error executing query 3402: Model only answers one image question SQLs
Error executing query 3403: Invalid expression / Unexpected token. Line 1, Col: 852.
  c_vqa("does a chest x-ray show any tubes/lines?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3404: Invalid expression / Unexpected token. Line 1, Col: 920.
  '%Y',diagnoses_icd.charttime) = '2105' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id
Error executing query 3405: Model only answers one image question SQLs
Error executing query 3406: Invalid expression / Unexpected token. Line 1, Col: 961.
  nth') = datetime('2105-12-31 23:59:00','start of month','-0 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3407: Model abstains from answering the question
Error executing query 3408: Model abstains from answering the question
Error executing query 3409: Invalid expression / Unexpected token. Line 1, Col: 750.
  mediastinal displacement indicated on an x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3411: Model abstains from answering the question
Error executing query 3414: Invalid expression / Unexpected token. Line 1, Col: 800.
  ns.hadm_id from admissions where admissions.subject_id = 10681061 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3416: Expecting ). Line 1, Col: 836.
  etime('2105-12-31 23:59:00','-3 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 3417: Model abstains from answering the question
Error executing query 3418: Model abstains from answering the question
Error executing query 3419: Invalid expression / Unexpected token. Line 1, Col: 765.
  ion of joint, other specified sites' ) ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
Error executing query 3422: Model only answers one image question SQLs
Error executing query 3423: Invalid expression / Unexpected token. Line 1, Col: 740.
  unc_vqa("is any diseases indicated on an x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3424: Expecting ). Line 1, Col: 810.
  microbiologyevents.charttime) = '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 3425: Model only answers one image question SQLs
Error executing query 3426: Invalid expression / Unexpected token. Line 1, Col: 894.
  %Y',procedures_icd.charttime) = '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id
Error executing query 3428: Model only answers one image question SQLs
Error executing query 3432: Model only answers one image question SQLs
Error executing query 3433: Expecting ). Line 1, Col: 879.
  etime('2105-12-31 23:59:00','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 3434: Model abstains from answering the question
Error executing query 3435: Model only answers one image question SQLs
Error executing query 3436: Model abstains from answering the question
Error executing query 3439: Model only answers one image question SQLs
Error executing query 3440: Model abstains from answering the question
Error executing query 3442: Expecting ). Line 1, Col: 651.
  '%Y',prescriptions.starttime) = '2105' ) as t2 on t1.subject_id = t2.subject_id where t1.starttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 3
Error executing query 3443: Invalid expression / Unexpected token. Line 1, Col: 756.
   of any technical assessments on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3444: Invalid expression / Unexpected token. Line 1, Col: 880.
  s.dischtime is not null order by admissions.admittime asc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3445: Model abstains from answering the question
Error executing query 3446: Model only answers one image question SQLs
Error executing query 3447: Model only answers one image question SQLs
Error executing query 3448: Model only answers one image question SQLs
Error executing query 3452: Model abstains from answering the question
Error executing query 3454: Model abstains from answering the question
Error executing query 3455: Model only answers one image question SQLs
Error executing query 3458: Model abstains from answering the question
Error executing query 3459: Model abstains from answering the question
Error executing query 3460: Model abstains from answering the question
Error executing query 3465: Invalid expression / Unexpected token. Line 1, Col: 892.
  s.dischtime is not null order by admissions.admittime asc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3470: Invalid expression / Unexpected token. Line 1, Col: 750.
  indication of any abnormality on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3471: Model abstains from answering the question
Error executing query 3474: Model abstains from answering the question
Error executing query 3475: Model abstains from answering the question
Error executing query 3476: Model abstains from answering the question
Error executing query 3477: Invalid expression / Unexpected token. Line 1, Col: 797.
  chest x-ray reveal any any anatomical findings?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 3478: Invalid expression / Unexpected token. Line 1, Col: 924.
  etime('2105-12-31 23:59:00','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id
Error executing query 3479: Model abstains from answering the question
Error executing query 3480: Model abstains from answering the question
Error executing query 3482: Model only answers one image question SQLs
Error executing query 3483: Model only answers one image question SQLs
[False]
Error executing query 3485: Model abstains from answering the question
Error executing query 3486: Model abstains from answering the question
Error executing query 3487: Invalid expression / Unexpected token. Line 1, Col: 997.
  ay show lung opacity in the cardiac silhouette?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3488: Invalid expression / Unexpected token. Line 1, Col: 997.
  gnoses_icd.charttime) = datetime('2105-12-31 23:59:00','-21 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3489: Model abstains from answering the question
[False]
Error executing query 3493: Invalid expression / Unexpected token. Line 1, Col: 933.
  d = 11131026 ) and strftime('%Y',diagnoses_icd.charttime) >= '2105' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3494: Invalid expression / Unexpected token. Line 1, Col: 961.
  nes in the cardiac silhouette on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3495: Invalid expression / Unexpected token. Line 1, Col: 775.
  nc_vqa("is a chest x-ray showing consolidation?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 3496: Model abstains from answering the question
Error executing query 3497: Model abstains from answering the question
Error executing query 3498: Model abstains from answering the question
Error executing query 3501: Model only answers one image question SQLs
[False]
Error executing query 3504: Expecting ). Line 1, Col: 940.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.itemid ) as t3 where t3.c1 = 4 )
Error executing query 3506: Model abstains from answering the question
Error executing query 3507: Model abstains from answering the question
Error executing query 3508: Invalid expression / Unexpected token. Line 1, Col: 892.
  "does the chest x-ray indicate any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3509: Model only answers one image question SQLs
Error executing query 3510: Invalid expression / Unexpected token. Line 1, Col: 742.
  s a chest x-ray reveal any anatomical findings?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3511: Model only answers one image question SQLs
Error executing query 3512: Model only answers one image question SQLs
Error executing query 3513: Model only answers one image question SQLs
Error executing query 3514: Invalid expression / Unexpected token. Line 1, Col: 738.
  _vqa("is a chest x-ray showing any tubes/lines?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3515: Invalid expression / Unexpected token. Line 1, Col: 978.
  indication of any abnormality on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3516: Model abstains from answering the question
Error executing query 3517: Model abstains from answering the question
Error executing query 3519: Model only answers one image question SQLs
Error executing query 3520: Model only answers one image question SQLs
Error executing query 3521: Model abstains from answering the question
Error executing query 3522: Model only answers one image question SQLs
Error executing query 3524: Model only answers one image question SQLs
Error executing query 3525: Model abstains from answering the question
Error executing query 3527: Model abstains from answering the question
Error executing query 3528: Model only answers one image question SQLs
Error executing query 3529: Error tokenizing 'ydatetime) and datetime(t3.studydatetime,'+2 mont'
Error executing query 3532: Model abstains from answering the question
Error executing query 3534: Model abstains from answering the question
Error executing query 3537: Invalid expression / Unexpected token. Line 1, Col: 650.
  ns.hadm_id from admissions where admissions.subject_id = 19155097 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3539: Invalid expression / Unexpected token. Line 1, Col: 1115.
  year','-0 year') and strftime('%m',procedures_icd.charttime) = '09' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and date
Error executing query 3540: Model only answers one image question SQLs
Error executing query 3541: Model abstains from answering the question
[True]
Error executing query 3543: Expecting ). Line 1, Col: 683.
  ogyevents.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
[False]
Error executing query 3545: Model abstains from answering the question
Error executing query 3548: Expecting ). Line 1, Col: 869.
  '%Y',prescriptions.starttime) = '2102' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 3549: Model abstains from answering the question
Error executing query 3550: Model only answers one image question SQLs
Error executing query 3551: Model only answers one image question SQLs
Error executing query 3552: Model abstains from answering the question
Error executing query 3553: Model abstains from answering the question
Error executing query 3555: Model abstains from answering the question
Error executing query 3559: Model abstains from answering the question
Error executing query 3560: Model only answers one image question SQLs
Error executing query 3563: Model abstains from answering the question
Error executing query 3564: Model abstains from answering the question
Error executing query 3566: Invalid expression / Unexpected token. Line 1, Col: 840.
  nc_vqa("has an x-ray indicated any tubes/lines?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3567: Invalid expression / Unexpected token. Line 1, Col: 820.
  id = 17268795 ) and strftime('%Y',diagnoses_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3570: Model only answers one image question SQLs
Error executing query 3571: Model abstains from answering the question
Error executing query 3573: Invalid expression / Unexpected token. Line 1, Col: 934.
   anatomical findings in the left mid lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3575: Invalid expression / Unexpected token. Line 1, Col: 850.
   = 13656933 ) and strftime('%Y',procedures_icd.charttime) >= '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3576: Model abstains from answering the question
Error executing query 3577: Model only answers one image question SQLs
Error executing query 3579: Model abstains from answering the question
Error executing query 3580: Model abstains from answering the question
Error executing query 3581: Invalid expression / Unexpected token. Line 1, Col: 792.
  oes a chest x-ray reveal sub-diaphragmatic air?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 3586: Model abstains from answering the question
Error executing query 3588: Model abstains from answering the question
Error executing query 3590: Model abstains from answering the question
Error executing query 3591: Model only answers one image question SQLs
Error executing query 3592: Model abstains from answering the question
Error executing query 3594: Model abstains from answering the question
Error executing query 3596: Model only answers one image question SQLs
Error executing query 3597: Model abstains from answering the question
Error executing query 3598: Model abstains from answering the question
Error executing query 3599: Model only answers one image question SQLs
Error executing query 3600: Invalid expression / Unexpected token. Line 1, Col: 749.
  id = 19919980 ) and strftime('%Y',prescriptions.starttime) = '2105' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 3601: Model abstains from answering the question
Error executing query 3602: Model abstains from answering the question
Error executing query 3603: Model only answers one image question SQLs
Error executing query 3605: Model only answers one image question SQLs
Error executing query 3606: Model abstains from answering the question
Error executing query 3607: Model only answers one image question SQLs
Error executing query 3608: Model abstains from answering the question
Error executing query 3609: Invalid expression / Unexpected token. Line 1, Col: 873.
  0938464 ) and strftime('%Y-%m',diagnoses_icd.charttime) = '2105-10' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3610: Invalid expression / Unexpected token. Line 1, Col: 1056.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3611: Model abstains from answering the question
Error executing query 3613: Expecting ). Line 1, Col: 678.
  ogyevents.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 3614: Expecting ). Line 1, Col: 889.
  %Y',prescriptions.starttime) >= '2105' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 3615: Model abstains from answering the question
Error executing query 3617: Model only answers one image question SQLs
Error executing query 3619: Invalid expression / Unexpected token. Line 1, Col: 888.
  ray show any diseases in the right apical zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3620: Model only answers one image question SQLs
Error executing query 3622: Model abstains from answering the question
Error executing query 3624: Model abstains from answering the question
Error executing query 3626: Model abstains from answering the question
Error executing query 3627: Model abstains from answering the question
Error executing query 3628: Model only answers one image question SQLs
Error executing query 3630: Model abstains from answering the question
Error executing query 3632: Expecting ). Line 1, Col: 988.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 3633: Expecting ). Line 1, Col: 904.
  ime) >= '2105' ) as t2 join admissions on t2.subject_id = admissions.subject_id where t2.charttime  [4madmissions[0m.admittime and strftime('%Y',admissions.admittime) >= '2105' and datetime(t2.charttime,'start of mon
Error executing query 3634: Invalid expression / Unexpected token. Line 1, Col: 871.
  043637 ) and strftime('%Y-%m',diagnoses_icd.charttime) >= '2104-11' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3636: Model only answers one image question SQLs
Error executing query 3638: Model abstains from answering the question
Error executing query 3639: Invalid expression / Unexpected token. Line 1, Col: 947.
  unc_vqa("is any devices shown on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3640: Model abstains from answering the question
Error executing query 3641: Model abstains from answering the question
Error executing query 3642: Invalid expression / Unexpected token. Line 1, Col: 745.
  est x-ray indicate enlarged cardiac silhouette?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 3643: Model abstains from answering the question
Error executing query 3645: Model only answers one image question SQLs
Error executing query 3646: near "(": syntax error
Error executing query 3648: Model abstains from answering the question
Error executing query 3650: Invalid expression / Unexpected token. Line 1, Col: 979.
   year','-1 year') and strftime('%m',prescriptions.starttime) = '11' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3651: Model abstains from answering the question
Error executing query 3653: Invalid expression / Unexpected token. Line 1, Col: 972.
  edures_icd.charttime) = datetime('2105-12-31 23:59:00','-23 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3654: Model only answers one image question SQLs
Error executing query 3655: Model abstains from answering the question
Error executing query 3656: Invalid expression / Unexpected token. Line 1, Col: 1002.
  ny abnormality in the right costophrenic angle?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
[True]
Error executing query 3657: near "(": syntax error
Error executing query 3659: Invalid expression / Unexpected token. Line 1, Col: 876.
  ny indication of rib fracture on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3660: Model abstains from answering the question
Error executing query 3662: Model only answers one image question SQLs
Error executing query 3663: Model abstains from answering the question
Error executing query 3664: Invalid expression / Unexpected token. Line 1, Col: 943.
  mality in the left chest wall on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3665: Model abstains from answering the question
Error executing query 3668: Model abstains from answering the question
[True]
Error executing query 3671: Invalid expression / Unexpected token. Line 1, Col: 870.
  id = 16631797 ) and strftime('%Y',diagnoses_icd.charttime) = '2102' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3672: Model abstains from answering the question
Error executing query 3673: Model abstains from answering the question
Error executing query 3675: Model only answers one image question SQLs
Error executing query 3676: Expecting ). Line 1, Col: 607.
  criptions.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month') gro
Error executing query 3679: Model abstains from answering the question
Error executing query 3681: Model abstains from answering the question
Error executing query 3682: Model abstains from answering the question
Error executing query 3683: Model only answers one image question SQLs
Error executing query 3685: Model abstains from answering the question
Error executing query 3686: Invalid expression / Unexpected token. Line 1, Col: 876.
  %Y',procedures_icd.charttime) = '2100' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id
Error executing query 3687: Model only answers one image question SQLs
Error executing query 3688: Model only answers one image question SQLs
Error executing query 3689: Model only answers one image question SQLs
Error executing query 3691: Model abstains from answering the question
Error executing query 3695: Model only answers one image question SQLs
Error executing query 3696: Model only answers one image question SQLs
Error executing query 3697: Model only answers one image question SQLs
Error executing query 3700: Model only answers one image question SQLs
Error executing query 3703: Model abstains from answering the question
Error executing query 3704: Model abstains from answering the question
Error executing query 3705: Model abstains from answering the question
Error executing query 3706: Invalid expression / Unexpected token. Line 1, Col: 850.
  an-ganz catheter in the right hilar structures?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3707: Model only answers one image question SQLs
Error executing query 3708: Model abstains from answering the question
Error executing query 3711: Model abstains from answering the question
Error executing query 3713: Model abstains from answering the question
Error executing query 3715: Model abstains from answering the question
Error executing query 3716: Invalid expression / Unexpected token. Line 1, Col: 873.
  hown in the upper mediastinum on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3717: Model abstains from answering the question
Error executing query 3718: Model abstains from answering the question
Error executing query 3719: Invalid expression / Unexpected token. Line 1, Col: 864.
   an indication of any devices on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3720: Model abstains from answering the question
Error executing query 3721: Model abstains from answering the question
Error executing query 3722: Model abstains from answering the question
Error executing query 3723: Invalid expression / Unexpected token. Line 1, Col: 890.
  neumomediastinum in the right hilar structures?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 3725: Model only answers one image question SQLs
Error executing query 3726: Model only answers one image question SQLs
Error executing query 3727: Model abstains from answering the question
Error executing query 3729: Invalid expression / Unexpected token. Line 1, Col: 917.
  656933 ) and strftime('%Y-%m',procedures_icd.charttime) = '2104-05' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3730: Model abstains from answering the question
Error executing query 3731: Invalid expression / Unexpected token. Line 1, Col: 667.
  ns.hadm_id from admissions where admissions.subject_id = 14117444 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 3732: Invalid expression / Unexpected token. Line 1, Col: 873.
  d = 18487097 ) and strftime('%Y',procedures_icd.charttime) = '2101' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3733: Model abstains from answering the question
Error executing query 3734: Model abstains from answering the question
Error executing query 3739: Model only answers one image question SQLs
Error executing query 3740: Model abstains from answering the question
Error executing query 3742: Model abstains from answering the question
[False]
[False]
Error executing query 3744: Invalid expression / Unexpected token. Line 1, Col: 752.
  itus with hypoglycemia without coma' ) ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
Error executing query 3745: Model only answers one image question SQLs
Error executing query 3746: Invalid expression / Unexpected token. Line 1, Col: 845.
  _vqa("is a chest x-ray showing any abnormality?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3747: Model abstains from answering the question
Error executing query 3748: Model abstains from answering the question
Error executing query 3749: Invalid expression / Unexpected token. Line 1, Col: 629.
  ns.hadm_id from admissions where admissions.subject_id = 19385269 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3750: Invalid expression / Unexpected token. Line 1, Col: 730.
  id = 15110303 ) and strftime('%Y',prescriptions.starttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 3751: Invalid expression / Unexpected token. Line 1, Col: 970.
  ocedures_icd.charttime) = datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3753: Invalid expression / Unexpected token. Line 1, Col: 857.
  hown in the upper mediastinum on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
[True]
Error executing query 3755: Model only answers one image question SQLs
Error executing query 3757: Model only answers one image question SQLs
Error executing query 3760: Expecting ). Line 1, Col: 764.
  '%Y',prescriptions.starttime) = '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 4
[True]
Error executing query 3763: near "(": syntax error
Error executing query 3764: Model only answers one image question SQLs
Error executing query 3765: Model abstains from answering the question
Error executing query 3766: Model abstains from answering the question
Error executing query 3767: Model only answers one image question SQLs
Error executing query 3769: Invalid expression / Unexpected token. Line 1, Col: 750.
   a chest x-ray depicts any anatomical findings?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 3770: Model abstains from answering the question
Error executing query 3771: Invalid expression / Unexpected token. Line 1, Col: 903.
   indicate any abnormality in the left clavicle?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3772: Invalid expression / Unexpected token. Line 1, Col: 870.
  7622334 ) and strftime('%Y-%m',diagnoses_icd.charttime) = '2103-05' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3773: Model only answers one image question SQLs
Error executing query 3774: Model abstains from answering the question
Error executing query 3775: Model abstains from answering the question
Error executing query 3776: Model abstains from answering the question
Error executing query 3777: Invalid expression / Unexpected token. Line 1, Col: 930.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 3778: Model abstains from answering the question
Error executing query 3779: Model only answers one image question SQLs
Error executing query 3780: Model abstains from answering the question
Error executing query 3781: Invalid expression / Unexpected token. Line 1, Col: 903.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
Error executing query 3782: Model abstains from answering the question
Error executing query 3783: Model abstains from answering the question
Error executing query 3784: Model abstains from answering the question
Error executing query 3785: Model abstains from answering the question
Error executing query 3786: Model abstains from answering the question
Error executing query 3788: Model abstains from answering the question
Error executing query 3789: Model abstains from answering the question
Error executing query 3791: Model abstains from answering the question
Error executing query 3792: Model abstains from answering the question
Error executing query 3794: Invalid expression / Unexpected token. Line 1, Col: 865.
   = 13710683 ) and strftime('%Y',procedures_icd.charttime) >= '2105' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3796: Invalid expression / Unexpected token. Line 1, Col: 765.
  ns.hadm_id from admissions where admissions.subject_id = 15689544 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3797: Model abstains from answering the question
Error executing query 3798: Invalid expression / Unexpected token. Line 1, Col: 869.
  _vqa("is any abnormality revealed in the spine?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3800: near "(": syntax error
Error executing query 3801: Model only answers one image question SQLs
Error executing query 3803: Model only answers one image question SQLs
Error executing query 3807: Model only answers one image question SQLs
Error executing query 3808: Model abstains from answering the question
Error executing query 3810: Invalid expression / Unexpected token. Line 1, Col: 819.
  criptions.starttime) >= datetime('2105-12-31 23:59:00','-39 month') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3812: Model abstains from answering the question
Error executing query 3813: Model abstains from answering the question
Error executing query 3814: Model abstains from answering the question
Error executing query 3815: Invalid expression / Unexpected token. Line 1, Col: 907.
  etime('2105-12-31 23:59:00','-3 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 3816: Invalid expression / Unexpected token. Line 1, Col: 819.
  escriptions.starttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 3817: Model abstains from answering the question
Error executing query 3818: Invalid expression / Unexpected token. Line 1, Col: 868.
   = 15949703 ) and strftime('%Y',procedures_icd.charttime) >= '2101' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3820: Model abstains from answering the question
Error executing query 3822: Expecting ). Line 1, Col: 887.
  etime('2105-12-31 23:59:00','-4 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 3823: Invalid expression / Unexpected token. Line 1, Col: 897.
  vqa("is any abnormality shown on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3824: Model only answers one image question SQLs
Error executing query 3825: Model abstains from answering the question
Error executing query 3827: Model only answers one image question SQLs
Error executing query 3828: Invalid expression / Unexpected token. Line 1, Col: 1020.
  .dischtime is not null order by admissions.admittime desc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3830: Model abstains from answering the question
Error executing query 3831: Model abstains from answering the question
Error executing query 3833: Model abstains from answering the question
Error executing query 3834: Model abstains from answering the question
Error executing query 3835: Model abstains from answering the question
Error executing query 3839: Model abstains from answering the question
Error executing query 3840: Model only answers one image question SQLs
Error executing query 3841: Model only answers one image question SQLs
Error executing query 3842: Model abstains from answering the question
Error executing query 3843: Invalid expression / Unexpected token. Line 1, Col: 862.
  e chest x-ray revealing granulomatous diseases?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3844: near "(": syntax error
Error executing query 3845: Model abstains from answering the question
Error executing query 3847: Model abstains from answering the question
Error executing query 3848: Model abstains from answering the question
Error executing query 3849: Model only answers one image question SQLs
Error executing query 3851: Model abstains from answering the question
Error executing query 3852: Model abstains from answering the question
Error executing query 3853: Invalid expression / Unexpected token. Line 1, Col: 744.
  hest x-ray indicate any granulomatous diseases?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3854: Invalid expression / Unexpected token. Line 1, Col: 834.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 3855: Model abstains from answering the question
Error executing query 3857: Invalid expression / Unexpected token. Line 1, Col: 1034.
  nth') = datetime('2105-12-31 23:59:00','start of month','-0 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3858: Model only answers one image question SQLs
Error executing query 3859: Model abstains from answering the question
Error executing query 3861: Invalid expression / Unexpected token. Line 1, Col: 807.
  rescriptions.starttime) = datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 3862: Expecting ). Line 1, Col: 746.
  '%Y',prescriptions.starttime) = '2102' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 3863: Model only answers one image question SQLs
Error executing query 3865: Model only answers one image question SQLs
Error executing query 3867: Model only answers one image question SQLs
Error executing query 3869: Model only answers one image question SQLs
Error executing query 3870: Model only answers one image question SQLs
Error executing query 3871: Model only answers one image question SQLs
Error executing query 3873: Model only answers one image question SQLs
Error executing query 3874: Model abstains from answering the question
Error executing query 3875: Model only answers one image question SQLs
Error executing query 3877: Model abstains from answering the question
Error executing query 3881: Model abstains from answering the question
Error executing query 3884: Invalid expression / Unexpected token. Line 1, Col: 748.
  id = 17968028 ) and strftime('%Y',prescriptions.starttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3885: Model abstains from answering the question
Error executing query 3886: Model abstains from answering the question
Error executing query 3889: Model abstains from answering the question
Error executing query 3891: Model only answers one image question SQLs
Error executing query 3892: Invalid expression / Unexpected token. Line 1, Col: 976.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 3893: Model abstains from answering the question
Error executing query 3894: Model abstains from answering the question
[True]
[True]
Error executing query 3896: Model abstains from answering the question
Error executing query 3897: Model abstains from answering the question
Error executing query 3898: Model abstains from answering the question
Error executing query 3899: Model only answers one image question SQLs
Error executing query 3900: Expecting ). Line 1, Col: 1106.
   year') order by tb_cxr.studydatetime desc limit 1 ) ) ) order by tb_cxr.studydatetime desc limit 1 [4m)[0m
Error executing query 3901: Model only answers one image question SQLs
Error executing query 3903: Invalid expression / Unexpected token. Line 1, Col: 1065.
  vqa("does a chest x-ray reveal any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3904: Model abstains from answering the question
Error executing query 3906: Model abstains from answering the question
Error executing query 3907: Expecting ). Line 1, Col: 767.
  '%Y',prescriptions.starttime) = '2102' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month') gro
Error executing query 3908: Expecting ). Line 1, Col: 821.
  etime('2105-12-31 23:59:00','-3 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 4
Error executing query 3909: Model only answers one image question SQLs
Error executing query 3910: Model abstains from answering the question
Error executing query 3911: Model abstains from answering the question
Error executing query 3912: Model abstains from answering the question
Error executing query 3914: Invalid expression / Unexpected token. Line 1, Col: 802.
  scriptions.starttime) = datetime('2105-12-31 23:59:00','-21 month') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3917: Model abstains from answering the question
Error executing query 3918: Model abstains from answering the question
Error executing query 3919: Model abstains from answering the question
Error executing query 3920: Model only answers one image question SQLs
Error executing query 3922: Model abstains from answering the question
Error executing query 3923: Model abstains from answering the question
Error executing query 3927: Model abstains from answering the question
Error executing query 3928: Model abstains from answering the question
Error executing query 3930: Invalid expression / Unexpected token. Line 1, Col: 874.
  %Y',diagnoses_icd.charttime) >= '2105' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 3931: Invalid expression / Unexpected token. Line 1, Col: 791.
  ("is a chest x-ray showing vascular congestion?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 3932: Model abstains from answering the question
Error executing query 3933: Invalid expression / Unexpected token. Line 1, Col: 950.
  re func_vqa("is breast/nipple shadows revealed?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3935: Model abstains from answering the question
Error executing query 3936: Model abstains from answering the question
Error executing query 3937: Model only answers one image question SQLs
Error executing query 3940: Model only answers one image question SQLs
Error executing query 3941: Model only answers one image question SQLs
Error executing query 3942: Model only answers one image question SQLs
Error executing query 3943: Invalid expression / Unexpected token. Line 1, Col: 982.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 3944: Model abstains from answering the question
Error executing query 3945: Model only answers one image question SQLs
Error executing query 3946: Model only answers one image question SQLs
Error executing query 3947: Invalid expression / Unexpected token. Line 1, Col: 871.
  indicate any diseases in the upper mediastinum?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 3948: Model abstains from answering the question
Error executing query 3949: Invalid expression / Unexpected token. Line 1, Col: 976.
   of any technical assessments on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 3950: Invalid expression / Unexpected token. Line 1, Col: 737.
   x-ray show any any abnormality in the trachea?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 3952: Model only answers one image question SQLs
Error executing query 3953: Model abstains from answering the question
Error executing query 3954: Invalid expression / Unexpected token. Line 1, Col: 632.
  has a chest x-ray demonstrated any abnormality?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 3955: Invalid expression / Unexpected token. Line 1, Col: 821.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month')
Error executing query 3957: Model abstains from answering the question
[True]
[True]
Error executing query 3959: Model only answers one image question SQLs
Error executing query 3960: Model abstains from answering the question
Error executing query 3962: Model abstains from answering the question
Error executing query 3963: Model abstains from answering the question
Error executing query 3964: Invalid expression / Unexpected token. Line 1, Col: 998.
  indication of any abnormality on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3966: Model only answers one image question SQLs
Error executing query 3968: Invalid expression / Unexpected token. Line 1, Col: 999.
  .dischtime is not null order by admissions.admittime desc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3969: Invalid expression / Unexpected token. Line 1, Col: 943.
  iagnoses_icd.charttime) = datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3971: Invalid expression / Unexpected token. Line 1, Col: 919.
  d = 11441830 ) and strftime('%Y',procedures_icd.charttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 3972: Model abstains from answering the question
Error executing query 3973: Model abstains from answering the question
Error executing query 3977: Model only answers one image question SQLs
Error executing query 3978: Invalid expression / Unexpected token. Line 1, Col: 923.
  gnoses_icd.charttime) = datetime('2105-12-31 23:59:00','-22 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3979: Model only answers one image question SQLs
Error executing query 3982: Model only answers one image question SQLs
Error executing query 3985: Model abstains from answering the question
Error executing query 3986: Model abstains from answering the question
Error executing query 3988: near "(": syntax error
Error executing query 3989: Expecting ). Line 1, Col: 902.
  etime('2105-12-31 23:59:00','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 3990: Model abstains from answering the question
Error executing query 3991: Expecting ). Line 1, Col: 750.
  microbiologyevents.charttime) = '2101' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 3992: Invalid expression / Unexpected token. Line 1, Col: 938.
  anatomical findings in the right hemidiaphragm?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3993: Invalid expression / Unexpected token. Line 1, Col: 784.
  ns.hadm_id from admissions where admissions.subject_id = 16326772 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 3994: Invalid expression / Unexpected token. Line 1, Col: 860.
  vqa("is lung opacity revealed on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 3996: Model abstains from answering the question
Error executing query 3997: Model abstains from answering the question
Error executing query 4001: Model abstains from answering the question
Error executing query 4002: Invalid expression / Unexpected token. Line 1, Col: 966.
  ocedures_icd.charttime) = datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 4003: Model abstains from answering the question
Error executing query 4004: Model only answers one image question SQLs
Error executing query 4005: Invalid expression / Unexpected token. Line 1, Col: 893.
  iagnoses_icd.charttime) = datetime('2105-12-31 23:59:00','-2 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 4009: Model only answers one image question SQLs
Error executing query 4011: Model only answers one image question SQLs
Error executing query 4012: Invalid expression / Unexpected token. Line 1, Col: 928.
  n the left costophrenic angle on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4013: Invalid expression / Unexpected token. Line 1, Col: 894.
  ny tubes/lines identified in the left clavicle?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4014: Model abstains from answering the question
Error executing query 4015: Invalid expression / Unexpected token. Line 1, Col: 842.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 4016: Model abstains from answering the question
Error executing query 4018: Expecting ). Line 1, Col: 951.
  etime('2105-12-31 23:59:00','-3 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 3
Error executing query 4020: Model only answers one image question SQLs
Error executing query 4023: Model abstains from answering the question
Error executing query 4024: Invalid expression / Unexpected token. Line 1, Col: 825.
  y anatomical findings in the upper mediastinum?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 4028: Model only answers one image question SQLs
Error executing query 4029: Invalid expression / Unexpected token. Line 1, Col: 769.
  947284 ) and strftime('%Y-%m',prescriptions.starttime) >= '2105-11' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4030: Invalid expression / Unexpected token. Line 1, Col: 899.
  ns.hadm_id from admissions where admissions.subject_id = 12935888 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4031: Model only answers one image question SQLs
Error executing query 4032: Expecting ). Line 1, Col: 909.
  etime('2105-12-31 23:59:00','-3 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.itemid ) as t3 where t3.c1 = 4 )
Error executing query 4033: Model abstains from answering the question
Error executing query 4034: Invalid expression / Unexpected token. Line 1, Col: 920.
  agnoses_icd.charttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 4037: Model abstains from answering the question
Error executing query 4038: Model abstains from answering the question
Error executing query 4039: Model abstains from answering the question
Error executing query 4041: near "(": syntax error
Error executing query 4042: Model abstains from answering the question
Error executing query 4043: Model only answers one image question SQLs
Error executing query 4044: Expecting ). Line 1, Col: 969.
  ere prescriptions.drug = 'viaflex bag' ) as t3 on t2.subject_id = t3.subject_id where t2.charttime  [4mt3[0m.starttime ) as t4 join patients on t4.subject_id = patients.subject_id
Error executing query 4045: Invalid expression / Unexpected token. Line 1, Col: 652.
  ns.hadm_id from admissions where admissions.subject_id = 12645334 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4046: Model only answers one image question SQLs
Error executing query 4047: Model only answers one image question SQLs
Error executing query 4048: Model abstains from answering the question
[False]
[False]
Error executing query 4055: Model abstains from answering the question
Error executing query 4056: Invalid expression / Unexpected token. Line 1, Col: 870.
  s.dischtime is not null order by admissions.admittime asc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4057: Invalid expression / Unexpected token. Line 1, Col: 888.
  chymal scarring in the left costophrenic angle?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4058: Model abstains from answering the question
Error executing query 4059: Invalid expression / Unexpected token. Line 1, Col: 769.
  622334 ) and strftime('%Y-%m',prescriptions.starttime) >= '2103-01' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
[True]
Error executing query 4062: Model only answers one image question SQLs
Error executing query 4063: Model abstains from answering the question
Error executing query 4064: Model abstains from answering the question
Error executing query 4065: Model abstains from answering the question
Error executing query 4067: Model abstains from answering the question
Error executing query 4069: Model abstains from answering the question
Error executing query 4070: Model only answers one image question SQLs
Error executing query 4071: Model abstains from answering the question
Error executing query 4072: Model only answers one image question SQLs
Error executing query 4073: Model abstains from answering the question
Error executing query 4074: Model only answers one image question SQLs
Error executing query 4075: Model abstains from answering the question
Error executing query 4077: Invalid expression / Unexpected token. Line 1, Col: 880.
  nc_vqa("has an x-ray indicated any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4078: Expecting ). Line 1, Col: 799.
  etime('2105-12-31 23:59:00','-4 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 4079: Model abstains from answering the question
Error executing query 4080: Model abstains from answering the question
Error executing query 4081: Model abstains from answering the question
Error executing query 4083: Model abstains from answering the question
Error executing query 4085: Model only answers one image question SQLs
Error executing query 4086: Model abstains from answering the question
Error executing query 4089: Model abstains from answering the question
Error executing query 4090: Model abstains from answering the question
Error executing query 4091: Model only answers one image question SQLs
Error executing query 4092: Invalid expression / Unexpected token. Line 1, Col: 992.
  .dischtime is not null order by admissions.admittime desc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4095: Model abstains from answering the question
Error executing query 4096: Model abstains from answering the question
Error executing query 4097: Model abstains from answering the question
Error executing query 4098: Model abstains from answering the question
Error executing query 4100: Model only answers one image question SQLs
Error executing query 4102: Model abstains from answering the question
Error executing query 4105: Model abstains from answering the question
Error executing query 4108: Invalid expression / Unexpected token. Line 1, Col: 881.
  _vqa("does a chest x-ray indicate any diseases?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4111: Invalid expression / Unexpected token. Line 1, Col: 937.
  chnical assessments in the right mid lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4112: Model abstains from answering the question
Error executing query 4115: Model abstains from answering the question
Error executing query 4116: Model abstains from answering the question
Error executing query 4117: Model abstains from answering the question
Error executing query 4119: Model abstains from answering the question
Error executing query 4120: Model only answers one image question SQLs
Error executing query 4121: Model only answers one image question SQLs
Error executing query 4122: Model abstains from answering the question
Error executing query 4124: Model abstains from answering the question
Error executing query 4125: Model abstains from answering the question
Error executing query 4126: Model abstains from answering the question
Error executing query 4127: Model only answers one image question SQLs
Error executing query 4128: Model only answers one image question SQLs
Error executing query 4129: Model abstains from answering the question
Error executing query 4131: Model abstains from answering the question
Error executing query 4132: Model abstains from answering the question
Error executing query 4133: Invalid expression / Unexpected token. Line 1, Col: 936.
  dures_icd.charttime) >= datetime('2105-12-31 23:59:00','-26 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4134: Model only answers one image question SQLs
Error executing query 4135: Model abstains from answering the question
Error executing query 4137: Invalid expression / Unexpected token. Line 1, Col: 638.
  ns.hadm_id from admissions where admissions.subject_id = 16419341 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4138: Model abstains from answering the question
Error executing query 4140: Model abstains from answering the question
Error executing query 4142: Expecting ). Line 1, Col: 1118.
   ) order by tb_cxr.studydatetime desc limit 1 ) ) ) order by tb_cxr.studydatetime desc limit 1 ) as [4mt2[0m
Error executing query 4143: Model abstains from answering the question
Error executing query 4144: Model abstains from answering the question
Error executing query 4146: Model abstains from answering the question
Error executing query 4147: Model abstains from answering the question
Error executing query 4148: Model abstains from answering the question
Error executing query 4149: Model only answers one image question SQLs
Error executing query 4150: Model only answers one image question SQLs
Error executing query 4151: Model only answers one image question SQLs
Error executing query 4154: Model only answers one image question SQLs
Error executing query 4155: Expecting ). Line 1, Col: 968.
  re prescriptions.drug ='systane ultra' ) as t3 on t2.subject_id = t3.subject_id where t2.charttime  [4mt3[0m.starttime ) as t4 join patients on t4.subject_id = patients.subject_id
Error executing query 4156: Model abstains from answering the question
Error executing query 4158: Model abstains from answering the question
Error executing query 4160: Model abstains from answering the question
Error executing query 4161: Model abstains from answering the question
Error executing query 4163: Model only answers one image question SQLs
Error executing query 4164: Model only answers one image question SQLs
[True]
Error executing query 4165: Model abstains from answering the question
Error executing query 4166: Invalid expression / Unexpected token. Line 1, Col: 781.
  concentrated nutritional substances' ) ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id
Error executing query 4168: Model abstains from answering the question
Error executing query 4170: Model abstains from answering the question
Error executing query 4172: Invalid expression / Unexpected token. Line 1, Col: 865.
  ny indication of lung opacity on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4175: Model abstains from answering the question
Error executing query 4177: Model only answers one image question SQLs
Error executing query 4178: Invalid expression / Unexpected token. Line 1, Col: 821.
  y pneumothorax in the right costophrenic angle?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4179: Model only answers one image question SQLs
Error executing query 4180: Invalid expression / Unexpected token. Line 1, Col: 813.
  escriptions.starttime) = datetime('2105-12-31 23:59:00','-7 month') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4182: Model abstains from answering the question
Error executing query 4183: Invalid expression / Unexpected token. Line 1, Col: 1118.
  year','-0 year') and strftime('%m',procedures_icd.charttime) = '01' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.stud
Error executing query 4185: Model abstains from answering the question
Error executing query 4186: Model only answers one image question SQLs
Error executing query 4187: Model abstains from answering the question
Error executing query 4188: Model abstains from answering the question
Error executing query 4189: Model abstains from answering the question
Error executing query 4190: near "(": syntax error
Error executing query 4192: Model abstains from answering the question
Error executing query 4193: Invalid expression / Unexpected token. Line 1, Col: 476.
  'arterial blood pressure diastolic' and d_items.linksto = 'chartevents' ) and chartevents.valuenum  [4m66.0[0m
Error executing query 4198: Model only answers one image question SQLs
Error executing query 4200: Model abstains from answering the question
Error executing query 4201: Invalid expression / Unexpected token. Line 1, Col: 845.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 4202: Invalid expression / Unexpected token. Line 1, Col: 874.
  owing intra-aortic balloon pump in the abdomen?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 4203: Expecting ). Line 1, Col: 1167.
  ttime desc limit 1 ) order by tb_cxr.studydatetime desc limit 1 ) ) ) order by tb_cxr.studydatetime [4mdesc[0m
[False]
Error executing query 4205: Model abstains from answering the question
Error executing query 4206: Model only answers one image question SQLs
Error executing query 4207: Model abstains from answering the question
Error executing query 4208: Model only answers one image question SQLs
[False]
[False]
Error executing query 4213: Invalid expression / Unexpected token. Line 1, Col: 945.
  iagnoses_icd.charttime) = datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
[False]
Error executing query 4216: Invalid expression / Unexpected token. Line 1, Col: 896.
  d = 15689818 ) and strftime('%Y',diagnoses_icd.charttime) >= '2101' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4217: Model abstains from answering the question
Error executing query 4219: Model only answers one image question SQLs
Error executing query 4221: Invalid expression / Unexpected token. Line 1, Col: 737.
  2 where func_vqa("is tortuous aorta identified?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4222: Model abstains from answering the question
Error executing query 4225: near "(": syntax error
Error executing query 4226: Invalid expression / Unexpected token. Line 1, Col: 752.
  %Y',prescriptions.starttime) >= '2103' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id
Error executing query 4227: Invalid expression / Unexpected token. Line 1, Col: 749.
  110303 ) and strftime('%Y-%m',prescriptions.starttime) >= '2103-10' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4228: Model only answers one image question SQLs
Error executing query 4229: Model only answers one image question SQLs
Error executing query 4231: Model abstains from answering the question
Error executing query 4232: Model abstains from answering the question
Error executing query 4233: Expecting ). Line 1, Col: 1001.
  e prescriptions.drug ='sodium citrate' ) as t3 on t2.subject_id = t3.subject_id where t2.charttime  [4mt3[0m.starttime ) as t4 join patients on t4.subject_id = patients.subject_id
Error executing query 4234: Model only answers one image question SQLs
Error executing query 4236: Invalid expression / Unexpected token. Line 1, Col: 783.
  ns.hadm_id from admissions where admissions.subject_id = 15439081 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4237: Model only answers one image question SQLs
Error executing query 4238: Model abstains from answering the question
Error executing query 4240: Model only answers one image question SQLs
Error executing query 4241: Model abstains from answering the question
Error executing query 4242: Model abstains from answering the question
Error executing query 4244: Expecting ). Line 1, Col: 860.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 4245: Invalid expression / Unexpected token. Line 1, Col: 732.
   func_vqa("has a chest x-ray shown any devices?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4247: Model abstains from answering the question
Error executing query 4248: Model abstains from answering the question
Error executing query 4250: Model abstains from answering the question
Error executing query 4252: Model abstains from answering the question
Error executing query 4256: Invalid expression / Unexpected token. Line 1, Col: 937.
  ns.hadm_id from admissions where admissions.subject_id = 19155097 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and t1.hadm_id = t3.hadm_id
Error executing query 4258: Invalid expression / Unexpected token. Line 1, Col: 1020.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4259: Model only answers one image question SQLs
Error executing query 4260: Model abstains from answering the question
Error executing query 4262: Model abstains from answering the question
Error executing query 4266: Model abstains from answering the question
Error executing query 4268: Model abstains from answering the question
Error executing query 4270: Model only answers one image question SQLs
Error executing query 4271: Model only answers one image question SQLs
Error executing query 4273: Model only answers one image question SQLs
Error executing query 4275: Model abstains from answering the question
Error executing query 4277: Model abstains from answering the question
Error executing query 4278: Model abstains from answering the question
Error executing query 4279: Invalid expression / Unexpected token. Line 1, Col: 1018.
  egmental collapse in the right upper lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
[True]
Error executing query 4281: near "(": syntax error
Error executing query 4285: Model abstains from answering the question
Error executing query 4286: Invalid expression / Unexpected token. Line 1, Col: 863.
  s.dischtime is not null order by admissions.admittime asc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4289: Model abstains from answering the question
Error executing query 4292: Model abstains from answering the question
Error executing query 4294: Model only answers one image question SQLs
Error executing query 4295: Model abstains from answering the question
Error executing query 4298: Model abstains from answering the question
Error executing query 4300: Expecting ). Line 1, Col: 795.
  etime('2105-12-31 23:59:00','-3 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month') gro
Error executing query 4301: Invalid expression / Unexpected token. Line 1, Col: 785.
  qa("does a chest x-ray depicts any abnormality?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 4302: Model abstains from answering the question
Error executing query 4303: Model abstains from answering the question
Error executing query 4304: Model abstains from answering the question
Error executing query 4305: Invalid expression / Unexpected token. Line 1, Col: 960.
   year','-0 year') and strftime('%m',prescriptions.starttime) = '04' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4306: Expecting ). Line 1, Col: 996.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 4307: Model abstains from answering the question
Error executing query 4309: Model abstains from answering the question
Error executing query 4312: Model abstains from answering the question
Error executing query 4313: Invalid expression / Unexpected token. Line 1, Col: 916.
  c_vqa("does a chest x-ray show any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4314: Invalid expression / Unexpected token. Line 1, Col: 1089.
  .dischtime is not null order by admissions.admittime desc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4315: Model abstains from answering the question
Error executing query 4316: Model abstains from answering the question
[False]
Error executing query 4320: Model only answers one image question SQLs
Error executing query 4321: Expecting ). Line 1, Col: 804.
  '%Y',prescriptions.starttime) = '2101' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 3
Error executing query 4322: Invalid expression / Unexpected token. Line 1, Col: 823.
  %Y',procedures_icd.charttime) = '2103' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
Error executing query 4323: Invalid expression / Unexpected token. Line 1, Col: 1052.
  est x-ray indicate costophrenic angle blunting?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4324: Model only answers one image question SQLs
Error executing query 4328: Invalid expression / Unexpected token. Line 1, Col: 739.
  a("does a chest x-ray indicate any tubes/lines?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 4330: Model abstains from answering the question
Error executing query 4331: Model abstains from answering the question
Error executing query 4333: Invalid expression / Unexpected token. Line 1, Col: 624.
  a("does a chest x-ray show any any tubes/lines?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4334: Model abstains from answering the question
[True]
[True]
Error executing query 4339: Invalid expression / Unexpected token. Line 1, Col: 792.
  5712372 ) and strftime('%Y-%m',prescriptions.starttime) = '2103-10' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4343: Model abstains from answering the question
Error executing query 4345: Model abstains from answering the question
Error executing query 4347: Model only answers one image question SQLs
Error executing query 4349: Model abstains from answering the question
Error executing query 4351: Invalid expression / Unexpected token. Line 1, Col: 837.
   the chest x-ray depicting alveolar hemorrhage?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4352: Invalid expression / Unexpected token. Line 1, Col: 640.
  ns.hadm_id from admissions where admissions.subject_id = 15866760 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4353: Model only answers one image question SQLs
Error executing query 4354: Invalid expression / Unexpected token. Line 1, Col: 782.
  ns.hadm_id from admissions where admissions.subject_id = 12974480 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4355: Model abstains from answering the question
Error executing query 4356: Invalid expression / Unexpected token. Line 1, Col: 640.
  ns.hadm_id from admissions where admissions.subject_id = 16043637 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4357: Model only answers one image question SQLs
Error executing query 4358: Model only answers one image question SQLs
Error executing query 4360: Invalid expression / Unexpected token. Line 1, Col: 877.
  has a chest x-ray shown granulomatous diseases?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4361: Expecting ). Line 1, Col: 647.
  where admissions.age between 30 and 39 ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 4362: Invalid expression / Unexpected token. Line 1, Col: 1000.
  153920 ) and strftime('%Y-%m',procedures_icd.charttime) = '2102-01' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and t1.hadm_id = t3.hadm_id
Error executing query 4363: Model only answers one image question SQLs
Error executing query 4365: Model abstains from answering the question
Error executing query 4366: Model abstains from answering the question
Error executing query 4367: Invalid expression / Unexpected token. Line 1, Col: 980.
  ocedures_icd.charttime) = datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 4368: Model abstains from answering the question
Error executing query 4369: Model abstains from answering the question
Error executing query 4373: Model abstains from answering the question
Error executing query 4374: Model only answers one image question SQLs
Error executing query 4375: Model only answers one image question SQLs
Error executing query 4376: Model only answers one image question SQLs
Error executing query 4378: Model only answers one image question SQLs
[False]
Error executing query 4380: Model abstains from answering the question
Error executing query 4381: Model only answers one image question SQLs
Error executing query 4382: Invalid expression / Unexpected token. Line 1, Col: 741.
  has an x-ray revealed mediastinal displacement?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4383: Invalid expression / Unexpected token. Line 1, Col: 894.
  iagnoses_icd.charttime) = datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 4384: Invalid expression / Unexpected token. Line 1, Col: 941.
  shown in the right chest wall on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4385: Model abstains from answering the question
Error executing query 4387: Model abstains from answering the question
Error executing query 4388: Invalid expression / Unexpected token. Line 1, Col: 805.
  me('2105-12-31 23:59:00','-155 month') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of day') = datetime(t2.starttime,'start of day')
Error executing query 4390: Expecting ). Line 1, Col: 780.
  etime('2105-12-31 23:59:00','-5 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 4391: Invalid expression / Unexpected token. Line 1, Col: 716.
  = 'insertion of two vascular stents' ) ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
Error executing query 4392: Invalid expression / Unexpected token. Line 1, Col: 795.
  a("does a chest x-ray indicate any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4394: Model only answers one image question SQLs
Error executing query 4395: Model abstains from answering the question
Error executing query 4396: Model only answers one image question SQLs
Error executing query 4398: Model abstains from answering the question
Error executing query 4399: Invalid expression / Unexpected token. Line 1, Col: 863.
  ("is the chest x-ray depicting any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4400: Model abstains from answering the question
Error executing query 4401: Model only answers one image question SQLs
Error executing query 4402: Invalid expression / Unexpected token. Line 1, Col: 727.
  %Y',prescriptions.starttime) >= '2103' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month')
Error executing query 4403: Expecting ). Line 1, Col: 867.
  '%Y',prescriptions.starttime) = '2102' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month') gro
Error executing query 4404: Invalid expression / Unexpected token. Line 1, Col: 852.
  a("is the chest x-ray revealing tortuous aorta?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4405: Invalid expression / Unexpected token. Line 1, Col: 828.
  d = 12712004 ) and strftime('%Y',diagnoses_icd.charttime) >= '2105' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4407: Model abstains from answering the question
Error executing query 4408: Model abstains from answering the question
Error executing query 4409: Model only answers one image question SQLs
Error executing query 4410: Model abstains from answering the question
Error executing query 4414: Model abstains from answering the question
Error executing query 4415: Model abstains from answering the question
Error executing query 4416: Invalid expression / Unexpected token. Line 1, Col: 967.
  e any tubes/lines in the left hilar structures?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4419: Model abstains from answering the question
Error executing query 4420: Model abstains from answering the question
Error executing query 4421: Model abstains from answering the question
Error executing query 4422: Model abstains from answering the question
Error executing query 4423: Model only answers one image question SQLs
Error executing query 4425: Model abstains from answering the question
Error executing query 4426: Model abstains from answering the question
Error executing query 4428: Model only answers one image question SQLs
Error executing query 4430: Model abstains from answering the question
Error executing query 4431: Invalid expression / Unexpected token. Line 1, Col: 794.
  escriptions.starttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4433: Model abstains from answering the question
Error executing query 4435: Model abstains from answering the question
Error executing query 4437: Invalid expression / Unexpected token. Line 1, Col: 785.
  ns.hadm_id from admissions where admissions.subject_id = 16484690 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4438: Invalid expression / Unexpected token. Line 1, Col: 1112.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id
Error executing query 4439: Model only answers one image question SQLs
Error executing query 4440: Invalid expression / Unexpected token. Line 1, Col: 864.
  %Y',diagnoses_icd.charttime) >= '2105' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 4441: Invalid expression / Unexpected token. Line 1, Col: 1002.
   year') = datetime('2105-12-31 23:59:00','start of year','-0 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 4442: Model only answers one image question SQLs
Error executing query 4444: Invalid expression / Unexpected token. Line 1, Col: 843.
  a chest x-ray reveal any technical assessments?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4445: Invalid expression / Unexpected token. Line 1, Col: 888.
   = 10452075 ) and strftime('%Y',procedures_icd.charttime) >= '2105' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 4446: Model only answers one image question SQLs
Error executing query 4447: Model abstains from answering the question
Error executing query 4448: Model abstains from answering the question
Error executing query 4450: Model abstains from answering the question
Error executing query 4451: Model abstains from answering the question
Error executing query 4453: Model abstains from answering the question
Error executing query 4456: Model abstains from answering the question
Error executing query 4457: Model abstains from answering the question
Error executing query 4458: Model abstains from answering the question
Error executing query 4459: Expecting ). Line 1, Col: 854.
  %Y',diagnoses_icd.charttime) >= '2105' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 4460: Invalid expression / Unexpected token. Line 1, Col: 895.
  6566006 ) and strftime('%Y-%m',diagnoses_icd.charttime) = '2105-09' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4461: Model abstains from answering the question
Error executing query 4462: Invalid expression / Unexpected token. Line 1, Col: 890.
  a("does a chest x-ray reveal pneumomediastinum?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4463: Model abstains from answering the question
Error executing query 4466: Expecting ). Line 1, Col: 1242.
  ar','-0 year') ) as t2 join admissions on t2.subject_id = admissions.subject_id where t2.charttime  [4madmissions[0m.admittime and datetime(admissions.admittime,'start of year') = datetime('2105-12-31 23:59:00','star
Error executing query 4467: Model abstains from answering the question
Error executing query 4469: Expecting ). Line 1, Col: 741.
  microbiologyevents.charttime) = '2102' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 4470: Model abstains from answering the question
Error executing query 4472: Model only answers one image question SQLs
Error executing query 4474: Model abstains from answering the question
Error executing query 4475: Model abstains from answering the question
Error executing query 4476: Model abstains from answering the question
Error executing query 4477: Model abstains from answering the question
Error executing query 4478: Model abstains from answering the question
Error executing query 4479: Model abstains from answering the question
Error executing query 4480: Invalid expression / Unexpected token. Line 1, Col: 895.
  y show subcutaneous air in the left chest wall?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4482: Invalid expression / Unexpected token. Line 1, Col: 1038.
  t2 where func_vqa("is any abnormality revealed?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4483: Model abstains from answering the question
Error executing query 4485: Model abstains from answering the question
Error executing query 4486: Model abstains from answering the question
Error executing query 4487: Expecting ). Line 1, Col: 826.
  ime('%Y',labevents.charttime) = '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.itemid ) as t3 where t3.c1 = 3 )
Error executing query 4489: Model abstains from answering the question
Error executing query 4491: Model abstains from answering the question
Error executing query 4492: Model only answers one image question SQLs
Error executing query 4493: Model abstains from answering the question
Error executing query 4494: Model abstains from answering the question
Error executing query 4495: Model abstains from answering the question
Error executing query 4500: Model abstains from answering the question
Error executing query 4502: Invalid expression / Unexpected token. Line 1, Col: 889.
   = 16044504 ) and strftime('%Y',procedures_icd.charttime) >= '2105' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 4504: Model only answers one image question SQLs
Error executing query 4506: Model abstains from answering the question
Error executing query 4508: Invalid expression / Unexpected token. Line 1, Col: 641.
  te swan-ganz catheter in the upper mediastinum?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4509: Expecting ). Line 1, Col: 675.
  criptions.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 4511: Model abstains from answering the question
Error executing query 4512: Model abstains from answering the question
Error executing query 4514: Invalid expression / Unexpected token. Line 1, Col: 879.
  ormality in the left clavicle on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4515: Model only answers one image question SQLs
Error executing query 4518: Model abstains from answering the question
Error executing query 4519: near "(": syntax error
Error executing query 4521: Model abstains from answering the question
Error executing query 4522: Model only answers one image question SQLs
Error executing query 4523: Model abstains from answering the question
Error executing query 4524: Model abstains from answering the question
Error executing query 4525: Model only answers one image question SQLs
Error executing query 4526: Expecting ). Line 1, Col: 860.
  etime('2105-12-31 23:59:00','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 4527: Model only answers one image question SQLs
Error executing query 4528: Model abstains from answering the question
Error executing query 4529: Model abstains from answering the question
Error executing query 4531: Model abstains from answering the question
Error executing query 4532: Model only answers one image question SQLs
Error executing query 4533: Model only answers one image question SQLs
Error executing query 4534: Invalid expression / Unexpected token. Line 1, Col: 972.
  picts any abnormality in the upper mediastinum?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 4535: Model only answers one image question SQLs
[True]
Error executing query 4538: Invalid expression / Unexpected token. Line 1, Col: 830.
  ny indication of any diseases on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4539: Invalid expression / Unexpected token. Line 1, Col: 1031.
  own in the cardiac silhouette on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4540: Expecting ). Line 1, Col: 728.
  '%Y',prescriptions.starttime) = '2102' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month') gro
Error executing query 4541: Invalid expression / Unexpected token. Line 1, Col: 952.
  any indication of any devices on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 4542: Model abstains from answering the question
Error executing query 4543: Invalid expression / Unexpected token. Line 1, Col: 738.
  ns.hadm_id from admissions where admissions.subject_id = 15234578 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
[False]
Error executing query 4544: Model abstains from answering the question
Error executing query 4545: Invalid expression / Unexpected token. Line 1, Col: 980.
   year') = datetime('2105-12-31 23:59:00','start of year','-0 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4547: Model abstains from answering the question
Error executing query 4548: Model abstains from answering the question
Error executing query 4549: Model abstains from answering the question
Error executing query 4550: Invalid expression / Unexpected token. Line 1, Col: 881.
  ny abnormality in the trachea on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4551: Model abstains from answering the question
Error executing query 4552: Model abstains from answering the question
Error executing query 4553: Invalid expression / Unexpected token. Line 1, Col: 890.
  %Y',procedures_icd.charttime) = '2100' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 4554: Model abstains from answering the question
Error executing query 4556: Invalid expression / Unexpected token. Line 1, Col: 870.
  id = 14097607 ) and strftime('%Y',diagnoses_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 4557: Model abstains from answering the question
Error executing query 4559: Model abstains from answering the question
Error executing query 4561: Model abstains from answering the question
Error executing query 4562: Model abstains from answering the question
Error executing query 4564: Model only answers one image question SQLs
Error executing query 4565: Model abstains from answering the question
Error executing query 4567: Model abstains from answering the question
Error executing query 4569: Invalid expression / Unexpected token. Line 1, Col: 889.
  t2 where func_vqa("is any abnormality revealed?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4571: Invalid expression / Unexpected token. Line 1, Col: 886.
  es an x-ray reveal any diseases in the trachea?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4572: Expecting ). Line 1, Col: 830.
  '%Y',diagnoses_icd.charttime) = '2102' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 4574: Model abstains from answering the question
Error executing query 4576: near "(": syntax error
Error executing query 4577: Model only answers one image question SQLs
Error executing query 4578: Invalid expression / Unexpected token. Line 1, Col: 885.
  s.dischtime is not null order by admissions.admittime asc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4579: Invalid expression / Unexpected token. Line 1, Col: 768.
  etime('2105-12-31 23:59:00','-3 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month')
Error executing query 4582: Model abstains from answering the question
Error executing query 4584: Model abstains from answering the question
Error executing query 4587: Model abstains from answering the question
Error executing query 4588: Invalid expression / Unexpected token. Line 1, Col: 778.
  func_vqa("does a chest x-ray show any diseases?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4590: Invalid expression / Unexpected token. Line 1, Col: 976.
  unc_vqa("does a chest x-ray reveal any devices?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4593: Expecting ). Line 1, Col: 718.
  labevents.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.itemid ) as t3 where t3.c1 = 3 )
Error executing query 4595: Model abstains from answering the question
Error executing query 4596: Model abstains from answering the question
Error executing query 4597: Model abstains from answering the question
Error executing query 4599: Model abstains from answering the question
Error executing query 4600: Model abstains from answering the question
Error executing query 4603: Invalid expression / Unexpected token. Line 1, Col: 843.
  y technical assessments in the left chest wall?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4604: Model abstains from answering the question
Error executing query 4606: Expecting ). Line 1, Col: 870.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 4608: Model abstains from answering the question
Error executing query 4611: Invalid expression / Unexpected token. Line 1, Col: 755.
  id = 15319241 ) and strftime('%Y',prescriptions.starttime) = '2105' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 4612: Model only answers one image question SQLs
Error executing query 4613: Model only answers one image question SQLs
Error executing query 4614: Model only answers one image question SQLs
Error executing query 4615: Invalid expression / Unexpected token. Line 1, Col: 968.
  te any tubes/lines in the left lower lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4616: Model only answers one image question SQLs
Error executing query 4618: Invalid expression / Unexpected token. Line 1, Col: 936.
  icated in the left lower lung zone on an x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
[False]
[False]
Error executing query 4621: Model abstains from answering the question
Error executing query 4622: Model abstains from answering the question
Error executing query 4623: Invalid expression / Unexpected token. Line 1, Col: 751.
  id = 13888167 ) and strftime('%Y',prescriptions.starttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 4624: Model abstains from answering the question
Error executing query 4625: Invalid expression / Unexpected token. Line 1, Col: 1072.
   year','-0 year') and strftime('%m',diagnoses_icd.charttime) = '12' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
[True]
Error executing query 4628: Invalid expression / Unexpected token. Line 1, Col: 660.
  ns.hadm_id from admissions where admissions.subject_id = 14880685 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4631: Model abstains from answering the question
Error executing query 4632: Model abstains from answering the question
Error executing query 4633: Model abstains from answering the question
Error executing query 4636: Model only answers one image question SQLs
Error executing query 4640: Expecting ). Line 1, Col: 840.
  microbiologyevents.charttime) = '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.test_name ) as t3 where t3.c1 = 4
Error executing query 4642: Model abstains from answering the question
Error executing query 4644: Expecting ). Line 1, Col: 785.
  '%Y',prescriptions.starttime) = '2102' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 4
Error executing query 4646: Invalid expression / Unexpected token. Line 1, Col: 637.
  ns.hadm_id from admissions where admissions.subject_id = 17622334 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4648: Model only answers one image question SQLs
Error executing query 4649: Model abstains from answering the question
Error executing query 4651: Expecting ). Line 1, Col: 1157.
  imit 1 ) order by tb_cxr.studydatetime asc limit 1 ) ) ) order by tb_cxr.studydatetime desc limit 1 [4m)[0m
Error executing query 4652: Invalid expression / Unexpected token. Line 1, Col: 886.
  ime('2105-12-31 23:59:00','-81 month') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id
Error executing query 4654: Model only answers one image question SQLs
Error executing query 4655: Model only answers one image question SQLs
Error executing query 4657: Invalid expression / Unexpected token. Line 1, Col: 879.
  d = 18956189 ) and strftime('%Y',procedures_icd.charttime) = '2101' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 4658: Model abstains from answering the question
Error executing query 4659: Model only answers one image question SQLs
Error executing query 4660: Model abstains from answering the question
Error executing query 4663: Model only answers one image question SQLs
Error executing query 4667: Model only answers one image question SQLs
Error executing query 4669: Model only answers one image question SQLs
Error executing query 4670: near "(": syntax error
Error executing query 4671: Expecting ). Line 1, Col: 1130.
  it 1 ) order by tb_cxr.studydatetime asc limit 1 ) ) ) order by tb_cxr.studydatetime desc limit 1 ) [4mas[0m
Error executing query 4672: Model only answers one image question SQLs
Error executing query 4673: Model only answers one image question SQLs
Error executing query 4675: Model abstains from answering the question
Error executing query 4676: Invalid expression / Unexpected token. Line 1, Col: 1032.
  .dischtime is not null order by admissions.admittime desc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4677: Model only answers one image question SQLs
Error executing query 4678: Model abstains from answering the question
Error executing query 4680: Model abstains from answering the question
Error executing query 4681: Model abstains from answering the question
Error executing query 4682: Model only answers one image question SQLs
Error executing query 4684: Expecting ). Line 1, Col: 978.
  here prescriptions.drug = 'zidovudine' ) as t3 on t2.subject_id = t3.subject_id where t2.charttime  [4mt3[0m.starttime ) as t4 join patients on t4.subject_id = patients.subject_id
Error executing query 4685: Invalid expression / Unexpected token. Line 1, Col: 746.
  normality indicated in the abdomen on an x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4689: Model abstains from answering the question
Error executing query 4691: Model only answers one image question SQLs
Error executing query 4692: Model abstains from answering the question
Error executing query 4693: Model abstains from answering the question
Error executing query 4694: Model abstains from answering the question
Error executing query 4697: Model abstains from answering the question
Error executing query 4699: Invalid expression / Unexpected token. Line 1, Col: 759.
  atomical findings in the right upper lung zone?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4700: Model only answers one image question SQLs
Error executing query 4702: Model only answers one image question SQLs
Error executing query 4703: Invalid expression / Unexpected token. Line 1, Col: 837.
   where func_vqa("is any abnormality identified?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4705: Model abstains from answering the question
Error executing query 4707: Model abstains from answering the question
Error executing query 4709: Model abstains from answering the question
Error executing query 4711: Model abstains from answering the question
Error executing query 4712: Invalid expression / Unexpected token. Line 1, Col: 954.
  cedures_icd.charttime) >= datetime('2105-12-31 23:59:00','-5 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 4713: Model abstains from answering the question
Error executing query 4714: Model abstains from answering the question
Error executing query 4715: Invalid expression / Unexpected token. Line 1, Col: 831.
  escriptions.starttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 4717: Model only answers one image question SQLs
Error executing query 4718: Invalid expression / Unexpected token. Line 1, Col: 1122.
  year','-1 year') and strftime('%m',procedures_icd.charttime) = '02' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.
Error executing query 4721: Model abstains from answering the question
Error executing query 4723: Model abstains from answering the question
Error executing query 4724: Model abstains from answering the question
Error executing query 4725: Invalid expression / Unexpected token. Line 1, Col: 649.
  strated lung cancer in the right mid lung zone?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4727: Model abstains from answering the question
Error executing query 4728: Model only answers one image question SQLs
Error executing query 4730: Expecting ). Line 1, Col: 990.
  scriptions.drug = 'alendronate sodium' ) as t3 on t2.subject_id = t3.subject_id where t2.charttime  [4mt3[0m.starttime ) as t4 join patients on t4.subject_id = patients.subject_id
Error executing query 4732: Model abstains from answering the question
Error executing query 4734: Invalid expression / Unexpected token. Line 1, Col: 870.
  unc_vqa("has a chest x-ray shown consolidation?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4735: Model abstains from answering the question
Error executing query 4736: Model abstains from answering the question
Error executing query 4737: Invalid expression / Unexpected token. Line 1, Col: 790.
  escriptions.starttime) >= datetime('2105-12-31 23:59:00','-2 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 4738: Model abstains from answering the question
Error executing query 4739: Invalid expression / Unexpected token. Line 1, Col: 646.
  ns.hadm_id from admissions where admissions.subject_id = 17931647 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 4740: Model abstains from answering the question
Error executing query 4741: Model abstains from answering the question
Error executing query 4742: Model only answers one image question SQLs
Error executing query 4745: Model abstains from answering the question
Error executing query 4746: Model abstains from answering the question
Error executing query 4747: Model only answers one image question SQLs
Error executing query 4748: Model abstains from answering the question
Error executing query 4749: Model abstains from answering the question
Error executing query 4751: Invalid expression / Unexpected token. Line 1, Col: 781.
  a("does a chest x-ray indicate any tubes/lines?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4752: Model abstains from answering the question
Error executing query 4753: Invalid expression / Unexpected token. Line 1, Col: 881.
  noses_icd.charttime) >= datetime('2105-12-31 23:59:00','-16 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4754: Model only answers one image question SQLs
Error executing query 4755: Model abstains from answering the question
[False]
Error executing query 4758: Invalid expression / Unexpected token. Line 1, Col: 744.
  ns.hadm_id from admissions where admissions.subject_id = 17442326 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4759: Invalid expression / Unexpected token. Line 1, Col: 858.
  id = 18843391 ) and strftime('%Y',diagnoses_icd.charttime) = '2102' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 4761: Model abstains from answering the question
Error executing query 4762: Model only answers one image question SQLs
Error executing query 4763: Invalid expression / Unexpected token. Line 1, Col: 763.
  ns.hadm_id from admissions where admissions.subject_id = 13778342 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 4764: Model only answers one image question SQLs
Error executing query 4765: Model only answers one image question SQLs
Error executing query 4766: Model abstains from answering the question
[False]
[False]
Error executing query 4770: Model abstains from answering the question
Error executing query 4772: Invalid expression / Unexpected token. Line 1, Col: 776.
  abg grafts in the mediastinum on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4773: Invalid expression / Unexpected token. Line 1, Col: 751.
  rved in the right apical zone on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4774: Model only answers one image question SQLs
Error executing query 4775: Invalid expression / Unexpected token. Line 1, Col: 1082.
  year','-1 year') and strftime('%m',procedures_icd.charttime) = '06' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4778: Model abstains from answering the question
Error executing query 4779: Invalid expression / Unexpected token. Line 1, Col: 772.
  ns.hadm_id from admissions where admissions.subject_id = 12645334 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 4780: Model abstains from answering the question
Error executing query 4781: Model only answers one image question SQLs
Error executing query 4782: Model only answers one image question SQLs
Error executing query 4783: Model abstains from answering the question
Error executing query 4784: Model only answers one image question SQLs
Error executing query 4785: Model abstains from answering the question
Error executing query 4786: Model abstains from answering the question
Error executing query 4787: Invalid expression / Unexpected token. Line 1, Col: 731.
  ns.hadm_id from admissions where admissions.subject_id = 12974480 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4788: Expecting ). Line 1, Col: 836.
  etime('2105-12-31 23:59:00','-3 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 4789: Model only answers one image question SQLs
Error executing query 4791: Expecting ). Line 1, Col: 984.
  ptions.drug = 'hydrocortisone acetate' ) as t3 on t2.subject_id = t3.subject_id where t2.charttime  [4mt3[0m.starttime ) as t4 join patients on t4.subject_id = patients.subject_id
Error executing query 4792: Model only answers one image question SQLs
Error executing query 4793: Model abstains from answering the question
Error executing query 4795: Invalid expression / Unexpected token. Line 1, Col: 797.
  ns.hadm_id from admissions where admissions.subject_id = 18970393 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4796: Model only answers one image question SQLs
Error executing query 4798: Model abstains from answering the question
Error executing query 4804: Model abstains from answering the question
Error executing query 4805: Model only answers one image question SQLs
Error executing query 4806: Model abstains from answering the question
Error executing query 4807: Model abstains from answering the question
Error executing query 4808: Model abstains from answering the question
Error executing query 4809: Model abstains from answering the question
Error executing query 4811: Invalid expression / Unexpected token. Line 1, Col: 867.
  t x-ray depicting pulmonary edema/hazy opacity?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4812: Model abstains from answering the question
Error executing query 4813: Model abstains from answering the question
Error executing query 4816: Model abstains from answering the question
Error executing query 4817: Invalid expression / Unexpected token. Line 1, Col: 847.
  a chest x-ray reveal any technical assessments?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4818: Model abstains from answering the question
Error executing query 4819: Model only answers one image question SQLs
Error executing query 4820: Model abstains from answering the question
Error executing query 4821: Model abstains from answering the question
Error executing query 4823: Model only answers one image question SQLs
Error executing query 4824: Invalid expression / Unexpected token. Line 1, Col: 899.
  has a chest x-ray shown elevated hemidiaphragm?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4825: Model only answers one image question SQLs
Error executing query 4827: Invalid expression / Unexpected token. Line 1, Col: 763.
  atomical findings in the neck on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4828: Invalid expression / Unexpected token. Line 1, Col: 898.
  44092 ) and strftime('%Y-%m',procedures_icd.charttime) >= '2105-12' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4829: Model abstains from answering the question
Error executing query 4831: Model abstains from answering the question
Error executing query 4833: Model abstains from answering the question
Error executing query 4836: Model only answers one image question SQLs
Error executing query 4837: Model abstains from answering the question
Error executing query 4838: Model only answers one image question SQLs
Error executing query 4839: Model abstains from answering the question
Error executing query 4840: Invalid expression / Unexpected token. Line 1, Col: 932.
  gnoses_icd.charttime) = datetime('2105-12-31 23:59:00','-33 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4841: Model abstains from answering the question
Error executing query 4842: Invalid expression / Unexpected token. Line 1, Col: 730.
  d = 10463724 ) and strftime('%Y',prescriptions.starttime) >= '2104' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 4845: Invalid expression / Unexpected token. Line 1, Col: 736.
  vqa("is any abnormality shown on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4847: Invalid expression / Unexpected token. Line 1, Col: 670.
  ns.hadm_id from admissions where admissions.subject_id = 19155097 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 4848: Invalid expression / Unexpected token. Line 1, Col: 751.
  lines indicated in the aortic arch on an x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4849: Expecting ). Line 1, Col: 885.
  '%Y',prescriptions.starttime) = '2102' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month') gro
Error executing query 4851: Model abstains from answering the question
Error executing query 4852: Invalid expression / Unexpected token. Line 1, Col: 872.
  _vqa("is the chest x-ray revealing cabg grafts?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4853: Model abstains from answering the question
Error executing query 4855: Model abstains from answering the question
Error executing query 4856: Model only answers one image question SQLs
Error executing query 4858: Model abstains from answering the question
Error executing query 4859: Model only answers one image question SQLs
Error executing query 4860: Model abstains from answering the question
Error executing query 4861: Invalid expression / Unexpected token. Line 1, Col: 930.
  n in the left upper lung zone on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4862: Model abstains from answering the question
Error executing query 4863: Model abstains from answering the question
Error executing query 4868: Model abstains from answering the question
Error executing query 4869: Model abstains from answering the question
Error executing query 4871: Model abstains from answering the question
Error executing query 4873: Model only answers one image question SQLs
Error executing query 4875: Model only answers one image question SQLs
Error executing query 4876: Model abstains from answering the question
Error executing query 4878: Invalid expression / Unexpected token. Line 1, Col: 927.
  natomical findings in the left lower lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4879: Model only answers one image question SQLs
Error executing query 4880: Model abstains from answering the question
Error executing query 4882: Model abstains from answering the question
Error executing query 4883: Model only answers one image question SQLs
Error executing query 4885: Expecting ). Line 1, Col: 847.
  etime('2105-12-31 23:59:00','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 4888: Model abstains from answering the question
Error executing query 4889: Model abstains from answering the question
Error executing query 4890: Model abstains from answering the question
Error executing query 4891: Invalid expression / Unexpected token. Line 1, Col: 737.
  id = 16306505 ) and strftime('%Y',prescriptions.starttime) = '2102' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 4894: Model abstains from answering the question
Error executing query 4895: Invalid expression / Unexpected token. Line 1, Col: 735.
  id = 17454400 ) and strftime('%Y',prescriptions.starttime) = '2105' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4896: Model abstains from answering the question
Error executing query 4897: Model only answers one image question SQLs
Error executing query 4898: Model only answers one image question SQLs
Error executing query 4902: Model abstains from answering the question
Error executing query 4904: Model abstains from answering the question
Error executing query 4906: Model abstains from answering the question
Error executing query 4907: Model abstains from answering the question
Error executing query 4908: Invalid expression / Unexpected token. Line 1, Col: 924.
  id = 19090380 ) and strftime('%Y',diagnoses_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 4909: Model abstains from answering the question
Error executing query 4910: Expecting ). Line 1, Col: 968.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 4911: Invalid expression / Unexpected token. Line 1, Col: 636.
  a("does a chest x-ray show any any abnormality?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 4913: Invalid expression / Unexpected token. Line 1, Col: 784.
  er by admissions.admittime asc limit 1 ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of day') = datetime(t2.starttime,'start of day')
Error executing query 4915: Model only answers one image question SQLs
Error executing query 4916: Model abstains from answering the question
Error executing query 4917: Invalid expression / Unexpected token. Line 1, Col: 873.
  a("does a chest x-ray indicate any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4918: Model abstains from answering the question
[False]
Error executing query 4920: near "(": syntax error
Error executing query 4921: Model abstains from answering the question
Error executing query 4924: Model abstains from answering the question
[True]
[True]
Error executing query 4926: Expecting ). Line 1, Col: 995.
  s.drug = 'ns epidural bag (0.9% nacl)' ) as t3 on t2.subject_id = t3.subject_id where t2.charttime  [4mt3[0m.starttime ) as t4 join patients on t4.subject_id = patients.subject_id
Error executing query 4928: Invalid expression / Unexpected token. Line 1, Col: 884.
  any diseases revealed in the upper mediastinum?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4929: Model only answers one image question SQLs
Error executing query 4930: Invalid expression / Unexpected token. Line 1, Col: 844.
  id = 15583423 ) and strftime('%Y',diagnoses_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 4933: Invalid expression / Unexpected token. Line 1, Col: 838.
  id = 17454400 ) and strftime('%Y',diagnoses_icd.charttime) = '2105' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4934: Model only answers one image question SQLs
Error executing query 4935: Model abstains from answering the question
Error executing query 4936: Invalid expression / Unexpected token. Line 1, Col: 765.
  ns.hadm_id from admissions where admissions.subject_id = 19261953 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 4937: Model abstains from answering the question
Error executing query 4939: Invalid expression / Unexpected token. Line 1, Col: 1005.
  186925 ) and strftime('%Y-%m',procedures_icd.charttime) = '2103-05' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and t1.hadm_id = t3.hadm_id
Error executing query 4941: Model abstains from answering the question
Error executing query 4942: Invalid expression / Unexpected token. Line 1, Col: 961.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
Error executing query 4945: Model abstains from answering the question
Error executing query 4947: Model only answers one image question SQLs
Error executing query 4948: Invalid expression / Unexpected token. Line 1, Col: 854.
  d = 14611780 ) and strftime('%Y',procedures_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4949: Model only answers one image question SQLs
Error executing query 4952: Model abstains from answering the question
[False]
Error executing query 4958: Invalid expression / Unexpected token. Line 1, Col: 775.
  ns.hadm_id from admissions where admissions.subject_id = 17421577 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4960: Model abstains from answering the question
Error executing query 4961: Invalid expression / Unexpected token. Line 1, Col: 891.
  ved in the left hemidiaphragm on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4963: Model only answers one image question SQLs
Error executing query 4964: Model abstains from answering the question
Error executing query 4965: Model abstains from answering the question
Error executing query 4966: Model abstains from answering the question
Error executing query 4967: Invalid expression / Unexpected token. Line 1, Col: 919.
  c_vqa("is enlarged hilum indicated on an x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4968: Model abstains from answering the question
Error executing query 4969: Invalid expression / Unexpected token. Line 1, Col: 787.
  escriptions.starttime) >= datetime('2105-12-31 23:59:00','-2 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 4970: Model abstains from answering the question
Error executing query 4971: Invalid expression / Unexpected token. Line 1, Col: 932.
  dicate lung cancer in the left upper lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4973: Model only answers one image question SQLs
Error executing query 4975: Expecting ). Line 1, Col: 513.
  criptions.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.starttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.starttime) and datetime(t1.starttime,'+2 m
Error executing query 4976: Model abstains from answering the question
Error executing query 4977: Model abstains from answering the question
Error executing query 4978: Invalid expression / Unexpected token. Line 1, Col: 734.
  2250544 ) and strftime('%Y-%m',prescriptions.starttime) = '2104-12' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 4979: Invalid expression / Unexpected token. Line 1, Col: 889.
  d = 12645334 ) and strftime('%Y',diagnoses_icd.charttime) >= '2105' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 4980: Model abstains from answering the question
Error executing query 4981: Invalid expression / Unexpected token. Line 1, Col: 760.
  indication of any abnormality on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 4985: Model abstains from answering the question
Error executing query 4987: Model abstains from answering the question
Error executing query 4988: Model only answers one image question SQLs
Error executing query 4990: Model only answers one image question SQLs
Error executing query 4994: Model abstains from answering the question
Error executing query 4995: Invalid expression / Unexpected token. Line 1, Col: 921.
  vqa("does a chest x-ray show mediastinal drain?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 4996: Expecting ). Line 1, Col: 949.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 4998: Model only answers one image question SQLs
Error executing query 4999: Invalid expression / Unexpected token. Line 1, Col: 813.
  escriptions.starttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 5001: Invalid expression / Unexpected token. Line 1, Col: 801.
  s in the left lower lung zone on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 5003: Invalid expression / Unexpected token. Line 1, Col: 1019.
  c_vqa("does a chest x-ray indicate any devices?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 5004: Model only answers one image question SQLs
Error executing query 5006: Model abstains from answering the question
Error executing query 5007: near "(": syntax error
Error executing query 5008: Invalid expression / Unexpected token. Line 1, Col: 853.
  unc_vqa("has an x-ray revealed any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 5009: Model abstains from answering the question
Error executing query 5010: Model only answers one image question SQLs
Error executing query 5011: Invalid expression / Unexpected token. Line 1, Col: 889.
  w any abnormality in the right upper lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 5012: Model abstains from answering the question
Error executing query 5014: Model abstains from answering the question
Error executing query 5016: Model abstains from answering the question
Error executing query 5019: Model only answers one image question SQLs
Error executing query 5020: Model only answers one image question SQLs
Error executing query 5021: Model only answers one image question SQLs
Error executing query 5022: Invalid expression / Unexpected token. Line 1, Col: 786.
  ns.hadm_id from admissions where admissions.subject_id = 12408912 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 5025: Model abstains from answering the question
Error executing query 5026: Invalid expression / Unexpected token. Line 1, Col: 909.
  iagnoses_icd.charttime) = datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 5028: Model only answers one image question SQLs
Error executing query 5030: Model abstains from answering the question
Error executing query 5031: Model abstains from answering the question
Error executing query 5033: Invalid expression / Unexpected token. Line 1, Col: 785.
  does the chest x-ray indicate any any diseases?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 5035: Model abstains from answering the question
Error executing query 5036: Model only answers one image question SQLs
Error executing query 5037: Model abstains from answering the question
Error executing query 5038: Model abstains from answering the question
Error executing query 5039: Invalid expression / Unexpected token. Line 1, Col: 803.
  me('2105-12-31 23:59:00','-165 month') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 d
Error executing query 5040: Model only answers one image question SQLs
Error executing query 5041: Model abstains from answering the question
Error executing query 5043: Model abstains from answering the question
Error executing query 5047: Model abstains from answering the question
Error executing query 5048: Model only answers one image question SQLs
Error executing query 5049: Model only answers one image question SQLs
Error executing query 5051: Invalid expression / Unexpected token. Line 1, Col: 406.
  'arterial blood pressure diastolic' and d_items.linksto = 'chartevents' ) and chartevents.valuenum  [4m62.0[0m and strftime('%Y-%m-%d',chartevents.charttime) = '2103-12-25'
Error executing query 5052: Model only answers one image question SQLs
Error executing query 5053: Invalid expression / Unexpected token. Line 1, Col: 983.
   year','-1 year') and strftime('%m',prescriptions.starttime) = '09' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 5054: Model abstains from answering the question
Error executing query 5055: Model abstains from answering the question
Error executing query 5056: Invalid expression / Unexpected token. Line 1, Col: 907.
   vascular redistribution indicated on an x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 5059: Model only answers one image question SQLs
Error executing query 5060: Model only answers one image question SQLs
Error executing query 5061: Model only answers one image question SQLs
Error executing query 5066: Model abstains from answering the question
Error executing query 5067: Expecting ). Line 1, Col: 608.
  criptions.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 5069: Model abstains from answering the question
Error executing query 5070: Model only answers one image question SQLs
Error executing query 5071: Model abstains from answering the question
Error executing query 5072: Invalid expression / Unexpected token. Line 1, Col: 734.
  _vqa("is a chest x-ray showing any abnormality?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 5075: Expecting ). Line 1, Col: 918.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 5076: Invalid expression / Unexpected token. Line 1, Col: 999.
  nth') = datetime('2105-12-31 23:59:00','start of month','-1 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 5077: Model abstains from answering the question
Error executing query 5079: Invalid expression / Unexpected token. Line 1, Col: 861.
   = 10938464 ) and strftime('%Y',procedures_icd.charttime) >= '2105' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 5080: Invalid expression / Unexpected token. Line 1, Col: 665.
  ns.hadm_id from admissions where admissions.subject_id = 15956135 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 5081: Model abstains from answering the question
Error executing query 5083: Model abstains from answering the question
Error executing query 5084: Model abstains from answering the question
Error executing query 5085: Invalid expression / Unexpected token. Line 1, Col: 733.
  ("is the chest x-ray depicting any tubes/lines?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 5086: Model abstains from answering the question
Error executing query 5087: Model abstains from answering the question
Error executing query 5088: Model abstains from answering the question
Error executing query 5090: Model abstains from answering the question
Error executing query 5091: Model only answers one image question SQLs
Error executing query 5093: Invalid expression / Unexpected token. Line 1, Col: 942.
  d any anatomical findings in the left shoulder?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 5094: Model abstains from answering the question
Error executing query 5096: Model abstains from answering the question
Error executing query 5098: Model only answers one image question SQLs
Error executing query 5099: Model abstains from answering the question
Error executing query 5100: Model abstains from answering the question
Error executing query 5101: Model abstains from answering the question
Error executing query 5102: Model only answers one image question SQLs
Error executing query 5103: Model abstains from answering the question
Error executing query 5104: Model abstains from answering the question
Error executing query 5106: Model abstains from answering the question
Error executing query 5107: Model only answers one image question SQLs
Error executing query 5108: Model only answers one image question SQLs
Error executing query 5109: Model only answers one image question SQLs
Error executing query 5110: Invalid expression / Unexpected token. Line 1, Col: 879.
   of any technical assessments on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 5111: Model abstains from answering the question
Error executing query 5112: Model abstains from answering the question
Error executing query 5113: Model abstains from answering the question
Error executing query 5114: Invalid expression / Unexpected token. Line 1, Col: 983.
  nth') = datetime('2105-12-31 23:59:00','start of month','-0 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 5115: Invalid expression / Unexpected token. Line 1, Col: 717.
  c_vqa("does a chest x-ray show any tubes/lines?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 5116: Expecting ). Line 1, Col: 978.
  iptions.drug = 'lidocaine 5% ointment' ) as t3 on t2.subject_id = t3.subject_id where t2.charttime  [4mt3[0m.starttime ) as t4 join patients on t4.subject_id = patients.subject_id
Error executing query 5117: Model only answers one image question SQLs
Error executing query 5119: Model abstains from answering the question
Error executing query 5121: Invalid expression / Unexpected token. Line 1, Col: 804.
  ns.hadm_id from admissions where admissions.subject_id = 16043637 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 5122: Model only answers one image question SQLs
Error executing query 5123: Invalid expression / Unexpected token. Line 1, Col: 849.
  vqa("does a chest x-ray reveal any tubes/lines?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 5124: Expecting ). Line 1, Col: 817.
  etime('2105-12-31 23:59:00','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 5126: Model abstains from answering the question
Error executing query 5127: Model abstains from answering the question
Error executing query 5129: Model abstains from answering the question
Error executing query 5130: Model only answers one image question SQLs
[False]
Error executing query 5132: Model only answers one image question SQLs
Error executing query 5133: Invalid expression / Unexpected token. Line 1, Col: 853.
  a("has a chest x-ray shown vascular congestion?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 5134: Model only answers one image question SQLs
Error executing query 5135: Model abstains from answering the question
Error executing query 5136: Model only answers one image question SQLs
Error executing query 5137: Model abstains from answering the question
Error executing query 5138: Model abstains from answering the question
Error executing query 5139: Model abstains from answering the question
Error executing query 5141: Model only answers one image question SQLs
Error executing query 5142: Model abstains from answering the question
Error executing query 5143: Model abstains from answering the question
Error executing query 5146: Invalid expression / Unexpected token. Line 1, Col: 900.
  y reveal any tubes/lines in the right shoulder?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 5149: Invalid expression / Unexpected token. Line 1, Col: 1048.
  ing linear/patchy atelectasis in the left lung?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 5151: Model abstains from answering the question
Error executing query 5154: Model only answers one image question SQLs
Error executing query 5155: Model only answers one image question SQLs
Error executing query 5156: Model only answers one image question SQLs
Error executing query 5157: Model abstains from answering the question
Error executing query 5158: Model abstains from answering the question
Error executing query 5161: Invalid expression / Unexpected token. Line 1, Col: 735.
  250544 ) and strftime('%Y-%m',prescriptions.starttime) >= '2104-04' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 5163: Invalid expression / Unexpected token. Line 1, Col: 664.
  ns.hadm_id from admissions where admissions.subject_id = 11119441 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 5164: Invalid expression / Unexpected token. Line 1, Col: 935.
  edures_icd.charttime) = datetime('2105-12-31 23:59:00','-27 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 5165: Invalid expression / Unexpected token. Line 1, Col: 820.
  escriptions.starttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 5166: Model abstains from answering the question
[False]
Error executing query 5168: Model abstains from answering the question
Error executing query 5169: Invalid expression / Unexpected token. Line 1, Col: 739.
  normality observed in the svc on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Correct count: 1158
Wrong count: 175
Correct count image: 78
Wrong count image: 55
Image questions: 3318
```
wandb: - 0.005 MB of 0.005 MB uploadedwandb: \ 0.005 MB of 0.461 MB uploadedwandb: | 0.461 MB of 0.461 MB uploadedwandb: / 0.461 MB of 0.461 MB uploadedwandb: 
wandb: Run history:
wandb: accuracy ▁
wandb: 
wandb: Run summary:
wandb: accuracy 0.24507
wandb: 
wandb: 🚀 View run test_final_08-0 at: https://wandb.ai/kobomao/ML_healthcare/runs/rwcoy6ck
wandb: ⭐️ View project at: https://wandb.ai/kobomao/ML_healthcare
wandb: Synced 5 W&B file(s), 0 media file(s), 0 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20240604_131955-rwcoy6ck/logs

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21909966: <test_final_08_0> in cluster <dcc> Done

Job <test_final_08_0> was submitted from host <n-62-30-3> by user <s183914> in cluster <dcc> at Tue Jun  4 10:34:35 2024
Job was executed on host(s) <4*n-62-11-14>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue Jun  4 13:19:34 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_final/ML_final> was used as the working directory.
Started at Tue Jun  4 13:19:34 2024
Terminated at Tue Jun  4 15:00:35 2024
Results reported at Tue Jun  4 15:00:35 2024

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

    CPU time :                                   6458.07 sec.
    Max Memory :                                 18923 MB
    Average Memory :                             13734.40 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               46613.00 MB
    Max Swap :                                   -
    Max Processes :                              6
    Max Threads :                                67
    Run time :                                   6063 sec.
    Turnaround time :                            15960 sec.

The output (if any) is above this job summary.

