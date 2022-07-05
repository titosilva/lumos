from numpy import sign
from core.default_signals import signal_from_values, d, u
from core.signal_plot import SignalPlotter
from core.system import LTISystem
from core.signal import n

if __name__ == "__main__":
    Td = LTISystem(d)
    SignalPlotter.plot(Td(u), (-5, 5))

    Tu = LTISystem(u)
    SignalPlotter.plot(Tu(d), (-5, 5))

    T9 = LTISystem(signal_from_values([1, 2, 1, -2]))
    x9 = (u - u[n - 5]) * 3
    SignalPlotter.plot(T9(x9), (-5, 15))

    T10 = LTISystem(signal_from_values([0, 1, 2, 3]))
    x10 = (signal_from_values([-2, -1, 0, 1, 2]))[n + 2]
    SignalPlotter.plot(T10(x10), (-5, 15))

    T11 = LTISystem(signal_from_values([0, 2, 1, -4]))
    x1 = signal_from_values([0, 1, 2, 3, 2, 1, 0])[n + 3]
    SignalPlotter.plot(T11(x9), (-5, 15))

    h12 = signal_from_values([1, 1, 1, -1, -1])[n + 2]
    T12 = LTISystem(h12)
    x12 = signal_from_values([3, 3, -2, -2])[n + 1]
    SignalPlotter.plot(T12(x12), (-5, 15))

