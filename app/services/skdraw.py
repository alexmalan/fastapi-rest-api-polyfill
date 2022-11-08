"""
SkDraw algorithm.
"""
from skimage.draw import polygon


def fill_polygon_fast(nparr: "nparray", rows: list, columns: list) -> "nparray":
    """
    Fill a polygon defined by a list of points.

    Parameters
    ----------
    nparr : nparray
        Array of points that define the filled polygon.
    rows : list
        Row coordinates of vertices of polygon.
    columns : list
        Column coordinates of vertices of polygon.

    Returns
    -------
    numpy.ndarray
        Array of points that define the filled polygon.

    Raises
    ------
    ValueError
        If there is an error within the algorithm execution.
    """
    try:
        row_values, column_values = polygon(rows, columns)
        nparr[row_values, column_values] = 1

        return nparr
    except Exception as e:
        raise ValueError(
            f"Something went wrong filling the polygon. Please try again. Message: {e}"
        )
