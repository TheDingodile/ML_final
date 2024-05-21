#!/bin/sh
mkdir -p outputs/Test1GPU/Markdown
bsub -o "outputs/Test1GPU/Markdown/Test1GPU_0.md" -J "Test1GPU_0" -env MYARGS="-name Test1GPU-0 -time 3600 -ID 0" < submit_gpu_v32.sh
