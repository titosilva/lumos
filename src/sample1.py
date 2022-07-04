from core.default_signals import d, u
from core.signal import n
from core.signal_plot import SignalPlotter

if __name__ == "__main__":
    # You can easily define a signal by using the 'n' imported from core.signal
    x1 = n * 2 + 2
    # You may apply the signal to an input and see the results
    print(f"x[2] = {x1[2]}")
    # You may also plot a signal and see its shape
    SignalPlotter.plot(x1, (-5, 5))

    # A nice way to define complex signals is by using 'constructing blocks'
    # Some basic signals are defined on core.default_signals and may be used 
    # 'u' is an alias to unit_step and 'd' is an alias to unit_impulse
    x2 = u[n] - u[n-4] - 0.5 * d[n-1]
    # You may also add the '[n]' after a signal, if you want to
    SignalPlotter.plot(x2[n], (-5, 5))