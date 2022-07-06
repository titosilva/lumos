from cmath import pi
from core.plot_utils import PlotUtils
from core.transforms import Z
from core.signal import n
from core.default_signals import d, dexp, dsin, signal_from_values, u, dcos
import numpy as np

if __name__ == "__main__":
    limits = (-1.5, 1.5)

    # An increase in this number improves the resolution
    # but also increases the plotting time
    divisions = 200 

    x1 = d[n - 1] + d[n - 2] + d[n - 3] + d[n - 4]
    # X1(z) = z + z ** 2 + z ** 3 + z ** 4
    Hx1 = Z(x1)
    # PlotUtils.plot_complex_function(Hx1, limits, limits, divisions)

    x1_v2 = signal_from_values([0, 1, 1, 1, 1])
    Hx1_v2 = Z(x1_v2)
    # PlotUtils.plot_complex_function(Hx1_v2, limits, limits, divisions)

    # Let's test it against the unit step
    # PlotUtils.plot_complex_function(Z[u], limits, limits, divisions, lambda z: np.abs(z) > 1)

    x2 = dcos[pi * n / 3] * u[n]
    # Z[...] is also valid
    Hx2 = Z[x2]
    # PlotUtils.plot_complex_function(Hx2, limits, limits, divisions, lambda z: np.abs(z) > 1)

    a = 0.6 + 0.8j
    x3 = dexp(a) * u[n]
    Hx3 = Z[x3]
    # PlotUtils.plot_complex_function(Hx3, limits, limits, divisions, lambda z: np.abs(z) > np.abs(a))

    a = 0.6 + 0.8j
    x4 = -1 * dexp(a) * u[-1 * n - 1]
    Hx4 = Z[x4]
    # PlotUtils.plot_complex_function(Hx4, limits, limits, divisions, lambda z: np.abs(z) < np.abs(a))

    PlotUtils.plot_many_complex_functions([
        (Hx3, '$a^nu[n]$', limits, limits, lambda z: np.abs(z) > np.abs(a)),
        (Hx4, '$-a^nu[-n-1]$', limits, limits, lambda z: np.abs(z) < np.abs(a))
    ], rows=1, divisions=divisions)
