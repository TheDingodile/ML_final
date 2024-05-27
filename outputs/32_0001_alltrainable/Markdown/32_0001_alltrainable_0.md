2024-05-24 03:04:24.275504: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.17.0
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_final/ML_final/wandb/run-20240524_030439-zt0ah5sa
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run 32_0001_alltrainable-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/zt0ah5sa
2024-05-24 03:05:08.021560: W external/xla/xla/service/gpu/nvptx_compiler.cc:760] The NVIDIA driver's CUDA version is 12.4 which is older than the ptxas CUDA version (12.5.40). Because the driver is older than the ptxas version, XLA is disabling parallel compilation, which may slow down compilation. You should update your NVIDIA driver or use the NVIDIA-provided CUDA forward compatibility packages.
2024-05-24 03:05:13.182774: W tensorflow/core/common_runtime/gpu/gpu_device.cc:2251] Cannot dlopen some GPU libraries. Please make sure the missing libraries mentioned above are installed properly if you would like to use GPU. Follow the guide at https://www.tensorflow.org/install/gpu for how to download and setup the required libraries for your platform.
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
| <c>name</c>       | <d>str</d>        | <j>"32_0001_alltrainable-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>3600</f>       |
| <c>lr</c>         | <d>float</d>      | <f>0.001</f>      |
| <c>batch_size</c> | <d>int</d>        | <f>32</f>         |
| <c>steps</c>      | <d>int</d>        | <f>5000</f>       |

# Output

```
Traced<ShapedArray(float32[32,63])>with<JVPTrace(level=3/0)> with
  primal = Traced<ShapedArray(float32[32,63])>with<DynamicJaxprTrace(level=1/0)>
  tangent = Traced<ShapedArray(float32[32,63])>with<JaxprTrace(level=2/0)> with
    pval = (ShapedArray(float32[32,63]), None)
    recipe = JaxprEqnRecipe(eqn_id=<object object at 0x7fd88f21eaa0>, in_tracers=(Traced<ShapedArray(float32[32,63,257152]):JaxprTrace(level=2/0)>, Traced<ShapedArray(float32[32,63,257152]):JaxprTrace(level=2/0)>, Traced<ShapedArray(float32[32,63]):JaxprTrace(level=2/0)>), out_tracer_refs=[<weakref at 0x7fd88f0a6d90; to 'JaxprTracer' at 0x7fd88f0a4950>], out_avals=[ShapedArray(float32[32,63])], primitive=pjit, params={'jaxpr': { lambda ; a:f32[32,63,257152] b:f32[32,63,257152] c:f32[32,63]. let
    d:f32[32,63,257152] = mul a b
    e:f32[32,63] = reduce_sum[axes=(2,)] d
    f:f32[32,63] = div e c
  in (f,) }, 'in_shardings': (UnspecifiedValue, UnspecifiedValue, UnspecifiedValue), 'out_shardings': (UnspecifiedValue,), 'in_layouts': (None, None, None), 'out_layouts': (None,), 'resource_env': None, 'donated_invars': (False, False, False), 'name': '_reduce_max', 'keep_unused': False, 'inline': True}, effects=set(), source_info=SourceInfo(traceback=<jaxlib.xla_extension.Traceback object at 0x14bfc4d0>, name_stack=NameStack(stack=(Transform(name='jvp'),)))) (32, 63)
```
wandb: - 0.005 MB of 0.005 MB uploadedwandb: \ 0.005 MB of 0.005 MB uploadedwandb: | 0.005 MB of 0.005 MB uploadedwandb: / 0.010 MB of 0.016 MB uploaded (0.004 MB deduped)wandb: - 0.016 MB of 0.016 MB uploaded (0.004 MB deduped)wandb: 
wandb: Run history:
wandb: loss █▅▆▃▃▂▆▆▄█▅▃▂▅▃▅▄▃▄▃▅▄▂▂▃▄▅▄▃▅▂▃▃▂▃▂▄▂▂▁
wandb:   lr ███████▇▇▇▇▇▆▆▆▆▅▅▅▅▄▄▄▄▃▃▃▃▂▂▂▂▂▁▁▁▁▁▁▁
wandb: step ▁▁▁▁▂▂▂▂▂▃▃▃▃▃▃▄▄▄▄▄▅▅▅▅▅▅▆▆▆▆▆▇▇▇▇▇▇███
wandb: 
wandb: Run summary:
wandb: loss 0.12484
wandb:   lr 0.0
wandb: step 5000
wandb: 
wandb: 🚀 View run 32_0001_alltrainable-0 at: https://wandb.ai/kobomao/ML_healthcare/runs/zt0ah5sa
wandb: ⭐️ View project at: https://wandb.ai/kobomao/ML_healthcare
wandb: Synced 5 W&B file(s), 0 media file(s), 2 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20240524_030439-zt0ah5sa/logs

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21839961: <32_0001_alltrainable_0> in cluster <dcc> Done

Job <32_0001_alltrainable_0> was submitted from host <n-62-27-19> by user <s183914> in cluster <dcc> at Thu May 23 12:34:59 2024
Job was executed on host(s) <4*n-62-18-11>, in queue <gpua100>, as user <s183914> in cluster <dcc> at Fri May 24 03:03:43 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_final/ML_final> was used as the working directory.
Started at Fri May 24 03:03:43 2024
Terminated at Fri May 24 06:09:14 2024
Results reported at Fri May 24 06:09:14 2024

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

Successfully completed.

Resource usage summary:

    CPU time :                                   9882.43 sec.
    Max Memory :                                 4227 MB
    Average Memory :                             3993.64 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               61309.00 MB
    Max Swap :                                   -
    Max Processes :                              6
    Max Threads :                                63
    Run time :                                   11131 sec.
    Turnaround time :                            63255 sec.

The output (if any) is above this job summary.

