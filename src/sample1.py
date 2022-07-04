from core.default_signals import d
from core.signal import n
from core.signal_plot import SignalPlotter

if __name__ == "__main__":
    print(d[0])
    SignalPlotter.plot(d[n-3], (-5, 5))