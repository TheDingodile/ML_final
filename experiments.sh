#!/bin/sh
mkdir -p outputs/CrashTest/Markdown
bsub -o "outputs/CrashTest/Markdown/CrashTest_0.md" -J "CrashTest_0" -env MYARGS="-name CrashTest-0 -time 3600 -ID 0" < submit_cpu.sh
mkdir -p outputs/CrashTestGPU/Markdown
bsub -o "outputs/CrashTestGPU/Markdown/CrashTestGPU_0.md" -J "CrashTestGPU_0" -env MYARGS="-name CrashTestGPU-0 -time 3600 -ID 0" < submit_gpu_v32.sh
