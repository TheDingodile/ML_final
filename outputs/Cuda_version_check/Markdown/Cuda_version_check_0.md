2024-05-23 08:28:57.459739: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.17.0
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_final/ML_final/wandb/run-20240523_082902-7clpd8ly
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run Cuda_version_check-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/7clpd8ly

Aborted!
Terminated

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21839026: <Cuda_version_check_0> in cluster <dcc> Exited

Job <Cuda_version_check_0> was submitted from host <n-62-30-2> by user <s183914> in cluster <dcc> at Thu May 23 08:28:35 2024
Job was executed on host(s) <n-62-31-22>, in queue <hpc>, as user <s183914> in cluster <dcc> at Thu May 23 08:28:37 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_final/ML_final> was used as the working directory.
Started at Thu May 23 08:28:37 2024
Terminated at Thu May 23 08:34:26 2024
Results reported at Thu May 23 08:34:26 2024

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 4320
# end of BSUB options
module -s load python3
source ../project-env/bin/activate

python main.py $MYARGS
------------------------------------------------------------

TERM_OWNER: job killed by owner.
Exited with exit code 143.

Resource usage summary:

    CPU time :                                   313.00 sec.
    Max Memory :                                 12028 MB
    Average Memory :                             5414.20 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               4356.00 MB
    Max Swap :                                   -
    Max Processes :                              6
    Max Threads :                                38
    Run time :                                   364 sec.
    Turnaround time :                            351 sec.

The output (if any) is above this job summary.

