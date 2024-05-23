#!/bin/sh
mkdir -p outputs/CPU_check/Markdown
bsub -o "outputs/CPU_check/Markdown/CPU_check_0.md" -J "CPU_check_0" -env MYARGS="-name CPU_check-0 -time 3600 -lr 0.03 -batch_size 8 -steps 1000 -ID 0" < submit_cpu.sh
