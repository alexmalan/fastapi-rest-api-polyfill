"""
File management service.
"""
from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt
from numpy import save


def save_nparray_to_file(nparray, filename):
    """
    Save numpy array to file.

    params numpy.ndarray nparray: The numpy array to save.
    params str filename: The filename to save the numpy array to.
    """
    loc_path = Path(__file__).parents[1] / f"data/{filename}"
    try:
        save(loc_path, nparray)
        loc_path = loc_path.with_suffix(".npy")

        return loc_path
    except:
        raise ValueError("Something went wrong saving the file. Please try again.")


def save_matplot_figure(nparr, filename):
    """
    Save matplotlib figure to file.

    params nparr nparray: nparray to save.
    params str filename: The filename to save the matplotlib figure to.
    """
    loc_path = Path(__file__).parents[1] / f"data/{filename}-plot.png"
    try:
        poly_check = np.where(nparr == 1)
        plt.plot(poly_check[0], poly_check[1])
        plt.savefig(loc_path)

        return loc_path
    except:
        raise ValueError("Something went wrong saving the file. Please try again.")
