#!/bin/sh
mkdir -p outputs/vision4test09/Markdown
bsub -o "outputs/vision4test09/Markdown/vision4test09_0.md" -J "vision4test09_0" -env MYARGS="-name vision4test09-0 -time 3600 -vqa_module_type custom -prediction_file_name predictions_LLM_1-0_test -threshold 0.9 -table_path database/mimic_iv_cxr/gold -model_path_name params_model_4-0 -ID 0" < submit_gpu_a80.sh
