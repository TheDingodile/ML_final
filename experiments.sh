#!/bin/sh
mkdir -p outputs/eval_fulla40/Markdown
bsub -o "outputs/eval_fulla40/Markdown/eval_fulla40_0.md" -J "eval_fulla40_0" -env MYARGS="-name eval_fulla40-0 -time 3600 -vqa_module_type custom -ID 0" < submit_gpu_a40.sh
