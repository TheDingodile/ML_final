2024-06-04 09:07:52.550396: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.17.0
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_final/ML_final/wandb/run-20240604_090805-o2wjx975
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run test_final_a80-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/o2wjx975
2024-06-04 09:08:23.716684: W tensorflow/core/common_runtime/gpu/gpu_device.cc:2251] Cannot dlopen some GPU libraries. Please make sure the missing libraries mentioned above are installed properly if you would like to use GPU. Follow the guide at https://www.tensorflow.org/install/gpu for how to download and setup the required libraries for your platform.
Skipping registering GPU devices...
2024-06-04 09:08:29.403324: W external/xla/xla/service/gpu/nvptx_compiler.cc:760] The NVIDIA driver's CUDA version is 12.4 which is older than the ptxas CUDA version (12.5.40). Because the driver is older than the ptxas version, XLA is disabling parallel compilation, which may slow down compilation. You should update your NVIDIA driver or use the NVIDIA-provided CUDA forward compatibility packages.

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
| <c>name</c>       | <d>str</d>        | <j>"test_final_a80-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>3600</f>       |
| <c>vqa_module_type</c>| <d>str</d>        | <j>"custom"</j>   |
| <c>prediction_file_name</c>| <d>str</d>        | <j>"predictions_LLM_1-0"</j> |

# Output

```
sid_to_ipath_map loaded. (1896 entries)
Error executing query 1: Invalid expression / Unexpected token. Line 1, Col: 651.
  ns.hadm_id from admissions where admissions.subject_id = 12252397 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 2: Model only answers one image question SQLs
Error executing query 3: Invalid expression / Unexpected token. Line 1, Col: 914.
  func_vqa("does a chest x-ray show any diseases?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 5: Model abstains from answering the question
Error executing query 12: Model only answers one image question SQLs
Error executing query 14: Model only answers one image question SQLs
Error executing query 16: Model abstains from answering the question
Error executing query 17: Invalid expression / Unexpected token. Line 1, Col: 958.
  nth') = datetime('2105-12-31 23:59:00','start of month','-0 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 23: Model abstains from answering the question
Error executing query 26: Invalid expression / Unexpected token. Line 1, Col: 821.
  escriptions.starttime) >= datetime('2105-12-31 23:59:00','-5 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 29: Model only answers one image question SQLs
Error executing query 33: Invalid expression / Unexpected token. Line 1, Col: 914.
  dures_icd.charttime) >= datetime('2105-12-31 23:59:00','-12 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 34: Model only answers one image question SQLs
Error executing query 35: Model only answers one image question SQLs
Error executing query 37: Model abstains from answering the question
Error executing query 41: Invalid expression / Unexpected token. Line 1, Col: 779.
  aling copd/emphysema in the left mid lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 42: Invalid expression / Unexpected token. Line 1, Col: 777.
  _vqa("is a chest x-ray showing any abnormality?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 43: Model abstains from answering the question
Error executing query 53: Model only answers one image question SQLs
Error executing query 54: Invalid expression / Unexpected token. Line 1, Col: 746.
  st x-ray show any abnormality in the left lung?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 55: Model only answers one image question SQLs
Error executing query 59: Model only answers one image question SQLs
Error executing query 62: Model abstains from answering the question
Error executing query 64: Model only answers one image question SQLs
Error executing query 66: Invalid expression / Unexpected token. Line 1, Col: 1103.
   year','-0 year') and strftime('%m',diagnoses_icd.charttime) = '09' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime
Error executing query 69: Expecting ). Line 1, Col: 1072.
  ar','-0 year') ) as t2 join admissions on t2.subject_id = admissions.subject_id where t2.charttime  [4madmissions[0m.admittime and datetime(admissions.admittime,'start of year') = datetime('2105-12-31 23:59:00','star
Error executing query 71: Model only answers one image question SQLs
Error executing query 74: Model only answers one image question SQLs
Error executing query 85: Model abstains from answering the question
Error executing query 87: Model abstains from answering the question
Error executing query 88: Invalid expression / Unexpected token. Line 1, Col: 957.
  iagnoses_icd.charttime) = datetime('2105-12-31 23:59:00','-2 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 89: Invalid expression / Unexpected token. Line 1, Col: 652.
  ns.hadm_id from admissions where admissions.subject_id = 17198431 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 94: Model only answers one image question SQLs
Error executing query 101: Invalid expression / Unexpected token. Line 1, Col: 760.
  w any spinal degenerative changes in the spine?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 102: Invalid expression / Unexpected token. Line 1, Col: 882.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 103: Invalid expression / Unexpected token. Line 1, Col: 949.
  380697 ) and strftime('%Y-%m',procedures_icd.charttime) = '2105-06' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 104: Model abstains from answering the question
Error executing query 108: Invalid expression / Unexpected token. Line 1, Col: 1010.
   year') = datetime('2105-12-31 23:59:00','start of year','-0 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
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
Error executing query 134: Model abstains from answering the question
Error executing query 137: Model abstains from answering the question
Error executing query 139: Invalid expression / Unexpected token. Line 1, Col: 757.
  ns.hadm_id from admissions where admissions.subject_id = 19385269 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 140: Model only answers one image question SQLs
Error executing query 141: Invalid expression / Unexpected token. Line 1, Col: 1065.
  cedures_icd.charttime) >= datetime('2105-12-31 23:59:00','-2 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and t1.hadm_id = t3.hadm_id
Error executing query 145: Model only answers one image question SQLs
Error executing query 146: Model only answers one image question SQLs
Error executing query 149: Model only answers one image question SQLs
Error executing query 150: Model abstains from answering the question
Error executing query 153: Model abstains from answering the question
Error executing query 155: Model only answers one image question SQLs
Error executing query 157: Invalid expression / Unexpected token. Line 1, Col: 871.
   where func_vqa("is any abnormality identified?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 160: Invalid expression / Unexpected token. Line 1, Col: 994.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id
Error executing query 162: Invalid expression / Unexpected token. Line 1, Col: 736.
  id = 18380697 ) and strftime('%Y',prescriptions.starttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 166: Model only answers one image question SQLs
Error executing query 168: Invalid expression / Unexpected token. Line 1, Col: 938.
  etime('2105-12-31 23:59:00','-2 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id
Error executing query 169: Model only answers one image question SQLs
Error executing query 171: Model only answers one image question SQLs
Error executing query 173: Model abstains from answering the question
Error executing query 175: Model abstains from answering the question
Error executing query 176: Model only answers one image question SQLs
Error executing query 178: Invalid expression / Unexpected token. Line 1, Col: 876.
  s.dischtime is not null order by admissions.admittime asc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 179: Model only answers one image question SQLs
Error executing query 180: Model only answers one image question SQLs
Error executing query 181: Model abstains from answering the question
Error executing query 183: Model only answers one image question SQLs
Error executing query 184: Invalid expression / Unexpected token. Line 1, Col: 930.
  t x-ray show any abnormality in the right lung?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 188: Invalid expression / Unexpected token. Line 1, Col: 829.
  iple masses/nodules in the right mid lung zone?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 190: Invalid expression / Unexpected token. Line 1, Col: 887.
  id = 15467362 ) and strftime('%Y',diagnoses_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 194: Model abstains from answering the question
Error executing query 195: Invalid expression / Unexpected token. Line 1, Col: 925.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 196: Invalid expression / Unexpected token. Line 1, Col: 758.
  y any abnormality in the right upper lung zone?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 197: Model abstains from answering the question
Error executing query 199: Model only answers one image question SQLs
Error executing query 204: Invalid expression / Unexpected token. Line 1, Col: 935.
  agnoses_icd.charttime) >= datetime('2105-12-31 23:59:00','-2 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 208: Model only answers one image question SQLs
Error executing query 209: Model only answers one image question SQLs
Error executing query 211: Invalid expression / Unexpected token. Line 1, Col: 960.
  dures_icd.charttime) >= datetime('2105-12-31 23:59:00','-33 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 216: Model abstains from answering the question
Error executing query 218: Invalid expression / Unexpected token. Line 1, Col: 731.
  id = 19970078 ) and strftime('%Y',prescriptions.starttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 219: Model only answers one image question SQLs
Error executing query 221: Model only answers one image question SQLs
Error executing query 222: Model abstains from answering the question
Error executing query 224: Model only answers one image question SQLs
Error executing query 225: Error tokenizing 'in patients on t4.subject_id = patients.subject_i'
Error executing query 233: Invalid expression / Unexpected token. Line 1, Col: 620.
  _vqa("is any devices observed on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 240: Model abstains from answering the question
Error executing query 241: Model abstains from answering the question
Error executing query 242: Model abstains from answering the question
Error executing query 244: Model only answers one image question SQLs
Error executing query 245: Model only answers one image question SQLs
Error executing query 246: Invalid expression / Unexpected token. Line 1, Col: 810.
  escriptions.starttime) >= datetime('2105-12-31 23:59:00','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 247: Model only answers one image question SQLs
Error executing query 248: Model abstains from answering the question
Error executing query 253: Model only answers one image question SQLs
Error executing query 255: Invalid expression / Unexpected token. Line 1, Col: 746.
   observed in the right atrium on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 256: Model abstains from answering the question
Error executing query 257: Model only answers one image question SQLs
Error executing query 259: Model abstains from answering the question
Error executing query 262: Invalid expression / Unexpected token. Line 1, Col: 903.
  vqa("is any abnormality shown on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 265: Model only answers one image question SQLs
Error executing query 267: Model abstains from answering the question
Error executing query 269: Model only answers one image question SQLs
Error executing query 270: Model only answers one image question SQLs
Error executing query 271: Model only answers one image question SQLs
Error executing query 272: Invalid expression / Unexpected token. Line 1, Col: 727.
  id = 11685699 ) and strftime('%Y',prescriptions.starttime) = '2105' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 273: Model only answers one image question SQLs
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
Error executing query 294: Model only answers one image question SQLs
Error executing query 296: Model abstains from answering the question
Error executing query 297: Model only answers one image question SQLs
Error executing query 298: Model only answers one image question SQLs
Error executing query 303: Model abstains from answering the question
Error executing query 304: Invalid expression / Unexpected token. Line 1, Col: 848.
  d = 13411278 ) and strftime('%Y',procedures_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 305: Model abstains from answering the question
Error executing query 309: Invalid expression / Unexpected token. Line 1, Col: 1025.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 311: Model only answers one image question SQLs
Error executing query 313: Model only answers one image question SQLs
Error executing query 319: Model only answers one image question SQLs
Error executing query 321: Model only answers one image question SQLs
Error executing query 322: Model only answers one image question SQLs
Error executing query 323: Model only answers one image question SQLs
Error executing query 328: Model only answers one image question SQLs
Error executing query 331: Model only answers one image question SQLs
Error executing query 333: Invalid expression / Unexpected token. Line 1, Col: 1042.
   in the right lower lung zone on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 335: Model only answers one image question SQLs
Error executing query 336: Invalid expression / Unexpected token. Line 1, Col: 985.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 338: Model only answers one image question SQLs
Error executing query 351: Invalid expression / Unexpected token. Line 1, Col: 733.
  unc_vqa("is a chest x-ray showing infiltration?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 352: Model only answers one image question SQLs
Error executing query 356: Model abstains from answering the question
Error executing query 357: Model only answers one image question SQLs
Error executing query 359: Invalid expression / Unexpected token. Line 1, Col: 995.
   year') = datetime('2105-12-31 23:59:00','start of year','-0 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 360: Model only answers one image question SQLs
Error executing query 366: Invalid expression / Unexpected token. Line 1, Col: 764.
  etime('2105-12-31 23:59:00','-5 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 367: Invalid expression / Unexpected token. Line 1, Col: 735.
  ion of four or more vascular stents' ) ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 369: Model only answers one image question SQLs
Error executing query 370: Model only answers one image question SQLs
Error executing query 372: Model only answers one image question SQLs
Error executing query 374: Model only answers one image question SQLs
Error executing query 375: Model only answers one image question SQLs
Error executing query 376: Model only answers one image question SQLs
Error executing query 383: Model only answers one image question SQLs
Error executing query 385: Invalid expression / Unexpected token. Line 1, Col: 936.
  agnoses_icd.charttime) = datetime('2105-12-31 23:59:00','-3 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 387: Invalid expression / Unexpected token. Line 1, Col: 801.
  ray indicate any abnormality in the right lung?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 389: Model only answers one image question SQLs
Error executing query 391: Model only answers one image question SQLs
Error executing query 397: Model abstains from answering the question
Error executing query 400: Model only answers one image question SQLs
Error executing query 407: Model only answers one image question SQLs
Error executing query 410: Model abstains from answering the question
Error executing query 412: Invalid expression / Unexpected token. Line 1, Col: 879.
   shoulder osteoarthritis in the right shoulder?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 413: Model abstains from answering the question
Error executing query 415: Model abstains from answering the question
Error executing query 416: Invalid expression / Unexpected token. Line 1, Col: 971.
  y reveal mass/nodule (not otherwise specified)?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 421: Model abstains from answering the question
Error executing query 423: Invalid expression / Unexpected token. Line 1, Col: 734.
  id = 10681061 ) and strftime('%Y',prescriptions.starttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 424: Model abstains from answering the question
Error executing query 425: Invalid expression / Unexpected token. Line 1, Col: 895.
  a("does a chest x-ray indicate any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 427: Model only answers one image question SQLs
Error executing query 428: Model only answers one image question SQLs
Error executing query 435: Invalid expression / Unexpected token. Line 1, Col: 732.
  ns.hadm_id from admissions where admissions.subject_id = 15234578 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 438: Invalid expression / Unexpected token. Line 1, Col: 775.
  ns.hadm_id from admissions where admissions.subject_id = 15346117 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 441: Model abstains from answering the question
Error executing query 443: Invalid expression / Unexpected token. Line 1, Col: 880.
  s.dischtime is not null order by admissions.admittime asc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 444: Invalid expression / Unexpected token. Line 1, Col: 841.
  ns.hadm_id from admissions where admissions.subject_id = 11131026 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
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
Error executing query 461: Expecting ). Line 1, Col: 794.
  of the jaws' ) ) as t2 join admissions on t2.subject_id = admissions.subject_id where t2.charttime  [4madmissions[0m.admittime and datetime(admissions.admittime) between datetime(t2.charttime) and datetime(t2.chartti
Error executing query 462: Model abstains from answering the question
Error executing query 463: Invalid expression / Unexpected token. Line 1, Col: 895.
  id = 15584605 ) and strftime('%Y',diagnoses_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 464: Invalid expression / Unexpected token. Line 1, Col: 955.
  cedures_icd.charttime) = datetime('2105-12-31 23:59:00','-2 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 465: Invalid expression / Unexpected token. Line 1, Col: 863.
  e func_vqa("has an x-ray indicated lung lesion?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 466: Model abstains from answering the question
Error executing query 467: Model abstains from answering the question
Error executing query 472: Model only answers one image question SQLs
Error executing query 473: Invalid expression / Unexpected token. Line 1, Col: 962.
  1 23:59:00','start of year','-1 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t1.charttime,'start of month') = datetime(t2.charttime,'start of month')
Error executing query 474: Invalid expression / Unexpected token. Line 1, Col: 825.
  rated any diseases in the left upper lung zone?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 475: Model abstains from answering the question
Error executing query 477: Invalid expression / Unexpected token. Line 1, Col: 868.
   = 19896759 ) and strftime('%Y',procedures_icd.charttime) >= '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 478: Model only answers one image question SQLs
Error executing query 483: Model only answers one image question SQLs
Error executing query 487: Model only answers one image question SQLs
Error executing query 488: Model abstains from answering the question
Error executing query 490: Model only answers one image question SQLs
Error executing query 491: Model abstains from answering the question
Error executing query 494: Model abstains from answering the question
Error executing query 496: Model only answers one image question SQLs
Error executing query 498: Model abstains from answering the question
Error executing query 499: Invalid expression / Unexpected token. Line 1, Col: 919.
  edures_icd.charttime) >= datetime('2105-12-31 23:59:00','-1 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 500: Invalid expression / Unexpected token. Line 1, Col: 918.
  t x-ray detecting pleural/parenchymal scarring?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 502: Invalid expression / Unexpected token. Line 1, Col: 895.
   indication of tortuous aorta on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 503: Model abstains from answering the question
Error executing query 507: Model abstains from answering the question
Error executing query 509: Model only answers one image question SQLs
Error executing query 513: Model only answers one image question SQLs
Error executing query 514: Model abstains from answering the question
Error executing query 515: Model only answers one image question SQLs
Error executing query 516: Model only answers one image question SQLs
Error executing query 517: Model only answers one image question SQLs
Error executing query 518: Model abstains from answering the question
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
Error executing query 542: Model only answers one image question SQLs
Error executing query 543: Model abstains from answering the question
Error executing query 544: Model abstains from answering the question
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
Error executing query 561: Invalid expression / Unexpected token. Line 1, Col: 1031.
  s.dischtime is not null order by admissions.admittime asc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 565: Invalid expression / Unexpected token. Line 1, Col: 879.
  ng any abnormality in the left upper lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 566: Model abstains from answering the question
Error executing query 567: Model abstains from answering the question
Error executing query 571: Model abstains from answering the question
Error executing query 573: Model only answers one image question SQLs
Error executing query 576: Invalid expression / Unexpected token. Line 1, Col: 777.
  ns.hadm_id from admissions where admissions.subject_id = 18380697 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 580: Model only answers one image question SQLs
Error executing query 581: Invalid expression / Unexpected token. Line 1, Col: 797.
  est x-ray indicate any any anatomical findings?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 588: Model abstains from answering the question
Error executing query 593: Model abstains from answering the question
Error executing query 594: Model abstains from answering the question
Error executing query 596: Invalid expression / Unexpected token. Line 1, Col: 880.
  .dischtime is not null order by admissions.admittime desc limit 1 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 599: Model abstains from answering the question
Error executing query 600: Model abstains from answering the question
Error executing query 601: Invalid expression / Unexpected token. Line 1, Col: 786.
  1468671 ) and strftime('%Y-%m',prescriptions.starttime) = '2102-01' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 602: Model abstains from answering the question
Error executing query 603: Model only answers one image question SQLs
Error executing query 604: Model only answers one image question SQLs
Error executing query 605: Model only answers one image question SQLs
Error executing query 608: Model abstains from answering the question
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
Error executing query 626: Model abstains from answering the question
Error executing query 627: Invalid expression / Unexpected token. Line 1, Col: 913.
  id = 18380697 ) and strftime('%Y',diagnoses_icd.charttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
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
Error executing query 652: Model abstains from answering the question
Error executing query 653: Invalid expression / Unexpected token. Line 1, Col: 891.
  func_vqa("does an x-ray reveal any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 655: Model only answers one image question SQLs
Error executing query 657: Invalid expression / Unexpected token. Line 1, Col: 726.
  qa("does a chest x-ray reveal any any diseases?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 659: Invalid expression / Unexpected token. Line 1, Col: 988.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 664: Model only answers one image question SQLs
Error executing query 665: Invalid expression / Unexpected token. Line 1, Col: 878.
  398283 ) and strftime('%Y-%m',procedures_icd.charttime) = '2104-08' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 666: Model only answers one image question SQLs
Error executing query 667: Model only answers one image question SQLs
Error executing query 668: Model only answers one image question SQLs
Error executing query 669: Model only answers one image question SQLs
Error executing query 671: Invalid expression / Unexpected token. Line 1, Col: 749.
  id = 18136887 ) and strftime('%Y',prescriptions.starttime) = '2104' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 672: Model abstains from answering the question
Error executing query 679: Model only answers one image question SQLs
Error executing query 680: Model only answers one image question SQLs
Error executing query 687: Invalid expression / Unexpected token. Line 1, Col: 769.
  how any any abnormality in the left chest wall?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 694: Model abstains from answering the question
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
Error executing query 706: Model only answers one image question SQLs
Error executing query 707: Model only answers one image question SQLs
Error executing query 709: Model only answers one image question SQLs
Error executing query 713: Model only answers one image question SQLs
Error executing query 715: Model only answers one image question SQLs
Error executing query 717: Model only answers one image question SQLs
Error executing query 718: Model only answers one image question SQLs
Error executing query 719: Invalid expression / Unexpected token. Line 1, Col: 877.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 720: Model only answers one image question SQLs
Error executing query 724: Invalid expression / Unexpected token. Line 1, Col: 745.
  ns.hadm_id from admissions where admissions.subject_id = 10938464 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 728: Invalid expression / Unexpected token. Line 1, Col: 978.
  f costophrenic angle blunting on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 729: Model only answers one image question SQLs
Error executing query 732: Invalid expression / Unexpected token. Line 1, Col: 889.
  does a chest x-ray show elevated hemidiaphragm?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 733: Invalid expression / Unexpected token. Line 1, Col: 959.
  1 23:59:00','start of year','-0 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and t1.hadm_id = t2.hadm_id
Error executing query 734: Invalid expression / Unexpected token. Line 1, Col: 629.
  ns.hadm_id from admissions where admissions.subject_id = 16922420 ) ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
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
Error executing query 751: Model abstains from answering the question
Error executing query 752: Model abstains from answering the question
Error executing query 754: Invalid expression / Unexpected token. Line 1, Col: 716.
  ns.hadm_id from admissions where admissions.subject_id = 12408912 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 756: Expecting ). Line 1, Col: 1031.
  olume ( dialysis/pheresis catheters )' ) as t3 on t2.subject_id = t3.subject_id where t2.charttime  [4mt3[0m.starttime ) as t4 join patients on t4.subject_id = patients.subject_id
Error executing query 758: Model only answers one image question SQLs
Error executing query 759: Model abstains from answering the question
Error executing query 760: Expecting ). Line 1, Col: 970.
  ere prescriptions.drug = 'colesevelam' ) as t3 on t2.subject_id = t3.subject_id where t2.charttime  [4mt3[0m.starttime ) as t4 join patients on t4.subject_id = patients.subject_id
Error executing query 764: Invalid expression / Unexpected token. Line 1, Col: 1095.
  agnoses_icd.charttime) >= datetime('2105-12-31 23:59:00','-3 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 765: Model only answers one image question SQLs
Error executing query 766: Model only answers one image question SQLs
Error executing query 767: Invalid expression / Unexpected token. Line 1, Col: 927.
   anatomical findings in the left mid lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 768: Model only answers one image question SQLs
Error executing query 774: Model abstains from answering the question
Error executing query 775: Invalid expression / Unexpected token. Line 1, Col: 1005.
  _vqa("does a chest x-ray indicate any diseases?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 776: Invalid expression / Unexpected token. Line 1, Col: 883.
  any indication of any devices on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 779: Model only answers one image question SQLs
Error executing query 782: Model abstains from answering the question
Error executing query 785: Invalid expression / Unexpected token. Line 1, Col: 767.
  ns.hadm_id from admissions where admissions.subject_id = 13119866 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 788: Model only answers one image question SQLs
Error executing query 797: Invalid expression / Unexpected token. Line 1, Col: 913.
  s a chest x-ray show goiter in the mediastinum?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 798: Invalid expression / Unexpected token. Line 1, Col: 747.
  icate any abnormality in the right apical zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 802: Invalid expression / Unexpected token. Line 1, Col: 882.
  ay indicate cardiac pacer and wires in the svc?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 803: Model abstains from answering the question
Error executing query 809: Model only answers one image question SQLs
Error executing query 810: Invalid expression / Unexpected token. Line 1, Col: 726.
   t2 where func_vqa("is tortuous aorta revealed?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 811: Model abstains from answering the question
Error executing query 812: Model abstains from answering the question
Error executing query 813: Model abstains from answering the question
Error executing query 814: Model abstains from answering the question
Error executing query 819: Model only answers one image question SQLs
Error executing query 820: Invalid expression / Unexpected token. Line 1, Col: 861.
  id = 17968028 ) and strftime('%Y',diagnoses_icd.charttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 821: Model abstains from answering the question
Error executing query 822: Model only answers one image question SQLs
Error executing query 823: Model only answers one image question SQLs
Error executing query 824: Model only answers one image question SQLs
Error executing query 825: Invalid expression / Unexpected token. Line 1, Col: 779.
  ns.hadm_id from admissions where admissions.subject_id = 16529186 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 830: Model only answers one image question SQLs
Error executing query 831: Invalid expression / Unexpected token. Line 1, Col: 768.
  ns.hadm_id from admissions where admissions.subject_id = 13411278 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
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
Error executing query 846: Model only answers one image question SQLs
Error executing query 847: Model only answers one image question SQLs
Error executing query 856: Model abstains from answering the question
Error executing query 857: Model only answers one image question SQLs
Error executing query 860: Model only answers one image question SQLs
Error executing query 861: Model only answers one image question SQLs
Error executing query 862: Model abstains from answering the question
Error executing query 864: Model abstains from answering the question
Error executing query 865: Invalid expression / Unexpected token. Line 1, Col: 853.
  nc_vqa("has an x-ray indicated any abnormality?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 866: Model only answers one image question SQLs
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
Error executing query 891: Invalid expression / Unexpected token. Line 1, Col: 737.
  831708 ) and strftime('%Y-%m',prescriptions.starttime) >= '2104-02' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 892: Model only answers one image question SQLs
Error executing query 894: Model only answers one image question SQLs
Error executing query 897: Model abstains from answering the question
Error executing query 898: Invalid expression / Unexpected token. Line 1, Col: 936.
  gnoses_icd.charttime) = datetime('2105-12-31 23:59:00','-25 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 901: Model abstains from answering the question
Error executing query 903: Invalid expression / Unexpected token. Line 1, Col: 861.
  segmental collapse in the left upper lung zone?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 904: Model only answers one image question SQLs
Error executing query 906: Invalid expression / Unexpected token. Line 1, Col: 1056.
   year') = datetime('2105-12-31 23:59:00','start of year','-1 year') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 907: Model only answers one image question SQLs
Error executing query 914: Model abstains from answering the question
Error executing query 915: Model only answers one image question SQLs
Error executing query 916: Model abstains from answering the question
Error executing query 918: Model only answers one image question SQLs
Error executing query 919: Invalid expression / Unexpected token. Line 1, Col: 751.
   in the left hilar structures on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 921: Invalid expression / Unexpected token. Line 1, Col: 970.
   year','-0 year') and strftime('%m',prescriptions.starttime) = '01' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 922: Model only answers one image question SQLs
Error executing query 926: Model only answers one image question SQLs
Error executing query 927: Model only answers one image question SQLs
Error executing query 930: Invalid expression / Unexpected token. Line 1, Col: 827.
  etime('2105-12-31 23:59:00','-5 year') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and t1.hadm_id = t2.hadm_id
Error executing query 931: Invalid expression / Unexpected token. Line 1, Col: 647.
  t x-ray showing any abnormality in the abdomen?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 933: Model abstains from answering the question
Error executing query 934: Model only answers one image question SQLs
Error executing query 935: Model only answers one image question SQLs
Error executing query 936: Invalid expression / Unexpected token. Line 1, Col: 862.
  ny technical assessments indicated on an x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 942: Model only answers one image question SQLs
Error executing query 944: Invalid expression / Unexpected token. Line 1, Col: 759.
   anatomical findings in the left hemidiaphragm?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and datetime(t1.starttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 949: Invalid expression / Unexpected token. Line 1, Col: 739.
  d = 12864997 ) and strftime('%Y',prescriptions.starttime) >= '2104' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 950: Model only answers one image question SQLs
Error executing query 951: Required keyword: 'expressions' missing for <class 'sqlglot.expressions.Aliases'>. Line 1, Col: 519.
  re systolic' and d_items.linksto = 'chartevents' ) order by chartevents.charttime desc limit 1 )  ( [4mselect[0m chartevents.valuenum from chartevents where chartevents.stay_id in ( select icustays.stay_id from i
Error executing query 953: Invalid expression / Unexpected token. Line 1, Col: 869.
  23:59:00','start of month','-0 month') ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.starttime and datetime(t2.starttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 d
Error executing query 955: Invalid expression / Unexpected token. Line 1, Col: 769.
  ated any anatomical findings in the right lung?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 957: Invalid expression / Unexpected token. Line 1, Col: 992.
  x-ray reveal rotated in the cardiac silhouette?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 958: Model only answers one image question SQLs
Error executing query 960: Model abstains from answering the question
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
Error executing query 975: Model abstains from answering the question
Error executing query 977: Invalid expression / Unexpected token. Line 1, Col: 762.
  on of any anatomical findings on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 982: Invalid expression / Unexpected token. Line 1, Col: 847.
  %Y',procedures_icd.charttime) = '2100' ) as t2 on t1.subject_id = t2.subject_id where t1.charttime  [4mt2[0m.charttime and datetime(t2.charttime) between datetime(t1.charttime) and datetime(t1.charttime,'+2 m
Error executing query 983: Invalid expression / Unexpected token. Line 1, Col: 835.
  es an x-ray reveal spinal degenerative changes?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.charttime) and datetime(t1.chart
Error executing query 984: Invalid expression / Unexpected token. Line 1, Col: 756.
  089595 ) and strftime('%Y-%m',prescriptions.starttime) >= '2102-04' ) as t3 where t1.studydatetime  [4mt3[0m.starttime and ( datetime(t3.starttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 986: Model only answers one image question SQLs
Error executing query 987: Model only answers one image question SQLs
Error executing query 988: Model only answers one image question SQLs
Error executing query 991: Model only answers one image question SQLs
Error executing query 992: Model only answers one image question SQLs
Error executing query 993: Model only answers one image question SQLs
Error executing query 994: Model abstains from answering the question
Error executing query 995: Model only answers one image question SQLs
Error executing query 997: Invalid expression / Unexpected token. Line 1, Col: 952.
   = 16484690 ) and strftime('%Y',procedures_icd.charttime) >= '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
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
Error executing query 1016: Model abstains from answering the question
Error executing query 1017: Invalid expression / Unexpected token. Line 1, Col: 767.
  ns.hadm_id from admissions where admissions.subject_id = 11685699 ) ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1018: Model abstains from answering the question
Error executing query 1020: Invalid expression / Unexpected token. Line 1, Col: 868.
  ere func_vqa("does an x-ray reveal lung cancer?", t2.study_id) = true ) ) as t3 where t1.charttime  [4mt3[0m.studydatetime and datetime(t1.charttime,'start of month') = datetime(t3.studydatetime,'start of mon
Error executing query 1021: Model only answers one image question SQLs
Error executing query 1022: Invalid expression / Unexpected token. Line 1, Col: 914.
  gnoses_icd.charttime) = datetime('2105-12-31 23:59:00','-15 month') ) as t3 where t1.studydatetime  [4mt3[0m.charttime and ( datetime(t3.charttime) between datetime(t1.studydatetime) and datetime(t1.studydate
Error executing query 1024: Invalid expression / Unexpected token. Line 1, Col: 848.
   year') = datetime('2105-12-31 23:59:00','start of year','-0 year') ) as t3 where t1.studydatetime  [4mt3[0m.starttime and datetime(t1.studydatetime,'start of month') = datetime(t3.starttime,'start of month')
Error executing query 1025: Model only answers one image question SQLs
Error executing query 1026: Model only answers one image question SQLs
Error executing query 1027: Model only answers one image question SQLs
Error executing query 1028: Model abstains from answering the question
Error executing query 1030: Model only answers one image question SQLs
Error executing query 1031: Invalid expression / Unexpected token. Line 1, Col: 874.
  d = 17622334 ) and strftime('%Y',procedures_icd.charttime) = '2103' ) as t3 where t1.studydatetime  [4mt3[0m.charttime and datetime(t1.studydatetime,'start of month') = datetime(t3.charttime,'start of month')
Error executing query 1034: Model only answers one image question SQLs
Error executing query 1037: Model only answers one image question SQLs
Error executing query 1039: Model only answers one image question SQLs
Error executing query 1040: Model abstains from answering the question
Error executing query 1044: Invalid expression / Unexpected token. Line 1, Col: 993.
  lity in the right apical zone on a chest x-ray?", t2.study_id) = true ) ) as t3 where t1.starttime  [4mt3[0m.studydatetime and ( datetime(t3.studydatetime) between datetime(t1.starttime) and datetime(t1.start
Error executing query 1047: Model abstains from answering the question
Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 123, in <module>
    Defaults.start()
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/dtu/__init__.py", line 235, in start
    cls.run(*args)
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 65, in run
    executed_result = run_execution_for_gt_query(executor, parsed_result_gt, name)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/NeuralSQL/execute_nsql.py", line 89, in run_execution_for_gt_query
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
Subject: Job 21909559: <test_final_a80_0> in cluster <dcc> Exited

Job <test_final_a80_0> was submitted from host <n-62-27-17> by user <s183914> in cluster <dcc> at Tue Jun  4 09:01:57 2024
Job was executed on host(s) <4*n-62-18-8>, in queue <gpua100>, as user <s183914> in cluster <dcc> at Tue Jun  4 09:07:00 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_final/ML_final> was used as the working directory.
Started at Tue Jun  4 09:07:00 2024
Terminated at Tue Jun  4 09:18:18 2024
Results reported at Tue Jun  4 09:18:18 2024

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q gpua100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 4
#BSUB -R "rusage[mem=16G]"
#BSUB -R "select[gpu80gb]"
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

    CPU time :                                   682.00 sec.
    Max Memory :                                 10115 MB
    Average Memory :                             8313.86 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               55421.00 MB
    Max Swap :                                   -
    Max Processes :                              6
    Max Threads :                                67
    Run time :                                   678 sec.
    Turnaround time :                            981 sec.

The output (if any) is above this job summary.

