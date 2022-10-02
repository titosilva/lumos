from typing import Tuple
from core.signal import Signal

def dot(s1: Signal, s2: Signal, limits: Tuple[int, int] = (-1000, 1000)) -> Signal:
    result = 0

    for n in range(limits[0], limits[1]):
        result += s1[n] * s2[n]

    return result
