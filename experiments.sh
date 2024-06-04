#!/bin/sh
mkdir -p outputs/test_set08_fix/Markdown
bsub -o "outputs/test_set08_fix/Markdown/test_set08_fix_0.md" -J "test_set08_fix_0" -env MYARGS="-name test_set08_fix-0 -time 3600 -vqa_module_type custom -prediction_file_name predictions_LLM_1-0_test -threshold 0.8 -table_path database/mimic_iv_cxr/gold -ID 0" < submit_gpu_v32.sh
mkdir -p outputs/test_set09_fix/Markdown
bsub -o "outputs/test_set09_fix/Markdown/test_set09_fix_0.md" -J "test_set09_fix_0" -env MYARGS="-name test_set09_fix-0 -time 3600 -vqa_module_type custom -prediction_file_name predictions_LLM_1-0_test -threshold 0.9 -table_path database/mimic_iv_cxr/gold -ID 0" < submit_gpu_v32.sh
