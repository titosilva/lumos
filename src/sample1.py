from core.default_signals import d, dexp, u, dsin
from core.signal import n
from core.plot_utils import PlotUtils
import numpy as np

if __name__ == "__main__":
    # Common signals

    # You can easily define a signal by using the 'n' imported from core.signal
    x1 = n * 2 + 2
    # You may apply the signal to an input and see the results
    print(f"x[2] = {x1[2]}")
    # You may also plot a signal and see its shape
    PlotUtils.plot_signal(x1, (-5, 5), title='$x_1[n] = 2n + 2$')

    # A nice way to define complex signals is by using 'constructing blocks'
    # Some basic signals are defined on core.default_signals and may be used 
    # 'u' is an alias to unit_step and 'd' is an alias to unit_impulse
    x2 = u[n] - u[n-4] - 0.5 * d[n-1]
    # You may also add the '[n]' after a signal, if you want to
    PlotUtils.plot_signal(x2[n], (-5, 5), title='$x_2 = u[n] - u[n-4] - 0.5 * \delta [n-1]$')

    PlotUtils.plot_many_signals([
        (5 * dsin[np.pi * n / 4], '$sin(\\frac{\pi n}{4})$', (-10, 10)),
        (5 * dsin[np.pi * n / 6], '$sin(\\frac{\pi n}{6})$', (-10, 10)),
        (5 * dsin[np.pi * n / 6 - np.pi / 6], '$sin(\\frac{\pi n}{6} - \frac{\pi}{6})$', (-10, 10)),
        (5 * dsin[n], '$sin(\pi n)$', (-10, 10)),
    ], rows=4)

    PlotUtils.plot_many_signals([
        (dexp(2) * u[n], '$2 ^{n} u[n]$', (-3, 3)),
        (dexp(0.5) * u[n], '$2 ^{-n} u[n]$', (-3, 3)),
    ], rows=2)