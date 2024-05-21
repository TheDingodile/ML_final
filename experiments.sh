#!/bin/sh
mkdir -p outputs/Test100/Markdown
bsub -o "outputs/Test100/Markdown/Test100_0.md" -J "Test100_0" -env MYARGS="-name Test100-0 -time 3600 -ID 0" < submit_gpu_v32.sh
