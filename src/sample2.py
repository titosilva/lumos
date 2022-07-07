from core.default_signals import signal_from_values, d, u
from core.signal import n
from core.plot_utils import PlotUtils

if __name__ == "__main__":
    # More complex combinations of signals

    x1 = signal_from_values([0, 1, 2, 3, 2, 1, 0])[n + 3]
    x2 = signal_from_values([1, 0.5, 1, 1])
    x3 = signal_from_values([1, 1, 1, -1, -1])[n + 2]
    x4 = (u - u[n-5]) * 3

    # SignalPlotter.plot(x1, (-5, 5))
    # SignalPlotter.plot(x2, (-5, 5))
    # SignalPlotter.plot(x3, (-5, 5))
    # SignalPlotter.plot(x4, (-5, 5))

    wa = x2[n] - x4[n-2]
    PlotUtils.plot_many_signals([
        (x2, '$x_2[n]$', (-8, 8)),
        (x4, '$x_4[n]$', (-8, 8)),
        (wa, '$x_2[n] - x_4[n-2]$', (-8, 8)),
    ], rows=3)

    wb = -1 * x3[n - 1] * x1[n + 1]
    PlotUtils.plot_many_signals([
        (x3, '$x_3[n]$', (-8, 8)),
        (x1, '$x_1[n]$', (-8, 8)),
        (wb, '$-1 x_3[n - 1] x_1[n + 1]$', (-8, 8)),
    ], rows=3)

    wc = x2 * x3[n - 1] + x1
    PlotUtils.plot_many_signals([
        (x2, '$x_2[n]$', (-8, 8)),
        (x3, '$x_3[n]$', (-8, 8)),
        (x1, '$x_1[n]$', (-8, 8)),
        (wc, '$x_2[n] * x_3[n-1] + x_1[n]$', (-8, 8)),
    ], rows=4)
