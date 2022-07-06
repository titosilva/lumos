from math import ceil, floor
from typing import Callable, Dict, List, Tuple
from matplotlib.colors import hsv_to_rgb
import matplotlib.pyplot as plt
import numpy as np

from core.signal import Signal

class PlotUtils:
    @staticmethod
    def plot_signal(signal: Signal, limits: Tuple[int, int]):
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
        ax.set_yticks(range(floor(y_lower_lim), ceil(y_upper_lim)))
        ax.grid(True)

        plt.show()

    @staticmethod
    def plot_many_signals(signal_plots: List[Tuple[Signal, str, Tuple[int, int]]], rows: int):
        subplot_idx = 0
        _, axs = plt.subplots(rows, len(signal_plots) // rows)

        for signal_plot in signal_plots:
            signal, title, limits = signal_plot
            ax = axs[subplot_idx]

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
            ax.set_yticks(range(floor(y_lower_lim), ceil(y_upper_lim)))
            ax.grid(True)
            ax.set_title(title)

            subplot_idx += 1

        plt.show()

    @staticmethod
    def compute_complex_at_grid(fn, re_lim: Tuple[float, float], im_lim: Tuple[float, float],  N: int, area_def: Callable[[complex], bool] = None):
        #evaluates the complex function at the nodes of the grid
        # N is the number of discrete points per unit interval 
        
        l = re_lim[1]-re_lim[0]
        h = im_lim[1]-im_lim[0]
        resL = N * l # horizontal resolution
        resH = N * h # vertical resolution
        x = np.linspace(re_lim[0], re_lim[1], int(resL))
        y = np.linspace(im_lim[0], im_lim[1], int(resH))
        x, y = np.meshgrid(x,y)
        z = x + 1j*y

        if area_def is not None:
            result = fn(z)
            area = area_def(z)
            return result * area

        return fn(z)

    @staticmethod
    def compute_hue_from_complex(z: complex):
        # computes the hue corresponding to the complex number z
        H = np.angle(z) / (2*np.pi) + 1
        return np.mod(H, 1)

    @staticmethod
    def classical_domain_colouring(w, s, max_mod: float = None):
        # w is the  array of values f(z)
        # s is the constant saturation
        
        H = PlotUtils.compute_hue_from_complex(w)
        S = s * np.ones(H.shape)
        modul = np.absolute(w)

        if max_mod is not None:
            modul[modul > max_mod] = 0

        V = (1.0-1.0/(1+modul**2))**0.2
        # the points mapped to infinity are colored with white; hsv_to_rgb(0, 0, 1)=(1, 1, 1)=white

        HSV = np.dstack((H, S, V))
        RGB = hsv_to_rgb(HSV)
        return RGB

    @staticmethod
    def plot_complex_function(
        fn: Callable[[complex], complex], 
        re_lim: Tuple[float, float], 
        im_lim: Tuple[float, float], 
        divisions: int = 100,
        area_def: Callable[[complex], bool] = None):

        w = PlotUtils.compute_complex_at_grid(fn, re_lim, im_lim, divisions, area_def)
        domc = PlotUtils.classical_domain_colouring(w, 0.9)
        plt.xlabel("$\Re(z)$")
        plt.ylabel("$\Im(z)$")
        plt.imshow(domc, origin="lower", extent=[re_lim[0], re_lim[1], im_lim[0], im_lim[1]])

        plt.tight_layout()
        plt.show()
