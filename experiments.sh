#!/bin/sh
mkdir -p outputs/test_final_07/Markdown
bsub -o "outputs/test_final_07/Markdown/test_final_07_0.md" -J "test_final_07_0" -env MYARGS="-name test_final_07-0 -time 3600 -vqa_module_type custom -prediction_file_name predictions_LLM_1-0 -threshold 0.7 -ID 0" < submit_gpu_v32.sh
mkdir -p outputs/test_final_08/Markdown
bsub -o "outputs/test_final_08/Markdown/test_final_08_0.md" -J "test_final_08_0" -env MYARGS="-name test_final_08-0 -time 3600 -vqa_module_type custom -prediction_file_name predictions_LLM_1-0 -threshold 0.8 -ID 0" < submit_gpu_v32.sh
mkdir -p outputs/test_final_09/Markdown
bsub -o "outputs/test_final_09/Markdown/test_final_09_0.md" -J "test_final_09_0" -env MYARGS="-name test_final_09-0 -time 3600 -vqa_module_type custom -prediction_file_name predictions_LLM_1-0 -threshold 0.9 -ID 0" < submit_gpu_v32.sh
