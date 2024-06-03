#!/bin/sh
mkdir -p outputs/VQA_eval/Markdown
bsub -o "outputs/VQA_eval/Markdown/VQA_eval_0.md" -J "VQA_eval_0" -env MYARGS="-name VQA_eval-0 -time 3600 -vqa_module_type custom -ID 0" < submit_gpu_v32.sh
