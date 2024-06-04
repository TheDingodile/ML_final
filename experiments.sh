#!/bin/sh
mkdir -p outputs/True_SQL_test/Markdown
bsub -o "outputs/True_SQL_test/Markdown/True_SQL_test_0.md" -J "True_SQL_test_0" -env MYARGS="-name True_SQL_test-0 -time 3600 -vqa_module_type custom -ID 0" < submit_gpu_v32.sh
