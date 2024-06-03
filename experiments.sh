#!/bin/sh
mkdir -p outputs/eval_full/Markdown
bsub -o "outputs/eval_full/Markdown/eval_full_0.md" -J "eval_full_0" -env MYARGS="-name eval_full-0 -time 3600 -vqa_module_type yes -ID 0" < submit_gpu_a80.sh
