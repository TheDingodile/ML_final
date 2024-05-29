2024-05-29 06:51:42.317629: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.17.0
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_final/ML_final/wandb/run-20240529_065147-2n7ttdvw
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run train_saved_model-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/2n7ttdvw

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
| <c>name</c>       | <d>str</d>        | <j>"train_saved_model-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>3600</f>       |
| <c>lr</c>         | <d>float</d>      | <f>0.01</f>       |
| <c>batch_size</c> | <d>int</d>        | <f>8</f>          |
| <c>steps</c>      | <d>int</d>        | <f>10000</f>      |

# Output

```
Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/big_vision/utils.py", line 715, in tree_get
    return flattened[name]
           ~~~~~~~~~^^^^^^
KeyError: 'img'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 141, in <module>
    Defaults.start()
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/dtu/__init__.py", line 235, in start
    cls.run(*args)
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 38, in run
    if (isServer): predictor_function, tokenizer, trainable_mask, params, model, save_func = big_vision_test(isServer=isServer)
                                                                                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/big_vision_test.py", line 43, in big_vision_test
    params = paligemma.load(None, MODEL_PATH, model_config)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/big_vision/models/proj/paligemma/paligemma.py", line 276, in load
    restored_params["img"] = importlib.import_module(
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/big_vision/models/vit.py", line 409, in load
    restored_params = utils.load_params(init_file)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/big_vision/utils.py", line 222, in load_params
    params = tree_get(params, key)
             ^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/big_vision/utils.py", line 723, in tree_get
    raise KeyError(Msg(msg)) from e
KeyError: img
Available keys:
param_0
param_1
param_10
param_11
param_12
param_13
param_14
param_15
param_16
param_17
param_18
param_19
param_2
param_20
param_21
param_22
param_23
param_24
param_25
param_26
param_27
param_28
param_29
param_3
param_30
param_31
param_4
param_5
param_6
param_7
param_8
param_9


wandb: - 0.005 MB of 0.005 MB uploadedwandb: \ 0.005 MB of 0.005 MB uploadedwandb: | 0.005 MB of 0.005 MB uploadedwandb: / 0.009 MB of 0.016 MB uploaded (0.004 MB deduped)wandb: 🚀 View run train_saved_model-0 at: https://wandb.ai/kobomao/ML_healthcare/runs/2n7ttdvw
wandb: ⭐️ View project at: https://wandb.ai/kobomao/ML_healthcare
wandb: Synced 5 W&B file(s), 0 media file(s), 2 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20240529_065147-2n7ttdvw/logs

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21875703: <train_saved_model_0> in cluster <dcc> Exited

Job <train_saved_model_0> was submitted from host <n-62-30-6> by user <s183914> in cluster <dcc> at Wed May 29 06:51:24 2024
Job was executed on host(s) <4*n-62-20-10>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed May 29 06:51:26 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_final/ML_final> was used as the working directory.
Started at Wed May 29 06:51:26 2024
Terminated at Wed May 29 06:52:11 2024
Results reported at Wed May 29 06:52:11 2024

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

    CPU time :                                   16.69 sec.
    Max Memory :                                 311 MB
    Average Memory :                             311.00 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               65225.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                5
    Run time :                                   112 sec.
    Turnaround time :                            47 sec.

The output (if any) is above this job summary.

