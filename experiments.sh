#!/bin/sh
mkdir -p outputs/True_SQL_evala80/Markdown
bsub -o "outputs/True_SQL_evala80/Markdown/True_SQL_evala80_0.md" -J "True_SQL_evala80_0" -env MYARGS="-name True_SQL_evala80-0 -time 3600 -vqa_module_type custom -ID 0" < submit_gpu_a80.sh
