#!/bin/sh
mkdir -p outputs/True_SQL_eval/Markdown
bsub -o "outputs/True_SQL_eval/Markdown/True_SQL_eval_0.md" -J "True_SQL_eval_0" -env MYARGS="-name True_SQL_eval-0 -time 3600 -vqa_module_type custom -ID 0" < submit_gpu_a40.sh
