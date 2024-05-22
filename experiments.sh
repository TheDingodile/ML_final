#!/bin/sh
mkdir -p outputs/CrashTester/Markdown
bsub -o "outputs/CrashTester/Markdown/CrashTester_0.md" -J "CrashTester_0" -env MYARGS="-name CrashTester-0 -time 3600 -lr 0.03 -batch_size 2 -steps 1000 -ID 0" < submit_cpu.sh
