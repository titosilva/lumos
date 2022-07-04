from core.signal import Signal

class LTISystem:
    def __init__(self, unit_impulse_response: Signal) -> None:
        self.__h = unit_impulse_response

    def __call__(self, signal: Signal):
        return signal ** self.__h