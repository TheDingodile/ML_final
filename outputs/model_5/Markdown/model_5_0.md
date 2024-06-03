2024-05-30 02:23:53.052665: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.17.0
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_final/ML_final/wandb/run-20240530_022404-e1gjfbzw
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run model_5-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/e1gjfbzw
2024-05-30 02:24:36.259675: W external/xla/xla/service/gpu/nvptx_compiler.cc:760] The NVIDIA driver's CUDA version is 12.4 which is older than the ptxas CUDA version (12.5.40). Because the driver is older than the ptxas version, XLA is disabling parallel compilation, which may slow down compilation. You should update your NVIDIA driver or use the NVIDIA-provided CUDA forward compatibility packages.
2024-05-30 02:24:42.830810: W tensorflow/core/common_runtime/gpu/gpu_device.cc:2251] Cannot dlopen some GPU libraries. Please make sure the missing libraries mentioned above are installed properly if you would like to use GPU. Follow the guide at https://www.tensorflow.org/install/gpu for how to download and setup the required libraries for your platform.
Skipping registering GPU devices...

<style>
c { color: #9cdcfe; font-family: 'Verdana', sans-serif;} /* VARIABLE */
d { color: #4EC9B0; font-family: 'Verdana', sans-serif;} /* CLASS */
e { color: #569cd6; font-family: 'Verdana', sans-serif;} /* BOOL */
f { color: #b5cea8; font-family: 'Verdana', sans-serif;} /* NUMBERS */
j { color: #ce9178; font-family: 'Verdana', sans-serif;} /* STRING */
k { font-family: 'Verdana', sans-serif;} /* SYMBOLS */
</style>

# Parameters

| PARAMETER         | TYPE              | VALUE             |
|-------------------|-------------------|-------------------|
| <c>name</c>       | <d>str</d>        | <j>"model_5-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>3600</f>       |
| <c>lr</c>         | <d>float</d>      | <f>0.01</f>       |
| <c>batch_size</c> | <d>int</d>        | <f>8</f>          |
| <c>steps</c>      | <d>int</d>        | <f>10000</f>      |

# Output

```
```
wandb: - 0.005 MB of 0.005 MB uploadedwandb: \ 0.005 MB of 0.005 MB uploadedwandb: | 0.005 MB of 0.010 MB uploadedwandb: / 0.009 MB of 0.010 MB uploadedwandb: - 0.009 MB of 0.010 MB uploadedwandb: \ 0.009 MB of 0.010 MB uploadedwandb: | 0.009 MB of 0.010 MB uploadedwandb: / 0.009 MB of 0.010 MB uploadedwandb: - 0.009 MB of 0.010 MB uploadedwandb: 
wandb: Run history:
wandb: abstain_rate_0.55 █▇▆▅▅▆█▂▆▂▄▅▁▄▅▄▄▅▂▂▄▅▃▂▃▃▅▄▂▄▆▂▄▅▄▄▃▂▅▆
wandb: abstain_rate_0.75 ████████▆██▆▆▃█▆███▁▅▆▃▃▆█▆▆▃▆▅▆█▆█▅█▁▆▆
wandb:  abstain_rate_0.9 ███████████████████▁████▅█▅███▅██▅███▅██
wandb:     accuracy_0.55 █▆▆▆▆██▆▆▃▅█▅██▃▃▆▅▅▅▅▅▆▆██▆▃▆▆▁▅▆▅▆▆▆▅█
wandb:     accuracy_0.75 ████████████▅██████▁▅█▅█████▅█▅█████████
wandb:      accuracy_0.9 ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:              loss █▃▃▃▇▃▂▂▂▄▃▃▃▂▃▁▄▁▂▃▂▁▁▃▂▁▂▃▁▂▃▂▁▂▄▃▂▂▂▂
wandb:                lr ███████▇▇▇▇▇▆▆▆▆▅▅▅▅▄▄▄▄▃▃▃▃▂▂▂▂▂▁▁▁▁▁▁▁
wandb:              step ▁▁▁▁▂▂▂▂▂▃▃▃▃▃▃▄▄▄▄▄▅▅▅▅▅▅▆▆▆▆▆▇▇▇▇▇▇███
wandb: 
wandb: Run summary:
wandb: abstain_rate_0.55 0.375
wandb: abstain_rate_0.75 0.625
wandb:  abstain_rate_0.9 0.75
wandb:     accuracy_0.55 1.0
wandb:     accuracy_0.75 1.0
wandb:      accuracy_0.9 1.0
wandb:              loss 0.18871
wandb:                lr 0.0
wandb:              step 10000
wandb: 
wandb: 🚀 View run model_5-0 at: https://wandb.ai/kobomao/ML_healthcare/runs/e1gjfbzw
wandb: ⭐️ View project at: https://wandb.ai/kobomao/ML_healthcare
wandb: Synced 5 W&B file(s), 0 media file(s), 0 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20240530_022404-e1gjfbzw/logs

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21875723: <model_5_0> in cluster <dcc> Done

Job <model_5_0> was submitted from host <n-62-30-6> by user <s183914> in cluster <dcc> at Wed May 29 07:35:31 2024
Job was executed on host(s) <4*n-62-11-14>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu May 30 02:23:23 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_final/ML_final> was used as the working directory.
Started at Thu May 30 02:23:23 2024
Terminated at Thu May 30 10:13:15 2024
Results reported at Thu May 30 10:13:15 2024

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 4
#BSUB -R "rusage[mem=16G]"
#BSUB -R "select[gpu32gb]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
module -s load python3
source ../project-env/bin/activate

python main.py $MYARGS
------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   27640.47 sec.
    Max Memory :                                 14795 MB
    Average Memory :                             6252.33 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               50741.00 MB
    Max Swap :                                   -
    Max Processes :                              6
    Max Threads :                                69
    Run time :                                   28192 sec.
    Turnaround time :                            95864 sec.

The output (if any) is above this job summary.

