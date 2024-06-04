from .vqa_module import VQAModule
from .yes_vqa_module import YesVQAModule
# from .m3ae_vqa_module import M3AEVQAModule
from .custom_vqa_module import CustomVQAModule
import big_vision.utils as bv_utils


import os


def get_vqa_module(vqa_module_type: str, threshold:float) -> VQAModule:
    """Get the VQA module based on the specified type."""
    if vqa_module_type == "yes" or vqa_module_type == "debug":  # NOTE: this could be a baseline model
        return YesVQAModule()
    # elif vqa_module_type == "paligemma":
    #     model_path = "../../../../../../../work1/s183914/ml_healthcare/models/model1.npz"
    #     params = bv_utils.load_checkpoint_np(f"{path}/params_{name}.npz")
    #     return M3AEVQAModule(model_path=model_path)
    
    elif vqa_module_type == "custom":
        return CustomVQAModule(threshold=threshold)
    else:
        raise NotImplementedError("Only support debug model")
