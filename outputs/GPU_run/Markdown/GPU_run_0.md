2024-05-23 08:24:16.213047: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.17.0
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_final/ML_final/wandb/run-20240523_082421-x2b0c3np
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run GPU_run-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/x2b0c3np
An NVIDIA GPU may be present on this machine, but a CUDA-enabled jaxlib is not installed. Falling back to cpu.
2024-05-23 08:24:49.494636: W tensorflow/core/common_runtime/gpu/gpu_device.cc:2251] Cannot dlopen some GPU libraries. Please make sure the missing libraries mentioned above are installed properly if you would like to use GPU. Follow the guide at https://www.tensorflow.org/install/gpu for how to download and setup the required libraries for your platform.
Skipping registering GPU devices...

Aborted!
Terminated

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21839019: <GPU_run_0> in cluster <dcc> Exited

Job <GPU_run_0> was submitted from host <n-62-30-2> by user <s183914> in cluster <dcc> at Thu May 23 08:18:41 2024
Job was executed on host(s) <4*n-62-11-15>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu May 23 08:24:07 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_final/ML_final> was used as the working directory.
Started at Thu May 23 08:24:07 2024
Terminated at Thu May 23 08:38:02 2024
Results reported at Thu May 23 08:38:02 2024

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

TERM_OWNER: job killed by owner.
Exited with exit code 143.

Resource usage summary:

    CPU time :                                   2881.00 sec.
    Max Memory :                                 11834 MB
    Average Memory :                             8730.89 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               53702.00 MB
    Max Swap :                                   -
    Max Processes :                              6
    Max Threads :                                57
    Run time :                                   836 sec.
    Turnaround time :                            1161 sec.

The output (if any) is above this job summary.

