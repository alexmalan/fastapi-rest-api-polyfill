"""
File management service.
"""
from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt
from numpy import save

from .utils import arr_to_x_y


def save_nparray_to_file(nparray: "nparray", filename: str):
    """
    Save numpy array to file.

    Parameters
    ----------
    nparray : nparray
        Numpy array to save.
    filename : str
        The filename to save the numpy array to.
    """
    try:
        loc_path = Path(__file__).parents[1] / f"data/{filename}"

        # save the numpy array to the npy file
        save(loc_path, nparray)
        loc_path = loc_path.with_suffix(".npy")

        return loc_path
    except:
        raise ValueError("Something went wrong saving the file. Please try again.")


def save_matplot_figure(nparr: "nparray", filename: str, points: list):
    """
    Save matplotlib figure to file.

    Parameters
    ----------
    nparr : nparray
        Numpy array to save.
    filename : str
        The filename to save the plot to.
    """
    try:
        loc_path = Path(__file__).parents[1] / f"data/{filename}-plot.png"
        rows, columns = arr_to_x_y(points)

        plt.clf()
        poly_check = np.where(nparr == 1)
        plt.plot(poly_check[0], poly_check[1])

        plt.plot(rows, columns, "bo-")
        count = 1
        # zip joins x and y coordinates in pairs
        for x, y in zip(rows, columns):
            plt.annotate(
                f"{count} ({x}, {y})",  # this is the text
                (x, y),  # these are the coordinates to position the label
                textcoords="offset points",  # how to position the text
                xytext=(0, 10),  # distance from text to points (x,y)
                ha="center",
            )  # horizontal alignment can be left, right or center
            count += 1
        plt.savefig(loc_path)
        plt.close()

        return loc_path
    except:
        raise ValueError("Something went wrong saving the file. Please try again.")
