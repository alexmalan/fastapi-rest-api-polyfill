"""
Polygon filling service.
"""
from datetime import datetime

import numpy as np
from skimage.draw import polygon


def fill_polygon(x_shape, y_shape, polygon_points):
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
        nparr = np.zeros((x_shape, y_shape), dtype=np.uint8)
        rows, columns = [], []

        for i in range(len(polygon_points)):
            rows.append(polygon_points[i][0])
            columns.append(polygon_points[i][1])

        start_time = datetime.now()
        row_values, column_values = polygon(rows, columns)
        nparr[row_values, column_values] = 1
        end_time = datetime.now()
        exec_time = end_time - start_time

        return (nparr, exec_time.total_seconds())
    except:
        raise ValueError("Something went wrong filling the polygon. Please try again.")
