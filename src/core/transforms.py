from typing import Callable
from core.system import LTISystem

class ZTransform:
    def __call__(self, signal, calc_limits=(-100, 100)) -> Callable[[complex], complex]:
        return self.transform(signal, calc_limits)

    __getitem__ = __call__

    def transform(self, signal, calc_limits=(-100, 100)) -> Callable[[complex], complex]:
        return lambda z: sum(signal[k] * (z ** (-k)) for k in range(calc_limits[0], calc_limits[1]))

Z = ZTransform()