2024-06-03 16:52:05.360164: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.17.0
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_final/ML_final/wandb/run-20240603_165218-o8y7tfae
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run eval_fulla40-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/o8y7tfae
2024-06-03 16:52:35.241210: W tensorflow/core/common_runtime/gpu/gpu_device.cc:2251] Cannot dlopen some GPU libraries. Please make sure the missing libraries mentioned above are installed properly if you would like to use GPU. Follow the guide at https://www.tensorflow.org/install/gpu for how to download and setup the required libraries for your platform.
Skipping registering GPU devices...
2024-06-03 16:52:40.653328: W external/xla/xla/service/gpu/nvptx_compiler.cc:760] The NVIDIA driver's CUDA version is 12.4 which is older than the ptxas CUDA version (12.5.40). Because the driver is older than the ptxas version, XLA is disabling parallel compilation, which may slow down compilation. You should update your NVIDIA driver or use the NVIDIA-provided CUDA forward compatibility packages.

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
| <c>name</c>       | <d>str</d>        | <j>"eval_fulla40-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>3600</f>       |
| <c>vqa_module_type</c>| <d>str</d>        | <j>"custom"</j>   |

# Output

```
sid_to_ipath_map loaded. (1896 entries)
Error executing query 1: Invalid expression / Unexpected token. Line 1, Col: 651.
  ns.hadm_id from admissions where admissions.subject_id = 12252397 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 2: Answer count mismatch: 4 != 2
Error executing query 3: Invalid expression / Unexpected token. Line 1, Col: 914.
  func_vqa("does a chest x-ray show any diseases?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
['null']
Error executing query 5: Unexpected answer type: <class 'str'>
['null']
Error executing query 9: Unexpected answer type: <class 'str'>
['null']
Error executing query 10: Unexpected answer type: <class 'str'>
['null']
Error executing query 11: Unexpected answer type: <class 'str'>
Error executing query 12: Answer count mismatch: 4 != 8
Error executing query 14: Answer count mismatch: 4 != 6
['null']
Error executing query 16: Unexpected answer type: <class 'str'>
Error executing query 17: Invalid expression / Unexpected token. Line 1, Col: 958.
  nth') = datetime('2105-12-31 23:59:00','start of month','-0 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
['null']
Error executing query 19: Unexpected answer type: <class 'str'>
['null']
Error executing query 23: Unexpected answer type: <class 'str'>
['null']
Error executing query 24: Unexpected answer type: <class 'str'>
['null']
Error executing query 25: Unexpected answer type: <class 'str'>
Error executing query 26: Invalid expression / Unexpected token. Line 1, Col: 821.
  escriptions.starttime) >= datetime('2105-12-31 23:59:00','-5 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 29: Answer count mismatch: 4 != 28
Error executing query 33: Invalid expression / Unexpected token. Line 1, Col: 914.
  dures_icd.charttime) >= datetime('2105-12-31 23:59:00','-12 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 34: Answer count mismatch: 4 != 32
Error executing query 35: Answer count mismatch: 4 != 32
['null']
Error executing query 37: Unexpected answer type: <class 'str'>
['null']
Error executing query 40: Unexpected answer type: <class 'str'>
Error executing query 41: Invalid expression / Unexpected token. Line 1, Col: 779.
  aling copd/emphysema in the left mid lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 42: Invalid expression / Unexpected token. Line 1, Col: 777.
  _vqa("is a chest x-ray showing any abnormality?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
['null']
Error executing query 43: Unexpected answer type: <class 'str'>
['null']
Error executing query 44: Unexpected answer type: <class 'str'>
['null']
Error executing query 46: Unexpected answer type: <class 'str'>
['null']
Error executing query 50: Unexpected answer type: <class 'str'>
Error executing query 52: near "(": syntax error
Error executing query 53: Answer count mismatch: 4 != 32
Error executing query 54: Invalid expression / Unexpected token. Line 1, Col: 746.
  st x-ray show any abnormality in the left lung?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 55: Answer count mismatch: 4 != 17
['null']
Error executing query 56: Unexpected answer type: <class 'str'>
['null']
Error executing query 57: Unexpected answer type: <class 'str'>
Error executing query 59: Answer count mismatch: 4 != 17
['null']
Error executing query 60: Unexpected answer type: <class 'str'>
['null']
Error executing query 61: Unexpected answer type: <class 'str'>
['null']
Error executing query 62: Unexpected answer type: <class 'str'>
Error executing query 64: Answer count mismatch: 4 != 3
['null']
Error executing query 65: Unexpected answer type: <class 'str'>
Error executing query 66: Invalid expression / Unexpected token. Line 1, Col: 1103.
   year','-0 year') and strftime('%m',diagnoses_icd.charttime) = '09' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime
Error executing query 69: Expecting ). Line 1, Col: 1072.
  ar','-0 year') ) as t2 join admissions on t2.subject_id = admissions.subject_id where t2.charttime  [4madmissions[0m.admittime and datetime(admissions.admittime,'start of year') = datetime('2105-12-31 23:59:00','star
['null']
Error executing query 70: Unexpected answer type: <class 'str'>
Error executing query 71: Answer count mismatch: 4 != 32
['null']
Error executing query 72: Unexpected answer type: <class 'str'>
Error executing query 74: Unexpected answer type: <class 'str'>
['null']
Error executing query 76: Unexpected answer type: <class 'str'>
['null']
Error executing query 78: Unexpected answer type: <class 'str'>
['null']
Error executing query 83: Unexpected answer type: <class 'str'>
['null']
Error executing query 85: Unexpected answer type: <class 'str'>
['null']
Error executing query 87: Unexpected answer type: <class 'str'>
Error executing query 88: Invalid expression / Unexpected token. Line 1, Col: 957.
  iagnoses_icd.charttime) = datetime('2105-12-31 23:59:00','-2 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 89: Invalid expression / Unexpected token. Line 1, Col: 652.
  ns.hadm_id from admissions where admissions.subject_id = 17198431 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
['null']
Error executing query 93: Unexpected answer type: <class 'str'>
Error executing query 94: Answer count mismatch: 4 != 32
Error executing query 95: Expecting ). Line 1, Col: 859.
  etime('2105-12-31 23:59:00','-5 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
['null']
Error executing query 96: Unexpected answer type: <class 'str'>
['null']
Error executing query 98: Unexpected answer type: <class 'str'>
['null']
Error executing query 99: Unexpected answer type: <class 'str'>
['null']
Error executing query 100: Unexpected answer type: <class 'str'>
Error executing query 101: Invalid expression / Unexpected token. Line 1, Col: 760.
  w any spinal degenerative changes in the spine?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 102: Invalid expression / Unexpected token. Line 1, Col: 882.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 103: Invalid expression / Unexpected token. Line 1, Col: 949.
  380697 ) and strftime('%Y-%m',procedures_icd.charttime) = '2105-06' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
['null']
Error executing query 104: Unexpected answer type: <class 'str'>
['null']
Error executing query 105: Unexpected answer type: <class 'str'>
Error executing query 106: Expecting ). Line 1, Col: 898.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
['null']
Error executing query 107: Unexpected answer type: <class 'str'>
Error executing query 108: Invalid expression / Unexpected token. Line 1, Col: 1010.
   year') = datetime('2105-12-31 23:59:00','start of year','-0 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
['null']
Error executing query 110: Unexpected answer type: <class 'str'>
Error executing query 111: Expecting ). Line 1, Col: 719.
  ogyevents.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.test_name ) as t3 where t3.c1 = 5
['null']
Error executing query 112: Unexpected answer type: <class 'str'>
Error executing query 113: Answer count mismatch: 4 != 12
Error executing query 114: Invalid expression / Unexpected token. Line 1, Col: 948.
  dicate clavicle fracture in the right clavicle?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 115: Answer count mismatch: 4 != 2
Error executing query 116: Answer count mismatch: 4 != 2
[False]
Error executing query 121: Invalid expression / Unexpected token. Line 1, Col: 891.
  d = 13888167 ) and strftime('%Y',procedures_icd.charttime) = '2105' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 122: Answer count mismatch: 4 != 6
Error executing query 125: Answer count mismatch: 4 != 2
Error executing query 128: Invalid expression / Unexpected token. Line 1, Col: 982.
   year') = datetime('2105-12-31 23:59:00','start of year','-0 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
['null']
Error executing query 130: Unexpected answer type: <class 'str'>
Error executing query 132: Invalid expression / Unexpected token. Line 1, Col: 845.
  qa("does a chest x-ray depicts any abnormality?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
['null']
Error executing query 133: Unexpected answer type: <class 'str'>
['null']
Error executing query 134: Unexpected answer type: <class 'str'>
['null']
Error executing query 137: Unexpected answer type: <class 'str'>
Error executing query 139: Invalid expression / Unexpected token. Line 1, Col: 757.
  ns.hadm_id from admissions where admissions.subject_id = 19385269 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 140: Answer count mismatch: 4 != 32
Error executing query 141: Invalid expression / Unexpected token. Line 1, Col: 1065.
  cedures_icd.charttime) >= datetime('2105-12-31 23:59:00','-2 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and t1.hadm_id = t3.hadm_id
['null']
Error executing query 143: Unexpected answer type: <class 'str'>
['null']
Error executing query 144: Unexpected answer type: <class 'str'>
Error executing query 145: Answer count mismatch: 4 != 32
Error executing query 146: Answer count mismatch: 4 != 5
Error executing query 149: Answer count mismatch: 4 != 32
['null']
Error executing query 150: Unexpected answer type: <class 'str'>
['null']
Error executing query 153: Unexpected answer type: <class 'str'>
Error executing query 155: Answer count mismatch: 4 != 8
Error executing query 157: Invalid expression / Unexpected token. Line 1, Col: 871.
   where func_vqa("is any abnormality identified?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
['null']
Error executing query 158: Unexpected answer type: <class 'str'>
Error executing query 160: Invalid expression / Unexpected token. Line 1, Col: 994.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id
['null']
Error executing query 161: Unexpected answer type: <class 'str'>
Error executing query 162: Invalid expression / Unexpected token. Line 1, Col: 736.
  id = 18380697 ) and strftime('%Y',prescriptions.starttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 166: Answer count mismatch: 4 != 2
['null']
Error executing query 167: Unexpected answer type: <class 'str'>
Error executing query 168: Invalid expression / Unexpected token. Line 1, Col: 938.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id
Error executing query 169: Answer count mismatch: 4 != 5
['null']
Error executing query 170: Unexpected answer type: <class 'str'>
Error executing query 171: Answer count mismatch: 4 != 5
Error executing query 172: Expecting ). Line 1, Col: 645.
  '%Y',prescriptions.starttime) = '2103' ) as t2 on t1.subject_id = t2.subject_id where t1.starttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 5
['null']
Error executing query 173: Unexpected answer type: <class 'str'>
['null']
Error executing query 175: Unexpected answer type: <class 'str'>
Error executing query 176: Answer count mismatch: 4 != 8
['null']
Error executing query 177: Unexpected answer type: <class 'str'>
Error executing query 178: Invalid expression / Unexpected token. Line 1, Col: 876.
  s.dischtime is not null order by admissions.admittime asc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 179: Answer count mismatch: 4 != 14
Error executing query 180: Answer count mismatch: 4 != 32
['null']
Error executing query 181: Unexpected answer type: <class 'str'>
Error executing query 183: Answer count mismatch: 4 != 2
Error executing query 184: Invalid expression / Unexpected token. Line 1, Col: 930.
  t x-ray show any abnormality in the right lung?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
['null']
Error executing query 186: Unexpected answer type: <class 'str'>
Error executing query 188: Invalid expression / Unexpected token. Line 1, Col: 829.
  iple masses/nodules in the right mid lung zone?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 189: Expecting ). Line 1, Col: 665.
  ogyevents.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 190: Invalid expression / Unexpected token. Line 1, Col: 887.
  id = 15467362 ) and strftime('%Y',diagnoses_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
['null']
Error executing query 192: Unexpected answer type: <class 'str'>
['null']
Error executing query 194: Unexpected answer type: <class 'str'>
Error executing query 195: Invalid expression / Unexpected token. Line 1, Col: 925.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 196: Invalid expression / Unexpected token. Line 1, Col: 758.
  y any abnormality in the right upper lung zone?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
['null']
Error executing query 197: Unexpected answer type: <class 'str'>
['null']
Error executing query 198: Unexpected answer type: <class 'str'>
Error executing query 199: Answer count mismatch: 4 != 2
['null']
Error executing query 200: Unexpected answer type: <class 'str'>
['null']
Error executing query 202: Unexpected answer type: <class 'str'>
Error executing query 204: Invalid expression / Unexpected token. Line 1, Col: 935.
  agnoses_icd.charttime) >= datetime('2105-12-31 23:59:00','-2 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
['null']
Error executing query 207: Unexpected answer type: <class 'str'>
Error executing query 208: Answer count mismatch: 4 != 2
Error executing query 209: Answer count mismatch: 4 != 8
Error executing query 210: Expecting ). Line 1, Col: 852.
  etime('2105-12-31 23:59:00','-3 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 211: Invalid expression / Unexpected token. Line 1, Col: 960.
  dures_icd.charttime) >= datetime('2105-12-31 23:59:00','-33 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
['null']
Error executing query 212: Unexpected answer type: <class 'str'>
Error executing query 215: Expecting ). Line 1, Col: 953.
  '%Y',prescriptions.starttime) = '2100' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 5
['null']
Error executing query 216: Unexpected answer type: <class 'str'>
Error executing query 217: Expecting ). Line 1, Col: 509.
  criptions.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.starttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.starttime) and datetime(t1.starttime,'+2 m
Error executing query 218: Invalid expression / Unexpected token. Line 1, Col: 731.
  id = 19970078 ) and strftime('%Y',prescriptions.starttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 219: Answer count mismatch: 4 != 32
Error executing query 221: Answer count mismatch: 4 != 16
['null']
Error executing query 222: Unexpected answer type: <class 'str'>
['null']
Error executing query 223: Unexpected answer type: <class 'str'>
Error executing query 224: Answer count mismatch: 4 != 2
Error executing query 225: Expecting ). Line 1, Col: 964.
  ere prescriptions.drug = 'finasteride' ) as t3 on t2.subject_id = t3.subject_id where t2.charttime  [4mt3[0m.starttime ) as t4 join patients on t4.subject_id = patients.subject_id
Error executing query 233: Invalid expression / Unexpected token. Line 1, Col: 620.
  _vqa("is any devices observed on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
['null']
Error executing query 235: Unexpected answer type: <class 'str'>
['null']
Error executing query 237: Unexpected answer type: <class 'str'>
['null']
Error executing query 238: Unexpected answer type: <class 'str'>
['null']
Error executing query 239: Unexpected answer type: <class 'str'>
['null']
Error executing query 240: Unexpected answer type: <class 'str'>
['null']
Error executing query 241: Unexpected answer type: <class 'str'>
['null']
Error executing query 242: Unexpected answer type: <class 'str'>
['null']
Error executing query 243: Unexpected answer type: <class 'str'>
Error executing query 244: Answer count mismatch: 4 != 17
Error executing query 245: Answer count mismatch: 4 != 11
Error executing query 246: Invalid expression / Unexpected token. Line 1, Col: 810.
  escriptions.starttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 247: Answer count mismatch: 4 != 5
['null']
Error executing query 248: Unexpected answer type: <class 'str'>
['null']
Error executing query 249: Unexpected answer type: <class 'str'>
['null']
Error executing query 250: Unexpected answer type: <class 'str'>
['null']
Error executing query 252: Unexpected answer type: <class 'str'>
Error executing query 253: Answer count mismatch: 4 != 14
Error executing query 254: near "(": syntax error
Error executing query 255: Invalid expression / Unexpected token. Line 1, Col: 746.
   observed in the right atrium on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
['null']
Error executing query 256: Unexpected answer type: <class 'str'>
Error executing query 257: Answer count mismatch: 4 != 9
['null']
Error executing query 258: Unexpected answer type: <class 'str'>
['null']
Error executing query 259: Unexpected answer type: <class 'str'>
['null']
Error executing query 260: Unexpected answer type: <class 'str'>
['null']
Error executing query 261: Unexpected answer type: <class 'str'>
Error executing query 262: Invalid expression / Unexpected token. Line 1, Col: 903.
  vqa("is any abnormality shown on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
['null']
Error executing query 263: Unexpected answer type: <class 'str'>
Error executing query 265: Answer count mismatch: 4 != 2
['null']
Error executing query 266: Unexpected answer type: <class 'str'>
['null']
Error executing query 267: Unexpected answer type: <class 'str'>
['null']
Error executing query 268: Unexpected answer type: <class 'str'>
Error executing query 269: Unexpected answer type: <class 'str'>
Error executing query 270: Answer count mismatch: 4 != 32
Error executing query 271: Answer count mismatch: 4 != 5
Error executing query 272: Invalid expression / Unexpected token. Line 1, Col: 727.
  id = 11685699 ) and strftime('%Y',prescriptions.starttime) = '2105' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 273: Answer count mismatch: 4 != 6
Error executing query 274: Expecting ). Line 1, Col: 904.
  etime('2105-12-31 23:59:00','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 275: Invalid expression / Unexpected token. Line 1, Col: 885.
  x-ray reveal bone lesion in the right clavicle?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 276: Answer count mismatch: 4 != 3
Error executing query 278: Invalid expression / Unexpected token. Line 1, Col: 750.
  ns.hadm_id from admissions where admissions.subject_id = 17087118 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
['null']
Error executing query 280: Unexpected answer type: <class 'str'>
['null']
Error executing query 282: Unexpected answer type: <class 'str'>
Error executing query 284: Invalid expression / Unexpected token. Line 1, Col: 949.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
Error executing query 286: Answer count mismatch: 4 != 2
['null']
Error executing query 287: Unexpected answer type: <class 'str'>
Error executing query 289: Invalid expression / Unexpected token. Line 1, Col: 759.
   calcified nodule in the right lower lung zone?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 290: Invalid expression / Unexpected token. Line 1, Col: 650.
  ns.hadm_id from admissions where admissions.subject_id = 15689544 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
['null']
Error executing query 291: Unexpected answer type: <class 'str'>
['null']
Error executing query 292: Unexpected answer type: <class 'str'>
Error executing query 294: Answer count mismatch: 4 != 5
['null']
Error executing query 296: Unexpected answer type: <class 'str'>
Error executing query 297: Answer count mismatch: 4 != 32
Error executing query 298: Answer count mismatch: 4 != 7
['null']
Error executing query 299: Unexpected answer type: <class 'str'>
['null']
Error executing query 303: Unexpected answer type: <class 'str'>
Error executing query 304: Invalid expression / Unexpected token. Line 1, Col: 848.
  d = 13411278 ) and strftime('%Y',procedures_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
['null']
Error executing query 305: Unexpected answer type: <class 'str'>
Error executing query 307: Expecting ). Line 1, Col: 898.
  %Y',prescriptions.starttime) >= '2103' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 5
Error executing query 309: Invalid expression / Unexpected token. Line 1, Col: 1025.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 311: Answer count mismatch: 4 != 5
Error executing query 313: Answer count mismatch: 4 != 16
['null']
Error executing query 315: Unexpected answer type: <class 'str'>
Error executing query 316: near "(": syntax error
['null']
Error executing query 317: Unexpected answer type: <class 'str'>
Error executing query 319: Answer count mismatch: 4 != 32
Error executing query 321: Answer count mismatch: 4 != 2
Error executing query 322: Answer count mismatch: 4 != 5
Error executing query 323: Answer count mismatch: 4 != 32
['null']
Error executing query 327: Unexpected answer type: <class 'str'>
Error executing query 328: Answer count mismatch: 4 != 10
['null']
Error executing query 330: Unexpected answer type: <class 'str'>
Error executing query 331: Answer count mismatch: 4 != 12
Error executing query 333: Invalid expression / Unexpected token. Line 1, Col: 1042.
   in the right lower lung zone on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 335: Answer count mismatch: 4 != 10
Error executing query 336: Invalid expression / Unexpected token. Line 1, Col: 985.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
['null']
Error executing query 337: Unexpected answer type: <class 'str'>
Error executing query 338: Answer count mismatch: 4 != 2
Error executing query 339: Expecting ). Line 1, Col: 824.
  etime('2105-12-31 23:59:00','-3 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
['null']
Error executing query 341: Unexpected answer type: <class 'str'>
['null']
Error executing query 343: Unexpected answer type: <class 'str'>
['null']
Error executing query 347: Unexpected answer type: <class 'str'>
['null']
Error executing query 348: Unexpected answer type: <class 'str'>
[False]
['null']
Error executing query 350: Unexpected answer type: <class 'str'>
Error executing query 351: Invalid expression / Unexpected token. Line 1, Col: 733.
  unc_vqa("is a chest x-ray showing infiltration?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 352: Answer count mismatch: 4 != 32
['null']
Error executing query 356: Unexpected answer type: <class 'str'>
Error executing query 357: Answer count mismatch: 4 != 10
['null']
Error executing query 358: Unexpected answer type: <class 'str'>
Error executing query 359: Invalid expression / Unexpected token. Line 1, Col: 995.
   year') = datetime('2105-12-31 23:59:00','start of year','-0 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 360: Answer count mismatch: 4 != 9
['null']
Error executing query 361: Unexpected answer type: <class 'str'>
['null']
Error executing query 363: Unexpected answer type: <class 'str'>
['null']
Error executing query 365: Unexpected answer type: <class 'str'>
Error executing query 366: Invalid expression / Unexpected token. Line 1, Col: 764.
  etime('2105-12-31 23:59:00','-5 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 367: Invalid expression / Unexpected token. Line 1, Col: 735.
  ion of four or more vascular stents' ) ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
['null']
Error executing query 368: Unexpected answer type: <class 'str'>
Error executing query 369: Answer count mismatch: 4 != 10
Error executing query 370: Answer count mismatch: 4 != 32
Error executing query 372: Answer count mismatch: 4 != 19
['null']
Error executing query 373: Unexpected answer type: <class 'str'>
Error executing query 374: Answer count mismatch: 4 != 2
Error executing query 375: Answer count mismatch: 4 != 13
Error executing query 376: Answer count mismatch: 4 != 6
['null']
Error executing query 378: Unexpected answer type: <class 'str'>
['null']
Error executing query 379: Unexpected answer type: <class 'str'>
Error executing query 381: Expecting ). Line 1, Col: 883.
  %Y',procedures_icd.charttime) = '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.icd_code ) as t3 where t3.c1 = 5 )
Error executing query 383: Answer count mismatch: 4 != 9
Error executing query 385: Invalid expression / Unexpected token. Line 1, Col: 936.
  agnoses_icd.charttime) = datetime('2105-12-31 23:59:00','-3 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
['null']
Error executing query 386: Unexpected answer type: <class 'str'>
Error executing query 387: Invalid expression / Unexpected token. Line 1, Col: 801.
  ray indicate any abnormality in the right lung?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 389: Answer count mismatch: 4 != 2
Error executing query 391: Answer count mismatch: 4 != 3
['null']
Error executing query 395: Unexpected answer type: <class 'str'>
['null']
Error executing query 397: Unexpected answer type: <class 'str'>
['null']
Error executing query 398: Unexpected answer type: <class 'str'>
Error executing query 400: Answer count mismatch: 4 != 9
['null']
Error executing query 401: Unexpected answer type: <class 'str'>
['null']
Error executing query 405: Unexpected answer type: <class 'str'>
Error executing query 407: Answer count mismatch: 4 != 2
['null']
Error executing query 408: Unexpected answer type: <class 'str'>
['null']
Error executing query 409: Unexpected answer type: <class 'str'>
['null']
Error executing query 410: Unexpected answer type: <class 'str'>
Error executing query 412: Invalid expression / Unexpected token. Line 1, Col: 881.
   shoulder osteoarthritis in the right shoulder?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
['null']
Error executing query 413: Unexpected answer type: <class 'str'>
['null']
Error executing query 415: Unexpected answer type: <class 'str'>
Error executing query 416: Invalid expression / Unexpected token. Line 1, Col: 971.
  y reveal mass/nodule (not otherwise specified)?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 418: Expecting ). Line 1, Col: 780.
  dures_icd.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.icd_code ) as t3 where t3.c1 = 4 )
['null']
Error executing query 421: Unexpected answer type: <class 'str'>
Error executing query 423: Invalid expression / Unexpected token. Line 1, Col: 734.
  id = 10681061 ) and strftime('%Y',prescriptions.starttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
['null']
Error executing query 424: Unexpected answer type: <class 'str'>
Error executing query 425: Invalid expression / Unexpected token. Line 1, Col: 895.
  a("does a chest x-ray indicate any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
['null']
Error executing query 426: Unexpected answer type: <class 'str'>
Error executing query 427: Answer count mismatch: 4 != 3
Error executing query 428: Answer count mismatch: 4 != 8
['null']
Error executing query 429: Unexpected answer type: <class 'str'>
['null']
Error executing query 433: Unexpected answer type: <class 'str'>
Error executing query 435: Invalid expression / Unexpected token. Line 1, Col: 732.
  ns.hadm_id from admissions where admissions.subject_id = 15234578 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 437: Expecting ). Line 1, Col: 649.
  '%Y',prescriptions.starttime) = '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.starttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 5
Error executing query 438: Invalid expression / Unexpected token. Line 1, Col: 775.
  ns.hadm_id from admissions where admissions.subject_id = 15346117 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
['null']
Error executing query 439: Unexpected answer type: <class 'str'>
Error executing query 440: near "(": syntax error
['null']
Error executing query 441: Unexpected answer type: <class 'str'>
['null']
Error executing query 442: Unexpected answer type: <class 'str'>
Error executing query 443: Invalid expression / Unexpected token. Line 1, Col: 880.
  s.dischtime is not null order by admissions.admittime asc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 444: Invalid expression / Unexpected token. Line 1, Col: 841.
  ns.hadm_id from admissions where admissions.subject_id = 11131026 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 447: Expecting ). Line 1, Col: 786.
  ender = 'f' ) and admissions.age >= 60 ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 5
Error executing query 448: Answer count mismatch: 4 != 10
Error executing query 449: Answer count mismatch: 4 != 32
Error executing query 450: Answer count mismatch: 4 != 32
Error executing query 452: Answer count mismatch: 4 != 2
Error executing query 453: Unexpected answer type: <class 'str'>
Error executing query 454: Invalid expression / Unexpected token. Line 1, Col: 945.
  ocedures_icd.charttime) = datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 455: Answer count mismatch: 4 != 3
Error executing query 457: Answer count mismatch: 4 != 17
Error executing query 459: Answer count mismatch: 4 != 5
['null']
Error executing query 460: Unexpected answer type: <class 'str'>
Error executing query 461: Expecting ). Line 1, Col: 794.
  of the jaws' ) ) as t2 join admissions on t2.subject_id = admissions.subject_id where t2.charttime  [4madmissions[0m.admittime and datetime(admissions.admittime) between datetime(t2.charttime) and datetime(t2.chartti
['null']
Error executing query 462: Unexpected answer type: <class 'str'>
Error executing query 463: Invalid expression / Unexpected token. Line 1, Col: 895.
  id = 15584605 ) and strftime('%Y',diagnoses_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 464: Invalid expression / Unexpected token. Line 1, Col: 955.
  cedures_icd.charttime) = datetime('2105-12-31 23:59:00','-2 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 465: Invalid expression / Unexpected token. Line 1, Col: 863.
  e func_vqa("has an x-ray indicated lung lesion?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
['null']
Error executing query 466: Unexpected answer type: <class 'str'>
['null']
Error executing query 467: Unexpected answer type: <class 'str'>
Error executing query 468: Expecting ). Line 1, Col: 880.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
['null']
Error executing query 469: Unexpected answer type: <class 'str'>
['null']
Error executing query 470: Unexpected answer type: <class 'str'>
['null']
Error executing query 471: Unexpected answer type: <class 'str'>
Error executing query 472: Answer count mismatch: 4 != 15
Error executing query 473: Invalid expression / Unexpected token. Line 1, Col: 962.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
Error executing query 474: Invalid expression / Unexpected token. Line 1, Col: 825.
  rated any diseases in the left upper lung zone?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
['null']
Error executing query 475: Unexpected answer type: <class 'str'>
Error executing query 477: Invalid expression / Unexpected token. Line 1, Col: 868.
   = 19896759 ) and strftime('%Y',procedures_icd.charttime) >= '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 478: Answer count mismatch: 4 != 7
['null']
Error executing query 480: Unexpected answer type: <class 'str'>
['null']
Error executing query 482: Unexpected answer type: <class 'str'>
Error executing query 483: Answer count mismatch: 4 != 5
['null']
Error executing query 485: Unexpected answer type: <class 'str'>
['null']
Error executing query 486: Unexpected answer type: <class 'str'>
Error executing query 487: Answer count mismatch: 4 != 3
['null']
Error executing query 488: Unexpected answer type: <class 'str'>
Error executing query 490: Answer count mismatch: 4 != 15
['null']
Error executing query 491: Unexpected answer type: <class 'str'>
['null']
Error executing query 493: Unexpected answer type: <class 'str'>
['null']
Error executing query 494: Unexpected answer type: <class 'str'>
['null']
Error executing query 495: Unexpected answer type: <class 'str'>
Error executing query 496: Answer count mismatch: 4 != 2
Error executing query 497: Expecting ). Line 1, Col: 896.
  etime('2105-12-31 23:59:00','-4 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.itemid ) as t3 where t3.c1 = 4 )
['null']
Error executing query 498: Unexpected answer type: <class 'str'>
Error executing query 499: Invalid expression / Unexpected token. Line 1, Col: 919.
  edures_icd.charttime) >= datetime('2105-12-31 23:59:00','-1 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 500: Invalid expression / Unexpected token. Line 1, Col: 918.
  t x-ray detecting pleural/parenchymal scarring?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 502: Invalid expression / Unexpected token. Line 1, Col: 895.
   indication of tortuous aorta on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
['null']
Error executing query 503: Unexpected answer type: <class 'str'>
['null']
Error executing query 504: Unexpected answer type: <class 'str'>
Error executing query 506: near "(": syntax error
['null']
Error executing query 507: Unexpected answer type: <class 'str'>
['null']
Error executing query 508: Unexpected answer type: <class 'str'>
Error executing query 509: Answer count mismatch: 4 != 3
['null']
Error executing query 510: Unexpected answer type: <class 'str'>
['null']
Error executing query 511: Unexpected answer type: <class 'str'>
['null']
Error executing query 512: Unexpected answer type: <class 'str'>
Error executing query 513: Answer count mismatch: 4 != 5
Error executing query 515: Answer count mismatch: 4 != 3
Error executing query 516: Answer count mismatch: 4 != 32
Error executing query 517: Answer count mismatch: 4 != 14
['null']
Error executing query 518: Unexpected answer type: <class 'str'>
['null']
Error executing query 519: Unexpected answer type: <class 'str'>
['null']
Error executing query 520: Unexpected answer type: <class 'str'>
['null']
Error executing query 522: Unexpected answer type: <class 'str'>
Error executing query 525: Answer count mismatch: 4 != 3
Error executing query 526: Answer count mismatch: 4 != 2
Error executing query 527: Answer count mismatch: 4 != 32
Error executing query 528: Invalid expression / Unexpected token. Line 1, Col: 904.
  vqa("is any abnormality shown on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 530: Invalid expression / Unexpected token. Line 1, Col: 881.
  566805 ) and strftime('%Y-%m',diagnoses_icd.charttime) >= '2104-09' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 533: Unexpected answer type: <class 'str'>
Error executing query 535: Answer count mismatch: 4 != 32
Error executing query 536: Invalid expression / Unexpected token. Line 1, Col: 798.
  st x-ray indicate pleural/parenchymal scarring?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 537: Invalid expression / Unexpected token. Line 1, Col: 637.
  ns.hadm_id from admissions where admissions.subject_id = 17328792 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 538: Answer count mismatch: 4 != 6
['null']
Error executing query 539: Unexpected answer type: <class 'str'>
Error executing query 540: Invalid expression / Unexpected token. Line 1, Col: 757.
  n pneumothorax in the right costophrenic angle?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
['null']
Error executing query 541: Unexpected answer type: <class 'str'>
Error executing query 542: Answer count mismatch: 4 != 32
['null']
Error executing query 543: Unexpected answer type: <class 'str'>
['null']
Error executing query 544: Unexpected answer type: <class 'str'>
['null']
Error executing query 546: Unexpected answer type: <class 'str'>
['null']
Error executing query 548: Unexpected answer type: <class 'str'>
Error executing query 552: Answer count mismatch: 4 != 32
Error executing query 553: Invalid expression / Unexpected token. Line 1, Col: 783.
  ns.hadm_id from admissions where admissions.subject_id = 14623286 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 554: Answer count mismatch: 4 != 32
Error executing query 555: Answer count mismatch: 4 != 2
['null']
Error executing query 556: Unexpected answer type: <class 'str'>
Error executing query 557: Invalid expression / Unexpected token. Line 1, Col: 917.
  a("does an x-ray reveal vascular calcification?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 558: Invalid expression / Unexpected token. Line 1, Col: 796.
  e any abnormality in the right lower lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
['null']
Error executing query 560: Unexpected answer type: <class 'str'>
Error executing query 561: Invalid expression / Unexpected token. Line 1, Col: 1031.
  s.dischtime is not null order by admissions.admittime asc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 565: Invalid expression / Unexpected token. Line 1, Col: 879.
  ng any abnormality in the left upper lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
['null']
Error executing query 566: Unexpected answer type: <class 'str'>
['null']
Error executing query 567: Unexpected answer type: <class 'str'>
['null']
Error executing query 568: Unexpected answer type: <class 'str'>
['null']
Error executing query 571: Unexpected answer type: <class 'str'>
Error executing query 572: Expecting ). Line 1, Col: 967.
  etime('2105-12-31 23:59:00','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 573: Answer count mismatch: 4 != 2
Error executing query 576: Invalid expression / Unexpected token. Line 1, Col: 777.
  ns.hadm_id from admissions where admissions.subject_id = 18380697 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
['null']
Error executing query 577: Unexpected answer type: <class 'str'>
Error executing query 580: Answer count mismatch: 4 != 3
Error executing query 581: Invalid expression / Unexpected token. Line 1, Col: 797.
  est x-ray indicate any any anatomical findings?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
['null']
Error executing query 582: Unexpected answer type: <class 'str'>
['null']
Error executing query 583: Unexpected answer type: <class 'str'>
['null']
Error executing query 585: Unexpected answer type: <class 'str'>
['null']
Error executing query 586: Unexpected answer type: <class 'str'>
['null']
Error executing query 588: Unexpected answer type: <class 'str'>
['null']
Error executing query 589: Unexpected answer type: <class 'str'>
Error executing query 591: near "(": syntax error
['null']
Error executing query 593: Unexpected answer type: <class 'str'>
['null']
Error executing query 594: Unexpected answer type: <class 'str'>
Error executing query 596: Invalid expression / Unexpected token. Line 1, Col: 880.
  .dischtime is not null order by admissions.admittime desc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 598: Expecting ). Line 1, Col: 971.
  %Y',diagnoses_icd.charttime) >= '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
['null']
Error executing query 599: Unexpected answer type: <class 'str'>
['null']
Error executing query 600: Unexpected answer type: <class 'str'>
Error executing query 601: Invalid expression / Unexpected token. Line 1, Col: 786.
  1468671 ) and strftime('%Y-%m',prescriptions.starttime) = '2102-01' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
['null']
Error executing query 602: Unexpected answer type: <class 'str'>
Error executing query 603: Answer count mismatch: 4 != 7
Error executing query 604: Answer count mismatch: 4 != 32
Error executing query 605: Answer count mismatch: 4 != 2
['null']
Error executing query 608: Unexpected answer type: <class 'str'>
['null']
Error executing query 609: Unexpected answer type: <class 'str'>
Error executing query 610: Answer count mismatch: 4 != 32
['null']
Error executing query 611: Unexpected answer type: <class 'str'>
['null']
Error executing query 612: Unexpected answer type: <class 'str'>
Error executing query 617: Invalid expression / Unexpected token. Line 1, Col: 892.
  d = 13506966 ) and strftime('%Y',procedures_icd.charttime) = '2105' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
['null']
Error executing query 620: Unexpected answer type: <class 'str'>
Error executing query 621: Answer count mismatch: 4 != 32
Error executing query 622: Invalid expression / Unexpected token. Line 1, Col: 891.
  55097 ) and strftime('%Y-%m',procedures_icd.charttime) >= '2104-08' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
['null']
Error executing query 624: Unexpected answer type: <class 'str'>
['null']
Error executing query 625: Unexpected answer type: <class 'str'>
['null']
Error executing query 626: Unexpected answer type: <class 'str'>
Error executing query 627: Invalid expression / Unexpected token. Line 1, Col: 913.
  id = 18380697 ) and strftime('%Y',diagnoses_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
['null']
Error executing query 629: Unexpected answer type: <class 'str'>
Error executing query 630: Invalid expression / Unexpected token. Line 1, Col: 859.
  a("does a chest x-ray indicate any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 631: Answer count mismatch: 4 != 32
Error executing query 633: Expecting ). Line 1, Col: 1215.
  year') = datetime('2105-12-31 23:59:00','start of year','-0 year') and strftime('%m',procedures_icd.[4mchart[0m
['null']
Error executing query 634: Unexpected answer type: <class 'str'>
Error executing query 635: Answer count mismatch: 4 != 5
Error executing query 636: Invalid expression / Unexpected token. Line 1, Col: 852.
  2140106 ) and strftime('%Y-%m',diagnoses_icd.charttime) = '2104-05' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 637: Invalid expression / Unexpected token. Line 1, Col: 777.
  g of any diseases in the neck on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
['null']
Error executing query 640: Unexpected answer type: <class 'str'>
Error executing query 641: Answer count mismatch: 4 != 32
['null']
Error executing query 642: Unexpected answer type: <class 'str'>
Error executing query 643: Invalid expression / Unexpected token. Line 1, Col: 856.
  d = 16827631 ) and strftime('%Y',diagnoses_icd.charttime) >= '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 644: Answer count mismatch: 4 != 2
Error executing query 645: Invalid expression / Unexpected token. Line 1, Col: 831.
  ("is the chest x-ray revealing any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 647: Invalid expression / Unexpected token. Line 1, Col: 813.
  rescriptions.starttime) = datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 648: Invalid expression / Unexpected token. Line 1, Col: 751.
   any anatomical findings in the right clavicle?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 649: Invalid expression / Unexpected token. Line 1, Col: 736.
  chest x-ray indicate any technical assessments?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
['null']
Error executing query 650: Unexpected answer type: <class 'str'>
Error executing query 651: Expecting ). Line 1, Col: 856.
  etime('2105-12-31 23:59:00','-3 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
['null']
Error executing query 652: Unexpected answer type: <class 'str'>
Error executing query 653: Invalid expression / Unexpected token. Line 1, Col: 891.
  func_vqa("does an x-ray reveal any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
['null']
Error executing query 654: Unexpected answer type: <class 'str'>
Error executing query 655: Answer count mismatch: 4 != 9
['null']
Error executing query 656: Unexpected answer type: <class 'str'>
Error executing query 657: Invalid expression / Unexpected token. Line 1, Col: 726.
  qa("does a chest x-ray reveal any any diseases?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 659: Invalid expression / Unexpected token. Line 1, Col: 988.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
['null']
Error executing query 661: Unexpected answer type: <class 'str'>
['null']
Error executing query 662: Unexpected answer type: <class 'str'>
Error executing query 664: Answer count mismatch: 4 != 32
Error executing query 665: Invalid expression / Unexpected token. Line 1, Col: 878.
  398283 ) and strftime('%Y-%m',procedures_icd.charttime) = '2104-08' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 666: Answer count mismatch: 4 != 32
Error executing query 667: Answer count mismatch: 4 != 32
Error executing query 668: Answer count mismatch: 4 != 14
Error executing query 669: Answer count mismatch: 4 != 32
['null']
Error executing query 670: Unexpected answer type: <class 'str'>
Error executing query 671: Invalid expression / Unexpected token. Line 1, Col: 749.
  id = 18136887 ) and strftime('%Y',prescriptions.starttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
['null']
Error executing query 672: Unexpected answer type: <class 'str'>
['null']
Error executing query 673: Unexpected answer type: <class 'str'>
['null']
Error executing query 674: Unexpected answer type: <class 'str'>
['null']
Error executing query 677: Unexpected answer type: <class 'str'>
['null']
Error executing query 678: Unexpected answer type: <class 'str'>
Error executing query 679: Answer count mismatch: 4 != 8
Error executing query 680: Answer count mismatch: 4 != 32
['null']
Error executing query 684: Unexpected answer type: <class 'str'>
['null']
Error executing query 685: Unexpected answer type: <class 'str'>
Error executing query 687: Invalid expression / Unexpected token. Line 1, Col: 769.
  how any any abnormality in the left chest wall?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
['null']
Error executing query 688: Unexpected answer type: <class 'str'>
['null']
Error executing query 690: Unexpected answer type: <class 'str'>
['null']
Error executing query 691: Unexpected answer type: <class 'str'>
['null']
Error executing query 693: Unexpected answer type: <class 'str'>
['null']
Error executing query 694: Unexpected answer type: <class 'str'>
['null']
Error executing query 695: Unexpected answer type: <class 'str'>
['null']
Error executing query 696: Unexpected answer type: <class 'str'>
Error executing query 699: Answer count mismatch: 4 != 15
Error executing query 700: Invalid expression / Unexpected token. Line 1, Col: 973.
  nstrated any tubes/lines in the right shoulder?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 701: Invalid expression / Unexpected token. Line 1, Col: 660.
  ns.hadm_id from admissions where admissions.subject_id = 18044092 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
['null']
Error executing query 702: Unexpected answer type: <class 'str'>
['null']
Error executing query 703: Unexpected answer type: <class 'str'>
Error executing query 704: Invalid expression / Unexpected token. Line 1, Col: 632.
  ns.hadm_id from admissions where admissions.subject_id = 16807878 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 705: Expecting ). Line 1, Col: 674.
  ons.hadm_id where admissions.age >= 60 ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 4
Error executing query 706: Answer count mismatch: 4 != 2
Error executing query 707: Answer count mismatch: 4 != 7
Error executing query 708: Expecting ). Line 1, Col: 920.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 709: Answer count mismatch: 4 != 3
['null']
Error executing query 711: Unexpected answer type: <class 'str'>
['null']
Error executing query 712: Unexpected answer type: <class 'str'>
Error executing query 713: Answer count mismatch: 4 != 5
Error executing query 715: Answer count mismatch: 4 != 32
Error executing query 717: Answer count mismatch: 4 != 32
Error executing query 718: Answer count mismatch: 4 != 2
Error executing query 719: Invalid expression / Unexpected token. Line 1, Col: 877.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 720: Answer count mismatch: 4 != 10
Error executing query 724: Invalid expression / Unexpected token. Line 1, Col: 745.
  ns.hadm_id from admissions where admissions.subject_id = 10938464 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
['null']
Error executing query 726: Unexpected answer type: <class 'str'>
['null']
Error executing query 727: Unexpected answer type: <class 'str'>
Error executing query 728: Invalid expression / Unexpected token. Line 1, Col: 978.
  f costophrenic angle blunting on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 729: Answer count mismatch: 4 != 11
Error executing query 732: Invalid expression / Unexpected token. Line 1, Col: 889.
  does a chest x-ray show elevated hemidiaphragm?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 733: Invalid expression / Unexpected token. Line 1, Col: 947.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id
Error executing query 734: Invalid expression / Unexpected token. Line 1, Col: 629.
  ns.hadm_id from admissions where admissions.subject_id = 16922420 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 735: Expecting ). Line 1, Col: 872.
  '%Y',diagnoses_icd.charttime) = '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
['null']
Error executing query 736: Unexpected answer type: <class 'str'>
Error executing query 737: Invalid expression / Unexpected token. Line 1, Col: 851.
  t x-ray indicate any abnormality in the carina?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 738: Invalid expression / Unexpected token. Line 1, Col: 875.
  431875 ) and strftime('%Y-%m',diagnoses_icd.charttime) >= '2103-12' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 739: Invalid expression / Unexpected token. Line 1, Col: 725.
  d = 12712004 ) and strftime('%Y',prescriptions.starttime) >= '2105' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 740: Answer count mismatch: 4 != 15
['null']
Error executing query 743: Unexpected answer type: <class 'str'>
Error executing query 744: Invalid expression / Unexpected token. Line 1, Col: 1122.
  nth') = datetime('2105-12-31 23:59:00','start of month','-0 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and t1.hadm_id = t3.hadm_id
['null']
Error executing query 745: Unexpected answer type: <class 'str'>
['null']
Error executing query 746: Unexpected answer type: <class 'str'>
['null']
Error executing query 751: Unexpected answer type: <class 'str'>
['null']
Error executing query 752: Unexpected answer type: <class 'str'>
Error executing query 754: Invalid expression / Unexpected token. Line 1, Col: 716.
  ns.hadm_id from admissions where admissions.subject_id = 12408912 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 755: Expecting ). Line 1, Col: 918.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.test_name ) as t3 where t3.c1 = 3
Error executing query 756: Expecting ). Line 1, Col: 1031.
  olume ( dialysis/pheresis catheters )' ) as t3 on t2.subject_id = t3.subject_id where t2.charttime  [4mt3[0m.starttime ) as t4 join patients on t4.subject_id = patients.subject_id
['null']
Error executing query 757: Unexpected answer type: <class 'str'>
Error executing query 758: Answer count mismatch: 4 != 32
['null']
Error executing query 759: Unexpected answer type: <class 'str'>
Error executing query 760: Expecting ). Line 1, Col: 970.
  ere prescriptions.drug = 'colesevelam' ) as t3 on t2.subject_id = t3.subject_id where t2.charttime  [4mt3[0m.starttime ) as t4 join patients on t4.subject_id = patients.subject_id
Error executing query 761: near "(": syntax error
['null']
Error executing query 762: Unexpected answer type: <class 'str'>
Error executing query 764: Invalid expression / Unexpected token. Line 1, Col: 1095.
  agnoses_icd.charttime) >= datetime('2105-12-31 23:59:00','-3 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 765: Answer count mismatch: 4 != 6
Error executing query 766: Answer count mismatch: 4 != 17
Error executing query 767: Invalid expression / Unexpected token. Line 1, Col: 927.
   anatomical findings in the left mid lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 768: Answer count mismatch: 4 != 2
['null']
Error executing query 771: Unexpected answer type: <class 'str'>
['null']
Error executing query 773: Unexpected answer type: <class 'str'>
['null']
Error executing query 774: Unexpected answer type: <class 'str'>
Error executing query 775: Invalid expression / Unexpected token. Line 1, Col: 1005.
  _vqa("does a chest x-ray indicate any diseases?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 776: Invalid expression / Unexpected token. Line 1, Col: 883.
  any indication of any devices on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 778: Expecting ). Line 1, Col: 860.
  microbiologyevents.charttime) = '2103' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.test_name ) as t3 where t3.c1 = 5
Error executing query 779: Answer count mismatch: 4 != 2
Error executing query 781: Expecting ). Line 1, Col: 870.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
['null']
Error executing query 782: Unexpected answer type: <class 'str'>
Error executing query 785: Invalid expression / Unexpected token. Line 1, Col: 767.
  ns.hadm_id from admissions where admissions.subject_id = 13119866 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 786: Expecting ). Line 1, Col: 833.
  me('%Y',labevents.charttime) >= '2105' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.itemid ) as t3 where t3.c1 = 5 )
Error executing query 788: Answer count mismatch: 4 != 9
['null']
Error executing query 790: Unexpected answer type: <class 'str'>
['null']
Error executing query 793: Unexpected answer type: <class 'str'>
Error executing query 795: Expecting ). Line 1, Col: 910.
  etime('2105-12-31 23:59:00','-6 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 797: Invalid expression / Unexpected token. Line 1, Col: 913.
  s a chest x-ray show goiter in the mediastinum?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 798: Invalid expression / Unexpected token. Line 1, Col: 747.
  icate any abnormality in the right apical zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
['null']
Error executing query 799: Unexpected answer type: <class 'str'>
['null']
Error executing query 800: Unexpected answer type: <class 'str'>
['null']
Error executing query 801: Unexpected answer type: <class 'str'>
Error executing query 802: Invalid expression / Unexpected token. Line 1, Col: 882.
  ay indicate cardiac pacer and wires in the svc?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
['null']
Error executing query 803: Unexpected answer type: <class 'str'>
Error executing query 805: near "(": syntax error
['null']
Error executing query 806: Unexpected answer type: <class 'str'>
Error executing query 809: Unexpected answer type: <class 'str'>
Error executing query 810: Invalid expression / Unexpected token. Line 1, Col: 726.
   t2 where func_vqa("is tortuous aorta revealed?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
['null']
Error executing query 811: Unexpected answer type: <class 'str'>
['null']
Error executing query 812: Unexpected answer type: <class 'str'>
['null']
Error executing query 813: Unexpected answer type: <class 'str'>
['null']
Error executing query 814: Unexpected answer type: <class 'str'>
Error executing query 817: Expecting ). Line 1, Col: 852.
  ) and admissions.age between 50 and 59 ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 3
Error executing query 819: Answer count mismatch: 4 != 32
Error executing query 820: Invalid expression / Unexpected token. Line 1, Col: 861.
  id = 17968028 ) and strftime('%Y',diagnoses_icd.charttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
['null']
Error executing query 821: Unexpected answer type: <class 'str'>
Error executing query 822: Unexpected answer type: <class 'str'>
Error executing query 823: Answer count mismatch: 4 != 12
Error executing query 824: Answer count mismatch: 4 != 2
Error executing query 825: Invalid expression / Unexpected token. Line 1, Col: 779.
  ns.hadm_id from admissions where admissions.subject_id = 16529186 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
['null']
Error executing query 827: Unexpected answer type: <class 'str'>
Error executing query 828: Expecting ). Line 1, Col: 670.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.starttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.starttime) and datetime(t1.starttime,'+2 m
Error executing query 829: Expecting ). Line 1, Col: 771.
  etime('2105-12-31 23:59:00','-4 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 830: Answer count mismatch: 4 != 32
Error executing query 831: Invalid expression / Unexpected token. Line 1, Col: 768.
  ns.hadm_id from admissions where admissions.subject_id = 13411278 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
['null']
Error executing query 832: Unexpected answer type: <class 'str'>
Error executing query 833: Invalid expression / Unexpected token. Line 1, Col: 850.
  id = 10681061 ) and strftime('%Y',diagnoses_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 834: Answer count mismatch: 4 != 32
Error executing query 836: Answer count mismatch: 4 != 8
Error executing query 838: Invalid expression / Unexpected token. Line 1, Col: 893.
  echnical assessments revealed on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 839: Invalid expression / Unexpected token. Line 1, Col: 1016.
  ting any anatomical findings in the right lung?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
['null']
Error executing query 842: Unexpected answer type: <class 'str'>
Error executing query 844: Invalid expression / Unexpected token. Line 1, Col: 1018.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id
Error executing query 845: near "(": syntax error
Error executing query 846: Answer count mismatch: 4 != 2
Error executing query 847: Answer count mismatch: 4 != 12
['null']
Error executing query 850: Unexpected answer type: <class 'str'>
Error executing query 851: Expecting ). Line 1, Col: 885.
  dures_icd.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
['null']
Error executing query 852: Unexpected answer type: <class 'str'>
Error executing query 853: Expecting ). Line 1, Col: 958.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 3
['null']
Error executing query 854: Unexpected answer type: <class 'str'>
['null']
Error executing query 856: Unexpected answer type: <class 'str'>
Error executing query 857: Answer count mismatch: 4 != 32
Error executing query 860: Answer count mismatch: 4 != 6
Error executing query 861: Answer count mismatch: 4 != 32
['null']
Error executing query 862: Unexpected answer type: <class 'str'>
['null']
Error executing query 864: Unexpected answer type: <class 'str'>
Error executing query 865: Invalid expression / Unexpected token. Line 1, Col: 853.
  nc_vqa("has an x-ray indicated any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 866: Answer count mismatch: 4 != 6
['null']
Error executing query 867: Unexpected answer type: <class 'str'>
['null']
Error executing query 869: Unexpected answer type: <class 'str'>
['null']
Error executing query 871: Unexpected answer type: <class 'str'>
['null']
Error executing query 876: Unexpected answer type: <class 'str'>
Error executing query 877: Invalid expression / Unexpected token. Line 1, Col: 937.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
Error executing query 878: Invalid expression / Unexpected token. Line 1, Col: 885.
  agnoses_icd.charttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 879: Invalid expression / Unexpected token. Line 1, Col: 700.
  '%Y',prescriptions.starttime) = '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month')
Error executing query 881: Invalid expression / Unexpected token. Line 1, Col: 926.
  pneumonia revealed in the left upper lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 882: Answer count mismatch: 4 != 2
Error executing query 883: Answer count mismatch: 4 != 32
['null']
Error executing query 884: Unexpected answer type: <class 'str'>
Error executing query 887: Expecting ). Line 1, Col: 781.
  etime('2105-12-31 23:59:00','-3 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
['null']
Error executing query 890: Unexpected answer type: <class 'str'>
Error executing query 891: Invalid expression / Unexpected token. Line 1, Col: 737.
  831708 ) and strftime('%Y-%m',prescriptions.starttime) >= '2104-02' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 892: Unexpected answer type: <class 'str'>
['null']
Error executing query 893: Unexpected answer type: <class 'str'>
Error executing query 894: Answer count mismatch: 4 != 5
['null']
Error executing query 897: Unexpected answer type: <class 'str'>
Error executing query 898: Invalid expression / Unexpected token. Line 1, Col: 936.
  gnoses_icd.charttime) = datetime('2105-12-31 23:59:00','-25 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
['null']
Error executing query 901: Unexpected answer type: <class 'str'>
Error executing query 903: Invalid expression / Unexpected token. Line 1, Col: 861.
  segmental collapse in the left upper lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 904: Answer count mismatch: 4 != 3
Error executing query 906: Invalid expression / Unexpected token. Line 1, Col: 1056.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 907: Answer count mismatch: 4 != 8
['null']
Error executing query 911: Unexpected answer type: <class 'str'>
['null']
Error executing query 914: Unexpected answer type: <class 'str'>
Error executing query 915: Answer count mismatch: 4 != 3
['null']
Error executing query 916: Unexpected answer type: <class 'str'>
['null']
Error executing query 917: Unexpected answer type: <class 'str'>
Error executing query 918: Answer count mismatch: 4 != 8
Error executing query 919: Invalid expression / Unexpected token. Line 1, Col: 751.
   in the left hilar structures on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
['null']
Error executing query 920: Unexpected answer type: <class 'str'>
Error executing query 921: Invalid expression / Unexpected token. Line 1, Col: 970.
   year','-0 year') and strftime('%m',prescriptions.starttime) = '01' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 922: Answer count mismatch: 4 != 5
['null']
Error executing query 924: Unexpected answer type: <class 'str'>
Error executing query 926: Answer count mismatch: 4 != 3
Error executing query 927: Answer count mismatch: 4 != 2
Error executing query 929: near "(": syntax error
Error executing query 930: Invalid expression / Unexpected token. Line 1, Col: 827.
  etime('2105-12-31 23:59:00','-5 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id
Error executing query 931: Invalid expression / Unexpected token. Line 1, Col: 647.
  t x-ray showing any abnormality in the abdomen?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
['null']
Error executing query 933: Unexpected answer type: <class 'str'>
Error executing query 934: Answer count mismatch: 4 != 5
Error executing query 935: Answer count mismatch: 4 != 5
Error executing query 936: Invalid expression / Unexpected token. Line 1, Col: 862.
  ny technical assessments indicated on an x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
['null']
Error executing query 939: Unexpected answer type: <class 'str'>
['null']
Error executing query 940: Unexpected answer type: <class 'str'>
Error executing query 941: Expecting ). Line 1, Col: 541.
  criptions.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.starttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 4
Error executing query 942: Answer count mismatch: 4 != 32
['null']
Error executing query 943: Unexpected answer type: <class 'str'>
Error executing query 944: Invalid expression / Unexpected token. Line 1, Col: 759.
   anatomical findings in the left hemidiaphragm?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
['null']
Error executing query 946: Unexpected answer type: <class 'str'>
['null']
Error executing query 947: Unexpected answer type: <class 'str'>
Error executing query 949: Invalid expression / Unexpected token. Line 1, Col: 739.
  d = 12864997 ) and strftime('%Y',prescriptions.starttime) >= '2104' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 950: Answer count mismatch: 4 != 18
Error executing query 951: Required keyword: 'expressions' missing for <class 'sqlglot.expressions.Aliases'>. Line 1, Col: 519.
  re systolic' and d_items.linksto = 'chartevents' ) order by chartevents.charttime desc limit 1 )  ( [4mselect[0m chartevents.valuenum from chartevents where chartevents.stay_id in ( select icustays.stay_id from i
['null']
Error executing query 952: Unexpected answer type: <class 'str'>
Error executing query 953: Invalid expression / Unexpected token. Line 1, Col: 869.
  23:59:00','start of month','-0 month') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 d
Error executing query 955: Invalid expression / Unexpected token. Line 1, Col: 769.
  ated any anatomical findings in the right lung?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 956: Expecting ). Line 1, Col: 792.
  ) and admissions.age between 30 and 39 ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 3
Error executing query 957: Invalid expression / Unexpected token. Line 1, Col: 992.
  x-ray reveal rotated in the cardiac silhouette?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 958: Answer count mismatch: 4 != 3
['null']
Error executing query 960: Unexpected answer type: <class 'str'>
Error executing query 961: Expecting ). Line 1, Col: 796.
  dures_icd.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.icd_code ) as t3 where t3.c1 = 5 )
['null']
Error executing query 965: Unexpected answer type: <class 'str'>
Error executing query 966: Invalid expression / Unexpected token. Line 1, Col: 1007.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
['null']
Error executing query 967: Unexpected answer type: <class 'str'>
Error executing query 968: Unexpected answer type: <class 'str'>
Error executing query 969: Invalid expression / Unexpected token. Line 1, Col: 657.
   depicts any abnormality in the right shoulder?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
['null']
Error executing query 970: Unexpected answer type: <class 'str'>
Error executing query 971: Answer count mismatch: 4 != 22
Error executing query 972: Invalid expression / Unexpected token. Line 1, Col: 832.
  c_vqa("does a chest x-ray show any tubes/lines?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
['null']
Error executing query 973: Unexpected answer type: <class 'str'>
['null']
Error executing query 975: Unexpected answer type: <class 'str'>
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
['null']
Error executing query 985: Unexpected answer type: <class 'str'>
Error executing query 986: Answer count mismatch: 4 != 32
Error executing query 987: Answer count mismatch: 4 != 2
Error executing query 988: Answer count mismatch: 4 != 3
['null']
Error executing query 989: Unexpected answer type: <class 'str'>
['null']
Error executing query 990: Unexpected answer type: <class 'str'>
Error executing query 991: Answer count mismatch: 4 != 2
Error executing query 992: Answer count mismatch: 4 != 10
Error executing query 993: Answer count mismatch: 4 != 5
['null']
Error executing query 994: Unexpected answer type: <class 'str'>
Error executing query 995: Answer count mismatch: 4 != 6
['null']
Error executing query 996: Unexpected answer type: <class 'str'>
Error executing query 997: Invalid expression / Unexpected token. Line 1, Col: 952.
   = 16484690 ) and strftime('%Y',procedures_icd.charttime) >= '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
['null']
Error executing query 998: Unexpected answer type: <class 'str'>
Error executing query 1000: Expecting ). Line 1, Col: 927.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
['null']
Error executing query 1001: Unexpected answer type: <class 'str'>
['null']
Error executing query 1002: Unexpected answer type: <class 'str'>
['null']
Error executing query 1003: Unexpected answer type: <class 'str'>
Error executing query 1005: Invalid expression / Unexpected token. Line 1, Col: 918.
  c_vqa("has a chest x-ray shown any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
['null']
Error executing query 1006: Unexpected answer type: <class 'str'>
Error executing query 1007: Invalid expression / Unexpected token. Line 1, Col: 885.
   the right costophrenic angle on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1008: Invalid expression / Unexpected token. Line 1, Col: 974.
  pleural/parenchymal scarring in the right lung?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 1010: Answer count mismatch: 4 != 3
Error executing query 1011: Invalid expression / Unexpected token. Line 1, Col: 733.
  id = 16484690 ) and strftime('%Y',prescriptions.starttime) = '2102' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
['null']
Error executing query 1012: Unexpected answer type: <class 'str'>
Error executing query 1013: Expecting ). Line 1, Col: 868.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
['null']
Error executing query 1014: Unexpected answer type: <class 'str'>
['null']
Error executing query 1015: Unexpected answer type: <class 'str'>
['null']
Error executing query 1016: Unexpected answer type: <class 'str'>
Error executing query 1017: Invalid expression / Unexpected token. Line 1, Col: 767.
  ns.hadm_id from admissions where admissions.subject_id = 11685699 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
['null']
Error executing query 1018: Unexpected answer type: <class 'str'>
Error executing query 1020: Invalid expression / Unexpected token. Line 1, Col: 868.
  ere func_vqa("does an x-ray reveal lung cancer?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1021: Answer count mismatch: 4 != 2
Error executing query 1022: Invalid expression / Unexpected token. Line 1, Col: 914.
  gnoses_icd.charttime) = datetime('2105-12-31 23:59:00','-15 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
['null']
Error executing query 1023: Unexpected answer type: <class 'str'>
Error executing query 1024: Invalid expression / Unexpected token. Line 1, Col: 848.
   year') = datetime('2105-12-31 23:59:00','start of year','-0 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 1025: Answer count mismatch: 4 != 32
Error executing query 1026: Answer count mismatch: 4 != 32
Error executing query 1027: Answer count mismatch: 4 != 2
['null']
Error executing query 1028: Unexpected answer type: <class 'str'>
Error executing query 1029: Expecting ). Line 1, Col: 734.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.starttime  [4mt2[0m.starttime and datetime(t1.starttime,'start of month') = datetime(t2.starttime,'start of month') gro
Error executing query 1030: Answer count mismatch: 4 != 5
Error executing query 1031: Invalid expression / Unexpected token. Line 1, Col: 874.
  d = 17622334 ) and strftime('%Y',procedures_icd.charttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1032: Expecting ). Line 1, Col: 974.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
Error executing query 1033: Expecting ). Line 1, Col: 923.
  %Y',procedures_icd.charttime) = '2102' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.icd_code ) as t3 where t3.c1 = 4 )
Error executing query 1034: Answer count mismatch: 4 != 3
['null']
Error executing query 1036: Unexpected answer type: <class 'str'>
Error executing query 1037: Answer count mismatch: 4 != 6
Error executing query 1038: near "(": syntax error
Error executing query 1039: Answer count mismatch: 4 != 2
['null']
Error executing query 1040: Unexpected answer type: <class 'str'>
Error executing query 1044: Invalid expression / Unexpected token. Line 1, Col: 993.
  lity in the right apical zone on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
['null']
Error executing query 1046: Unexpected answer type: <class 'str'>
['null']
Error executing query 1047: Unexpected answer type: <class 'str'>
['null']
Error executing query 1048: Unexpected answer type: <class 'str'>
['null']
Error executing query 1050: Unexpected answer type: <class 'str'>
Error executing query 1051: Answer count mismatch: 4 != 32
Error executing query 1053: Answer count mismatch: 4 != 32
Error executing query 1054: Unexpected answer type: <class 'str'>
Error executing query 1055: Answer count mismatch: 4 != 11
Error executing query 1056: Invalid expression / Unexpected token. Line 1, Col: 727.
  ns.hadm_id from admissions where admissions.subject_id = 10032409 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1059: Expecting ). Line 1, Col: 635.
  '%Y',prescriptions.starttime) = '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.starttime  [4mt2[0m.starttime and datetime(t1.starttime,'start of month') = datetime(t2.starttime,'start of month') gro
['null']
Error executing query 1060: Unexpected answer type: <class 'str'>
Error executing query 1061: Expecting ). Line 1, Col: 908.
  time) = '2105' ) as t2 join admissions on t2.subject_id = admissions.subject_id where t2.charttime  [4madmissions[0m.admittime and strftime('%Y',admissions.admittime) = '2105' and datetime(admissions.admittime) betwe
['null']
Error executing query 1062: Unexpected answer type: <class 'str'>
['null']
Error executing query 1066: Unexpected answer type: <class 'str'>
Error executing query 1068: Answer count mismatch: 4 != 2
Error executing query 1069: Invalid expression / Unexpected token. Line 1, Col: 790.
  a("does a chest x-ray show any any abnormality?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
['null']
Error executing query 1070: Unexpected answer type: <class 'str'>
Error executing query 1071: Answer count mismatch: 4 != 32
Error executing query 1072: Invalid expression / Unexpected token. Line 1, Col: 905.
  544660 ) and strftime('%Y-%m',procedures_icd.charttime) = '2103-02' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
['null']
Error executing query 1073: Unexpected answer type: <class 'str'>
Error executing query 1075: Invalid expression / Unexpected token. Line 1, Col: 725.
  _vqa("has a chest x-ray shown prosthetic valve?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1076: Answer count mismatch: 4 != 2
Error executing query 1077: Invalid expression / Unexpected token. Line 1, Col: 908.
  d = 13656933 ) and strftime('%Y',procedures_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
['null']
Error executing query 1078: Unexpected answer type: <class 'str'>
['null']
Error executing query 1079: Unexpected answer type: <class 'str'>
['null']
Error executing query 1080: Unexpected answer type: <class 'str'>
Error executing query 1081: Expecting ). Line 1, Col: 900.
  %Y',procedures_icd.charttime) = '2100' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
['null']
Error executing query 1082: Unexpected answer type: <class 'str'>
Error executing query 1083: Invalid expression / Unexpected token. Line 1, Col: 733.
  id = 18291049 ) and strftime('%Y',prescriptions.starttime) = '2102' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 1085: Answer count mismatch: 4 != 5
Error executing query 1087: Answer count mismatch: 4 != 32
['null']
Error executing query 1088: Unexpected answer type: <class 'str'>
Error executing query 1089: Invalid expression / Unexpected token. Line 1, Col: 732.
  id = 10254956 ) and strftime('%Y',prescriptions.starttime) = '2105' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 1091: Expecting ). Line 1, Col: 704.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.starttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 3
['null']
Error executing query 1092: Unexpected answer type: <class 'str'>
['null']
Error executing query 1093: Unexpected answer type: <class 'str'>
Error executing query 1097: Answer count mismatch: 4 != 3
['null']
Error executing query 1099: Unexpected answer type: <class 'str'>
Error executing query 1100: Invalid expression / Unexpected token. Line 1, Col: 751.
  ',prescriptions.starttime) = '2105-03' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 d
['null']
Error executing query 1101: Unexpected answer type: <class 'str'>
['null']
Error executing query 1102: Unexpected answer type: <class 'str'>
Error executing query 1103: Invalid expression / Unexpected token. Line 1, Col: 920.
  e chest x-ray revealing granulomatous diseases?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 1105: Invalid expression / Unexpected token. Line 1, Col: 996.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
['null']
Error executing query 1107: Unexpected answer type: <class 'str'>
['null']
Error executing query 1108: Unexpected answer type: <class 'str'>
['null']
Error executing query 1112: Unexpected answer type: <class 'str'>
Error executing query 1113: Expecting ). Line 1, Col: 896.
  etime('2105-12-31 23:59:00','-3 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1117: Invalid expression / Unexpected token. Line 1, Col: 755.
  any any abnormality in the right mid lung zone?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1118: Invalid expression / Unexpected token. Line 1, Col: 844.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1120: Invalid expression / Unexpected token. Line 1, Col: 658.
  ns.hadm_id from admissions where admissions.subject_id = 10032409 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
['null']
Error executing query 1121: Unexpected answer type: <class 'str'>
['null']
Error executing query 1122: Unexpected answer type: <class 'str'>
['null']
Error executing query 1123: Unexpected answer type: <class 'str'>
Error executing query 1124: Answer count mismatch: 4 != 6
['null']
Error executing query 1125: Unexpected answer type: <class 'str'>
Error executing query 1126: Invalid expression / Unexpected token. Line 1, Col: 635.
  ns.hadm_id from admissions where admissions.subject_id = 17988477 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
['null']
Error executing query 1127: Unexpected answer type: <class 'str'>
['null']
Error executing query 1129: Unexpected answer type: <class 'str'>
Error executing query 1131: Invalid expression / Unexpected token. Line 1, Col: 773.
  eft lower leg muscle, open approach' ) ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1132: Invalid expression / Unexpected token. Line 1, Col: 1092.
  dures_icd.charttime) >= datetime('2105-12-31 23:59:00','-12 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and t1.hadm_id = t3.hadm_id
Error executing query 1133: Required keyword: 'expressions' missing for <class 'sqlglot.expressions.Aliases'>. Line 1, Col: 410.
  tems where d_labitems.label = 'hemoglobin' ) order by labevents.charttime asc limit 1 offset 1 )  ( [4mselect[0m labevents.valuenum from labevents where labevents.hadm_id in ( select admissions.hadm_id from admis
['null']
Error executing query 1134: Unexpected answer type: <class 'str'>
Error executing query 1135: Invalid expression / Unexpected token. Line 1, Col: 854.
  nc_vqa("is a chest x-ray detecting any devices?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1136: Unexpected answer type: <class 'str'>
Error executing query 1137: Invalid expression / Unexpected token. Line 1, Col: 860.
  t x-ray showing any abnormality in the trachea?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
['null']
Error executing query 1139: Unexpected answer type: <class 'str'>
['null']
Error executing query 1141: Unexpected answer type: <class 'str'>
Error executing query 1143: Expecting ). Line 1, Col: 843.
  microbiologyevents.charttime) = '2105' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1144: Expecting ). Line 1, Col: 682.
  ogyevents.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
['null']
Error executing query 1146: Unexpected answer type: <class 'str'>
['null']
Error executing query 1149: Unexpected answer type: <class 'str'>
Error executing query 1150: Answer count mismatch: 4 != 32
['null']
Error executing query 1151: Unexpected answer type: <class 'str'>
Error executing query 1152: Answer count mismatch: 4 != 5
Error executing query 1153: Invalid expression / Unexpected token. Line 1, Col: 1005.
  iagnoses_icd.charttime) = datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
['null']
Error executing query 1155: Unexpected answer type: <class 'str'>
['null']
Error executing query 1159: Unexpected answer type: <class 'str'>
Error executing query 1160: Expecting ). Line 1, Col: 664.
  ogyevents.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
['null']
Error executing query 1161: Unexpected answer type: <class 'str'>
Error executing query 1162: Answer count mismatch: 4 != 32
['null']
Error executing query 1163: Unexpected answer type: <class 'str'>
['null']
Error executing query 1164: Unexpected answer type: <class 'str'>
Error executing query 1165: Invalid expression / Unexpected token. Line 1, Col: 661.
  ns.hadm_id from admissions where admissions.subject_id = 12126708 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 1168: Answer count mismatch: 4 != 2
['null']
Error executing query 1169: Unexpected answer type: <class 'str'>
Error executing query 1171: Answer count mismatch: 4 != 3
['null']
Error executing query 1172: Unexpected answer type: <class 'str'>
['null']
Error executing query 1173: Unexpected answer type: <class 'str'>
['null']
Error executing query 1176: Unexpected answer type: <class 'str'>
Error executing query 1178: Invalid expression / Unexpected token. Line 1, Col: 728.
  id = 10160202 ) and strftime('%Y',prescriptions.starttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
['null']
Error executing query 1180: Unexpected answer type: <class 'str'>
Error executing query 1182: Invalid expression / Unexpected token. Line 1, Col: 817.
  escriptions.starttime) >= datetime('2105-12-31 23:59:00','-2 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 1183: Answer count mismatch: 4 != 5
['null']
Error executing query 1184: Unexpected answer type: <class 'str'>
Error executing query 1187: Answer count mismatch: 4 != 32
['null']
Error executing query 1188: Unexpected answer type: <class 'str'>
Error executing query 1190: Invalid expression / Unexpected token. Line 1, Col: 895.
  23:59:00','start of month','-0 month') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 d
['null']
Error executing query 1191: Unexpected answer type: <class 'str'>
['null']
Error executing query 1192: Unexpected answer type: <class 'str'>
['null']
Error executing query 1193: Unexpected answer type: <class 'str'>
Error executing query 1194: Answer count mismatch: 4 != 2
['null']
Error executing query 1195: Unexpected answer type: <class 'str'>
['null']
Error executing query 1197: Unexpected answer type: <class 'str'>
Error executing query 1199: Answer count mismatch: 4 != 2
['null']
Error executing query 1202: Unexpected answer type: <class 'str'>
Error executing query 1203: Answer count mismatch: 4 != 5
Error executing query 1204: Answer count mismatch: 4 != 32
['null']
Error executing query 1205: Unexpected answer type: <class 'str'>
Error executing query 1207: Required keyword: 'expression' missing for <class 'sqlglot.expressions.EQ'>. Line 1, Col: 1168.
  tetime('2105-12-31 23:59:00','start of year','-1 year') and strftime('%m',procedures_icd.charttime) [4m=[0m
Error executing query 1208: Invalid expression / Unexpected token. Line 1, Col: 934.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
['null']
Error executing query 1209: Unexpected answer type: <class 'str'>
['null']
Error executing query 1212: Unexpected answer type: <class 'str'>
['null']
Error executing query 1215: Unexpected answer type: <class 'str'>
Error executing query 1218: Invalid expression / Unexpected token. Line 1, Col: 733.
  id = 17183305 ) and strftime('%Y',prescriptions.starttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1219: Invalid expression / Unexpected token. Line 1, Col: 738.
  id = 19606590 ) and strftime('%Y',prescriptions.starttime) = '2105' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 1220: Invalid expression / Unexpected token. Line 1, Col: 734.
  qa("does a chest x-ray depicts any abnormality?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
['null']
Error executing query 1221: Unexpected answer type: <class 'str'>
Error executing query 1223: Answer count mismatch: 4 != 17
Error executing query 1224: Invalid expression / Unexpected token. Line 1, Col: 744.
  ns.hadm_id from admissions where admissions.subject_id = 14117444 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1226: Answer count mismatch: 4 != 7
['null']
Error executing query 1229: Unexpected answer type: <class 'str'>
Error executing query 1230: Answer count mismatch: 4 != 2
Error executing query 1231: Answer count mismatch: 4 != 5
Error executing query 1232: Unexpected answer type: <class 'str'>
['null']
Error executing query 1233: Unexpected answer type: <class 'str'>
['null']
Error executing query 1234: Unexpected answer type: <class 'str'>
['null']
Error executing query 1235: Unexpected answer type: <class 'str'>
['null']
Error executing query 1236: Unexpected answer type: <class 'str'>
Error executing query 1237: Invalid expression / Unexpected token. Line 1, Col: 708.
  g_title = 'arterial catheterization' ) ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1238: Answer count mismatch: 4 != 5
Error executing query 1239: Answer count mismatch: 4 != 32
Error executing query 1240: Answer count mismatch: 4 != 32
['null']
Error executing query 1242: Unexpected answer type: <class 'str'>
['null']
Error executing query 1243: Unexpected answer type: <class 'str'>
Error executing query 1245: Unexpected answer type: <class 'str'>
Error executing query 1246: Answer count mismatch: 4 != 13
['null']
Error executing query 1247: Unexpected answer type: <class 'str'>
Error executing query 1248: Answer count mismatch: 4 != 3
Error executing query 1249: Answer count mismatch: 4 != 9
Error executing query 1251: Invalid expression / Unexpected token. Line 1, Col: 921.
  ated subclavian line in the cardiac silhouette?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1252: Answer count mismatch: 4 != 18
['null']
Error executing query 1253: Unexpected answer type: <class 'str'>
Error executing query 1254: Answer count mismatch: 4 != 14
['null']
Error executing query 1257: Unexpected answer type: <class 'str'>
Error executing query 1258: Invalid expression / Unexpected token. Line 1, Col: 400.
  bel = 'o2 saturation pulseoxymetry' and d_items.linksto = 'chartevents' ) and chartevents.valuenum  [4m97.0[0m and datetime(chartevents.charttime) = datetime('2105-12-31 23:59:00','-729 day')
Error executing query 1260: Invalid expression / Unexpected token. Line 1, Col: 937.
  8463717 ) and strftime('%Y-%m',diagnoses_icd.charttime) = '2105-12' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1261: Expecting ). Line 1, Col: 704.
  where admissions.age between 20 and 29 ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 3
Error executing query 1263: Answer count mismatch: 4 != 32
['null']
Error executing query 1264: Unexpected answer type: <class 'str'>
['null']
Error executing query 1265: Unexpected answer type: <class 'str'>
['null']
Error executing query 1266: Unexpected answer type: <class 'str'>
Error executing query 1267: Answer count mismatch: 4 != 2
Error executing query 1268: Invalid expression / Unexpected token. Line 1, Col: 768.
  ',prescriptions.starttime) = '2102-02' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id
Error executing query 1269: Invalid expression / Unexpected token. Line 1, Col: 912.
   a chest x-ray show interstitial lung diseases?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
['null']
Error executing query 1270: Unexpected answer type: <class 'str'>
['null']
Error executing query 1271: Unexpected answer type: <class 'str'>
['null']
Error executing query 1272: Unexpected answer type: <class 'str'>
['null']
Error executing query 1273: Unexpected answer type: <class 'str'>
Error executing query 1274: Answer count mismatch: 4 != 2
Error executing query 1275: Answer count mismatch: 4 != 32
['null']
Error executing query 1276: Unexpected answer type: <class 'str'>
Error executing query 1277: Answer count mismatch: 4 != 32
Error executing query 1278: Answer count mismatch: 4 != 6
['null']
Error executing query 1279: Unexpected answer type: <class 'str'>
['null']
Error executing query 1280: Unexpected answer type: <class 'str'>
Error executing query 1281: Invalid expression / Unexpected token. Line 1, Col: 928.
  etime('2105-12-31 23:59:00','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id
['null']
Error executing query 1283: Unexpected answer type: <class 'str'>
Error executing query 1284: Invalid expression / Unexpected token. Line 1, Col: 867.
  s an x-ray indicated any technical assessments?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 1286: Invalid expression / Unexpected token. Line 1, Col: 851.
  us catheter placement with guidance' ) ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
Error executing query 1287: Invalid expression / Unexpected token. Line 1, Col: 937.
  agnoses_icd.charttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1288: Answer count mismatch: 4 != 29
['null']
Error executing query 1289: Unexpected answer type: <class 'str'>
Error executing query 1291: Expecting ). Line 1, Col: 828.
  etime('2105-12-31 23:59:00','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
['null']
Error executing query 1293: Unexpected answer type: <class 'str'>
['null']
Error executing query 1294: Unexpected answer type: <class 'str'>
['null']
Error executing query 1295: Unexpected answer type: <class 'str'>
['null']
Error executing query 1296: Unexpected answer type: <class 'str'>
Error executing query 1297: Answer count mismatch: 4 != 8
Error executing query 1298: Invalid expression / Unexpected token. Line 1, Col: 984.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
['null']
Error executing query 1300: Unexpected answer type: <class 'str'>
['null']
Error executing query 1301: Unexpected answer type: <class 'str'>
Error executing query 1303: Invalid expression / Unexpected token. Line 1, Col: 905.
  agnoses_icd.charttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
['null']
Error executing query 1305: Unexpected answer type: <class 'str'>
Error executing query 1306: Invalid expression / Unexpected token. Line 1, Col: 690.
  ns.hadm_id from admissions where admissions.subject_id = 16484690 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
['null']
Error executing query 1307: Unexpected answer type: <class 'str'>
Error executing query 1308: Invalid expression / Unexpected token. Line 1, Col: 734.
  vqa("does a chest x-ray reveal any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
['null']
Error executing query 1310: Unexpected answer type: <class 'str'>
['null']
Error executing query 1312: Unexpected answer type: <class 'str'>
['null']
Error executing query 1315: Unexpected answer type: <class 'str'>
Error executing query 1317: Invalid expression / Unexpected token. Line 1, Col: 620.
  ns.hadm_id from admissions where admissions.subject_id = 19305006 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 1320: Expecting ). Line 1, Col: 843.
  microbiologyevents.charttime) = '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.test_name ) as t3 where t3.c1 = 3
Error executing query 1321: Answer count mismatch: 4 != 5
['null']
Error executing query 1325: Unexpected answer type: <class 'str'>
['null']
Error executing query 1327: Unexpected answer type: <class 'str'>
Error executing query 1328: Expecting ). Line 1, Col: 894.
  etime('2105-12-31 23:59:00','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1329: Invalid expression / Unexpected token. Line 1, Col: 866.
  etime('2105-12-31 23:59:00','-3 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1330: Answer count mismatch: 4 != 32
Error executing query 1331: Invalid expression / Unexpected token. Line 1, Col: 874.
  show hyperaeration in the left upper lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1333: Answer count mismatch: 4 != 10
Error executing query 1334: Answer count mismatch: 4 != 2
['null']
Error executing query 1336: Unexpected answer type: <class 'str'>
['null']
Error executing query 1337: Unexpected answer type: <class 'str'>
Error executing query 1338: Expecting ). Line 1, Col: 794.
  icrobiologyevents.charttime) >= '2102' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1339: Answer count mismatch: 4 != 32
['null']
Error executing query 1340: Unexpected answer type: <class 'str'>
['null']
Error executing query 1341: Unexpected answer type: <class 'str'>
Error executing query 1342: Answer count mismatch: 4 != 3
['null']
Error executing query 1347: Unexpected answer type: <class 'str'>
Error executing query 1348: Answer count mismatch: 4 != 32
['null']
Error executing query 1349: Unexpected answer type: <class 'str'>
['null']
Error executing query 1350: Unexpected answer type: <class 'str'>
['null']
Error executing query 1351: Unexpected answer type: <class 'str'>
Error executing query 1352: Answer count mismatch: 4 != 3
Error executing query 1354: Answer count mismatch: 4 != 32
Error executing query 1355: Invalid expression / Unexpected token. Line 1, Col: 863.
  id = 11725800 ) and strftime('%Y',diagnoses_icd.charttime) = '2105' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
['null']
Error executing query 1356: Unexpected answer type: <class 'str'>
Error executing query 1357: Invalid expression / Unexpected token. Line 1, Col: 812.
  ion of scoliosis in the spine on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
['null']
Error executing query 1358: Unexpected answer type: <class 'str'>
Error executing query 1359: Invalid expression / Unexpected token. Line 1, Col: 868.
  nth') = datetime('2105-12-31 23:59:00','start of month','-1 month') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
['null']
Error executing query 1360: Unexpected answer type: <class 'str'>
['null']
Error executing query 1361: Unexpected answer type: <class 'str'>
['null']
Error executing query 1362: Unexpected answer type: <class 'str'>
['null']
Error executing query 1363: Unexpected answer type: <class 'str'>
Error executing query 1366: Invalid expression / Unexpected token. Line 1, Col: 860.
  id = 10578743 ) and strftime('%Y',diagnoses_icd.charttime) = '2105' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1367: Invalid expression / Unexpected token. Line 1, Col: 872.
  d = 15110303 ) and strftime('%Y',procedures_icd.charttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
['null']
Error executing query 1369: Unexpected answer type: <class 'str'>
Error executing query 1370: Invalid expression / Unexpected token. Line 1, Col: 789.
   a chest x-ray reveal any mediastinal widening?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1371: Answer count mismatch: 4 != 6
['null']
Error executing query 1372: Unexpected answer type: <class 'str'>
['null']
Error executing query 1374: Unexpected answer type: <class 'str'>
Error executing query 1375: Answer count mismatch: 4 != 5
Error executing query 1377: Answer count mismatch: 4 != 8
Error executing query 1380: Invalid expression / Unexpected token. Line 1, Col: 1010.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1383: Invalid expression / Unexpected token. Line 1, Col: 990.
  vealing any anatomical findings in the trachea?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
['null']
Error executing query 1384: Unexpected answer type: <class 'str'>
['null']
Error executing query 1386: Unexpected answer type: <class 'str'>
Error executing query 1387: Invalid expression / Unexpected token. Line 1, Col: 873.
  d = 15546321 ) and strftime('%Y',procedures_icd.charttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1389: Invalid expression / Unexpected token. Line 1, Col: 658.
  ray reveal any devices in the right chest wall?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
['null']
Error executing query 1392: Unexpected answer type: <class 'str'>
Error executing query 1393: Invalid expression / Unexpected token. Line 1, Col: 875.
   airspace opacity in the left hilar structures?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1394: Invalid expression / Unexpected token. Line 1, Col: 955.
  etime('2105-12-31 23:59:00','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id
['null']
Error executing query 1396: Unexpected answer type: <class 'str'>
Error executing query 1398: Answer count mismatch: 4 != 32
['null']
Error executing query 1399: Unexpected answer type: <class 'str'>
Error executing query 1400: Invalid expression / Unexpected token. Line 1, Col: 772.
  synthetic substitute, open approach' ) ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
['null']
Error executing query 1401: Unexpected answer type: <class 'str'>
['null']
Error executing query 1402: Unexpected answer type: <class 'str'>
Error executing query 1403: Invalid expression / Unexpected token. Line 1, Col: 900.
  indicated in the upper mediastinum on an x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
['null']
Error executing query 1404: Unexpected answer type: <class 'str'>
Error executing query 1405: Answer count mismatch: 4 != 32
['null']
Error executing query 1406: Unexpected answer type: <class 'str'>
Error executing query 1409: Answer count mismatch: 4 != 14
['null']
Error executing query 1410: Unexpected answer type: <class 'str'>
Error executing query 1411: Invalid expression / Unexpected token. Line 1, Col: 754.
  qa("does a chest x-ray depicts any tubes/lines?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 1414: Answer count mismatch: 4 != 32
Error executing query 1417: Answer count mismatch: 4 != 12
['null']
Error executing query 1419: Unexpected answer type: <class 'str'>
Error executing query 1422: Invalid expression / Unexpected token. Line 1, Col: 730.
  a chest x-ray showing mediastinal displacement?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
['null']
Error executing query 1423: Unexpected answer type: <class 'str'>
['null']
Error executing query 1425: Unexpected answer type: <class 'str'>
['null']
Error executing query 1428: Unexpected answer type: <class 'str'>
['null']
Error executing query 1429: Unexpected answer type: <class 'str'>
Error executing query 1430: Answer count mismatch: 4 != 32
Error executing query 1433: Invalid expression / Unexpected token. Line 1, Col: 626.
  qa("does a chest x-ray depicts any abnormality?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
['null']
Error executing query 1434: Unexpected answer type: <class 'str'>
Error executing query 1436: Answer count mismatch: 4 != 14
Error executing query 1437: Answer count mismatch: 4 != 32
Error executing query 1438: Unexpected answer type: <class 'str'>
Error executing query 1440: Invalid expression / Unexpected token. Line 1, Col: 737.
  6505791 ) and strftime('%Y-%m',prescriptions.starttime) = '2105-12' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1442: Invalid expression / Unexpected token. Line 1, Col: 809.
  eal any abnormality in the cavoatrial junction?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
['null']
Error executing query 1443: Unexpected answer type: <class 'str'>
['null']
Error executing query 1444: Unexpected answer type: <class 'str'>
Error executing query 1445: Expecting ). Line 1, Col: 873.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1446: Invalid expression / Unexpected token. Line 1, Col: 990.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1447: Invalid expression / Unexpected token. Line 1, Col: 978.
  cedures_icd.charttime) >= datetime('2105-12-31 23:59:00','-4 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
['null']
Error executing query 1449: Unexpected answer type: <class 'str'>
['null']
Error executing query 1450: Unexpected answer type: <class 'str'>
Error executing query 1451: Invalid expression / Unexpected token. Line 1, Col: 735.
  ns.hadm_id from admissions where admissions.subject_id = 16484690 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1454: Invalid expression / Unexpected token. Line 1, Col: 739.
  d = 15981789 ) and strftime('%Y',prescriptions.starttime) >= '2105' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 1455: Invalid expression / Unexpected token. Line 1, Col: 853.
  r by admissions.admittime desc limit 1 ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of day') = datetime(t2.starttime,'start of day')
Error executing query 1456: Answer count mismatch: 4 != 11
['null']
Error executing query 1457: Unexpected answer type: <class 'str'>
['null']
Error executing query 1458: Unexpected answer type: <class 'str'>
['null']
Error executing query 1460: Unexpected answer type: <class 'str'>
['null']
Error executing query 1461: Unexpected answer type: <class 'str'>
['null']
Error executing query 1462: Unexpected answer type: <class 'str'>
['null']
Error executing query 1463: Unexpected answer type: <class 'str'>
Error executing query 1464: Answer count mismatch: 4 != 3
Error executing query 1465: Answer count mismatch: 4 != 3
['null']
Error executing query 1466: Unexpected answer type: <class 'str'>
['null']
Error executing query 1467: Unexpected answer type: <class 'str'>
['null']
Error executing query 1469: Unexpected answer type: <class 'str'>
['null']
Error executing query 1470: Unexpected answer type: <class 'str'>
['null']
Error executing query 1471: Unexpected answer type: <class 'str'>
['null']
Error executing query 1474: Unexpected answer type: <class 'str'>
['null']
Error executing query 1475: Unexpected answer type: <class 'str'>
['null']
Error executing query 1477: Unexpected answer type: <class 'str'>
Error executing query 1478: Invalid expression / Unexpected token. Line 1, Col: 1016.
   = 18684692 ) and strftime('%Y',procedures_icd.charttime) >= '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and t1.hadm_id = t3.hadm_id
Error executing query 1479: Expecting ). Line 1, Col: 892.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1480: Answer count mismatch: 4 != 2
['null']
Error executing query 1481: Unexpected answer type: <class 'str'>
Error executing query 1482: Expecting ). Line 1, Col: 921.
  etime('2105-12-31 23:59:00','-4 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1483: Expecting ). Line 1, Col: 977.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month') gro
['null']
Error executing query 1484: Unexpected answer type: <class 'str'>
['null']
Error executing query 1485: Unexpected answer type: <class 'str'>
Error executing query 1486: Answer count mismatch: 4 != 32
['null']
Error executing query 1487: Unexpected answer type: <class 'str'>
['null']
Error executing query 1488: Unexpected answer type: <class 'str'>
['null']
Error executing query 1489: Unexpected answer type: <class 'str'>
Error executing query 1490: Answer count mismatch: 4 != 3
Error executing query 1492: Invalid expression / Unexpected token. Line 1, Col: 891.
  ormality in the left shoulder on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
['null']
Error executing query 1494: Unexpected answer type: <class 'str'>
Error executing query 1495: Answer count mismatch: 4 != 2
['null']
Error executing query 1496: Unexpected answer type: <class 'str'>
['null']
Error executing query 1497: Unexpected answer type: <class 'str'>
Error executing query 1498: Invalid expression / Unexpected token. Line 1, Col: 872.
  id = 14097607 ) and strftime('%Y',diagnoses_icd.charttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
['null']
Error executing query 1500: Unexpected answer type: <class 'str'>
Error executing query 1501: Answer count mismatch: 4 != 14
Error executing query 1504: Answer count mismatch: 4 != 32
Error executing query 1505: Invalid expression / Unexpected token. Line 1, Col: 879.
   = 12864997 ) and strftime('%Y',procedures_icd.charttime) >= '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1506: Answer count mismatch: 4 != 14
['null']
Error executing query 1508: Unexpected answer type: <class 'str'>
['null']
Error executing query 1509: Unexpected answer type: <class 'str'>
['null']
Error executing query 1511: Unexpected answer type: <class 'str'>
['null']
Error executing query 1513: Unexpected answer type: <class 'str'>
['null']
Error executing query 1516: Unexpected answer type: <class 'str'>
Error executing query 1518: Answer count mismatch: 4 != 32
['null']
Error executing query 1519: Unexpected answer type: <class 'str'>
Error executing query 1521: Expecting ). Line 1, Col: 823.
  ime('%Y',labevents.charttime) = '2100' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.itemid ) as t3 where t3.c1 = 4 )
['null']
Error executing query 1522: Unexpected answer type: <class 'str'>
['null']
Error executing query 1523: Unexpected answer type: <class 'str'>
Error executing query 1524: Invalid expression / Unexpected token. Line 1, Col: 709.
  '%Y',prescriptions.starttime) = '2104' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
['null']
Error executing query 1528: Unexpected answer type: <class 'str'>
Error executing query 1531: near "(": syntax error
Error executing query 1533: Expecting ). Line 1, Col: 823.
  '%Y',diagnoses_icd.charttime) = '2105' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
['null']
Error executing query 1534: Unexpected answer type: <class 'str'>
Error executing query 1535: Invalid expression / Unexpected token. Line 1, Col: 714.
  c_vqa("does a chest x-ray show any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1536: Required keyword: 'expressions' missing for <class 'sqlglot.expressions.Aliases'>. Line 1, Col: 461.
  ratory rate' and d_items.linksto = 'chartevents' ) order by chartevents.charttime desc limit 1 )  ( [4mselect[0m chartevents.valuenum from chartevents where chartevents.stay_id in ( select icustays.stay_id from i
Error executing query 1537: Invalid expression / Unexpected token. Line 1, Col: 991.
  a("does a chest x-ray indicate any tubes/lines?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
['null']
Error executing query 1539: Unexpected answer type: <class 'str'>
['null']
Error executing query 1540: Unexpected answer type: <class 'str'>
Error executing query 1541: Invalid expression / Unexpected token. Line 1, Col: 749.
  x-ray show any abnormality in the right atrium?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1543: Invalid expression / Unexpected token. Line 1, Col: 989.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
['null']
Error executing query 1545: Unexpected answer type: <class 'str'>
['null']
Error executing query 1546: Unexpected answer type: <class 'str'>
Error executing query 1547: Answer count mismatch: 4 != 3
Error executing query 1550: Invalid expression / Unexpected token. Line 1, Col: 987.
  nth') = datetime('2105-12-31 23:59:00','start of month','-1 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1551: Expecting ). Line 1, Col: 985.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.spec_type_desc ) as t3 where t3.c1 = 3
['null']
Error executing query 1554: Unexpected answer type: <class 'str'>
['null']
Error executing query 1556: Unexpected answer type: <class 'str'>
['null']
Error executing query 1557: Unexpected answer type: <class 'str'>
['null']
Error executing query 1558: Unexpected answer type: <class 'str'>
Error executing query 1561: Answer count mismatch: 4 != 14
['null']
Error executing query 1563: Unexpected answer type: <class 'str'>
Error executing query 1564: Invalid expression / Unexpected token. Line 1, Col: 875.
  d = 16043637 ) and strftime('%Y',procedures_icd.charttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1566: Invalid expression / Unexpected token. Line 1, Col: 904.
  .dischtime is not null order by admissions.admittime desc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
['null']
Error executing query 1568: Unexpected answer type: <class 'str'>
['null']
Error executing query 1571: Unexpected answer type: <class 'str'>
['null']
Error executing query 1572: Unexpected answer type: <class 'str'>
['null']
Error executing query 1573: Unexpected answer type: <class 'str'>
['null']
Error executing query 1575: Unexpected answer type: <class 'str'>
['null']
Error executing query 1576: Unexpected answer type: <class 'str'>
['null']
Error executing query 1577: Unexpected answer type: <class 'str'>
['null']
Error executing query 1578: Unexpected answer type: <class 'str'>
Error executing query 1579: Invalid expression / Unexpected token. Line 1, Col: 930.
  etime('2105-12-31 23:59:00','-4 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
['null']
Error executing query 1580: Unexpected answer type: <class 'str'>
Error executing query 1582: Answer count mismatch: 4 != 17
Error executing query 1584: Invalid expression / Unexpected token. Line 1, Col: 968.
  dures_icd.charttime) >= datetime('2105-12-31 23:59:00','-51 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1585: Answer count mismatch: 4 != 2
Error executing query 1587: Answer count mismatch: 4 != 5
Error executing query 1588: Answer count mismatch: 4 != 10
Error executing query 1589: Answer count mismatch: 4 != 32
Error executing query 1590: Answer count mismatch: 4 != 32
['null']
Error executing query 1591: Unexpected answer type: <class 'str'>
Error executing query 1592: Answer count mismatch: 4 != 5
['null']
Error executing query 1593: Unexpected answer type: <class 'str'>
Error executing query 1594: Invalid expression / Unexpected token. Line 1, Col: 995.
   year','-0 year') and strftime('%m',prescriptions.starttime) = '06' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1595: Invalid expression / Unexpected token. Line 1, Col: 858.
   year') = datetime('2105-12-31 23:59:00','start of year','-0 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 1596: Answer count mismatch: 4 != 3
Error executing query 1598: Invalid expression / Unexpected token. Line 1, Col: 896.
   = 18246211 ) and strftime('%Y',procedures_icd.charttime) >= '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1600: Invalid expression / Unexpected token. Line 1, Col: 895.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id
Error executing query 1601: Answer count mismatch: 4 != 32
Error executing query 1603: Invalid expression / Unexpected token. Line 1, Col: 1017.
  .dischtime is not null order by admissions.admittime desc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
['null']
Error executing query 1604: Unexpected answer type: <class 'str'>
['null']
Error executing query 1606: Unexpected answer type: <class 'str'>
['null']
Error executing query 1609: Unexpected answer type: <class 'str'>
Error executing query 1610: Invalid expression / Unexpected token. Line 1, Col: 779.
  ns.hadm_id from admissions where admissions.subject_id = 13778342 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1611: Expecting ). Line 1, Col: 815.
  etime('2105-12-31 23:59:00','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 3
Error executing query 1612: Invalid expression / Unexpected token. Line 1, Col: 879.
  iagnoses_icd.charttime) = datetime('2105-12-31 23:59:00','-2 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
['null']
Error executing query 1613: Unexpected answer type: <class 'str'>
['null']
Error executing query 1614: Unexpected answer type: <class 'str'>
['null']
Error executing query 1616: Unexpected answer type: <class 'str'>
['null']
Error executing query 1617: Unexpected answer type: <class 'str'>
['null']
Error executing query 1618: Unexpected answer type: <class 'str'>
Error executing query 1620: Invalid expression / Unexpected token. Line 1, Col: 760.
  d = 17598348 ) and strftime('%Y',prescriptions.starttime) >= '2104' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 1621: Invalid expression / Unexpected token. Line 1, Col: 851.
  2601162 ) and strftime('%Y-%m',diagnoses_icd.charttime) = '2105-05' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1622: Expecting ). Line 1, Col: 709.
  ogyevents.hadm_id = admissions.hadm_id ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id group by t2.spec_type_desc ) as t3 where t3.c1 = 3
['null']
Error executing query 1623: Unexpected answer type: <class 'str'>
Error executing query 1624: Invalid expression / Unexpected token. Line 1, Col: 722.
  '%Y',prescriptions.starttime) = '2102' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id
['null']
Error executing query 1625: Unexpected answer type: <class 'str'>
['null']
Error executing query 1626: Unexpected answer type: <class 'str'>
Error executing query 1627: Invalid expression / Unexpected token. Line 1, Col: 849.
  442326 ) and strftime('%Y-%m',procedures_icd.charttime) = '2102-04' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1629: Unexpected answer type: <class 'str'>
Error executing query 1630: Invalid expression / Unexpected token. Line 1, Col: 942.
  etime('2105-12-31 23:59:00','-3 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1632: Invalid expression / Unexpected token. Line 1, Col: 731.
  d = 11184688 ) and strftime('%Y',prescriptions.starttime) >= '2105' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 1634: Answer count mismatch: 4 != 5
['null']
Error executing query 1636: Unexpected answer type: <class 'str'>
['null']
Error executing query 1640: Unexpected answer type: <class 'str'>
['null']
Error executing query 1641: Unexpected answer type: <class 'str'>
Error executing query 1644: Answer count mismatch: 4 != 32
['null']
Error executing query 1648: Unexpected answer type: <class 'str'>
['null']
Error executing query 1649: Unexpected answer type: <class 'str'>
Error executing query 1650: Expecting ). Line 1, Col: 801.
  microbiologyevents.charttime) = '2103' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month') gro
['null']
Error executing query 1651: Unexpected answer type: <class 'str'>
['null']
Error executing query 1652: Unexpected answer type: <class 'str'>
Error executing query 1654: Answer count mismatch: 4 != 2
['null']
Error executing query 1655: Unexpected answer type: <class 'str'>
['null']
Error executing query 1656: Unexpected answer type: <class 'str'>
Error executing query 1659: Expecting ). Line 1, Col: 759.
  %Y',prescriptions.starttime) >= '2102' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
['null']
Error executing query 1661: Unexpected answer type: <class 'str'>
['null']
Error executing query 1662: Unexpected answer type: <class 'str'>
['null']
Error executing query 1664: Unexpected answer type: <class 'str'>
['null']
Error executing query 1665: Unexpected answer type: <class 'str'>
Error executing query 1667: Invalid expression / Unexpected token. Line 1, Col: 954.
  ascular congestion in the left upper lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1669: Answer count mismatch: 4 != 3
Error executing query 1670: Expecting ). Line 1, Col: 1211.
  limit 1 ) order by tb_cxr.studydatetime desc limit 1 ) ) ) order by tb_cxr.studydatetime desc limit [4m1[0m
Error executing query 1672: Answer count mismatch: 4 != 32
['null']
Error executing query 1673: Unexpected answer type: <class 'str'>
['null']
Error executing query 1674: Unexpected answer type: <class 'str'>
Error executing query 1676: Answer count mismatch: 4 != 32
['null']
Error executing query 1677: Unexpected answer type: <class 'str'>
['null']
Error executing query 1678: Unexpected answer type: <class 'str'>
Error executing query 1679: Answer count mismatch: 4 != 9
Error executing query 1680: Invalid expression / Unexpected token. Line 1, Col: 472.
   t1.subject_id having min(t1.charttime) = t1.charttime and strftime('%Y',t1.charttime) = '2 month') [4m)[0m as t2 join ( select patients.subject_id, admissions.hadm_id, patients.dod from admissions join pati
['null']
Error executing query 1681: Unexpected answer type: <class 'str'>
['null']
Error executing query 1682: Unexpected answer type: <class 'str'>
Error executing query 1684: Invalid expression / Unexpected token. Line 1, Col: 825.
  rescriptions.starttime) = datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
['null']
Error executing query 1686: Unexpected answer type: <class 'str'>
Error executing query 1687: Invalid expression / Unexpected token. Line 1, Col: 919.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
Error executing query 1688: Answer count mismatch: 4 != 2
Error executing query 1689: Expecting ). Line 1, Col: 767.
  icrobiologyevents.charttime) >= '2101' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 1690: near "(": syntax error
['null']
Error executing query 1691: Unexpected answer type: <class 'str'>
Error executing query 1692: Invalid expression / Unexpected token. Line 1, Col: 632.
  a("does a chest x-ray indicate any abnormality?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1694: Answer count mismatch: 4 != 2
['null']
Error executing query 1695: Unexpected answer type: <class 'str'>
Error executing query 1696: Invalid expression / Unexpected token. Line 1, Col: 984.
  ng any abnormality in the left upper lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1697: Answer count mismatch: 4 != 24
['null']
Error executing query 1698: Unexpected answer type: <class 'str'>
['null']
Error executing query 1700: Unexpected answer type: <class 'str'>
['null']
Error executing query 1701: Unexpected answer type: <class 'str'>
['null']
Error executing query 1702: Unexpected answer type: <class 'str'>
['null']
Error executing query 1703: Unexpected answer type: <class 'str'>
Error executing query 1704: Answer count mismatch: 4 != 3
Error executing query 1705: Invalid expression / Unexpected token. Line 1, Col: 621.
  func_vqa("is a chest x-ray showing cyst/bullae?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1706: Answer count mismatch: 4 != 3
['null']
Error executing query 1708: Unexpected answer type: <class 'str'>
['null']
Error executing query 1711: Unexpected answer type: <class 'str'>
['null']
Error executing query 1712: Unexpected answer type: <class 'str'>
['null']
Error executing query 1713: Unexpected answer type: <class 'str'>
['null']
Error executing query 1716: Unexpected answer type: <class 'str'>
Error executing query 1717: Invalid expression / Unexpected token. Line 1, Col: 1006.
  769040 ) and strftime('%Y-%m',procedures_icd.charttime) = '2102-03' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and t1.hadm_id = t3.hadm_id
Error executing query 1718: Answer count mismatch: 4 != 6
Error executing query 1719: Answer count mismatch: 4 != 2
Error executing query 1720: Answer count mismatch: 4 != 32
Error executing query 1722: Invalid expression / Unexpected token. Line 1, Col: 870.
  ("is the chest x-ray depicting any tubes/lines?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
['null']
Error executing query 1723: Unexpected answer type: <class 'str'>
Error executing query 1724: Answer count mismatch: 4 != 2
['null']
Error executing query 1726: Unexpected answer type: <class 'str'>
['null']
Error executing query 1728: Unexpected answer type: <class 'str'>
['null']
Error executing query 1729: Unexpected answer type: <class 'str'>
Error executing query 1731: Invalid expression / Unexpected token. Line 1, Col: 851.
  c_vqa("is the chest x-ray revealing chest port?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
['null']
Error executing query 1732: Unexpected answer type: <class 'str'>
['null']
Error executing query 1734: Unexpected answer type: <class 'str'>
['null']
Error executing query 1735: Unexpected answer type: <class 'str'>
Error executing query 1736: Answer count mismatch: 4 != 15
['null']
Error executing query 1737: Unexpected answer type: <class 'str'>
['null']
Error executing query 1739: Unexpected answer type: <class 'str'>
['null']
Error executing query 1743: Unexpected answer type: <class 'str'>
['null']
Error executing query 1744: Unexpected answer type: <class 'str'>
['null']
Error executing query 1745: Unexpected answer type: <class 'str'>
Error executing query 1746: Invalid expression / Unexpected token. Line 1, Col: 850.
  vqa("is a chest x-ray detecting enlarged hilum?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
['null']
Error executing query 1749: Unexpected answer type: <class 'str'>
['null']
Error executing query 1751: Unexpected answer type: <class 'str'>
['null']
Error executing query 1754: Unexpected answer type: <class 'str'>
Error executing query 1755: Invalid expression / Unexpected token. Line 1, Col: 780.
   func_vqa("does a chest x-ray show any devices?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 1758: Invalid expression / Unexpected token. Line 1, Col: 901.
  d = 18679317 ) and strftime('%Y',diagnoses_icd.charttime) >= '2105' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
['null']
Error executing query 1763: Unexpected answer type: <class 'str'>
Error executing query 1765: Answer count mismatch: 4 != 5
['null']
Error executing query 1766: Unexpected answer type: <class 'str'>
['null']
Error executing query 1768: Unexpected answer type: <class 'str'>
Error executing query 1769: Answer count mismatch: 4 != 32
Error executing query 1770: Answer count mismatch: 4 != 3
['null']
Error executing query 1771: Unexpected answer type: <class 'str'>
Error executing query 1775: Answer count mismatch: 4 != 17
['null']
Error executing query 1777: Unexpected answer type: <class 'str'>
Error executing query 1779: Expecting ). Line 1, Col: 894.
  etime('2105-12-31 23:59:00','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
['null']
Error executing query 1780: Unexpected answer type: <class 'str'>
['null']
Error executing query 1781: Unexpected answer type: <class 'str'>
Error executing query 1782: Invalid expression / Unexpected token. Line 1, Col: 667.
   in the left hilar structures on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
['null']
Error executing query 1784: Unexpected answer type: <class 'str'>
Error executing query 1785: Invalid expression / Unexpected token. Line 1, Col: 868.
  ting any tubes/lines in the left mid lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1787: Invalid expression / Unexpected token. Line 1, Col: 782.
  ns.hadm_id from admissions where admissions.subject_id = 19265525 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1788: Answer count mismatch: 4 != 32
Error executing query 1789: Expecting ). Line 1, Col: 885.
  etime('2105-12-31 23:59:00','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 4
['null']
Error executing query 1790: Unexpected answer type: <class 'str'>
Error executing query 1791: Invalid expression / Unexpected token. Line 1, Col: 764.
  r by admissions.admittime desc limit 1 ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of day') = datetime(t2.starttime,'start of day')
['null']
Error executing query 1792: Unexpected answer type: <class 'str'>
['null']
Error executing query 1794: Unexpected answer type: <class 'str'>
['null']
Error executing query 1795: Unexpected answer type: <class 'str'>
['null']
Error executing query 1797: Unexpected answer type: <class 'str'>
Error executing query 1798: Invalid expression / Unexpected token. Line 1, Col: 858.
  d = 18961402 ) and strftime('%Y',diagnoses_icd.charttime) >= '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1801: Invalid expression / Unexpected token. Line 1, Col: 729.
  ns.hadm_id from admissions where admissions.subject_id = 11266631 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1802: Answer count mismatch: 4 != 16
['null']
Error executing query 1803: Unexpected answer type: <class 'str'>
['null']
Error executing query 1804: Unexpected answer type: <class 'str'>
['null']
Error executing query 1806: Unexpected answer type: <class 'str'>
Error executing query 1807: Answer count mismatch: 4 != 13
Error executing query 1808: Invalid expression / Unexpected token. Line 1, Col: 953.
   shown any abnormality in the right chest wall?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
['null']
Error executing query 1809: Unexpected answer type: <class 'str'>
Error executing query 1812: Invalid expression / Unexpected token. Line 1, Col: 854.
  nc_vqa("is a chest x-ray detecting any devices?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 1813: Invalid expression / Unexpected token. Line 1, Col: 938.
   = 14641317 ) and strftime('%Y',procedures_icd.charttime) >= '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
['null']
Error executing query 1814: Unexpected answer type: <class 'str'>
Error executing query 1815: Answer count mismatch: 4 != 6
['null']
Error executing query 1816: Unexpected answer type: <class 'str'>
['null']
Error executing query 1817: Unexpected answer type: <class 'str'>
Error executing query 1818: Unexpected answer type: <class 'str'>
Error executing query 1820: Invalid expression / Unexpected token. Line 1, Col: 880.
  23:59:00','start of month','-1 month') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of day') = datetime(t2.starttime,'start of day')
Error executing query 1821: Answer count mismatch: 4 != 14
Error executing query 1823: Invalid expression / Unexpected token. Line 1, Col: 764.
  eveal lung cancer in the left hilar structures?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 1829: Invalid expression / Unexpected token. Line 1, Col: 731.
  est x-ray showing fluid overload/heart failure?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
['null']
Error executing query 1831: Unexpected answer type: <class 'str'>
['null']
Error executing query 1833: Unexpected answer type: <class 'str'>
['null']
Error executing query 1836: Unexpected answer type: <class 'str'>
['null']
Error executing query 1837: Unexpected answer type: <class 'str'>
Error executing query 1838: Unexpected answer type: <class 'str'>
Error executing query 1840: Invalid expression / Unexpected token. Line 1, Col: 999.
  d = 15712372 ) and strftime('%Y',diagnoses_icd.charttime) >= '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
['null']
Error executing query 1841: Unexpected answer type: <class 'str'>
['null']
Error executing query 1842: Unexpected answer type: <class 'str'>
Error executing query 1843: Answer count mismatch: 4 != 8
Error executing query 1844: Invalid expression / Unexpected token. Line 1, Col: 924.
  d = 12907424 ) and strftime('%Y',procedures_icd.charttime) = '2100' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1847: Invalid expression / Unexpected token. Line 1, Col: 754.
  s a chest x-ray showing vascular calcification?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 1848: Invalid expression / Unexpected token. Line 1, Col: 923.
  qa("is a chest x-ray detecting any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
['null']
Error executing query 1849: Unexpected answer type: <class 'str'>
['null']
Error executing query 1850: Unexpected answer type: <class 'str'>
Error executing query 1851: Answer count mismatch: 4 != 13
Error executing query 1852: Answer count mismatch: 4 != 32
['null']
Error executing query 1854: Unexpected answer type: <class 'str'>
['null']
Error executing query 1857: Unexpected answer type: <class 'str'>
Error executing query 1858: Answer count mismatch: 4 != 32
['null']
Error executing query 1859: Unexpected answer type: <class 'str'>
['null']
Error executing query 1861: Unexpected answer type: <class 'str'>
Error executing query 1863: Answer count mismatch: 4 != 17
['null']
Error executing query 1865: Unexpected answer type: <class 'str'>
['null']
Error executing query 1866: Unexpected answer type: <class 'str'>
Error executing query 1867: Invalid expression / Unexpected token. Line 1, Col: 772.
  evealed in the right shoulder on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
['null']
Error executing query 1868: Unexpected answer type: <class 'str'>
Error executing query 1870: Answer count mismatch: 4 != 2
Error executing query 1871: Invalid expression / Unexpected token. Line 1, Col: 771.
  3710683 ) and strftime('%Y-%m',prescriptions.starttime) = '2105-08' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1873: Expecting ). Line 1, Col: 978.
  etime('2105-12-31 23:59:00','-3 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
['null']
Error executing query 1874: Unexpected answer type: <class 'str'>
['null']
Error executing query 1876: Unexpected answer type: <class 'str'>
['null']
Error executing query 1877: Unexpected answer type: <class 'str'>
Error executing query 1878: Answer count mismatch: 4 != 6
Error executing query 1881: Invalid expression / Unexpected token. Line 1, Col: 878.
  d = 18380697 ) and strftime('%Y',diagnoses_icd.charttime) >= '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
['null']
Error executing query 1882: Unexpected answer type: <class 'str'>
Error executing query 1883: Answer count mismatch: 4 != 32
Error executing query 1885: Expecting ). Line 1, Col: 826.
  microbiologyevents.charttime) = '2102' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
['null']
Error executing query 1886: Unexpected answer type: <class 'str'>
Error executing query 1887: Invalid expression / Unexpected token. Line 1, Col: 825.
  enchymal scarring in the left hilar structures?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1888: Unexpected answer type: <class 'str'>
Error executing query 1889: Answer count mismatch: 4 != 32
Error executing query 1891: Answer count mismatch: 4 != 5
['null']
Error executing query 1892: Unexpected answer type: <class 'str'>
Error executing query 1894: Invalid expression / Unexpected token. Line 1, Col: 897.
  .dischtime is not null order by admissions.admittime desc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
['null']
Error executing query 1896: Unexpected answer type: <class 'str'>
Error executing query 1897: Invalid expression / Unexpected token. Line 1, Col: 848.
  "does a chest x-ray reveal any any abnormality?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 1898: Invalid expression / Unexpected token. Line 1, Col: 728.
  vqa("does the chest x-ray indicate cabg grafts?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
['null']
Error executing query 1899: Unexpected answer type: <class 'str'>
['null']
Error executing query 1900: Unexpected answer type: <class 'str'>
['null']
Error executing query 1902: Unexpected answer type: <class 'str'>
['null']
Error executing query 1904: Unexpected answer type: <class 'str'>
['null']
Error executing query 1906: Unexpected answer type: <class 'str'>
Error executing query 1907: Expecting ). Line 1, Col: 773.
  icrobiologyevents.charttime) >= '2103' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
['null']
Error executing query 1909: Unexpected answer type: <class 'str'>
Error executing query 1910: Expecting ). Line 1, Col: 766.
  '%Y',prescriptions.starttime) = '2101' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id group by t2.drug ) as t3 where t3.c1 = 3
Error executing query 1912: Answer count mismatch: 4 != 2
Error executing query 1913: Invalid expression / Unexpected token. Line 1, Col: 862.
  w shoulder osteoarthritis in the left clavicle?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
['null']
Error executing query 1914: Unexpected answer type: <class 'str'>
Error executing query 1917: near "(": syntax error
['null']
Error executing query 1918: Unexpected answer type: <class 'str'>
Error executing query 1920: Invalid expression / Unexpected token. Line 1, Col: 887.
  etime('2105-12-31 23:59:00','-4 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
['null']
Error executing query 1921: Unexpected answer type: <class 'str'>
Error executing query 1924: near "(": syntax error
Error executing query 1925: Answer count mismatch: 4 != 32
Error executing query 1928: Invalid expression / Unexpected token. Line 1, Col: 817.
  re func_vqa("has an x-ray revealed cabg grafts?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
['null']
Error executing query 1929: Unexpected answer type: <class 'str'>
Error executing query 1930: Error tokenizing 'time) >= datetime('2105-12-31 23:59:00','-1 year''
Error executing query 1932: Answer count mismatch: 4 != 6
Error executing query 1933: Answer count mismatch: 4 != 2
['null']
Error executing query 1935: Unexpected answer type: <class 'str'>
Error executing query 1937: Invalid expression / Unexpected token. Line 1, Col: 775.
  ns.hadm_id from admissions where admissions.subject_id = 11553072 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
['null']
Error executing query 1938: Unexpected answer type: <class 'str'>
Error executing query 1939: Answer count mismatch: 4 != 3
['null']
Error executing query 1940: Unexpected answer type: <class 'str'>
Error executing query 1941: Invalid expression / Unexpected token. Line 1, Col: 882.
  iagnoses_icd.charttime) = datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
['null']
Error executing query 1942: Unexpected answer type: <class 'str'>
['null']
Error executing query 1944: Unexpected answer type: <class 'str'>
['null']
Error executing query 1945: Unexpected answer type: <class 'str'>
Error executing query 1946: Answer count mismatch: 4 != 32
Error executing query 1947: Answer count mismatch: 4 != 2
['null']
Error executing query 1950: Unexpected answer type: <class 'str'>
['null']
Error executing query 1953: Unexpected answer type: <class 'str'>
['null']
Error executing query 1954: Unexpected answer type: <class 'str'>
['null']
Error executing query 1955: Unexpected answer type: <class 'str'>
['null']
Error executing query 1956: Unexpected answer type: <class 'str'>
['null']
Error executing query 1957: Unexpected answer type: <class 'str'>
Error executing query 1958: Invalid expression / Unexpected token. Line 1, Col: 908.
  al any abnormality in the left upper lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
['null']
Error executing query 1959: Unexpected answer type: <class 'str'>
['null']
Error executing query 1960: Unexpected answer type: <class 'str'>
['null']
Error executing query 1961: Unexpected answer type: <class 'str'>
['null']
Error executing query 1962: Unexpected answer type: <class 'str'>
['null']
Error executing query 1963: Unexpected answer type: <class 'str'>
Error executing query 1964: Answer count mismatch: 4 != 32
Error executing query 1965: Invalid expression / Unexpected token. Line 1, Col: 783.
  escriptions.starttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
['null']
Error executing query 1966: Unexpected answer type: <class 'str'>
['null']
Error executing query 1967: Unexpected answer type: <class 'str'>
['null']
Error executing query 1968: Unexpected answer type: <class 'str'>
Error executing query 1969: Invalid expression / Unexpected token. Line 1, Col: 754.
  func_vqa("has a chest x-ray shown any diseases?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
['null']
Error executing query 1971: Unexpected answer type: <class 'str'>
Error executing query 1973: Expecting ). Line 1, Col: 928.
  etime('2105-12-31 23:59:00','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t1.charttime,'start of month') = datetime(t2.starttime,'start of month') gro
['null']
Error executing query 1974: Unexpected answer type: <class 'str'>
['null']
Error executing query 1976: Unexpected answer type: <class 'str'>
Error executing query 1977: Invalid expression / Unexpected token. Line 1, Col: 838.
  d = 19025961 ) and strftime('%Y',procedures_icd.charttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 104, in <module>
    Defaults.start()
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/dtu/__init__.py", line 235, in start
    cls.run(*args)
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 69, in run
    executed_result = run_execution_for_gt_query(executor, parsed_result_gt)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/NeuralSQL/execute_nsql.py", line 81, in run_execution_for_gt_query
    result = executor.execute_nsql(query)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/NeuralSQL/executor/nsql_executor.py", line 265, in execute_nsql
    return self._execute_select_query(query_root, nsql, tables)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/NeuralSQL/executor/nsql_executor.py", line 327, in _execute_select_query
    return self._execute_vqa_subquery(from_clause_node, query_root, nsql, tables)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/NeuralSQL/executor/nsql_executor.py", line 358, in _execute_vqa_subquery
    return self.execute_vqa_function_in_nsql(nsql, tables)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/NeuralSQL/executor/nsql_executor.py", line 191, in execute_vqa_function_in_nsql
    answer_batch = self._execute_vqa_function(image_batch=image_batch, question_batch=question_batch)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/NeuralSQL/executor/nsql_executor.py", line 120, in _execute_vqa_function
    answers = self.vqa_module(image_batch, question_batch)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/NeuralSQL/executor/visual_module/custom_vqa_module.py", line 81, in __call__
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
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/pjit.py", line 1462, in _pjit_call_impl_python
    return compiled.unsafe_call(*args), compiled
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/profiler.py", line 335, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/interpreters/pxla.py", line 1185, in __call__
    results = self.xla_executable.execute_sharded(input_bufs)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
KeyboardInterrupt
Terminated

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21905852: <eval_fulla40_0> in cluster <dcc> Exited

Job <eval_fulla40_0> was submitted from host <n-62-30-8> by user <s183914> in cluster <dcc> at Mon Jun  3 16:20:26 2024
Job was executed on host(s) <4*n-62-12-23>, in queue <gpua100>, as user <s183914> in cluster <dcc> at Mon Jun  3 16:51:00 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_final/ML_final> was used as the working directory.
Started at Mon Jun  3 16:51:00 2024
Terminated at Mon Jun  3 17:44:50 2024
Results reported at Mon Jun  3 17:44:50 2024

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q gpua100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 4
#BSUB -R "rusage[mem=16G]"
#BSUB -R "select[gpu40gb]"
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

    CPU time :                                   3308.00 sec.
    Max Memory :                                 13252 MB
    Average Memory :                             10491.22 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               52284.00 MB
    Max Swap :                                   -
    Max Processes :                              7
    Max Threads :                                68
    Run time :                                   3232 sec.
    Turnaround time :                            5064 sec.

The output (if any) is above this job summary.

