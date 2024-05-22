#!/bin/sh
mkdir -p outputs/Tester/Markdown
bsub -o "outputs/Tester/Markdown/Tester_0.md" -J "Tester_0" -env MYARGS="-name Tester-0 -time 3600 -ID 0" < submit_cpu.sh
