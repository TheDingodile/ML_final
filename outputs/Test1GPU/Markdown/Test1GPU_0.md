wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.17.0
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_final/ML_final/wandb/run-20240521_062425-6yp7gp0s
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run Test1GPU-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/6yp7gp0s
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
| <c>name</c>       | <d>str</d>        | <j>"Test1GPU-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>3600</f>       |

# Output

```
Loading checkpoint shards:   0%|          | 0/2 [00:00<?, ?it/s]Loading checkpoint shards:  50%|█████     | 1/2 [00:02<00:02,  2.05s/it]Loading checkpoint shards: 100%|██████████| 2/2 [00:02<00:00,  1.08s/it]Loading checkpoint shards: 100%|██████████| 2/2 [00:02<00:00,  1.22s/it]
You're using a GemmaTokenizerFast tokenizer. Please note that with a fast tokenizer, using the `__call__` method is faster than using a method to encode the text followed by a call to the `pad` method to get a padded encoding.
Is there any occurrence of anatomical findings in the left hilar structures?
['yes']
('No',)
Are there indications of any tubes/lines within the aortic arch?
['yes']
('yes',)
Are there indications of any technical assessments within the cardiac silhouette?
['yes']
('no',)
Is there an indication of any tubes/lines present in the svc?
['yes']
('no',)
Is there any sign of diseases present in the right mid lung zone?
['yes']
('yes',)
Is there an indication of any tubes/lines present in the mediastinum?
['yes']
('no',)
Does the left upper lung zone show any evidence of tubes/lines?
['yes']
('yes',)
Does the svc show any evidence of devices?
['yes']
('yes',)
Is there any occurrence of tubes/lines in the left hilar structures?
['yes']
('yes',)
Is there an indication of any anatomical findings present in the left chest wall?
['yes']
('No',)
```
wandb: - 0.004 MB of 0.004 MB uploadedwandb: \ 0.004 MB of 0.004 MB uploadedwandb: | 0.004 MB of 0.004 MB uploadedwandb: / 0.009 MB of 0.015 MB uploaded (0.003 MB deduped)wandb: - 0.015 MB of 0.015 MB uploaded (0.003 MB deduped)wandb: 
wandb: Run summary:
wandb: question Is there an indicati...
wandb: 
wandb: 🚀 View run Test1GPU-0 at: https://wandb.ai/kobomao/ML_healthcare/runs/6yp7gp0s
wandb: ⭐️ View project at: https://wandb.ai/kobomao/ML_healthcare
wandb: Synced 5 W&B file(s), 0 media file(s), 2 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20240521_062425-6yp7gp0s/logs

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21819214: <Test1GPU_0> in cluster <dcc> Done

Job <Test1GPU_0> was submitted from host <n-62-30-2> by user <s183914> in cluster <dcc> at Tue May 21 06:24:09 2024
Job was executed on host(s) <4*n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue May 21 06:24:09 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_final/ML_final> was used as the working directory.
Started at Tue May 21 06:24:09 2024
Terminated at Tue May 21 06:27:58 2024
Results reported at Tue May 21 06:27:58 2024

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

    CPU time :                                   44.03 sec.
    Max Memory :                                 5001 MB
    Average Memory :                             3837.00 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               60535.00 MB
    Max Swap :                                   -
    Max Processes :                              6
    Max Threads :                                32
    Run time :                                   346 sec.
    Turnaround time :                            229 sec.

The output (if any) is above this job summary.

