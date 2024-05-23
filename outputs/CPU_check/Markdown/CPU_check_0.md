2024-05-23 08:53:01.694692: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.17.0
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_final/ML_final/wandb/run-20240523_085306-dlxzqjio
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run CPU_check-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/dlxzqjio

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
| <c>name</c>       | <d>str</d>        | <j>"CPU_check-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>3600</f>       |
| <c>lr</c>         | <d>float</d>      | <f>0.03</f>       |
| <c>batch_size</c> | <d>int</d>        | <f>8</f>          |
| <c>steps</c>      | <d>int</d>        | <f>1000</f>       |

# Output

```
Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/xla_bridge.py", line 874, in backends
    backend = _init_backend(platform)
              ^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/xla_bridge.py", line 965, in _init_backend
    backend = registration.factory()
              ^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/xla_bridge.py", line 663, in factory
    return xla_client.make_c_api_client(plugin_name, updated_options, None)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jaxlib/xla_client.py", line 199, in make_c_api_client
    return _xla.get_c_api_client(plugin_name, options, distributed_client)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
jaxlib.xla_extension.XlaRuntimeError: FAILED_PRECONDITION: No visible GPU devices.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 93, in <module>
    Defaults.start()
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/dtu/__init__.py", line 235, in start
    cls.run(*args)
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 35, in run
    if (isServer): predictor_function, tokenizer, trainable_mask, params, model = big_vision_test(isServer=isServer)
                                                                                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/big_vision_test.py", line 46, in big_vision_test
    decode = functools.partial(decode_fn, devices=jax.devices(), eos_token=tokenizer.eos_id())
                                                  ^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/xla_bridge.py", line 1077, in devices
    return get_backend(backend).devices()
           ^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/xla_bridge.py", line 1011, in get_backend
    return _get_backend_uncached(platform)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/xla_bridge.py", line 990, in _get_backend_uncached
    bs = backends()
         ^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/xla_bridge.py", line 890, in backends
    raise RuntimeError(err_msg)
RuntimeError: Unable to initialize backend 'cuda': FAILED_PRECONDITION: No visible GPU devices. (you may need to uninstall the failing plugin package, or set JAX_PLATFORMS=cpu to skip this backend.)
wandb: - 0.004 MB of 0.004 MB uploadedwandb: \ 0.004 MB of 0.004 MB uploadedwandb: | 0.004 MB of 0.004 MB uploadedwandb: / 0.008 MB of 0.016 MB uploadedwandb: - 0.016 MB of 0.016 MB uploadedwandb: 🚀 View run CPU_check-0 at: https://wandb.ai/kobomao/ML_healthcare/runs/dlxzqjio
wandb: ⭐️ View project at: https://wandb.ai/kobomao/ML_healthcare
wandb: Synced 5 W&B file(s), 0 media file(s), 2 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20240523_085306-dlxzqjio/logs

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21839051: <CPU_check_0> in cluster <dcc> Exited

Job <CPU_check_0> was submitted from host <n-62-30-2> by user <s183914> in cluster <dcc> at Thu May 23 08:52:51 2024
Job was executed on host(s) <n-62-31-23>, in queue <hpc>, as user <s183914> in cluster <dcc> at Thu May 23 08:52:51 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_final/ML_final> was used as the working directory.
Started at Thu May 23 08:52:51 2024
Terminated at Thu May 23 08:53:43 2024
Results reported at Thu May 23 08:53:43 2024

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

    CPU time :                                   32.60 sec.
    Max Memory :                                 451 MB
    Average Memory :                             451.00 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15933.00 MB
    Max Swap :                                   -
    Max Processes :                              5
    Max Threads :                                6
    Run time :                                   52 sec.
    Turnaround time :                            52 sec.

The output (if any) is above this job summary.

