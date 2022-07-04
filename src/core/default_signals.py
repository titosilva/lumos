from cmath import cos, sin
from core.signal import Signal
from typing import List

def linear(ang_c: float = 1, linear_c: float = 0):
    return Signal(lambda n: ang_c * n + linear_c)

def signal_from_values(l: List[float], default_value: float = 0):
    return Signal(lambda n: default_value if n < 0 or n >= len(l) else l[n])

unit_impulse = Signal(lambda n: 1 if n == 0 else 0)
delta = unit_impulse
d = unit_impulse

unit_step = Signal(lambda n: 1 if n >= 0 else 0)
u = unit_step

dsin = Signal(lambda n: sin(n))
dcos = Signal(lambda n: cos(n))
