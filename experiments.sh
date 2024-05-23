#!/bin/sh
mkdir -p outputs/GPU_check/Markdown
bsub -o "outputs/GPU_check/Markdown/GPU_check_0.md" -J "GPU_check_0" -env MYARGS="-name GPU_check-0 -time 3600 -lr 0.03 -batch_size 8 -steps 1000 -ID 0" < submit_gpu_v32.sh
mkdir -p outputs/GPU_check2/Markdown
bsub -o "outputs/GPU_check2/Markdown/GPU_check2_0.md" -J "GPU_check2_0" -env MYARGS="-name GPU_check2-0 -time 3600 -lr 0.03 -batch_size 8 -steps 1000 -ID 0" < submit_gpu_a80.sh
