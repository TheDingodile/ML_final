2024-05-22 09:52:57.666196: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT

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
| <c>name</c>       | <d>str</d>        | <j>"CrashTest-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>3600</f>       |

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
```

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21832726: <CrashTest_0> in cluster <dcc> Done

Job <CrashTest_0> was submitted from host <n-62-27-18> by user <s183914> in cluster <dcc> at Wed May 22 09:52:49 2024
Job was executed on host(s) <n-62-31-21>, in queue <hpc>, as user <s183914> in cluster <dcc> at Wed May 22 09:52:49 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_final/ML_final> was used as the working directory.
Started at Wed May 22 09:52:49 2024
Terminated at Wed May 22 09:53:27 2024
Results reported at Wed May 22 09:53:27 2024

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

    CPU time :                                   25.20 sec.
    Max Memory :                                 778 MB
    Average Memory :                             518.67 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15606.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                5
    Run time :                                   38 sec.
    Turnaround time :                            38 sec.

The output (if any) is above this job summary.

