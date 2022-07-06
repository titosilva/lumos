from cmath import pi
from core.signal_plot import SignalPlotter
from core.transforms import Z
from core.signal import n
from core.default_signals import d, dexp, dsin, u, dcos
import numpy as np

if __name__ == "__main__":
    limits = (-1.5, 1.5)

    # An increase in this number improves the resolution
    # but also increases the plotting time
    divisions = 200 

    x1 = d[n - 1] + d[n - 2] + d[n - 3] + d[n - 4]
    Hx1 = Z(x1)
    SignalPlotter.plot_complex_function(Hx1, limits, limits, divisions)

    # Let's test it against the unit step
    SignalPlotter.plot_complex_function(Z[u], limits, limits, divisions, lambda z: np.abs(z) > 1)

    x2 = dcos[pi * n / 3] * u[n]
    # Z[...] is also valid
    Hx2 = Z[x2]
    SignalPlotter.plot_complex_function(Hx2, limits, limits, divisions, lambda z: np.abs(z) > 1)

    a = 0.6 + 0.8j
    x3 = dexp(a) * u[n]
    Hx3 = Z[x3]
    SignalPlotter.plot_complex_function(Hx3, limits, limits, divisions, lambda z: np.abs(z) > np.abs(a))

    a = 0.6 + 0.8j
    x4 = -1 * dexp(a) * u[-1 * n - 1]
    Hx4 = Z[x4]
    SignalPlotter.plot_complex_function(Hx4, limits, limits, divisions, lambda z: np.abs(z) < np.abs(a))
