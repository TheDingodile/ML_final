#!/bin/sh
mkdir -p outputs/v32test8/Markdown
bsub -o "outputs/v32test8/Markdown/v32test8_0.md" -J "v32test8_0" -env MYARGS="-name v32test8-0 -time 3600 -lr 0.01 -batch_size 8 -steps 5000 -ID 0" < submit_gpu_v32.sh
