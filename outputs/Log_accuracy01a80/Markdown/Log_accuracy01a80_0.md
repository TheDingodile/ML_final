2024-05-28 04:47:19.700024: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.17.0
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_final/ML_final/wandb/run-20240528_044731-k699rtxy
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run Log_accuracy01a80-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/k699rtxy
2024-05-28 04:48:02.870689: W external/xla/xla/service/gpu/nvptx_compiler.cc:760] The NVIDIA driver's CUDA version is 12.4 which is older than the ptxas CUDA version (12.5.40). Because the driver is older than the ptxas version, XLA is disabling parallel compilation, which may slow down compilation. You should update your NVIDIA driver or use the NVIDIA-provided CUDA forward compatibility packages.
2024-05-28 04:48:07.759847: W tensorflow/core/common_runtime/gpu/gpu_device.cc:2251] Cannot dlopen some GPU libraries. Please make sure the missing libraries mentioned above are installed properly if you would like to use GPU. Follow the guide at https://www.tensorflow.org/install/gpu for how to download and setup the required libraries for your platform.
Skipping registering GPU devices...
2024-05-28 04:50:04.861109: W external/xla/xla/service/gpu/gemm_fusion_autotuner.cc:864] Slow kernel for gemm_fusion_dot took: 1.003786255s. {block_m:16,block_n:16,block_k:512,split_k:1,num_stages:1,num_warps:4,num_ctas:1}

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
| <c>name</c>       | <d>str</d>        | <j>"Log_accuracy01a80-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>3600</f>       |
| <c>lr</c>         | <d>float</d>      | <f>0.1</f>        |
| <c>batch_size</c> | <d>int</d>        | <f>32</f>         |
| <c>steps</c>      | <d>int</d>        | <f>5000</f>       |

# Output

```
Traced<ShapedArray(float32[32,63])>with<JVPTrace(level=3/0)> with
  primal = Traced<ShapedArray(float32[32,63])>with<DynamicJaxprTrace(level=1/0)>
  tangent = Traced<ShapedArray(float32[32,63])>with<JaxprTrace(level=2/0)> with
    pval = (ShapedArray(float32[32,63]), None)
    recipe = JaxprEqnRecipe(eqn_id=<object object at 0x7f31cb70e9d0>, in_tracers=(Traced<ShapedArray(float32[32,63,257152]):JaxprTrace(level=2/0)>, Traced<ShapedArray(float32[32,63,257152]):JaxprTrace(level=2/0)>, Traced<ShapedArray(float32[32,63]):JaxprTrace(level=2/0)>), out_tracer_refs=[<weakref at 0x7f31cb78e430; to 'JaxprTracer' at 0x7f31cb78e4d0>], out_avals=[ShapedArray(float32[32,63])], primitive=pjit, params={'jaxpr': { lambda ; a:f32[32,63,257152] b:f32[32,63,257152] c:f32[32,63]. let
    d:f32[32,63,257152] = mul a b
    e:f32[32,63] = reduce_sum[axes=(2,)] d
    f:f32[32,63] = div e c
  in (f,) }, 'in_shardings': (UnspecifiedValue, UnspecifiedValue, UnspecifiedValue), 'out_shardings': (UnspecifiedValue,), 'in_layouts': (None, None, None), 'out_layouts': (None,), 'resource_env': None, 'donated_invars': (False, False, False), 'name': '_reduce_max', 'keep_unused': False, 'inline': True}, effects=set(), source_info=SourceInfo(traceback=<jaxlib.xla_extension.Traceback object at 0x14f55600>, name_stack=NameStack(stack=(Transform(name='jvp'),)))) (32, 63)
Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 124, in <module>
    Defaults.start()
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/dtu/__init__.py", line 235, in start
    cls.run(*args)
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 70, in run
    examples = [next(data_iterator) for _ in range(batch_size)]
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 70, in <listcomp>
    examples = [next(data_iterator) for _ in range(batch_size)]
                ^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/vqa_dataset.py", line 93, in train_data_iterator
    image = self.preprocess_image(image)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/vqa_dataset.py", line 40, in preprocess_image
    image = tf.image.resize(image, (self.image_resolution, self.image_resolution), method='bilinear', antialias=True)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/tensorflow/python/util/traceback_utils.py", line 150, in error_handler
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/tensorflow/python/util/dispatch.py", line 1260, in op_dispatch_handler
    return dispatch_target(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/tensorflow/python/ops/image_ops_impl.py", line 1789, in resize_images_v2
    return _resize_images_common(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/tensorflow/python/ops/image_ops_impl.py", line 1522, in _resize_images_common
    images = resizer_fn(images, size)
             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/tensorflow/python/ops/image_ops_impl.py", line 1769, in resize_fn
    return resize_with_scale_and_translate('triangle')
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/tensorflow/python/ops/image_ops_impl.py", line 1759, in resize_with_scale_and_translate
    return gen_image_ops.scale_and_translate(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/tensorflow/python/ops/gen_image_ops.py", line 4510, in scale_and_translate
    _result = pywrap_tfe.TFE_Py_FastPathExecute(
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
KeyboardInterrupt
Terminated
