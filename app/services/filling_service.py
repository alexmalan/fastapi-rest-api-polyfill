"""
Polygon filling service.
"""
from datetime import datetime

import numpy as np

from .boundary import flood_fill_4
from .bresenham import bresenham
from .rourke import fill_polyline_rourke
from .scanline import fill_polygon_scanline
from .skdraw import fill_polygon_fast
from .utils import arr_to_x_y


def fill_polyline(polygon_points, algorithm, flood_x=None, flood_y=None):
    """
    Method for handling algorithm selection.

    Parameters
    ----------
    arr : list
        Array of points that define the polygon.
    algorithm : str
        Algorithm to use for filling the polygon.

    Returns
    -------
    numpy.ndarray
        Array of points that define the filled polygon.
    execution_time : float
        Time taken to fill and process the polygon.
    """
    nparr = np.zeros((19200, 10800), dtype=np.uint8)

    if algorithm in ["rourke", "fast", "scanline"]:
        start_time = datetime.now()
        rows, columns = arr_to_x_y(polygon_points)

        if algorithm == "rourke":
            result = fill_polyline_rourke(rows, columns, nparr)
        if algorithm == "fast":
            result = fill_polygon_fast(nparr, rows, columns)
        if algorithm == "scanline":
            result = fill_polygon_scanline(rows, columns)

        end_time = datetime.now()
        execution_time = (end_time - start_time).total_seconds()

        return (result, execution_time)
    elif algorithm == "flood":
        start_time = datetime.now()
        fill_points = []
        polygon_points.append(polygon_points[0])

        # apply bresemham's line algorithm to each pair of points
        for i in range(len(polygon_points) - 1):
            fill_points.extend(
                list(
                    bresenham(
                        polygon_points[i][0],
                        polygon_points[i][1],
                        polygon_points[i + 1][0],
                        polygon_points[i + 1][1],
                    )
                )
            )

        # Fill the points
        xarr, yarr = [], []
        for i in fill_points:
            nparr[i[0]][i[1]] = 1
            xarr.append(i[0])
            yarr.append(i[1])

        if flood_x and flood_y:
            flood_fill_4(flood_x, flood_y, 0, 1, nparr)
        else:
            # find the latter points of the polygon
            min_x = min(xarr)
            max_x = max(xarr)
            min_y = min(yarr)
            max_y = max(yarr)

            # compute the center of the polygon
            x_start = max_x - (max_x - min_x)
            y_start = max_y - (max_y - min_y)

            # Fill the polygon recursively
            flood_fill_4(x_start, y_start, 0, 1, nparr)

        end_time = datetime.now()
        execution_time = (end_time - start_time).total_seconds()
        return (nparr, execution_time)
    else:
        raise ValueError("Invalid algorithm.")
