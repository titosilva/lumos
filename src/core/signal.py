from subprocess import call
from typing import Any, Callable

class Signal:
    def __init__(self, fn: Callable[[int], complex], convolution_limits = (-1000, 1000)):
        self._fn = fn
        self._conv_limits = convolution_limits

    def __call__(self, number_or_func) -> complex:
        if callable(number_or_func):
            fn = lambda n: self(number_or_func(n))
            return Signal(fn)
        else:
            return self._fn(number_or_func)

    def __add__(self, number_or_func):
        if hasattr(self.__class__, '__fastadd__') and callable(getattr(self.__class__, '__fastadd__')):
            return self.__fastadd__(number_or_func)

        if callable(number_or_func):
            return Signal(lambda n: self(n) + number_or_func(n))
        return Signal(lambda n: self(n) + number_or_func)
    
    def __sub__(self, number_or_func):
        if hasattr(self.__class__, '__fastsub__') and callable(getattr(self.__class__, '__fastsub__')):
            return self.__fastsub__(-1 * number_or_func)

        if callable(number_or_func):
            return Signal(lambda n: self(n) - number_or_func(n))
        return Signal(lambda n: self(n) - number_or_func)

    def __mul__(self, number_or_func: Any):
        if hasattr(self.__class__, '__fastmul__') and callable(getattr(self.__class__, '__fastmul__')):
            return self.__fastmul__(number_or_func)

        if callable(number_or_func):
            return Signal(lambda n: self(n) * number_or_func(n))
        else:
            return Signal(lambda n: self(n) * number_or_func)

    __rmul__ = __mul__

    def __pow__(self, number_or_func):
        if callable(number_or_func):
            return self.conv(number_or_func)
        else:
            return Signal(lambda n: self(n) ** number_or_func)
        
    def conv(self, func):
        if hasattr(self, '__fastconv__') and callable(getattr(self, '__fastconv__')):
            return self.__fastconv__(func)

        fn = lambda n: sum(self(m) * func(n - m) for m in range(self._conv_limits[0], self._conv_limits[1] + 1))
        return Signal(fn)
        

    def __truediv__(self, number_or_func):
        if callable(number_or_func):
            return Signal(lambda n: self(n) / number_or_func(n))
        else:
            return Signal(lambda n: self(n) / number_or_func)

    __getitem__ = __call__

    def move(self, d: int):
        return Signal(lambda n: self(n - d))

def signal_argument():
    return Signal(lambda n: n)

n = signal_argument()
