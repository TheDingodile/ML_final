#!/bin/sh
mkdir -p outputs/test_final_07_a80/Markdown
bsub -o "outputs/test_final_07_a80/Markdown/test_final_07_a80_0.md" -J "test_final_07_a80_0" -env MYARGS="-name test_final_07_a80-0 -time 3600 -vqa_module_type custom -prediction_file_name predictions_LLM_1-0 -threshold 0.7 -ID 0" < submit_gpu_a80.sh
