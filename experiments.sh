#!/bin/sh
mkdir -p outputs/test_set08_a80/Markdown
bsub -o "outputs/test_set08_a80/Markdown/test_set08_a80_0.md" -J "test_set08_a80_0" -env MYARGS="-name test_set08_a80-0 -time 3600 -vqa_module_type custom -prediction_file_name predictions_LLM_1-0_test -threshold 0.8 -table_path database/mimic_iv_cxr/gold -ID 0" < submit_gpu_a80.sh
mkdir -p outputs/test_set09_a80/Markdown
bsub -o "outputs/test_set09_a80/Markdown/test_set09_a80_0.md" -J "test_set09_a80_0" -env MYARGS="-name test_set09_a80-0 -time 3600 -vqa_module_type custom -prediction_file_name predictions_LLM_1-0_test -threshold 0.9 -table_path database/mimic_iv_cxr/gold -ID 0" < submit_gpu_a80.sh
mkdir -p outputs/test_set08/Markdown
bsub -o "outputs/test_set08/Markdown/test_set08_0.md" -J "test_set08_0" -env MYARGS="-name test_set08-0 -time 3600 -vqa_module_type custom -prediction_file_name predictions_LLM_1-0_test -threshold 0.8 -table_path database/mimic_iv_cxr/gold -ID 0" < submit_gpu_v32.sh
mkdir -p outputs/test_set09/Markdown
bsub -o "outputs/test_set09/Markdown/test_set09_0.md" -J "test_set09_0" -env MYARGS="-name test_set09-0 -time 3600 -vqa_module_type custom -prediction_file_name predictions_LLM_1-0_test -threshold 0.9 -table_path database/mimic_iv_cxr/gold -ID 0" < submit_gpu_v32.sh
