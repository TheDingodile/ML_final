#!/bin/sh
mkdir -p outputs/Batch_size_v32/Markdown
bsub -o "outputs/Batch_size_v32/Markdown/Batch_size_v32_0.md" -J "Batch_size_v32_0" -env MYARGS="-name Batch_size_v32-0 -time 3600 -lr 0.001 -batch_size 64 -steps 5000 -ID 0" < submit_gpu_v32.sh
