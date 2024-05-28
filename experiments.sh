#!/bin/sh
mkdir -p outputs/a80testa80/Markdown
bsub -o "outputs/a80testa80/Markdown/a80testa80_0.md" -J "a80testa80_0" -env MYARGS="-name a80testa80-0 -time 3600 -lr 0.01 -batch_size 16 -steps 5000 -ID 0" < submit_gpu_a80.sh
