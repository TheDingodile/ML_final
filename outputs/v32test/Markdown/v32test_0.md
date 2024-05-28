2024-05-28 06:59:20.506456: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.17.0
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_final/ML_final/wandb/run-20240528_065925-stur3mtd
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run v32test-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/stur3mtd
2024-05-28 06:59:52.883318: W external/xla/xla/service/gpu/nvptx_compiler.cc:760] The NVIDIA driver's CUDA version is 12.4 which is older than the ptxas CUDA version (12.5.40). Because the driver is older than the ptxas version, XLA is disabling parallel compilation, which may slow down compilation. You should update your NVIDIA driver or use the NVIDIA-provided CUDA forward compatibility packages.
2024-05-28 06:59:58.996147: W tensorflow/core/common_runtime/gpu/gpu_device.cc:2251] Cannot dlopen some GPU libraries. Please make sure the missing libraries mentioned above are installed properly if you would like to use GPU. Follow the guide at https://www.tensorflow.org/install/gpu for how to download and setup the required libraries for your platform.
Skipping registering GPU devices...
2024-05-28 07:02:44.349554: W external/tsl/tsl/framework/bfc_allocator.cc:482] Allocator (GPU_0_bfc) ran out of memory trying to allocate 1.97GiB (rounded to 2110783744)requested by op 
2024-05-28 07:02:44.350162: W external/tsl/tsl/framework/bfc_allocator.cc:494] ***************************__******************************************************************_____
E0528 07:02:44.350251   27487 pjrt_stream_executor_client.cc:2826] Execution of replica 0 failed: RESOURCE_EXHAUSTED: Out of memory while trying to allocate 2110783616 bytes.
BufferAssignment OOM Debugging.
BufferAssignment stats:
             parameter allocation:    1.02GiB
              constant allocation:         0B
        maybe_live_out allocation:    4.89GiB
     preallocated temp allocation:    1.97GiB
  preallocated temp fragmentation:         0B (0.00%)
                 total allocation:    7.88GiB
              total fragmentation:       112B (0.00%)
Peak buffers:
	Buffer 1:
		Size: 4.89GiB
		Operator: op_name="jit(dot)/jit(main)/dot_general[dimension_numbers=(((2,), (0,)), ((), ())) precision=None preferred_element_type=float32]" source_file="/zhome/ea/9/137501/Desktop/ML_final/ML_final/big_vision/models/ppp/gemma.py" source_line=175
		XLA Label: custom-call
		Shape: f32[5104,257152]
		==========================

	Buffer 2:
		Size: 1.96GiB
		Operator: op_name="jit(dot)/jit(main)/dot_general[dimension_numbers=(((2,), (0,)), ((), ())) precision=None preferred_element_type=float32]" source_file="/zhome/ea/9/137501/Desktop/ML_final/ML_final/big_vision/models/ppp/gemma.py" source_line=175
		XLA Label: fusion
		Shape: f32[2048,257152]
		==========================

	Buffer 3:
		Size: 1004.50MiB
		Entry Parameter Subshape: f16[2048,257152]
		==========================

	Buffer 4:
		Size: 39.88MiB
		Entry Parameter Subshape: f32[16,319,2048]
		==========================

	Buffer 5:
		Size: 4.00MiB
		Operator: op_name="jit(dot)/jit(main)/dot_general[dimension_numbers=(((2,), (0,)), ((), ())) precision=None preferred_element_type=float32]" source_file="/zhome/ea/9/137501/Desktop/ML_final/ML_final/big_vision/models/ppp/gemma.py" source_line=175
		XLA Label: custom-call
		Shape: s8[4194304]
		==========================

	Buffer 6:
		Size: 16B
		Operator: op_name="jit(dot)/jit(main)/dot_general[dimension_numbers=(((2,), (0,)), ((), ())) precision=None preferred_element_type=float32]" source_file="/zhome/ea/9/137501/Desktop/ML_final/ML_final/big_vision/models/ppp/gemma.py" source_line=175
		XLA Label: custom-call
		Shape: (f32[5104,257152], s8[4194304])
		==========================



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
| <c>name</c>       | <d>str</d>        | <j>"v32test-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>3600</f>       |
| <c>lr</c>         | <d>float</d>      | <f>0.01</f>       |
| <c>batch_size</c> | <d>int</d>        | <f>16</f>         |
| <c>steps</c>      | <d>int</d>        | <f>5000</f>       |

# Output

```
Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 135, in <module>
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
ValueError: RESOURCE_EXHAUSTED: Out of memory while trying to allocate 2110783616 bytes.
BufferAssignment OOM Debugging.
BufferAssignment stats:
             parameter allocation:    1.02GiB
              constant allocation:         0B
        maybe_live_out allocation:    4.89GiB
     preallocated temp allocation:    1.97GiB
  preallocated temp fragmentation:         0B (0.00%)
                 total allocation:    7.88GiB
              total fragmentation:       112B (0.00%)
Peak buffers:
	Buffer 1:
		Size: 4.89GiB
		Operator: op_name="jit(dot)/jit(main)/dot_general[dimension_numbers=(((2,), (0,)), ((), ())) precision=None preferred_element_type=float32]" source_file="/zhome/ea/9/137501/Desktop/ML_final/ML_final/big_vision/models/ppp/gemma.py" source_line=175
		XLA Label: custom-call
		Shape: f32[5104,257152]
		==========================

	Buffer 2:
		Size: 1.96GiB
		Operator: op_name="jit(dot)/jit(main)/dot_general[dimension_numbers=(((2,), (0,)), ((), ())) precision=None preferred_element_type=float32]" source_file="/zhome/ea/9/137501/Desktop/ML_final/ML_final/big_vision/models/ppp/gemma.py" source_line=175
		XLA Label: fusion
		Shape: f32[2048,257152]
		==========================

	Buffer 3:
		Size: 1004.50MiB
		Entry Parameter Subshape: f16[2048,257152]
		==========================

	Buffer 4:
		Size: 39.88MiB
		Entry Parameter Subshape: f32[16,319,2048]
		==========================

	Buffer 5:
		Size: 4.00MiB
		Operator: op_name="jit(dot)/jit(main)/dot_general[dimension_numbers=(((2,), (0,)), ((), ())) precision=None preferred_element_type=float32]" source_file="/zhome/ea/9/137501/Desktop/ML_final/ML_final/big_vision/models/ppp/gemma.py" source_line=175
		XLA Label: custom-call
		Shape: s8[4194304]
		==========================

	Buffer 6:
		Size: 16B
		Operator: op_name="jit(dot)/jit(main)/dot_general[dimension_numbers=(((2,), (0,)), ((), ())) precision=None preferred_element_type=float32]" source_file="/zhome/ea/9/137501/Desktop/ML_final/ML_final/big_vision/models/ppp/gemma.py" source_line=175
		XLA Label: custom-call
		Shape: (f32[5104,257152], s8[4194304])
		==========================


--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
wandb: - 0.004 MB of 0.004 MB uploadedwandb: \ 0.004 MB of 0.004 MB uploadedwandb: | 0.004 MB of 0.004 MB uploadedwandb: / 0.010 MB of 0.018 MB uploaded (0.004 MB deduped)wandb: - 0.010 MB of 0.018 MB uploaded (0.004 MB deduped)wandb: 
wandb: Run history:
wandb: abstain_rate_0.55 ▁
wandb: abstain_rate_0.75 ▁
wandb:  abstain_rate_0.9 ▁
wandb:     accuracy_0.55 ▁
wandb:     accuracy_0.75 ▁
wandb:      accuracy_0.9 ▁
wandb:              loss ▄█▂▁▁▂▂▂▁▁▁▁▁▁▁▁▁▁▁
wandb:                lr █████▇▇▇▆▆▆▅▅▄▄▃▂▂▁
wandb:              step ▁▁▂▂▃▃▃▄▄▅▅▅▆▆▆▇▇██
wandb: 
wandb: Run summary:
wandb: abstain_rate_0.55 0.8125
wandb: abstain_rate_0.75 1.0
wandb:  abstain_rate_0.9 1.0
wandb:     accuracy_0.55 1.0
wandb:     accuracy_0.75 1.0
wandb:      accuracy_0.9 1.0
wandb:              loss 0.25208
wandb:                lr 0.01
wandb:              step 19
wandb: 
wandb: 🚀 View run v32test-0 at: https://wandb.ai/kobomao/ML_healthcare/runs/stur3mtd
wandb: ⭐️ View project at: https://wandb.ai/kobomao/ML_healthcare
wandb: Synced 5 W&B file(s), 0 media file(s), 2 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20240528_065925-stur3mtd/logs

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21869429: <v32test_0> in cluster <dcc> Exited

Job <v32test_0> was submitted from host <n-62-30-6> by user <s183914> in cluster <dcc> at Tue May 28 05:08:25 2024
Job was executed on host(s) <4*n-62-20-13>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue May 28 06:59:09 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_final/ML_final> was used as the working directory.
Started at Tue May 28 06:59:09 2024
Terminated at Tue May 28 07:03:02 2024
Results reported at Tue May 28 07:03:02 2024

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

    CPU time :                                   183.92 sec.
    Max Memory :                                 2487 MB
    Average Memory :                             1969.00 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               63049.00 MB
    Max Swap :                                   -
    Max Processes :                              6
    Max Threads :                                61
    Run time :                                   232 sec.
    Turnaround time :                            6877 sec.

The output (if any) is above this job summary.

