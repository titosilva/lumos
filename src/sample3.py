from core.default_signals import signal_from_values, d, u
from core.signal import n
from core.plot_utils import PlotUtils


if __name__ == "__main__":
    # Examples of signals built with common signals

    xa = signal_from_values([-2, 3, -1, 0, 2, 0, -3]).move(-2)
    xb = -3 * d[n + 3] + 2 * u[n - 1]
    xc = u[n + 2] - u[n - 2] - 2 * d[n - 4]
    xd = 2 * u[n + 1] + u[n - 4] - 3 * u[n - 6]
    xe = (n + 22) * u[n + 2]
    xf = (n + 2) * u[n + 2] - (n - 2) * u[n - 2]

    # SignalPlotter.plot(xa, (-5, 5))
    # SignalPlotter.plot(xb, (-5, 5))
    # SignalPlotter.plot(xc, (-5, 5))
    # SignalPlotter.plot(xd, (-2, 10))
    PlotUtils.plot_signal(xe, (-5, 5))
    PlotUtils.plot_signal(xf, (-5, 5))


