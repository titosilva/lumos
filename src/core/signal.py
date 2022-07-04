from typing import Any, Callable

class RealSignal:
    def __init__(self, fn: Callable[[int], float], convolution_limits = (-1000, 1000)):
        self.__fn = fn
        self.__conv_limits = convolution_limits

    def __call__(self, n: int):
        return self.__fn(n)

    def __add__(self, number_or_func):
        if callable(number_or_func):
            return RealSignal(lambda n: self(n) + number_or_func(n))
        return RealSignal(lambda n: self(n) + number_or_func)
    
    def __sub__(self, number_or_func):
        if callable(number_or_func):
            return RealSignal(lambda n: self(n) - number_or_func(n))
        return RealSignal(lambda n: self(n) - number_or_func)

    def __mul__(self, number_or_func: Any):
        if callable(number_or_func):
            return RealSignal(lambda n: self(n) * number_or_func(n))
        else:
            return RealSignal(lambda n: self(n) * number_or_func)

    def __rmul__(self, number_or_func: Any):
        if callable(number_or_func):
            return RealSignal(lambda n: self(n) * number_or_func(n))
        else:
            return RealSignal(lambda n: self(n) * number_or_func)

    def __pow__(self, number_or_func):
        if callable(number_or_func):
            fn = lambda n: sum(self(m) * number_or_func(n - m) for m in range(self.__conv_limits[0], self.__conv_limits[1]))
            return RealSignal(fn)
        else:
            return RealSignal(lambda n: self(n) ** number_or_func)

    def __getitem__(self, number_or_func):
        if callable(number_or_func):
            fn = lambda n: self(number_or_func(n))
            return RealSignal(fn)
        else:
            return self(number_or_func)

    def move(self, d: int):
        return RealSignal(lambda n: self(n - d))

def signal_argument():
    return RealSignal(lambda n: n)

n = signal_argument()
