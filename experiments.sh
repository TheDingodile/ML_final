#!/bin/sh
mkdir -p outputs/Batch_size/Markdown
bsub -o "outputs/Batch_size/Markdown/Batch_size_0.md" -J "Batch_size_0" -env MYARGS="-name Batch_size-0 -time 3600 -lr 0.001 -batch_size 64 -steps 5000 -ID 0" < submit_gpu_a80.sh
