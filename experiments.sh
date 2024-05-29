#!/bin/sh
mkdir -p outputs/train_saved_model/Markdown
bsub -o "outputs/train_saved_model/Markdown/train_saved_model_0.md" -J "train_saved_model_0" -env MYARGS="-name train_saved_model-0 -time 3600 -lr 0.01 -batch_size 8 -steps 10000 -ID 0" < submit_gpu_v32.sh
