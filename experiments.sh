#!/bin/sh
mkdir -p outputs/test_eval/Markdown
bsub -o "outputs/test_eval/Markdown/test_eval_0.md" -J "test_eval_0" -env MYARGS="-name test_eval-0 -time 3600 -lr 0.01 -batch_size 8 -steps 5000 -ID 0" < submit_gpu_v32.sh
