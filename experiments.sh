#!/bin/sh
mkdir -p outputs/test_set07_fix/Markdown
bsub -o "outputs/test_set07_fix/Markdown/test_set07_fix_0.md" -J "test_set07_fix_0" -env MYARGS="-name test_set07_fix-0 -time 3600 -vqa_module_type custom -prediction_file_name predictions_LLM_1-0_test -threshold 0.7 -table_path database/mimic_iv_cxr/gold -model_path_name params_model_2-0 -ID 0" < submit_gpu_v32.sh
mkdir -p outputs/vision3valid09/Markdown
bsub -o "outputs/vision3valid09/Markdown/vision3valid09_0.md" -J "vision3valid09_0" -env MYARGS="-name vision3valid09-0 -time 3600 -vqa_module_type custom -prediction_file_name predictions_LLM_1-0 -threshold 0.9 -table_path database/mimic_iv_cxr/silver -model_path_name params_model_3-0 -ID 0" < submit_gpu_v32.sh
mkdir -p outputs/vision3test09/Markdown
bsub -o "outputs/vision3test09/Markdown/vision3test09_0.md" -J "vision3test09_0" -env MYARGS="-name vision3test09-0 -time 3600 -vqa_module_type custom -prediction_file_name predictions_LLM_1-0_test -threshold 0.9 -table_path database/mimic_iv_cxr/gold -model_path_name params_model_3-0 -ID 0" < submit_gpu_v32.sh
mkdir -p outputs/vision3valid08/Markdown
bsub -o "outputs/vision3valid08/Markdown/vision3valid08_0.md" -J "vision3valid08_0" -env MYARGS="-name vision3valid08-0 -time 3600 -vqa_module_type custom -prediction_file_name predictions_LLM_1-0 -threshold 0.8 -table_path database/mimic_iv_cxr/silver -model_path_name params_model_3-0 -ID 0" < submit_gpu_v32.sh
mkdir -p outputs/vision3test08/Markdown
bsub -o "outputs/vision3test08/Markdown/vision3test08_0.md" -J "vision3test08_0" -env MYARGS="-name vision3test08-0 -time 3600 -vqa_module_type custom -prediction_file_name predictions_LLM_1-0_test -threshold 0.8 -table_path database/mimic_iv_cxr/gold -model_path_name params_model_3-0 -ID 0" < submit_gpu_v32.sh
mkdir -p outputs/vision1valid09/Markdown
bsub -o "outputs/vision1valid09/Markdown/vision1valid09_0.md" -J "vision1valid09_0" -env MYARGS="-name vision1valid09-0 -time 3600 -vqa_module_type custom -prediction_file_name predictions_LLM_1-0 -threshold 0.9 -table_path database/mimic_iv_cxr/silver -model_path_name params_model_1-0 -ID 0" < submit_gpu_v32.sh
mkdir -p outputs/vision1test09/Markdown
bsub -o "outputs/vision1test09/Markdown/vision1test09_0.md" -J "vision1test09_0" -env MYARGS="-name vision1test09-0 -time 3600 -vqa_module_type custom -prediction_file_name predictions_LLM_1-0_test -threshold 0.9 -table_path database/mimic_iv_cxr/gold -model_path_name params_model_1-0 -ID 0" < submit_gpu_v32.sh
