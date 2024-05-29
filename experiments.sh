#!/bin/sh
mkdir -p outputs/mini_test/Markdown
bsub -o "outputs/mini_test/Markdown/mini_test_0.md" -J "mini_test_0" -env MYARGS="-name mini_test-0 -time 3600 -lr 0.01 -batch_size 8 -steps 100 -ID 0" < submit_gpu_v32.sh
mkdir -p outputs/model_0/Markdown
bsub -o "outputs/model_0/Markdown/model_0_0.md" -J "model_0_0" -env MYARGS="-name model_0-0 -time 3600 -lr 0.01 -batch_size 8 -steps 10000 -ID 0" < submit_gpu_v32.sh
mkdir -p outputs/model_1/Markdown
bsub -o "outputs/model_1/Markdown/model_1_0.md" -J "model_1_0" -env MYARGS="-name model_1-0 -time 3600 -lr 0.01 -batch_size 8 -steps 10000 -ID 0" < submit_gpu_v32.sh
mkdir -p outputs/model_2/Markdown
bsub -o "outputs/model_2/Markdown/model_2_0.md" -J "model_2_0" -env MYARGS="-name model_2-0 -time 3600 -lr 0.01 -batch_size 8 -steps 10000 -ID 0" < submit_gpu_v32.sh
mkdir -p outputs/model_3/Markdown
bsub -o "outputs/model_3/Markdown/model_3_0.md" -J "model_3_0" -env MYARGS="-name model_3-0 -time 3600 -lr 0.01 -batch_size 8 -steps 10000 -ID 0" < submit_gpu_v32.sh
mkdir -p outputs/model_4/Markdown
bsub -o "outputs/model_4/Markdown/model_4_0.md" -J "model_4_0" -env MYARGS="-name model_4-0 -time 3600 -lr 0.01 -batch_size 8 -steps 10000 -ID 0" < submit_gpu_v32.sh
mkdir -p outputs/model_5/Markdown
bsub -o "outputs/model_5/Markdown/model_5_0.md" -J "model_5_0" -env MYARGS="-name model_5-0 -time 3600 -lr 0.01 -batch_size 8 -steps 10000 -ID 0" < submit_gpu_v32.sh
