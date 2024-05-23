#!/bin/sh
mkdir -p outputs/32_001/Markdown
bsub -o "outputs/32_001/Markdown/32_001_0.md" -J "32_001_0" -env MYARGS="-name 32_001-0 -time 3600 -lr 0.01 -batch_size 32 -steps 5000 -ID 0" < submit_gpu_v32.sh
mkdir -p outputs/16_001/Markdown
bsub -o "outputs/16_001/Markdown/16_001_0.md" -J "16_001_0" -env MYARGS="-name 16_001-0 -time 3600 -lr 0.01 -batch_size 16 -steps 5000 -ID 0" < submit_gpu_v32.sh
mkdir -p outputs/32_01/Markdown
bsub -o "outputs/32_01/Markdown/32_01_0.md" -J "32_01_0" -env MYARGS="-name 32_01-0 -time 3600 -lr 0.1 -batch_size 32 -steps 5000 -ID 0" < submit_gpu_v32.sh
mkdir -p outputs/16_01/Markdown
bsub -o "outputs/16_01/Markdown/16_01_0.md" -J "16_01_0" -env MYARGS="-name 16_01-0 -time 3600 -lr 0.1 -batch_size 16 -steps 5000 -ID 0" < submit_gpu_v32.sh
