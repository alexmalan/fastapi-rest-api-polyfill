"""
Utils package contains the utility functions.
"""


def bubblesort(arr: list) -> list:
    """
    Bubble sort algorithm.
    Algorithn sorts the array by swapping the adjacent elements if they are in wrong order.

    Parameters
    ----------
    arr : list
        Array to sort.
    
    Returns
    -------
    list
        Sorted array.
    
    Raises
    ------
    ValueError
        If the algorithm throws an error.
    """
    try:
        for i in range(len(arr) - 1, 0, -1):
            for j in range(i):
                if arr[j].x_min > arr[j + 1].x_min:
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp
    except Exception as e:
        raise ValueError(f"Something went wrong sorting the array. Please try again. Message: {e}")

def arr_to_x_y(arr: list) -> list and list:
    """
    Transforms the array of points to two arrays of x and y coordinates.

    Parameters
    ----------
    arr : list
        Array of points x, y.

    Returns
    -------
    rows : list
        Array of points y.
    columns : list
        Array of points x.
    
    Raises
    ------
    ValueError
        If the algorithm throws an error.
    """
    try:
        rows, columns = [], []

        # prepare the x y points
        for i in range(len(arr)):
            rows.append(arr[i][0])
            columns.append(arr[i][1])

        return rows, columns
    except Exception as e:
        raise ValueError(f"Something went wrong transforming the array. Please try again. Message: {e}")
