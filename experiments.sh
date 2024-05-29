#!/bin/sh
mkdir -p outputs/test_save/Markdown
bsub -o "outputs/test_save/Markdown/test_save_0.md" -J "test_save_0" -env MYARGS="-name test_save-0 -time 3600 -lr 0.01 -batch_size 8 -steps 10000 -ID 0" < submit_gpu_v32.sh
mkdir -p outputs/test_save_a80/Markdown
bsub -o "outputs/test_save_a80/Markdown/test_save_a80_0.md" -J "test_save_a80_0" -env MYARGS="-name test_save_a80-0 -time 3600 -lr 0.01 -batch_size 8 -steps 10000 -ID 0" < submit_gpu_a80.sh
