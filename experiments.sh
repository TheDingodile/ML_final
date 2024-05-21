#!/bin/sh
mkdir -p outputs/Test/Markdown
bsub -o "outputs/Test/Markdown/Test_0.md" -J "Test_0" -env MYARGS="-name Test-0 -time 3600 -ID 0" < submit_cpu.sh
