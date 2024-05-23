#!/bin/sh
mkdir -p outputs/GPU_run_a80/Markdown
bsub -o "outputs/GPU_run_a80/Markdown/GPU_run_a80_0.md" -J "GPU_run_a80_0" -env MYARGS="-name GPU_run_a80-0 -time 3600 -lr 0.03 -batch_size 8 -steps 1000 -ID 0" < submit_gpu_a80.sh
