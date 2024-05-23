from main import Defaults, GPU


# Defaults("Test1CPU", GPU=None)
# Defaults("CPU_check", GPU=None)
# Defaults("GPU_check", GPU=GPU.v32)
Defaults("Batch_size", GPU=GPU.a80, batch_size=64, steps=5000, lr=0.001)

# Defaults("Cuda_version_check2", GPU=None)
