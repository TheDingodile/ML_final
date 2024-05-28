2024-05-27 21:06:34.380210: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.17.0
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_final/ML_final/wandb/run-20240527_210656-qmfsyd1b
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run Log_accuracy001a80-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/qmfsyd1b
2024-05-27 21:07:42.248299: W external/xla/xla/service/gpu/nvptx_compiler.cc:760] The NVIDIA driver's CUDA version is 12.4 which is older than the ptxas CUDA version (12.5.40). Because the driver is older than the ptxas version, XLA is disabling parallel compilation, which may slow down compilation. You should update your NVIDIA driver or use the NVIDIA-provided CUDA forward compatibility packages.
2024-05-27 21:07:49.773604: W tensorflow/core/common_runtime/gpu/gpu_device.cc:2251] Cannot dlopen some GPU libraries. Please make sure the missing libraries mentioned above are installed properly if you would like to use GPU. Follow the guide at https://www.tensorflow.org/install/gpu for how to download and setup the required libraries for your platform.
Skipping registering GPU devices...
2024-05-27 21:09:58.500981: W external/xla/xla/service/gpu/gemm_fusion_autotuner.cc:864] Slow kernel for gemm_fusion_dot took: 1.000675354s. {block_m:16,block_n:16,block_k:512,split_k:1,num_stages:1,num_warps:4,num_ctas:1}

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
| <c>name</c>       | <d>str</d>        | <j>"Log_accuracy001a80-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>3600</f>       |
| <c>lr</c>         | <d>float</d>      | <f>0.01</f>       |
| <c>batch_size</c> | <d>int</d>        | <f>32</f>         |
| <c>steps</c>      | <d>int</d>        | <f>5000</f>       |

# Output

```
Traced<ShapedArray(float32[32,63])>with<JVPTrace(level=3/0)> with
  primal = Traced<ShapedArray(float32[32,63])>with<DynamicJaxprTrace(level=1/0)>
  tangent = Traced<ShapedArray(float32[32,63])>with<JaxprTrace(level=2/0)> with
    pval = (ShapedArray(float32[32,63]), None)
    recipe = JaxprEqnRecipe(eqn_id=<object object at 0x7fe80b7ae9a0>, in_tracers=(Traced<ShapedArray(float32[32,63,257152]):JaxprTrace(level=2/0)>, Traced<ShapedArray(float32[32,63,257152]):JaxprTrace(level=2/0)>, Traced<ShapedArray(float32[32,63]):JaxprTrace(level=2/0)>), out_tracer_refs=[<weakref at 0x7fe80b628c70; to 'JaxprTracer' at 0x7fe80b628db0>], out_avals=[ShapedArray(float32[32,63])], primitive=pjit, params={'jaxpr': { lambda ; a:f32[32,63,257152] b:f32[32,63,257152] c:f32[32,63]. let
    d:f32[32,63,257152] = mul a b
    e:f32[32,63] = reduce_sum[axes=(2,)] d
    f:f32[32,63] = div e c
  in (f,) }, 'in_shardings': (UnspecifiedValue, UnspecifiedValue, UnspecifiedValue), 'out_shardings': (UnspecifiedValue,), 'in_layouts': (None, None, None), 'out_layouts': (None,), 'resource_env': None, 'donated_invars': (False, False, False), 'name': '_reduce_max', 'keep_unused': False, 'inline': True}, effects=set(), source_info=SourceInfo(traceback=<jaxlib.xla_extension.Traceback object at 0x13963520>, name_stack=NameStack(stack=(Transform(name='jvp'),)))) (32, 63)
Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 125, in <module>
    Defaults.start()
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/dtu/__init__.py", line 235, in start
    cls.run(*args)
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 92, in run
    answer_rate = jnp.sum((jnp.sum(abstain_filter, dim=-1) == jnp.sum(mask_loss, dim=-1))) / batch_size
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: sum() got an unexpected keyword argument 'dim'
wandb: - 0.005 MB of 0.005 MB uploadedwandb: \ 0.005 MB of 0.005 MB uploadedwandb: | 0.005 MB of 0.011 MB uploadedwandb: / 0.005 MB of 0.011 MB uploadedwandb: - 0.011 MB of 0.011 MB uploadedwandb: 
wandb: Run history:
wandb: loss ▄█▂▃▇▄▁▁▁
wandb:   lr ██▇▇▆▅▄▂▁
wandb: step ▁▂▃▄▅▅▆▇█
wandb: 
wandb: Run summary:
wandb: loss 0.33824
wandb:   lr 0.01
wandb: step 9
wandb: 
wandb: 🚀 View run Log_accuracy001a80-0 at: https://wandb.ai/kobomao/ML_healthcare/runs/qmfsyd1b
wandb: ⭐️ View project at: https://wandb.ai/kobomao/ML_healthcare
wandb: Synced 5 W&B file(s), 0 media file(s), 0 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20240527_210656-qmfsyd1b/logs

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21868468: <Log_accuracy001a80_0> in cluster <dcc> Exited

Job <Log_accuracy001a80_0> was submitted from host <n-62-27-20> by user <s183914> in cluster <dcc> at Mon May 27 17:21:34 2024
Job was executed on host(s) <4*n-62-18-8>, in queue <gpua100>, as user <s183914> in cluster <dcc> at Mon May 27 21:05:14 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_final/ML_final> was used as the working directory.
Started at Mon May 27 21:05:14 2024
Terminated at Mon May 27 21:10:31 2024
Results reported at Mon May 27 21:10:31 2024

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q gpua100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 4
#BSUB -R "rusage[mem=16G]"
#BSUB -R "select[gpu80gb]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
module -s load python3
source ../project-env/bin/activate

python main.py $MYARGS
------------------------------------------------------------

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   322.45 sec.
    Max Memory :                                 4713 MB
    Average Memory :                             3397.80 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               60823.00 MB
    Max Swap :                                   -
    Max Processes :                              6
    Max Threads :                                63
    Run time :                                   318 sec.
    Turnaround time :                            13737 sec.

The output (if any) is above this job summary.

