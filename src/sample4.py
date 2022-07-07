from typing import Tuple
from numpy import sign
from core.default_signals import signal_from_values, d, u
from core.plot_utils import PlotUtils
from core.system import LTISystem
from core.signal import Signal, n

def plot_lti_system_responses(h: Signal, input: Signal, limits: Tuple[int, int]):
    T = LTISystem(h)

    PlotUtils.plot_many_signals([
        (h, 'h[n]', limits),
        (input, 'x[n]', limits),
        (T(input), 'T{x[n]}', limits),
    ], rows=3)

if __name__ == "__main__":
    # Using LTISystem to compute system outputs

    # Building an LTI System and applying it
    hd = d[n]
    Td = LTISystem(hd)
    xd = u[n]
    yd = Td(xd)
    PlotUtils.plot_signal(Td(u), (-5, 5))

    # Other examples
    h1 = u[n]
    x1 = d[n] + d[n-1]
    plot_lti_system_responses(h1, x1, (-5, 5))

    h9 = signal_from_values([1, 2, 1, -2])
    x9 = (u - u[n - 5]) * 3
    plot_lti_system_responses(h9, x9, (-5, 15))

    h10 = signal_from_values([0, 1, 2, 3])
    x10 = (signal_from_values([-2, -1, 0, 1, 2]))[n + 2]
    plot_lti_system_responses(h10, x10, (-5, 15))

    h11 = signal_from_values([0, 2, 1, -4])
    x11 = signal_from_values([0, 1, 2, 3, 2, 1, 0])[n + 3]
    plot_lti_system_responses(h11, x11, (-5, 15))

    h12 = signal_from_values([1, 1, 1, -1, -1])[n + 2]
    x12 = signal_from_values([3, 3, -2, -2])[n + 1]
    plot_lti_system_responses(h12, x12, (-5, 15))

