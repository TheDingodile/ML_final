#!/bin/sh
mkdir -p outputs/test_final_a80_print/Markdown
bsub -o "outputs/test_final_a80_print/Markdown/test_final_a80_print_0.md" -J "test_final_a80_print_0" -env MYARGS="-name test_final_a80_print-0 -time 3600 -vqa_module_type custom -prediction_file_name predictions_LLM_1-0 -ID 0" < submit_gpu_a80.sh
