wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.17.0
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_final/ML_final/wandb/run-20240521_054715-z62s30i6
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run Test-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/z62s30i6

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
| <c>name</c>       | <d>str</d>        | <j>"Test-0"</j>   |
| <c>time</c>       | <d>int</d>        | <f>3600</f>       |

# Output

```
Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 34, in <module>
    Defaults.start()
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/dtu/__init__.py", line 235, in start
    cls.run(*args)
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 27, in run
    question_text, answer, result = next(run_test(path))
                                    ^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/paligemma.py", line 9, in run_test
    pg = PaliGemma(api_key=key)
         ^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/inference/models/paligemma/paligemma.py", line 37, in __init__
    self.model = PaliGemmaForConditionalGeneration.from_pretrained(
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/transformers/modeling_utils.py", line 3122, in from_pretrained
    raise ImportError(
ImportError: Using `low_cpu_mem_usage=True` or a `device_map` requires Accelerate: `pip install accelerate`
wandb: - 0.003 MB of 0.003 MB uploadedwandb: \ 0.003 MB of 0.003 MB uploadedwandb: | 0.003 MB of 0.003 MB uploadedwandb: / 0.008 MB of 0.013 MB uploadedwandb: - 0.013 MB of 0.013 MB uploadedwandb: 🚀 View run Test-0 at: https://wandb.ai/kobomao/ML_healthcare/runs/z62s30i6
wandb: ⭐️ View project at: https://wandb.ai/kobomao/ML_healthcare
wandb: Synced 5 W&B file(s), 0 media file(s), 2 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20240521_054715-z62s30i6/logs

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21819208: <Test_0> in cluster <dcc> Exited

Job <Test_0> was submitted from host <n-62-30-2> by user <s183914> in cluster <dcc> at Tue May 21 05:46:33 2024
Job was executed on host(s) <n-62-31-3>, in queue <hpc>, as user <s183914> in cluster <dcc> at Tue May 21 05:46:34 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_final/ML_final> was used as the working directory.
Started at Tue May 21 05:46:34 2024
Terminated at Tue May 21 05:51:15 2024
Results reported at Tue May 21 05:51:15 2024

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

    CPU time :                                   50.28 sec.
    Max Memory :                                 4094 MB
    Average Memory :                             2608.75 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               12290.00 MB
    Max Swap :                                   -
    Max Processes :                              6
    Max Threads :                                30
    Run time :                                   312 sec.
    Turnaround time :                            282 sec.

The output (if any) is above this job summary.

wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.17.0
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_final/ML_final/wandb/run-20240521_055702-tctj8lvk
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run Test-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/tctj8lvk
`config.hidden_act` is ignored, you should use `config.hidden_activation` instead.
Gemma's activation function will be set to `gelu_pytorch_tanh`. Please, use
`config.hidden_activation` if you want to override this behaviour.
See https://github.com/huggingface/transformers/pull/29402 for more details.

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
| <c>name</c>       | <d>str</d>        | <j>"Test-0"</j>   |
| <c>time</c>       | <d>int</d>        | <f>3600</f>       |

# Output

```
Loading checkpoint shards:   0%|          | 0/2 [00:00<?, ?it/s]Loading checkpoint shards:  50%|█████     | 1/2 [00:00<00:00,  3.07it/s]Loading checkpoint shards: 100%|██████████| 2/2 [00:00<00:00,  4.46it/s]Loading checkpoint shards: 100%|██████████| 2/2 [00:00<00:00,  4.17it/s]
You're using a GemmaTokenizerFast tokenizer. Please note that with a fast tokenizer, using the `__call__` method is faster than using a method to encode the text followed by a call to the `pad` method to get a padded encoding.
Is there any occurrence of anatomical findings in the left hilar structures?
['yes']
('No',)
Loading checkpoint shards:   0%|          | 0/2 [00:00<?, ?it/s]Loading checkpoint shards:  50%|█████     | 1/2 [00:00<00:00,  4.76it/s]Loading checkpoint shards: 100%|██████████| 2/2 [00:00<00:00,  5.63it/s]Loading checkpoint shards: 100%|██████████| 2/2 [00:00<00:00,  5.47it/s]
You're using a GemmaTokenizerFast tokenizer. Please note that with a fast tokenizer, using the `__call__` method is faster than using a method to encode the text followed by a call to the `pad` method to get a padded encoding.
Is there any occurrence of anatomical findings in the left hilar structures?
['yes']
('No',)
Loading checkpoint shards:   0%|          | 0/2 [00:00<?, ?it/s]Loading checkpoint shards:  50%|█████     | 1/2 [00:00<00:00,  4.34it/s]Loading checkpoint shards: 100%|██████████| 2/2 [00:00<00:00,  5.40it/s]Loading checkpoint shards: 100%|██████████| 2/2 [00:00<00:00,  5.20it/s]
You're using a GemmaTokenizerFast tokenizer. Please note that with a fast tokenizer, using the `__call__` method is faster than using a method to encode the text followed by a call to the `pad` method to get a padded encoding.
Is there any occurrence of anatomical findings in the left hilar structures?
['yes']
('No',)
Loading checkpoint shards:   0%|          | 0/2 [00:00<?, ?it/s]Loading checkpoint shards:  50%|█████     | 1/2 [00:00<00:00,  4.28it/s]Loading checkpoint shards: 100%|██████████| 2/2 [00:00<00:00,  5.37it/s]Loading checkpoint shards: 100%|██████████| 2/2 [00:00<00:00,  5.16it/s]
You're using a GemmaTokenizerFast tokenizer. Please note that with a fast tokenizer, using the `__call__` method is faster than using a method to encode the text followed by a call to the `pad` method to get a padded encoding.
Is there any occurrence of anatomical findings in the left hilar structures?
['yes']
('No',)
Loading checkpoint shards:   0%|          | 0/2 [00:00<?, ?it/s]Loading checkpoint shards:  50%|█████     | 1/2 [00:00<00:00,  4.28it/s]Loading checkpoint shards: 100%|██████████| 2/2 [00:00<00:00,  5.37it/s]Loading checkpoint shards: 100%|██████████| 2/2 [00:00<00:00,  5.16it/s]
You're using a GemmaTokenizerFast tokenizer. Please note that with a fast tokenizer, using the `__call__` method is faster than using a method to encode the text followed by a call to the `pad` method to get a padded encoding.
Is there any occurrence of anatomical findings in the left hilar structures?
['yes']
('No',)
Loading checkpoint shards:   0%|          | 0/2 [00:00<?, ?it/s]Loading checkpoint shards:  50%|█████     | 1/2 [00:00<00:00,  4.29it/s]Loading checkpoint shards: 100%|██████████| 2/2 [00:00<00:00,  5.37it/s]Loading checkpoint shards: 100%|██████████| 2/2 [00:00<00:00,  5.16it/s]
You're using a GemmaTokenizerFast tokenizer. Please note that with a fast tokenizer, using the `__call__` method is faster than using a method to encode the text followed by a call to the `pad` method to get a padded encoding.
Is there any occurrence of anatomical findings in the left hilar structures?
['yes']
('No',)
Loading checkpoint shards:   0%|          | 0/2 [00:00<?, ?it/s]Loading checkpoint shards:  50%|█████     | 1/2 [00:00<00:00,  4.70it/s]Loading checkpoint shards: 100%|██████████| 2/2 [00:00<00:00,  5.63it/s]Loading checkpoint shards: 100%|██████████| 2/2 [00:00<00:00,  5.45it/s]
You're using a GemmaTokenizerFast tokenizer. Please note that with a fast tokenizer, using the `__call__` method is faster than using a method to encode the text followed by a call to the `pad` method to get a padded encoding.
Is there any occurrence of anatomical findings in the left hilar structures?
['yes']
('No',)
Loading checkpoint shards:   0%|          | 0/2 [00:00<?, ?it/s]Loading checkpoint shards:  50%|█████     | 1/2 [00:00<00:00,  4.69it/s]Loading checkpoint shards: 100%|██████████| 2/2 [00:00<00:00,  5.62it/s]Loading checkpoint shards: 100%|██████████| 2/2 [00:00<00:00,  5.44it/s]
You're using a GemmaTokenizerFast tokenizer. Please note that with a fast tokenizer, using the `__call__` method is faster than using a method to encode the text followed by a call to the `pad` method to get a padded encoding.
Is there any occurrence of anatomical findings in the left hilar structures?
['yes']
('No',)
Loading checkpoint shards:   0%|          | 0/2 [00:00<?, ?it/s]Loading checkpoint shards:  50%|█████     | 1/2 [00:00<00:00,  4.32it/s]Loading checkpoint shards: 100%|██████████| 2/2 [00:00<00:00,  5.39it/s]Loading checkpoint shards: 100%|██████████| 2/2 [00:00<00:00,  5.19it/s]
You're using a GemmaTokenizerFast tokenizer. Please note that with a fast tokenizer, using the `__call__` method is faster than using a method to encode the text followed by a call to the `pad` method to get a padded encoding.
Is there any occurrence of anatomical findings in the left hilar structures?
['yes']
('No',)
Loading checkpoint shards:   0%|          | 0/2 [00:00<?, ?it/s]Loading checkpoint shards:  50%|█████     | 1/2 [00:00<00:00,  4.34it/s]Loading checkpoint shards: 100%|██████████| 2/2 [00:00<00:00,  5.36it/s]Loading checkpoint shards: 100%|██████████| 2/2 [00:00<00:00,  5.17it/s]
You're using a GemmaTokenizerFast tokenizer. Please note that with a fast tokenizer, using the `__call__` method is faster than using a method to encode the text followed by a call to the `pad` method to get a padded encoding.
Is there any occurrence of anatomical findings in the left hilar structures?
['yes']
('No',)
```
wandb: - 0.004 MB of 0.004 MB uploadedwandb: \ 0.004 MB of 0.004 MB uploadedwandb: | 0.009 MB of 0.017 MB uploadedwandb: / 0.009 MB of 0.017 MB uploadedwandb: - 0.017 MB of 0.017 MB uploadedwandb: 
wandb: Run summary:
wandb: question Is there any occurre...
wandb: 
wandb: 🚀 View run Test-0 at: https://wandb.ai/kobomao/ML_healthcare/runs/tctj8lvk
wandb: ⭐️ View project at: https://wandb.ai/kobomao/ML_healthcare
wandb: Synced 5 W&B file(s), 0 media file(s), 2 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20240521_055702-tctj8lvk/logs

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21819209: <Test_0> in cluster <dcc> Done

Job <Test_0> was submitted from host <n-62-30-2> by user <s183914> in cluster <dcc> at Tue May 21 05:56:46 2024
Job was executed on host(s) <n-62-31-22>, in queue <hpc>, as user <s183914> in cluster <dcc> at Tue May 21 05:56:46 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_final/ML_final> was used as the working directory.
Started at Tue May 21 05:56:46 2024
Terminated at Tue May 21 06:12:19 2024
Results reported at Tue May 21 06:12:19 2024

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

Successfully completed.

Resource usage summary:

    CPU time :                                   770.98 sec.
    Max Memory :                                 5686 MB
    Average Memory :                             1783.25 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               10698.00 MB
    Max Swap :                                   -
    Max Processes :                              6
    Max Threads :                                36
    Run time :                                   992 sec.
    Turnaround time :                            933 sec.

The output (if any) is above this job summary.

