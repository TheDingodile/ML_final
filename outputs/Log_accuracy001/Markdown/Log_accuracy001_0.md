2024-05-27 18:05:49.265872: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.17.0
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_final/ML_final/wandb/run-20240527_180648-wcssb8uk
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run Log_accuracy001-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/wcssb8uk
2024-05-27 18:07:35.883979: W external/xla/xla/service/gpu/nvptx_compiler.cc:760] The NVIDIA driver's CUDA version is 12.4 which is older than the ptxas CUDA version (12.5.40). Because the driver is older than the ptxas version, XLA is disabling parallel compilation, which may slow down compilation. You should update your NVIDIA driver or use the NVIDIA-provided CUDA forward compatibility packages.
2024-05-27 18:07:45.296685: W tensorflow/core/common_runtime/gpu/gpu_device.cc:2251] Cannot dlopen some GPU libraries. Please make sure the missing libraries mentioned above are installed properly if you would like to use GPU. Follow the guide at https://www.tensorflow.org/install/gpu for how to download and setup the required libraries for your platform.
Skipping registering GPU devices...
2024-05-27 18:10:45.065028: W external/tsl/tsl/framework/bfc_allocator.cc:291] Allocator (GPU_0_bfc) ran out of memory trying to allocate 9.79GiB with freed_by_count=0. The caller indicates that this is not a failure, but this may mean that there could be performance gains if more memory were available.

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
| <c>name</c>       | <d>str</d>        | <j>"Log_accuracy001-0"</j> |
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
    recipe = JaxprEqnRecipe(eqn_id=<object object at 0x7f6943ff29d0>, in_tracers=(Traced<ShapedArray(float32[32,63,257152]):JaxprTrace(level=2/0)>, Traced<ShapedArray(float32[32,63,257152]):JaxprTrace(level=2/0)>, Traced<ShapedArray(float32[32,63]):JaxprTrace(level=2/0)>), out_tracer_refs=[<weakref at 0x7f6943e76890; to 'JaxprTracer' at 0x7f6943e753f0>], out_avals=[ShapedArray(float32[32,63])], primitive=pjit, params={'jaxpr': { lambda ; a:f32[32,63,257152] b:f32[32,63,257152] c:f32[32,63]. let
    d:f32[32,63,257152] = mul a b
    e:f32[32,63] = reduce_sum[axes=(2,)] d
    f:f32[32,63] = div e c
  in (f,) }, 'in_shardings': (UnspecifiedValue, UnspecifiedValue, UnspecifiedValue), 'out_shardings': (UnspecifiedValue,), 'in_layouts': (None, None, None), 'out_layouts': (None,), 'resource_env': None, 'donated_invars': (False, False, False), 'name': '_reduce_max', 'keep_unused': False, 'inline': True}, effects=set(), source_info=SourceInfo(traceback=<jaxlib.xla_extension.Traceback object at 0x13136230>, name_stack=NameStack(stack=(Transform(name='jvp'),)))) (32, 63)
Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 125, in <module>
    Defaults.start()
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/dtu/__init__.py", line 235, in start
    cls.run(*args)
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 82, in run
    text_logits, _ = model.apply({"params": params}, imgs, txts[:, :-1], mask_ar[:, :-1], train=True)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/big_vision/models/proj/paligemma/paligemma.py", line 151, in __call__
    _, out_llm = self._llm(x, mask=attn_mask, train=train)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/big_vision/models/proj/paligemma/gemma_bv.py", line 81, in __call__
    logits, out = self.model(
                  ^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/big_vision/models/ppp/gemma.py", line 461, in __call__
    x = embedder.decode(x)
        ^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/big_vision/models/ppp/gemma.py", line 175, in decode
    return jnp.dot(x, self.input_embedding_table.T)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
jaxlib.xla_extension.XlaRuntimeError: RESOURCE_EXHAUSTED: Out of memory while trying to allocate 10516807680 bytes.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
wandb: - 0.005 MB of 0.005 MB uploadedwandb: \ 0.005 MB of 0.005 MB uploadedwandb: | 0.005 MB of 0.005 MB uploadedwandb: / 0.010 MB of 0.018 MB uploaded (0.004 MB deduped)wandb: - 0.018 MB of 0.018 MB uploaded (0.004 MB deduped)wandb: 
wandb: Run history:
wandb: loss ▄█▂▃▇▄▁▁▁
wandb:   lr ██▇▇▆▅▄▂▁
wandb: step ▁▂▃▄▅▅▆▇█
wandb: 
wandb: Run summary:
wandb: loss 0.33788
wandb:   lr 0.01
wandb: step 9
wandb: 
wandb: 🚀 View run Log_accuracy001-0 at: https://wandb.ai/kobomao/ML_healthcare/runs/wcssb8uk
wandb: ⭐️ View project at: https://wandb.ai/kobomao/ML_healthcare
wandb: Synced 5 W&B file(s), 0 media file(s), 2 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20240527_180648-wcssb8uk/logs

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21868465: <Log_accuracy001_0> in cluster <dcc> Exited

Job <Log_accuracy001_0> was submitted from host <n-62-27-20> by user <s183914> in cluster <dcc> at Mon May 27 17:21:33 2024
Job was executed on host(s) <4*n-62-20-10>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon May 27 18:03:20 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_final/ML_final> was used as the working directory.
Started at Mon May 27 18:03:20 2024
Terminated at Mon May 27 18:11:06 2024
Results reported at Mon May 27 18:11:06 2024

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

    CPU time :                                   175.48 sec.
    Max Memory :                                 3362 MB
    Average Memory :                             2175.60 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               62174.00 MB
    Max Swap :                                   -
    Max Processes :                              6
    Max Threads :                                63
    Run time :                                   467 sec.
    Turnaround time :                            2973 sec.

The output (if any) is above this job summary.

2024-05-28 03:49:56.184336: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.17.0
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_final/ML_final/wandb/run-20240528_035014-yyixe5md
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run Log_accuracy001-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/yyixe5md
2024-05-28 03:50:51.686280: W external/xla/xla/service/gpu/nvptx_compiler.cc:760] The NVIDIA driver's CUDA version is 12.4 which is older than the ptxas CUDA version (12.5.40). Because the driver is older than the ptxas version, XLA is disabling parallel compilation, which may slow down compilation. You should update your NVIDIA driver or use the NVIDIA-provided CUDA forward compatibility packages.
2024-05-28 03:51:00.381852: W tensorflow/core/common_runtime/gpu/gpu_device.cc:2251] Cannot dlopen some GPU libraries. Please make sure the missing libraries mentioned above are installed properly if you would like to use GPU. Follow the guide at https://www.tensorflow.org/install/gpu for how to download and setup the required libraries for your platform.
Skipping registering GPU devices...

Aborted!

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
| <c>name</c>       | <d>str</d>        | <j>"Log_accuracy001-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>3600</f>       |
| <c>lr</c>         | <d>float</d>      | <f>0.01</f>       |
| <c>batch_size</c> | <d>int</d>        | <f>8</f>          |
| <c>steps</c>      | <d>int</d>        | <f>5000</f>       |

# Output

```
Traced<ShapedArray(float32[8,63])>with<JVPTrace(level=3/0)> with
  primal = Traced<ShapedArray(float32[8,63])>with<DynamicJaxprTrace(level=1/0)>
  tangent = Traced<ShapedArray(float32[8,63])>with<JaxprTrace(level=2/0)> with
    pval = (ShapedArray(float32[8,63]), None)
    recipe = JaxprEqnRecipe(eqn_id=<object object at 0x7f39043de9d0>, in_tracers=(Traced<ShapedArray(float32[8,63,257152]):JaxprTrace(level=2/0)>, Traced<ShapedArray(float32[8,63,257152]):JaxprTrace(level=2/0)>, Traced<ShapedArray(float32[8,63]):JaxprTrace(level=2/0)>), out_tracer_refs=[<weakref at 0x7f390445ac00; to 'JaxprTracer' at 0x7f3904459a80>], out_avals=[ShapedArray(float32[8,63])], primitive=pjit, params={'jaxpr': { lambda ; a:f32[8,63,257152] b:f32[8,63,257152] c:f32[8,63]. let
    d:f32[8,63,257152] = mul a b
    e:f32[8,63] = reduce_sum[axes=(2,)] d
    f:f32[8,63] = div e c
  in (f,) }, 'in_shardings': (UnspecifiedValue, UnspecifiedValue, UnspecifiedValue), 'out_shardings': (UnspecifiedValue,), 'in_layouts': (None, None, None), 'out_layouts': (None,), 'resource_env': None, 'donated_invars': (False, False, False), 'name': '_reduce_max', 'keep_unused': False, 'inline': True}, effects=set(), source_info=SourceInfo(traceback=<jaxlib.xla_extension.Traceback object at 0x125ceea0>, name_stack=NameStack(stack=(Transform(name='jvp'),)))) (8, 63)
Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 124, in <module>
    Defaults.start()
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/dtu/__init__.py", line 235, in start
    cls.run(*args)
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 74, in run
    params, loss = update_fn(params, batch, learning_rate)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
KeyboardInterrupt
Terminated

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21869389: <Log_accuracy001_0> in cluster <dcc> Exited

Job <Log_accuracy001_0> was submitted from host <n-62-30-6> by user <s183914> in cluster <dcc> at Tue May 28 03:46:53 2024
Job was executed on host(s) <4*n-62-20-12>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue May 28 03:48:43 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_final/ML_final> was used as the working directory.
Started at Tue May 28 03:48:43 2024
Terminated at Tue May 28 05:07:03 2024
Results reported at Tue May 28 05:07:03 2024

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

    CPU time :                                   4244.00 sec.
    Max Memory :                                 3815 MB
    Average Memory :                             3082.84 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               61721.00 MB
    Max Swap :                                   -
    Max Processes :                              6
    Max Threads :                                63
    Run time :                                   4700 sec.
    Turnaround time :                            4810 sec.

The output (if any) is above this job summary.

