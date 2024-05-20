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

    def run(self, b: float, d: str, a: int) -> None:
        run_test()


Defaults.start()