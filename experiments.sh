#!/bin/sh
mkdir -p outputs/GPU_run/Markdown
bsub -o "outputs/GPU_run/Markdown/GPU_run_0.md" -J "GPU_run_0" -env MYARGS="-name GPU_run-0 -time 3600 -lr 0.03 -batch_size 8 -steps 1000 -ID 0" < submit_gpu_v32.sh
