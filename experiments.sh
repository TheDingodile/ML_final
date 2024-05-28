#!/bin/sh
mkdir -p outputs/v32test/Markdown
bsub -o "outputs/v32test/Markdown/v32test_0.md" -J "v32test_0" -env MYARGS="-name v32test-0 -time 3600 -lr 0.01 -batch_size 16 -steps 5000 -ID 0" < submit_gpu_v32.sh
mkdir -p outputs/a80test/Markdown
bsub -o "outputs/a80test/Markdown/a80test_0.md" -J "a80test_0" -env MYARGS="-name a80test-0 -time 3600 -lr 0.01 -batch_size 16 -steps 5000 -ID 0" < submit_gpu_v32.sh
