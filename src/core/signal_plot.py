from typing import Tuple
import matplotlib.pyplot as plt

from core.signal import Signal

class SignalPlotter:
    @staticmethod
    def plot(signal: Signal, limits: Tuple[int, int]):
        fig, ax = plt.subplots()

        x_points = []
        y_points = []

        for n in range(limits[0], limits[1] + 1):
            x_points.append(n)
            y = signal(n)

            if y.imag != 0:
                raise Exception("Plotting complex signals not yet supported :(")

            y_points.append(y.real)

        y_lower_lim = min(min(y_points) - 1, 0)
        y_upper_lim = max(max(y_points) + 1, 0)
        x_lower_lim = limits[0] - 1
        x_upper_lim = limits[1] + 1
        
        ax.hlines(0, limits[0] - 1, limits[1] + 1, colors=['black'])
        ax.vlines(0, min(y_points) - 1, max(y_points) + 1, colors=['black'])
        ax.set(xlim = (x_lower_lim, x_upper_lim), ylim=(y_lower_lim, y_upper_lim))
        ax.stem(x_points, y_points, basefmt=" ")
        ax.set_xticks(range(x_lower_lim, x_upper_lim))
        ax.set_yticks(range(y_lower_lim, y_upper_lim))
        ax.grid(True)

        plt.show()