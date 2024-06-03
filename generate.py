from main import Defaults, GPU


# Defaults("Test1CPU", GPU=None)
# Defaults("CPU_check", GPU=None)
# Defaults("GPU_check", GPU=GPU.v32)
# Defaults("Batch_size", GPU=GPU.a80, batch_size=64, steps=5000, lr=0.001)
# Defaults("32_001", GPU=GPU.v32, batch_size=32, steps=5000, lr=0.01)
# Defaults("16_001", GPU=GPU.v32, batch_size=16, steps=5000, lr=0.01)
# Defaults("32_01", GPU=GPU.v32, batch_size=32, steps=5000, lr=0.1)
# Defaults("16_01", GPU=GPU.v32, batch_size=16, steps=5000, lr=0.1)

# Defaults("32_001_alltrainable", GPU=GPU.a80, batch_size=32, steps=5000, lr=0.01)
# Defaults("32_0001_alltrainable", GPU=GPU.a80, batch_size=32, steps=5000, lr=0.001)

# Defaults("Log_accuracy001", GPU=GPU.v32, batch_size=8, steps=5000, lr=0.01)
# Defaults("Log_accuracy01", GPU=GPU.v32, batch_size=8, steps=5000, lr=0.1)
# Defaults("Log_accuracy001a80", GPU=GPU.a80, batch_size=32, steps=5000, lr=0.01)

# Defaults("Log_accuracy01a80", GPU=GPU.a80, batch_size=32, steps=5000, lr=0.1)

# Defaults("v32test8", GPU=GPU.v32, batch_size=8, steps=5000, lr=0.01)
# Defaults("a80test", GPU=GPU.v32, batch_size=16, steps=5000, lr=0.01)
# Defaults("a80testa80", GPU=GPU.a80, batch_size=16, steps=5000, lr=0.01)

# Defaults("test_eval", GPU=GPU.v32, batch_size=8, steps=10000, lr=0.01)

# Defaults("train_saved_model_test", GPU=GPU.v32, batch_size=8, steps=10000, lr=0.01)
# Defaults("test_save_a80", GPU=GPU.a80, batch_size=8, steps=10000, lr=0.01)

# Defaults("mini_test", GPU=GPU.v32, batch_size=8, steps=100, lr=0.01)
# for i in range(6):
#     Defaults(f"model_{i}", GPU=GPU.v32, batch_size=8, steps=10000, lr=0.01)

Defaults("VQA_eval", GPU=GPU.v32)



