from cmath import cos, sin
from core.signal import Signal
from typing import Callable, List

def signal_from_values(l: List[float], default_value: float = 0):
    return Signal(lambda n: default_value if n < 0 or n >= len(l) else l[n])

class UnitImpulse(Signal):
    def __init__(self, *args, **kwargs):
        super().__init__(lambda n: 1 if n == 0 else 0)

    def __fastconv__(self, func):
        return func

unit_impulse = UnitImpulse()
delta = UnitImpulse()
d = UnitImpulse()

class UnitStep(Signal):
    def __init__(self, *args, **kwargs):
        super().__init__(lambda n: 1 if n >= 0 else 0)

    def __fastconv__(self, func):
        upper_lim = self._conv_limits[1]
        if upper_lim < 0:
            return 0
        
        lower_lim = self._conv_limits[0]
        lower_lim = 0 if lower_lim < 0 else lower_lim

        fn = lambda n: sum(self(m) * func(n - m) for m in range(lower_lim, upper_lim + 1))
        return Signal(fn)
        
unit_step = UnitStep()
u = UnitStep()

dsin = Signal(sin)
dcos = Signal(cos)
