from typing import Tuple
from core.default_signals import signal_from_values, d, u
from core.operations import dot
from core.signal import n

from core.signal import Signal
from core.system import LTISystem

def build_predefined_signals() -> Tuple[Signal, Signal, Signal, Signal]:
    return (
        signal_from_values([0, 1, 2, 3, 2, 1, 0]).move(-3),
        signal_from_values([1, 0.5, 1, 1]),
        signal_from_values([1, 1, 1, -1, -1]).move(-3),
        signal_from_values([3, 3, 3, 3, 3])
    )

def run_sample_1():
    '''
    Carries out operations on the predefined signals
    '''
    x_1, x_2, x_3, x_4 = build_predefined_signals()

    # (a) w[n] = x_2[n] - x_4[n - 2]
    w_a = x_2[n] - x_4[n - 2]

    # (b) w[n] = - x_3[n - 1] * x_1[n + 1]
    w_b = - x_3[n - 1] * x_1[n + 1]

    # (c) w[n] = x_2[n] * x_3[n - 1] + x_1[n]
    w_c = x_2[n] * x_3[n - 1] + x_1[n]

def run_sample_2():
    '''
    Computes the dot product over signals defined with the predefined signals
    '''
    x_1, x_2, x_3, x_4 = build_predefined_signals()

    # (a) <x_1[n - 1] . x_2[n + 1]>
    x_a1 = x_1[n - 1],
    x_a2 = x_2[n + 1]
    print(f'<x_1[n - 1] . x_2[n + 1]> = {dot(x_a1, x_a2)}')

    # (b) <-x_3[n - 2] . x_4[n]>
    x_b1 = -x_3[n - 2]
    x_b2 = x_4[n]
    print(f'<-x_3[n - 2] . x_4[n]> = {dot(x_b1, x_b2)}')

    # (c) <x_1[n] . x_4[n]>
    x_c1 = x_1[n]
    x_c2 = x_4[n]
    print(f'<x_1[n] . x_4[n]> = {dot(x_c1, x_c2)}')

    # (d) <x_1[n - 2] . x_4[n]>
    x_d1 = x_1[n - 2]
    x_d2 = x_4
    print(f'<x_1[n - 2] . x_4[n]> = {dot(x_d1, x_d2)}')

def run_sample_4():
    '''
    Plots signals defined with the basic signals (u[n], d[n])
    '''

    # (a) x_a[n] = -2 * d[n + 2] + 3 * d[n + 1] - d[n] + 2 * d[n-2] - 3 * d[n-4]
    x_a = -2 * d[n + 2] + 3 * d[n + 1] - d[n] + 2 * d[n-2] - 3 * d[n-4]

    # (b) x_b[n] = -3 * d[n + 3] + 2 * u[n - 1]
    x_b = -3 * d[n + 3] + 2 * u[n - 1]

    # (c) x_c[n] = u[n + 2] - u[n - 2] - 2 * d[n - 4]
    x_c = u[n + 2] - u[n - 2] - 2 * d[n - 4]

    # (d) x_d[n] = 2 * u[n - 1] + u[n - 4] - 3 * u[n - 6]
    x_d = 2 * u[n - 1] + u[n - 4] - 3 * u[n - 6]

    # (e) x_e[n] = (n + 22) * u[n + 2]
    x_e = (n + 22) * u[n + 2]

    # (f) x_f[n] = (n + 2) * u[n + 2] - (n - 2) * u[n - 2]
    x_f = (n + 2) * u[n + 2] - (n - 2) * u[n - 2]

def run_sample_9():
    '''
    Determines the response of a LTI System to a signal based on its impulse response
    '''
    x_1, x_2, x_3, x_4 = build_predefined_signals()

    h = signal_from_values([1, 2, 1, -2])
    T = LTISystem(h)

    x = x_4
    y = T(x)

def run_sample_10():
    '''
    Determines the response of a LTI System to a signal based on its impulse response
    '''
    h = signal_from_values([0, 1, 2, 3])
    T = LTISystem(h)

    x = signal_from_values([-2, -1, 0, 1, 2])
    y = T(x)

def run_sample_11():
    '''
    Determines the response of a LTI System to a signal based on its impulse response
    '''
    x_1, x_2, x_3, x_4 = build_predefined_signals()

    h = signal_from_values([0, 2, 1, -4])
    T = LTISystem(h)

    x = x_1
    y = T(x)

def run_sample_12():
    '''
    Determines the response of a LTI System to a signal based on its impulse response
    '''
    x_1, x_2, x_3, x_4 = build_predefined_signals()

    h = x_3
    T = LTISystem(h)

    x = signal_from_values([3, 3, -2, -2]).move(-1)
    y = T(x)


