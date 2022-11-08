"""
Boundary 4-way algorithm.
"""


def flood_fill_4(x, y, old, new, arr):
    """
    Flood fill algorithm for 4-connected pixels.

    Parameters
    ----------
    x : int
        X coordinate of the start position.
    y : int
        Y coordinate of the start position.
    old : int
        Old value.
    new : int
        New value.
    arr : numpy.ndarray
        Array of points that define the filled polygon.
    """
    # the flood fill has 4 parts
    # firstly, make sure the x and y are inbounds
    if x < 0 or x >= len(arr[0]) or y < 0 or y >= len(arr):
        return

    # secondly, check if the current position equals the old value
    if arr[y][x] != old:
        return

    # thirdly, set the current position to the new value
    arr[y][x] = new

    # fourthly, attempt to fill the neighboring positions
    flood_fill_4(x + 1, y, old, new, arr)
    flood_fill_4(x - 1, y, old, new, arr)
    flood_fill_4(x, y + 1, old, new, arr)
    flood_fill_4(x, y - 1, old, new, arr)
