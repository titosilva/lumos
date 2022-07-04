from core.signal import Signal

class LTISystem:
    def __init__(self, unit_impulse_response: Signal) -> None:
        self.unit_impulse_response = unit_impulse_response

    def __call__(self, signal: Signal):
        return signal ** self.unit_impulse_response