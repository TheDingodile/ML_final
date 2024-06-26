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

# Defaults("VQA_eval", GPU=GPU.v32)

# Defaults("eval_full", GPU=GPU.a80)


# Defaults("True_SQL_eval", GPU=GPU.a40)

# Defaults("test_final", GPU=GPU.v32, vqa_module_type="custom")

# Defaults("test_final_07", GPU=GPU.v32, vqa_module_type="custom", threshold=0.7)
# Defaults("test_final_08", GPU=GPU.v32, vqa_module_type="custom", threshold=0.8)
# Defaults("test_final_09", GPU=GPU.v32, vqa_module_type="custom", threshold=0.9)

# Defaults("test_final_07_a80", GPU=GPU.a80, vqa_module_type="custom", threshold=0.7)

# Defaults("test_set08_a80", GPU=GPU.a80, vqa_module_type="custom", threshold=0.8, table_path="database/mimic_iv_cxr/gold", prediction_file_name="predictions_LLM_1-0_test")
# Defaults("test_set09_a80", GPU=GPU.a80, vqa_module_type="custom", threshold=0.9, table_path="database/mimic_iv_cxr/gold", prediction_file_name="predictions_LLM_1-0_test")

# Defaults("test_set08_fix", GPU=GPU.v32, vqa_module_type="custom", threshold=0.8, table_path="database/mimic_iv_cxr/gold", prediction_file_name="predictions_LLM_1-0_test")
# Defaults("test_set09_fix", GPU=GPU.v32, vqa_module_type="custom", threshold=0.9, table_path="database/mimic_iv_cxr/gold", prediction_file_name="predictions_LLM_1-0_test")
# Defaults("test_set07_fix", GPU=GPU.v32, vqa_module_type="custom", threshold=0.7, table_path="database/mimic_iv_cxr/gold", prediction_file_name="predictions_LLM_1-0_test")

# # 1, 3 and 4 are the good vision models

# Defaults("vision3valid09", GPU=GPU.v32, vqa_module_type="custom", threshold=0.9, model_path_name="params_model_3-0", 
#          table_path="database/mimic_iv_cxr/silver", prediction_file_name="predictions_LLM_1-0")

# Defaults("vision3test09", GPU=GPU.v32, vqa_module_type="custom", threshold=0.9, model_path_name="params_model_3-0", 
#          table_path="database/mimic_iv_cxr/gold", prediction_file_name="predictions_LLM_1-0_test")

# Defaults("vision3valid08", GPU=GPU.v32, vqa_module_type="custom", threshold=0.8, model_path_name="params_model_3-0", 
#          table_path="database/mimic_iv_cxr/silver", prediction_file_name="predictions_LLM_1-0")

# Defaults("vision3test08", GPU=GPU.v32, vqa_module_type="custom", threshold=0.8, model_path_name="params_model_3-0", 
#          table_path="database/mimic_iv_cxr/gold", prediction_file_name="predictions_LLM_1-0_test")

# Defaults("vision1valid09", GPU=GPU.v32, vqa_module_type="custom", threshold=0.9, model_path_name="params_model_1-0",
#          table_path="database/mimic_iv_cxr/silver", prediction_file_name="predictions_LLM_1-0")

# Defaults("vision1test09", GPU=GPU.v32, vqa_module_type="custom", threshold=0.9, model_path_name="params_model_1-0", 
#          table_path="database/mimic_iv_cxr/gold", prediction_file_name="predictions_LLM_1-0_test")

Defaults("vision4test09", GPU=GPU.a80, vqa_module_type="custom", threshold=0.9, model_path_name="params_model_4-0", 
         table_path="database/mimic_iv_cxr/gold", prediction_file_name="predictions_LLM_1-0_test")

