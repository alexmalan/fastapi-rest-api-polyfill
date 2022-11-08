"""
Utils package contains the utility functions.
"""


def bubblesort(arr: list):
    """
    Bubble sort algorithm.
    Algorithn sorts the array by swapping the adjacent elements if they are in wrong order.

    :param alist: list to be sorted
    """
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j].x_min > arr[j + 1].x_min:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp


def arr_to_x_y(arr: list):
    """
    Transforms the array of points to two arrays of x and y coordinates.

    :param arr: array of x, y coordinates
    """
    rows, columns = [], []

    # prepare the x y points
    for i in range(len(arr)):
        rows.append(arr[i][0])
        columns.append(arr[i][1])

    return rows, columns
