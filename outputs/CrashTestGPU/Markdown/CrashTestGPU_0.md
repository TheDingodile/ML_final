2024-05-22 11:40:01.865818: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
An NVIDIA GPU may be present on this machine, but a CUDA-enabled jaxlib is not installed. Falling back to cpu.
wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.17.0
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_final/ML_final/wandb/run-20240522_114036-yuztjdds
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run CrashTestGPU-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/yuztjdds
2024-05-22 11:40:38.241124: W tensorflow/core/common_runtime/gpu/gpu_device.cc:2251] Cannot dlopen some GPU libraries. Please make sure the missing libraries mentioned above are installed properly if you would like to use GPU. Follow the guide at https://www.tensorflow.org/install/gpu for how to download and setup the required libraries for your platform.
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
| <c>name</c>       | <d>str</d>        | <j>"CrashTestGPU-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>3600</f>       |
| <c>lr</c>         | <d>float</d>      | <f>0.03</f>       |
| <c>batch_size</c> | <d>int</d>        | <f>2</f>          |
| <c>steps</c>      | <d>int</d>        | <f>1000</f>       |

# Output

```
if the question is not a yes/no question answer null. Could you detail any abnormalities that are exclusive to right hilar structures and not present in right shoulder?
None
[2, 648, 573, 2872, 603, 780, 476, 7778, 235283, 956, 2872, 3448, 1468, 235265, 20337, 692, 8637, 1089, 82782, 674, 708, 15587, 577, 1833, 192777, 12225, 578, 780, 2835, 575, 1833, 14999, 235336, 108, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[array(2), array(648), array(573), array(2872), array(603), array(780), array(476), array(7778), array(235283), array(956), array(2872), array(3448), array(1468), array(235265), array(20337), array(692), array(8637), array(1089), array(82782), array(674), array(708), array(15587), array(577), array(1833), array(192777), array(12225), array(578), array(780), array(2835), array(575), array(1833), array(14999), array(235336), array(108), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0)]
if the question is not a yes/no question answer null. Is there any sign of both rib fracture and mediastinal drain?
no
[2, 648, 573, 2872, 603, 780, 476, 7778, 235283, 956, 2872, 3448, 1468, 235265, 2125, 1104, 1089, 2035, 576, 2145, 20791, 40977, 578, 10074, 897, 1248, 16800, 235336, 108, 956, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[array(2), array(648), array(573), array(2872), array(603), array(780), array(476), array(7778), array(235283), array(956), array(2872), array(3448), array(1468), array(235265), array(2125), array(1104), array(1089), array(2035), array(576), array(2145), array(20791), array(40977), array(578), array(10074), array(897), array(1248), array(16800), array(235336), array(108), array(956), array(1), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0)]
Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 65, in <module>
    Defaults.start()
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/dtu/__init__.py", line 235, in start
    cls.run(*args)
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 44, in run
    params, loss = update_fn(params, batch, learning_rate, model, trainable_mask)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: Cannot interpret value of type <class 'big_vision.models.proj.paligemma.paligemma.Model'> as an abstract array; it does not have a dtype attribute
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
wandb: - 0.004 MB of 0.004 MB uploadedwandb: \ 0.004 MB of 0.013 MB uploadedwandb: | 0.013 MB of 0.013 MB uploadedwandb: 🚀 View run CrashTestGPU-0 at: https://wandb.ai/kobomao/ML_healthcare/runs/yuztjdds
wandb: ⭐️ View project at: https://wandb.ai/kobomao/ML_healthcare
wandb: Synced 5 W&B file(s), 0 media file(s), 0 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20240522_114036-yuztjdds/logs

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21832727: <CrashTestGPU_0> in cluster <dcc> Exited

Job <CrashTestGPU_0> was submitted from host <n-62-27-18> by user <s183914> in cluster <dcc> at Wed May 22 09:52:49 2024
Job was executed on host(s) <4*n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed May 22 11:39:37 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_final/ML_final> was used as the working directory.
Started at Wed May 22 11:39:37 2024
Terminated at Wed May 22 11:40:48 2024
Results reported at Wed May 22 11:40:48 2024

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   33.03 sec.
    Max Memory :                                 157 MB
    Average Memory :                             157.00 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               65379.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                5
    Run time :                                   71 sec.
    Turnaround time :                            6479 sec.

The output (if any) is above this job summary.

