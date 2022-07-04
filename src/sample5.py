from cmath import pi
from core.signal_plot import SignalPlotter
from core.transforms import Z
from core.signal import n
from core.default_signals import d, dsin, u, dcos

if __name__ == "__main__":
    limits = (-1.5, 1.5)

    # An increase in this number improves the resolution
    # but also increases the plotting time
    divisions = 200 

    x = d[n - 1] + d[n - 2] + d[n - 3] + d[n - 4]
    Hx = Z(x)
    SignalPlotter.plot_complex_function(Hx, limits, limits, divisions = divisions)

    # Let's test it against the unit step
    SignalPlotter.plot_complex_function(Z[u], limits, limits, divisions = divisions)

    x2 = dsin[pi * n / 2 - 3]
    # Z[...] is also valid
    Hx2 = Z[x2]
    SignalPlotter.plot_complex_function(Hx2, limits, limits, divisions = divisions)

    x3 = dcos[pi * n / 2]
    # Z[...] is also valid
    Hx3 = Z[x3]
    SignalPlotter.plot_complex_function(Hx3, limits, limits, divisions = divisions)