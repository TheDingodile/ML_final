#!/bin/sh
mkdir -p outputs/Test1/Markdown
bsub -o "outputs/Test1/Markdown/Test1_0.md" -J "Test1_0" -env MYARGS="-name Test1-0 -time 3600 -b 4.0 -a 1 -d dsf -ID 0" < submit_cpu.sh
