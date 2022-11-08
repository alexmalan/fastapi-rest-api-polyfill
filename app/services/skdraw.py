"""
SkDraw algorithm.
"""
from skimage.draw import polygon


def fill_polygon_fast(nparr, rows, columns):
    """
    Fill a polygon defined by a list of points.

    Parameters
    ----------
    points : list of tuples
        List of points that define the polygon.

    Returns
    -------
    numpy.ndarray
        Array of points that define the filled polygon.

    """
    try:
        row_values, column_values = polygon(rows, columns)
        nparr[row_values, column_values] = 1

        return nparr
    except:
        raise ValueError("Something went wrong filling the polygon. Please try again.")
