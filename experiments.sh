#!/bin/sh
mkdir -p outputs/Cuda_version_check/Markdown
bsub -o "outputs/Cuda_version_check/Markdown/Cuda_version_check_0.md" -J "Cuda_version_check_0" -env MYARGS="-name Cuda_version_check-0 -time 3600 -lr 0.03 -batch_size 8 -steps 1000 -ID 0" < submit_cpu.sh
