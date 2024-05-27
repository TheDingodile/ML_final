#!/bin/sh
mkdir -p outputs/Log_accuracy001/Markdown
bsub -o "outputs/Log_accuracy001/Markdown/Log_accuracy001_0.md" -J "Log_accuracy001_0" -env MYARGS="-name Log_accuracy001-0 -time 3600 -lr 0.01 -batch_size 32 -steps 5000 -ID 0" < submit_gpu_v32.sh
mkdir -p outputs/Log_accuracy01/Markdown
bsub -o "outputs/Log_accuracy01/Markdown/Log_accuracy01_0.md" -J "Log_accuracy01_0" -env MYARGS="-name Log_accuracy01-0 -time 3600 -lr 0.1 -batch_size 32 -steps 5000 -ID 0" < submit_gpu_v32.sh
mkdir -p outputs/Log_accuracy001a80/Markdown
bsub -o "outputs/Log_accuracy001a80/Markdown/Log_accuracy001a80_0.md" -J "Log_accuracy001a80_0" -env MYARGS="-name Log_accuracy001a80-0 -time 3600 -lr 0.01 -batch_size 32 -steps 5000 -ID 0" < submit_gpu_a80.sh
mkdir -p outputs/Log_accuracy01a80/Markdown
bsub -o "outputs/Log_accuracy01a80/Markdown/Log_accuracy01a80_0.md" -J "Log_accuracy01a80_0" -env MYARGS="-name Log_accuracy01a80-0 -time 3600 -lr 0.1 -batch_size 32 -steps 5000 -ID 0" < submit_gpu_a80.sh
