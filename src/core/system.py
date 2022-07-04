from core.signal import RealSignal

class LTISystem:
    def __init__(self, unit_impulse_response: RealSignal) -> None:
        self.__h = unit_impulse_response

    def __call__(self, signal: RealSignal):
        return signal ** self.__h