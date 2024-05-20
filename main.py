from __future__ import annotations
from dtu import Parameters, dtu, GPU
from paligemma import run_test


@dtu
class Defaults(Parameters):
    name: str = "local"
    instances: int = 1
    GPU: None | GPU = None
    time: int = 3600

    b: float = 2.0
    a: int = 1
    d: str = "fd"

    def run(self, b: float, d: str, a: int, isServer: bool) -> None:
        if (isServer): path = "../../../../../../../work1/s183914/"
        else: path = "ehrxqa-2024-ml4h"
        run_test(path)


Defaults.start()