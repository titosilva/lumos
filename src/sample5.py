from cmath import pi
from core.signal_plot import SignalPlotter
from core.transforms import Z
from core.signal import n
from core.default_signals import d, dsin, u

if __name__ == "__main__":
    x = d[n - 1] + d[n - 2] + d[n - 3] + d[n - 4]
    Hx = Z(x)
    SignalPlotter.plot_complex_function(Hx, (-5, 5), (-5, 5), divisions = 50)

    SignalPlotter.plot_complex_function(Z[u], (-5, 5), (-5, 5), divisions = 50)

    x2 = dsin[pi * n / 2 - 3]
    # Z[...] is also valid
    Hx2 = Z[x2]
    SignalPlotter.plot_complex_function(Hx2, (-5, 5), (-5, 5), divisions = 50)