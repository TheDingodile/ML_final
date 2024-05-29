#!/bin/sh
mkdir -p outputs/test_save2/Markdown
bsub -o "outputs/test_save2/Markdown/test_save2_0.md" -J "test_save2_0" -env MYARGS="-name test_save2-0 -time 3600 -lr 0.01 -batch_size 8 -steps 10000 -ID 0" < submit_gpu_v32.sh
