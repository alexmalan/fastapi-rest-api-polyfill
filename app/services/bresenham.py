"""
Brsenham line algorithm.
"""


def bresenham(x0, y0, x1, y1):
    """
    Bresenham's line algorithm.

    Used to draw lines from one point to another.
    Yield integer coordinates on the line from (x0, y0) to (x1, y1).
    Input coordinates should be integers.

    The result will contain both the start and the end point.

    Parameters
    ----------
    x0 : int
        X coordinate of the start position.
    y0 : int
        Y coordinate of the start position.
    x1 : int
        X coordinate of the end position.
    y1 : int
        Y coordinate of the end position.

    Yield
    -------
    list
        List of points that define the line.
    """

    # calculate delta x and delta y
    dx = x1 - x0
    dy = y1 - y0

    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1

    # get abs value of delta x and delta y
    dx = abs(dx)
    dy = abs(dy)

    # compare delta x and delta y
    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0

    D = 2 * dy - dx
    y = 0

    # calculate slope based on P value
    for x in range(dx + 1):
        yield x0 + x * xx + y * yx, y0 + x * xy + y * yy
        if D >= 0:
            y += 1
            D -= 2 * dx
        D += 2 * dy
