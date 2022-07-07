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

    # X(z) = z**(-1) + z**(-2) + z**(-3) + z**(-4)
    x1 = d[n - 1] + d[n - 2] + d[n - 3] + d[n - 4]
    Hx1 = Z(x1)

    # X(z) = 1 + z**(-1) + z**(-2) + z**(-3)
    x1_v2 = x1[n + 1]
    Hx1_v2 = Z(x1_v2)

    # X(z) = z + 1 + z**(-1) + z**(-2)
    x1_v3 = x1[n + 2]
    Hx1_v3 = Z(x1_v3)

    PlotUtils.plot_many_complex_functions([
        (Hx1, '$x[n]$', limits, limits, None),
        (Hx1_v2, '$x[n + 1]$', limits, limits, None),
        (Hx1_v3, '$x[n + 2]$', limits, limits, None),
        
    ], rows=1, divisions=divisions)

    x1_v4 = signal_from_values([1, 2, -2, 1, -2, 2, 1])
    Hx1_v4 = Z(x1_v4)

    x1_v5 = signal_from_values([0, 1, 2, 3, 4])
    Hx1_v5 = Z(x1_v5)

    x1_v6 = signal_from_values([1, 2, 4, 8, 16])
    Hx1_v6 = Z(x1_v6)

    PlotUtils.plot_many_complex_functions([
        (Hx1_v4, '$Arbitrário$', limits, limits, None),
        (Hx1_v5, '$n (u[n] - u[n-5])$', (-3, 3), (-3, 3), None),
        (Hx1_v6, '$2^n (u[n] - u[n-5])$', (-3, 3), (-3, 3), None),
    ], rows=1, divisions=divisions)

    # Let's test it against the unit step
    PlotUtils.plot_complex_function(Z[u], limits, limits, divisions, lambda z: np.abs(z) > 1, title='$u[n]$')

    x2 = dcos[pi * n / 3] * u[n]
    # Z[...] is also valid
    Hx2 = Z[x2]
    PlotUtils.plot_complex_function(Hx2, limits, limits, divisions, lambda z: np.abs(z) > 1, title='$cos(\\frac{\pi * n}{3}) u[n]')

    a = 0.6 + 0.8j
    x3 = dexp(a) * u[n]
    Hx3 = Z[x3]

    a = 0.6 + 0.8j
    x4 = -1 * dexp(a) * u[-1 * n - 1]
    Hx4 = Z[x4]

    PlotUtils.plot_many_complex_functions([
        (Hx3, '$a^nu[n]$', limits, limits, lambda z: np.abs(z) > np.abs(a)),
        (Hx4, '$-a^nu[-n-1]$', limits, limits, lambda z: np.abs(z) < np.abs(a))
    ], rows=1, divisions=divisions)
