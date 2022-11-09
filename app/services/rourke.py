"""
Rourke inside/outside algorithm.
"""
import math

import numpy as np


def point_in_polygons(
    column_points: "nparray", row_points: "nparray", column_i: int, row_i: int
) -> int:
    """
    Test relative point position to a polygon.

    Parameters
    ----------
    column_points : nparray
        Array of x coordinates of the polygon.
    row_points : nparray
        Array of y coordinates of the polygon.
    column_i : int
        X coordinate of the point.
    row_i : int
        Y coordinate of the point.

    Returns
    -------
    c : int
        Point relative position to the polygon.
        O: outside.
        1: inside.
        2: vertex.
        3: edge.

    Raises
    ------
    ValueError
        If there is an error within the algorithm execution.
    """
    try:
        nr_vertices = column_points.shape[0]

        x0 = np.float64(0.0)
        x1 = np.float64(0.0)
        y0 = np.float64(0.0)
        y1 = np.float64(0.0)

        l_cross = 0
        r_cross = 0

        # Tolerance for vertices labelling
        eps = 1e-12

        # Initialization the loop
        x1 = column_points[nr_vertices - 1] - column_i
        y1 = row_points[nr_vertices - 1] - row_i

        # For each edge e = (i-1, i), see if it crosses ray
        for vertice in range(nr_vertices):
            x0 = column_points[vertice] - column_i
            y0 = row_points[vertice] - row_i

            if (-eps < x0 < eps) and (-eps < y0 < eps):
                # it is a vertex with an eps tolerance.
                # if the point is a vertex, it is inside the polygon
                # and you check if the point is on the same point so to speak
                # that is why the tolerance is used
                return 2

            # if e straddles the x-axis
            if (y0 > 0) != (y1 > 0):
                # check if it crosses the ray
                if ((x0 * y1 - x1 * y0) / (y1 - y0)) > 0:
                    r_cross += 1
            # if reversed e straddles the x-axis
            if (y0 < 0) != (y1 < 0):
                # check if it crosses the ray
                if ((x0 * y1 - x1 * y0) / (y1 - y0)) < 0:
                    l_cross += 1

            x1 = x0
            y1 = y0

        if (r_cross & 1) != (l_cross & 1):
            # on edge if left and right crossings not of same parity
            return 3

        if r_cross & 1:
            # inside if odd number of crossings.
            # if r_cross is odd, this will be true
            return 1

        # outside if even number of crossings
        return 0
    except Exception as e:
        raise ValueError(f"Error in point_in_polygons: {e}")


def fill_polyline_rourke(row: list, column: list, nparr: "nparray") -> "nparray":
    """
    Generate coordinates of pixels within polygon.

    Parameters
    ----------
    row : list
        Row coordinates of vertices of polygon.
    column : list
        Column coordinates of vertices of polygon.
    nparr : nparray
        Array of points that define the filled polygon.

    Returns
    -------
    nparr : numpy.ndarray
        Array of points that define the filled polygon.

    Raises
    ------
    ValueError
        If there is an error within the algorithm execution.
    """
    try:
        # check dimension of array
        rows = np.atleast_1d(row)
        columns = np.atleast_1d(column)

        # check minimum and maximum row and column values
        min_row = int(max(0, rows.min()))
        max_row = int(math.ceil(rows.max()))
        min_column = int(max(0, columns.min()))
        max_column = int(math.ceil(columns.max()))

        # make contiguous arrays of row and column coordinates
        # faster access in memory if they are next to each other
        row_points = np.ascontiguousarray(rows, "float64")
        column_points = np.ascontiguousarray(columns, "float64")

        # define output coordinate arrays
        row_coord_output = []
        column_coord_output = []

        # verify points in polygon
        for row_i in range(min_row, max_row + 1):
            for column_i in range(min_column, max_column + 1):
                # valid for 1, 2, 3
                if point_in_polygons(column_points, row_points, column_i, row_i):
                    row_coord_output.append(row_i)
                    column_coord_output.append(column_i)
        nparr[row_coord_output, column_coord_output] = 1

        return nparr
    except Exception as e:
        raise ValueError(f"Error in Rourke algorithm: {e}")
