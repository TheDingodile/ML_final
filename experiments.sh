#!/bin/sh
mkdir -p outputs/32_001_alltrainable/Markdown
bsub -o "outputs/32_001_alltrainable/Markdown/32_001_alltrainable_0.md" -J "32_001_alltrainable_0" -env MYARGS="-name 32_001_alltrainable-0 -time 3600 -lr 0.01 -batch_size 32 -steps 5000 -ID 0" < submit_gpu_a80.sh
mkdir -p outputs/32_0001_alltrainable/Markdown
bsub -o "outputs/32_0001_alltrainable/Markdown/32_0001_alltrainable_0.md" -J "32_0001_alltrainable_0" -env MYARGS="-name 32_0001_alltrainable-0 -time 3600 -lr 0.001 -batch_size 32 -steps 5000 -ID 0" < submit_gpu_a80.sh
