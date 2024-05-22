2024-05-22 10:39:25.164987: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.17.0
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_final/ML_final/wandb/run-20240522_104008-495p4du5
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run CrashTester-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/495p4du5

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
| <c>name</c>       | <d>str</d>        | <j>"CrashTester-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>3600</f>       |
| <c>lr</c>         | <d>float</d>      | <f>0.03</f>       |
| <c>batch_size</c> | <d>int</d>        | <f>8</f>          |
| <c>steps</c>      | <d>int</d>        | <f>1000</f>       |

# Output

```
 == Model params == 
img/Transformer/encoder_norm/bias                                                (1152,)                float16
img/Transformer/encoder_norm/scale                                               (1152,)                float16
img/Transformer/encoderblock/LayerNorm_0/bias                                    (27, 1152)             float16
img/Transformer/encoderblock/LayerNorm_0/scale                                   (27, 1152)             float16
img/Transformer/encoderblock/LayerNorm_1/bias                                    (27, 1152)             float16
img/Transformer/encoderblock/LayerNorm_1/scale                                   (27, 1152)             float16
img/Transformer/encoderblock/MlpBlock_0/Dense_0/bias                             (27, 4304)             float16
img/Transformer/encoderblock/MlpBlock_0/Dense_0/kernel                           (27, 1152, 4304)       float16
img/Transformer/encoderblock/MlpBlock_0/Dense_1/bias                             (27, 1152)             float16
img/Transformer/encoderblock/MlpBlock_0/Dense_1/kernel                           (27, 4304, 1152)       float16
img/Transformer/encoderblock/MultiHeadDotProductAttention_0/key/bias             (27, 16, 72)           float16
img/Transformer/encoderblock/MultiHeadDotProductAttention_0/key/kernel           (27, 1152, 16, 72)     float16
img/Transformer/encoderblock/MultiHeadDotProductAttention_0/out/bias             (27, 1152)             float16
img/Transformer/encoderblock/MultiHeadDotProductAttention_0/out/kernel           (27, 16, 72, 1152)     float16
img/Transformer/encoderblock/MultiHeadDotProductAttention_0/query/bias           (27, 16, 72)           float16
img/Transformer/encoderblock/MultiHeadDotProductAttention_0/query/kernel         (27, 1152, 16, 72)     float16
img/Transformer/encoderblock/MultiHeadDotProductAttention_0/value/bias           (27, 16, 72)           float16
img/Transformer/encoderblock/MultiHeadDotProductAttention_0/value/kernel         (27, 1152, 16, 72)     float16
img/embedding/bias                                                               (1152,)                float16
img/embedding/kernel                                                             (14, 14, 3, 1152)      float16
img/head/bias                                                                    (2048,)                float16
img/head/kernel                                                                  (1152, 2048)           float16
img/pos_embedding                                                                (1, 256, 1152)         float16
llm/embedder/input_embedding                                                     (257152, 2048)         float16
llm/final_norm/scale                                                             (2048,)                float16
llm/layers/attn/attn_vec_einsum/w                                                (18, 8, 256, 2048)     float32
llm/layers/attn/kv_einsum/w                                                      (18, 2, 1, 2048, 256)  float32
llm/layers/attn/q_einsum/w                                                       (18, 8, 2048, 256)     float32
llm/layers/mlp/gating_einsum                                                     (18, 2, 2048, 16384)   float16
llm/layers/mlp/linear                                                            (18, 16384, 2048)      float16
llm/layers/pre_attention_norm/scale                                              (18, 2048)             float16
llm/layers/pre_ffw_norm/scale                                                    (18, 2048)             float16
Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 64, in <module>
    Defaults.start()
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/dtu/__init__.py", line 235, in start
    cls.run(*args)
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 40, in run
    examples = [next(data_iterator) for _ in range(batch_size)]
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 40, in <listcomp>
    examples = [next(data_iterator) for _ in range(batch_size)]
                ^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/vqa_dataset.py", line 92, in train_data_iterator
    "text": np.asarray(tokens),
            ^^^^^^^^^^^^^^^^^^
ValueError: setting an array element with a sequence. The requested array has an inhomogeneous shape after 1 dimensions. The detected shape was (16,) + inhomogeneous part.
wandb: - 0.004 MB of 0.004 MB uploadedwandb: \ 0.004 MB of 0.004 MB uploadedwandb: | 0.008 MB of 0.014 MB uploadedwandb: / 0.008 MB of 0.014 MB uploadedwandb: 🚀 View run CrashTester-0 at: https://wandb.ai/kobomao/ML_healthcare/runs/495p4du5
wandb: ⭐️ View project at: https://wandb.ai/kobomao/ML_healthcare
wandb: Synced 5 W&B file(s), 0 media file(s), 2 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20240522_104008-495p4du5/logs

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21832938: <CrashTester_0> in cluster <dcc> Exited

Job <CrashTester_0> was submitted from host <n-62-27-18> by user <s183914> in cluster <dcc> at Wed May 22 10:39:14 2024
Job was executed on host(s) <n-62-31-3>, in queue <hpc>, as user <s183914> in cluster <dcc> at Wed May 22 10:39:14 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_final/ML_final> was used as the working directory.
Started at Wed May 22 10:39:14 2024
Terminated at Wed May 22 10:40:22 2024
Results reported at Wed May 22 10:40:22 2024

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   39.10 sec.
    Max Memory :                                 239 MB
    Average Memory :                             239.00 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16145.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                5
    Run time :                                   164 sec.
    Turnaround time :                            68 sec.

The output (if any) is above this job summary.

2024-05-22 10:45:03.045493: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.17.0
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_final/ML_final/wandb/run-20240522_104540-87googts
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run CrashTester-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/87googts

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
| <c>name</c>       | <d>str</d>        | <j>"CrashTester-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>3600</f>       |
| <c>lr</c>         | <d>float</d>      | <f>0.03</f>       |
| <c>batch_size</c> | <d>int</d>        | <f>8</f>          |
| <c>steps</c>      | <d>int</d>        | <f>1000</f>       |

# Output

```
[array(2), array(2437), array(1104), array(1089), array(28635), array(576), array(97999), array(14352), array(575), array(573), array(2731), array(192777), array(12225), array(235336), array(108), [array(3276), array(1)]]
Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 64, in <module>
    Defaults.start()
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/dtu/__init__.py", line 235, in start
    cls.run(*args)
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 40, in run
    examples = [next(data_iterator) for _ in range(batch_size)]
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 40, in <listcomp>
    examples = [next(data_iterator) for _ in range(batch_size)]
                ^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/vqa_dataset.py", line 93, in train_data_iterator
    "text": np.asarray(tokens),
            ^^^^^^^^^^^^^^^^^^
ValueError: setting an array element with a sequence. The requested array has an inhomogeneous shape after 1 dimensions. The detected shape was (16,) + inhomogeneous part.
wandb: - 0.004 MB of 0.004 MB uploadedwandb: \ 0.004 MB of 0.004 MB uploadedwandb: | 0.004 MB of 0.004 MB uploadedwandb: / 0.008 MB of 0.014 MB uploaded (0.004 MB deduped)wandb: - 0.014 MB of 0.014 MB uploaded (0.004 MB deduped)wandb: 🚀 View run CrashTester-0 at: https://wandb.ai/kobomao/ML_healthcare/runs/87googts
wandb: ⭐️ View project at: https://wandb.ai/kobomao/ML_healthcare
wandb: Synced 5 W&B file(s), 0 media file(s), 2 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20240522_104540-87googts/logs

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21832951: <CrashTester_0> in cluster <dcc> Exited

Job <CrashTester_0> was submitted from host <n-62-27-18> by user <s183914> in cluster <dcc> at Wed May 22 10:44:52 2024
Job was executed on host(s) <n-62-31-3>, in queue <hpc>, as user <s183914> in cluster <dcc> at Wed May 22 10:44:54 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_final/ML_final> was used as the working directory.
Started at Wed May 22 10:44:54 2024
Terminated at Wed May 22 10:45:54 2024
Results reported at Wed May 22 10:45:54 2024

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   38.48 sec.
    Max Memory :                                 329 MB
    Average Memory :                             329.00 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16055.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                5
    Run time :                                   142 sec.
    Turnaround time :                            62 sec.

The output (if any) is above this job summary.

2024-05-22 10:51:57.543380: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.17.0
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_final/ML_final/wandb/run-20240522_105234-3jgoj38a
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run CrashTester-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/3jgoj38a

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
| <c>name</c>       | <d>str</d>        | <j>"CrashTester-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>3600</f>       |
| <c>lr</c>         | <d>float</d>      | <f>0.03</f>       |
| <c>batch_size</c> | <d>int</d>        | <f>8</f>          |
| <c>steps</c>      | <d>int</d>        | <f>1000</f>       |

# Output

```
Is there any occurrence of anatomical findings in the left hilar structures?
['yes']
[2, 2437, 1104, 1089, 28635, 576, 97999, 14352, 575, 573, 2731, 192777, 12225, 235336, 108, [3276, 1]]
[array(2), array(2437), array(1104), array(1089), array(28635), array(576), array(97999), array(14352), array(575), array(573), array(2731), array(192777), array(12225), array(235336), array(108), [array(3276), array(1)]]
Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 64, in <module>
    Defaults.start()
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/dtu/__init__.py", line 235, in start
    cls.run(*args)
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 40, in run
    examples = [next(data_iterator) for _ in range(batch_size)]
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 40, in <listcomp>
    examples = [next(data_iterator) for _ in range(batch_size)]
                ^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/vqa_dataset.py", line 97, in train_data_iterator
    "text": np.asarray(tokens),
            ^^^^^^^^^^^^^^^^^^
ValueError: setting an array element with a sequence. The requested array has an inhomogeneous shape after 1 dimensions. The detected shape was (16,) + inhomogeneous part.
wandb: - 0.004 MB of 0.004 MB uploadedwandb: \ 0.004 MB of 0.004 MB uploadedwandb: | 0.004 MB of 0.004 MB uploadedwandb: / 0.008 MB of 0.014 MB uploaded (0.004 MB deduped)wandb: - 0.014 MB of 0.014 MB uploaded (0.004 MB deduped)wandb: 🚀 View run CrashTester-0 at: https://wandb.ai/kobomao/ML_healthcare/runs/3jgoj38a
wandb: ⭐️ View project at: https://wandb.ai/kobomao/ML_healthcare
wandb: Synced 5 W&B file(s), 0 media file(s), 2 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20240522_105234-3jgoj38a/logs

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21832968: <CrashTester_0> in cluster <dcc> Exited

Job <CrashTester_0> was submitted from host <n-62-27-18> by user <s183914> in cluster <dcc> at Wed May 22 10:51:48 2024
Job was executed on host(s) <n-62-31-4>, in queue <hpc>, as user <s183914> in cluster <dcc> at Wed May 22 10:51:49 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_final/ML_final> was used as the working directory.
Started at Wed May 22 10:51:49 2024
Terminated at Wed May 22 10:52:48 2024
Results reported at Wed May 22 10:52:48 2024

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   38.74 sec.
    Max Memory :                                 6191 MB
    Average Memory :                             4257.67 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               10193.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   127 sec.
    Turnaround time :                            60 sec.

The output (if any) is above this job summary.

2024-05-22 11:08:04.121601: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.17.0
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_final/ML_final/wandb/run-20240522_110838-pwct05ka
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run CrashTester-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/pwct05ka

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
| <c>name</c>       | <d>str</d>        | <j>"CrashTester-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>3600</f>       |
| <c>lr</c>         | <d>float</d>      | <f>0.03</f>       |
| <c>batch_size</c> | <d>int</d>        | <f>8</f>          |
| <c>steps</c>      | <d>int</d>        | <f>1000</f>       |

# Output

```
Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 64, in <module>
    Defaults.start()
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/dtu/__init__.py", line 235, in start
    cls.run(*args)
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 40, in run
    examples = [next(data_iterator) for _ in range(batch_size)]
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 40, in <listcomp>
    examples = [next(data_iterator) for _ in range(batch_size)]
                ^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/vqa_dataset.py", line 91, in train_data_iterator
    if len(suffix) > 0 and suffix[0].lower() in ['yes', 'no']:
           ^^^^^^
UnboundLocalError: cannot access local variable 'suffix' where it is not associated with a value
wandb: - 0.004 MB of 0.004 MB uploadedwandb: \ 0.004 MB of 0.004 MB uploadedwandb: | 0.004 MB of 0.004 MB uploadedwandb: / 0.008 MB of 0.014 MB uploaded (0.004 MB deduped)wandb: - 0.014 MB of 0.014 MB uploaded (0.004 MB deduped)wandb: 🚀 View run CrashTester-0 at: https://wandb.ai/kobomao/ML_healthcare/runs/pwct05ka
wandb: ⭐️ View project at: https://wandb.ai/kobomao/ML_healthcare
wandb: Synced 5 W&B file(s), 0 media file(s), 2 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20240522_110838-pwct05ka/logs

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21833549: <CrashTester_0> in cluster <dcc> Exited

Job <CrashTester_0> was submitted from host <n-62-27-18> by user <s183914> in cluster <dcc> at Wed May 22 11:07:54 2024
Job was executed on host(s) <n-62-31-21>, in queue <hpc>, as user <s183914> in cluster <dcc> at Wed May 22 11:07:56 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_final/ML_final> was used as the working directory.
Started at Wed May 22 11:07:56 2024
Terminated at Wed May 22 11:08:52 2024
Results reported at Wed May 22 11:08:52 2024

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   34.48 sec.
    Max Memory :                                 568 MB
    Average Memory :                             568.00 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15816.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                5
    Run time :                                   55 sec.
    Turnaround time :                            58 sec.

The output (if any) is above this job summary.

2024-05-22 11:10:21.282394: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.17.0
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_final/ML_final/wandb/run-20240522_111056-35uz38uz
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run CrashTester-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/35uz38uz

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
| <c>name</c>       | <d>str</d>        | <j>"CrashTester-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>3600</f>       |
| <c>lr</c>         | <d>float</d>      | <f>0.03</f>       |
| <c>batch_size</c> | <d>int</d>        | <f>8</f>          |
| <c>steps</c>      | <d>int</d>        | <f>1000</f>       |

# Output

```
if the question is not a yes/no question answer null. Is there any occurrence of anatomical findings in the left hilar structures?
yes
[2, 648, 573, 2872, 603, 780, 476, 7778, 235283, 956, 2872, 3448, 1468, 235265, 2125, 1104, 1089, 28635, 576, 97999, 14352, 575, 573, 2731, 192777, 12225, 235336, 108, 3276, 1]
[array(2), array(648), array(573), array(2872), array(603), array(780), array(476), array(7778), array(235283), array(956), array(2872), array(3448), array(1468), array(235265), array(2125), array(1104), array(1089), array(28635), array(576), array(97999), array(14352), array(575), array(573), array(2731), array(192777), array(12225), array(235336), array(108), array(3276), array(1)]
if the question is not a yes/no question answer null. Are there indications of any tubes/lines within the aortic arch?
yes
[2, 648, 573, 2872, 603, 780, 476, 7778, 235283, 956, 2872, 3448, 1468, 235265, 5881, 1104, 48826, 576, 1089, 26327, 235283, 5448, 2819, 573, 115361, 2951, 235336, 108, 3276, 1]
[array(2), array(648), array(573), array(2872), array(603), array(780), array(476), array(7778), array(235283), array(956), array(2872), array(3448), array(1468), array(235265), array(5881), array(1104), array(48826), array(576), array(1089), array(26327), array(235283), array(5448), array(2819), array(573), array(115361), array(2951), array(235336), array(108), array(3276), array(1)]
if the question is not a yes/no question answer null. Are there indications of any technical assessments within the cardiac silhouette?
yes
[2, 648, 573, 2872, 603, 780, 476, 7778, 235283, 956, 2872, 3448, 1468, 235265, 5881, 1104, 48826, 576, 1089, 9838, 37921, 2819, 573, 41821, 36690, 235336, 108, 3276, 1]
[array(2), array(648), array(573), array(2872), array(603), array(780), array(476), array(7778), array(235283), array(956), array(2872), array(3448), array(1468), array(235265), array(5881), array(1104), array(48826), array(576), array(1089), array(9838), array(37921), array(2819), array(573), array(41821), array(36690), array(235336), array(108), array(3276), array(1)]
if the question is not a yes/no question answer null. Is there an indication of any tubes/lines present in the svc?
yes
[2, 648, 573, 2872, 603, 780, 476, 7778, 235283, 956, 2872, 3448, 1468, 235265, 2125, 1104, 671, 29068, 576, 1089, 26327, 235283, 5448, 2835, 575, 573, 139687, 235336, 108, 3276, 1]
[array(2), array(648), array(573), array(2872), array(603), array(780), array(476), array(7778), array(235283), array(956), array(2872), array(3448), array(1468), array(235265), array(2125), array(1104), array(671), array(29068), array(576), array(1089), array(26327), array(235283), array(5448), array(2835), array(575), array(573), array(139687), array(235336), array(108), array(3276), array(1)]
if the question is not a yes/no question answer null. Is there any sign of diseases present in the right mid lung zone?
yes
[2, 648, 573, 2872, 603, 780, 476, 7778, 235283, 956, 2872, 3448, 1468, 235265, 2125, 1104, 1089, 2035, 576, 16011, 2835, 575, 573, 1833, 3465, 15382, 10277, 235336, 108, 3276, 1]
[array(2), array(648), array(573), array(2872), array(603), array(780), array(476), array(7778), array(235283), array(956), array(2872), array(3448), array(1468), array(235265), array(2125), array(1104), array(1089), array(2035), array(576), array(16011), array(2835), array(575), array(573), array(1833), array(3465), array(15382), array(10277), array(235336), array(108), array(3276), array(1)]
if the question is not a yes/no question answer null. Is there an indication of any tubes/lines present in the mediastinum?
yes
[2, 648, 573, 2872, 603, 780, 476, 7778, 235283, 956, 2872, 3448, 1468, 235265, 2125, 1104, 671, 29068, 576, 1089, 26327, 235283, 5448, 2835, 575, 573, 10074, 897, 20809, 235336, 108, 3276, 1]
[array(2), array(648), array(573), array(2872), array(603), array(780), array(476), array(7778), array(235283), array(956), array(2872), array(3448), array(1468), array(235265), array(2125), array(1104), array(671), array(29068), array(576), array(1089), array(26327), array(235283), array(5448), array(2835), array(575), array(573), array(10074), array(897), array(20809), array(235336), array(108), array(3276), array(1)]
if the question is not a yes/no question answer null. Does the left upper lung zone show any evidence of tubes/lines?
yes
[2, 648, 573, 2872, 603, 780, 476, 7778, 235283, 956, 2872, 3448, 1468, 235265, 11188, 573, 2731, 8776, 15382, 10277, 1500, 1089, 5820, 576, 26327, 235283, 5448, 235336, 108, 3276, 1]
[array(2), array(648), array(573), array(2872), array(603), array(780), array(476), array(7778), array(235283), array(956), array(2872), array(3448), array(1468), array(235265), array(11188), array(573), array(2731), array(8776), array(15382), array(10277), array(1500), array(1089), array(5820), array(576), array(26327), array(235283), array(5448), array(235336), array(108), array(3276), array(1)]
if the question is not a yes/no question answer null. Does the svc show any evidence of devices?
yes
[2, 648, 573, 2872, 603, 780, 476, 7778, 235283, 956, 2872, 3448, 1468, 235265, 11188, 573, 139687, 1500, 1089, 5820, 576, 9630, 235336, 108, 3276, 1]
[array(2), array(648), array(573), array(2872), array(603), array(780), array(476), array(7778), array(235283), array(956), array(2872), array(3448), array(1468), array(235265), array(11188), array(573), array(139687), array(1500), array(1089), array(5820), array(576), array(9630), array(235336), array(108), array(3276), array(1)]
Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 64, in <module>
    Defaults.start()
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/dtu/__init__.py", line 235, in start
    cls.run(*args)
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 41, in run
    batch = jax.tree.map(lambda *x: np.stack(x), *examples)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/tree.py", line 61, in map
    return tree_util.tree_map(f, tree, *rest, is_leaf=is_leaf)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/tree_util.py", line 320, in tree_map
    return treedef.unflatten(f(*xs) for xs in zip(*all_leaves))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/tree_util.py", line 320, in <genexpr>
    return treedef.unflatten(f(*xs) for xs in zip(*all_leaves))
                             ^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 41, in <lambda>
    batch = jax.tree.map(lambda *x: np.stack(x), *examples)
                                    ^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/numpy/core/shape_base.py", line 449, in stack
    raise ValueError('all input arrays must have the same shape')
ValueError: all input arrays must have the same shape
wandb: - 0.004 MB of 0.004 MB uploadedwandb: \ 0.004 MB of 0.004 MB uploadedwandb: | 0.004 MB of 0.004 MB uploadedwandb: / 0.008 MB of 0.020 MB uploaded (0.004 MB deduped)wandb: - 0.008 MB of 0.020 MB uploaded (0.004 MB deduped)wandb: 🚀 View run CrashTester-0 at: https://wandb.ai/kobomao/ML_healthcare/runs/35uz38uz
wandb: ⭐️ View project at: https://wandb.ai/kobomao/ML_healthcare
wandb: Synced 5 W&B file(s), 0 media file(s), 2 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20240522_111056-35uz38uz/logs

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21833578: <CrashTester_0> in cluster <dcc> Exited

Job <CrashTester_0> was submitted from host <n-62-27-18> by user <s183914> in cluster <dcc> at Wed May 22 11:10:10 2024
Job was executed on host(s) <n-62-31-21>, in queue <hpc>, as user <s183914> in cluster <dcc> at Wed May 22 11:10:11 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_final/ML_final> was used as the working directory.
Started at Wed May 22 11:10:11 2024
Terminated at Wed May 22 11:11:11 2024
Results reported at Wed May 22 11:11:11 2024

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   34.58 sec.
    Max Memory :                                 6419 MB
    Average Memory :                             4359.67 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               9965.00 MB
    Max Swap :                                   2 MB
    Max Processes :                              4
    Max Threads :                                5
    Run time :                                   60 sec.
    Turnaround time :                            61 sec.

The output (if any) is above this job summary.

2024-05-22 11:19:21.532743: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.17.0
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_final/ML_final/wandb/run-20240522_111956-memlckqb
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run CrashTester-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/memlckqb

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
| <c>name</c>       | <d>str</d>        | <j>"CrashTester-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>3600</f>       |
| <c>lr</c>         | <d>float</d>      | <f>0.03</f>       |
| <c>batch_size</c> | <d>int</d>        | <f>2</f>          |
| <c>steps</c>      | <d>int</d>        | <f>1000</f>       |

# Output

```
if the question is not a yes/no question answer null. Could you detail any abnormalities that are exclusive to right hilar structures and not present in right shoulder?
None
[2, 648, 573, 2872, 603, 780, 476, 7778, 235283, 956, 2872, 3448, 1468, 235265, 20337, 692, 8637, 1089, 82782, 674, 708, 15587, 577, 1833, 192777, 12225, 578, 780, 2835, 575, 1833, 14999, 235336, 108, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[array(2), array(648), array(573), array(2872), array(603), array(780), array(476), array(7778), array(235283), array(956), array(2872), array(3448), array(1468), array(235265), array(20337), array(692), array(8637), array(1089), array(82782), array(674), array(708), array(15587), array(577), array(1833), array(192777), array(12225), array(578), array(780), array(2835), array(575), array(1833), array(14999), array(235336), array(108), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0)]
if the question is not a yes/no question answer null. Is there any sign of both rib fracture and mediastinal drain?
no
[2, 648, 573, 2872, 603, 780, 476, 7778, 235283, 956, 2872, 3448, 1468, 235265, 2125, 1104, 1089, 2035, 576, 2145, 20791, 40977, 578, 10074, 897, 1248, 16800, 235336, 108, 956, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[array(2), array(648), array(573), array(2872), array(603), array(780), array(476), array(7778), array(235283), array(956), array(2872), array(3448), array(1468), array(235265), array(2125), array(1104), array(1089), array(2035), array(576), array(2145), array(20791), array(40977), array(578), array(10074), array(897), array(1248), array(16800), array(235336), array(108), array(956), array(1), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0), array(0)]
Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 64, in <module>
    Defaults.start()
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/dtu/__init__.py", line 235, in start
    cls.run(*args)
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 43, in run
    params, loss = update_fn(params, batch, learning_rate)
                             ^^^^^^
UnboundLocalError: cannot access local variable 'params' where it is not associated with a value
wandb: - 0.004 MB of 0.004 MB uploadedwandb: \ 0.004 MB of 0.004 MB uploadedwandb: | 0.008 MB of 0.015 MB uploaded (0.004 MB deduped)wandb: / 0.008 MB of 0.015 MB uploaded (0.004 MB deduped)wandb: - 0.015 MB of 0.015 MB uploaded (0.004 MB deduped)wandb: 🚀 View run CrashTester-0 at: https://wandb.ai/kobomao/ML_healthcare/runs/memlckqb
wandb: ⭐️ View project at: https://wandb.ai/kobomao/ML_healthcare
wandb: Synced 5 W&B file(s), 0 media file(s), 2 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20240522_111956-memlckqb/logs

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21834224: <CrashTester_0> in cluster <dcc> Exited

Job <CrashTester_0> was submitted from host <n-62-27-18> by user <s183914> in cluster <dcc> at Wed May 22 11:19:11 2024
Job was executed on host(s) <n-62-31-21>, in queue <hpc>, as user <s183914> in cluster <dcc> at Wed May 22 11:19:13 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_final/ML_final> was used as the working directory.
Started at Wed May 22 11:19:13 2024
Terminated at Wed May 22 11:20:09 2024
Results reported at Wed May 22 11:20:09 2024

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   33.40 sec.
    Max Memory :                                 345 MB
    Average Memory :                             345.00 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16039.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                5
    Run time :                                   60 sec.
    Turnaround time :                            58 sec.

The output (if any) is above this job summary.

2024-05-22 11:23:11.256717: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.17.0
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_final/ML_final/wandb/run-20240522_112348-j19ugvxk
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run CrashTester-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/j19ugvxk

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
| <c>name</c>       | <d>str</d>        | <j>"CrashTester-0"</j> |
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
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 64, in <module>
    Defaults.start()
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/dtu/__init__.py", line 235, in start
    cls.run(*args)
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 43, in run
    params, loss = update_fn(params, batch, learning_rate)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: update_fn() missing 2 required positional arguments: 'model' and 'trainable_mask'
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
wandb: - 0.004 MB of 0.004 MB uploadedwandb: \ 0.004 MB of 0.004 MB uploadedwandb: | 0.004 MB of 0.004 MB uploadedwandb: / 0.008 MB of 0.017 MB uploaded (0.004 MB deduped)wandb: - 0.017 MB of 0.017 MB uploaded (0.004 MB deduped)wandb: 🚀 View run CrashTester-0 at: https://wandb.ai/kobomao/ML_healthcare/runs/j19ugvxk
wandb: ⭐️ View project at: https://wandb.ai/kobomao/ML_healthcare
wandb: Synced 5 W&B file(s), 0 media file(s), 2 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20240522_112348-j19ugvxk/logs

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21834244: <CrashTester_0> in cluster <dcc> Exited

Job <CrashTester_0> was submitted from host <n-62-27-18> by user <s183914> in cluster <dcc> at Wed May 22 11:23:02 2024
Job was executed on host(s) <n-62-31-23>, in queue <hpc>, as user <s183914> in cluster <dcc> at Wed May 22 11:23:02 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_final/ML_final> was used as the working directory.
Started at Wed May 22 11:23:02 2024
Terminated at Wed May 22 11:24:02 2024
Results reported at Wed May 22 11:24:02 2024

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   38.77 sec.
    Max Memory :                                 3425 MB
    Average Memory :                             2433.33 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               12959.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                5
    Run time :                                   139 sec.
    Turnaround time :                            60 sec.

The output (if any) is above this job summary.

2024-05-22 11:27:16.490663: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.17.0
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_final/ML_final/wandb/run-20240522_112754-t5qfvxv2
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run CrashTester-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/t5qfvxv2

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
| <c>name</c>       | <d>str</d>        | <j>"CrashTester-0"</j> |
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
wandb: - 0.004 MB of 0.004 MB uploadedwandb: \ 0.004 MB of 0.004 MB uploadedwandb: | 0.004 MB of 0.004 MB uploadedwandb: / 0.008 MB of 0.017 MB uploaded (0.004 MB deduped)wandb: - 0.017 MB of 0.017 MB uploaded (0.004 MB deduped)wandb: 🚀 View run CrashTester-0 at: https://wandb.ai/kobomao/ML_healthcare/runs/t5qfvxv2
wandb: ⭐️ View project at: https://wandb.ai/kobomao/ML_healthcare
wandb: Synced 5 W&B file(s), 0 media file(s), 2 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20240522_112754-t5qfvxv2/logs

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21834290: <CrashTester_0> in cluster <dcc> Exited

Job <CrashTester_0> was submitted from host <n-62-27-18> by user <s183914> in cluster <dcc> at Wed May 22 11:27:06 2024
Job was executed on host(s) <n-62-31-23>, in queue <hpc>, as user <s183914> in cluster <dcc> at Wed May 22 11:27:07 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_final/ML_final> was used as the working directory.
Started at Wed May 22 11:27:07 2024
Terminated at Wed May 22 11:28:08 2024
Results reported at Wed May 22 11:28:08 2024

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   39.16 sec.
    Max Memory :                                 6916 MB
    Average Memory :                             4622.67 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               9468.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                15
    Run time :                                   175 sec.
    Turnaround time :                            62 sec.

The output (if any) is above this job summary.

2024-05-22 11:41:18.878308: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.17.0
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_final/ML_final/wandb/run-20240522_114154-zq9flkfr
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run CrashTester-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/zq9flkfr

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
| <c>name</c>       | <d>str</d>        | <j>"CrashTester-0"</j> |
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
    params, loss = update_fn(params, batch, learning_rate)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: Cannot interpret value of type <class 'big_vision.models.proj.paligemma.paligemma.Model'> as an abstract array; it does not have a dtype attribute
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
wandb: - 0.004 MB of 0.004 MB uploadedwandb: \ 0.004 MB of 0.004 MB uploadedwandb: | 0.004 MB of 0.004 MB uploadedwandb: / 0.008 MB of 0.017 MB uploaded (0.004 MB deduped)wandb: - 0.017 MB of 0.017 MB uploaded (0.004 MB deduped)wandb: 🚀 View run CrashTester-0 at: https://wandb.ai/kobomao/ML_healthcare/runs/zq9flkfr
wandb: ⭐️ View project at: https://wandb.ai/kobomao/ML_healthcare
wandb: Synced 5 W&B file(s), 0 media file(s), 2 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20240522_114154-zq9flkfr/logs

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21835893: <CrashTester_0> in cluster <dcc> Exited

Job <CrashTester_0> was submitted from host <n-62-27-18> by user <s183914> in cluster <dcc> at Wed May 22 11:41:12 2024
Job was executed on host(s) <n-62-31-23>, in queue <hpc>, as user <s183914> in cluster <dcc> at Wed May 22 11:41:12 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_final/ML_final> was used as the working directory.
Started at Wed May 22 11:41:12 2024
Terminated at Wed May 22 11:42:08 2024
Results reported at Wed May 22 11:42:08 2024

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   36.39 sec.
    Max Memory :                                 2036 MB
    Average Memory :                             2036.00 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14348.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                5
    Run time :                                   55 sec.
    Turnaround time :                            56 sec.

The output (if any) is above this job summary.

