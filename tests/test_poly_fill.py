"""
Poly service tests.
"""
from fastapi.testclient import TestClient

from app.services import fill_polygon
from main import app

client = TestClient(app)


def test_rectangle():
    """
    Testing a rectangle shape within the np.array

    0 0 0 0 0 0 0 0 0 0 0 0 0 ...
    0 1 1 1 1 1 1 0 0 0 0 0 0 ...
    0 1 1 1 1 1 1 0 0 0 0 0 0 ...
    0 1 1 1 1 1 1 0 0 0 0 0 0 ...
    0 1 1 1 1 1 1 0 0 0 0 0 0 ...
    0 1 1 1 1 1 1 0 0 0 0 0 0 ...
    0 0 0 0 0 0 0 0 0 0 0 0 0 ...
    .............................

    shape = (19200, 10800)
    """
    points = [[1, 1], [1, 5], [5, 5], [5, 1]]
    result = fill_polygon(10, 10, points)

    assert result[0].shape == (10, 10)
    assert (0 in result[0][0][1:6]) == True
    assert (0 in result[0][1][1:6]) == False
    assert (0 in result[0][2][1:6]) == False
    assert (0 in result[0][3][1:6]) == False
    assert (0 in result[0][4][1:6]) == False
    assert (0 in result[0][5][1:6]) == False
    assert (0 in result[0][6][1:6]) == True


def test_triangle():
    """
    Testing a triangle shape within the np.array

    0 0 0 0 0 0 0 0 0 0 0 0 0 ...
    0 1 0 0 0 0 0 0 0 0 0 0 0 ...
    0 1 1 0 0 0 0 0 0 0 0 0 0 ...
    0 1 1 1 0 0 0 0 0 0 0 0 0 ...
    0 1 1 1 1 0 0 0 0 0 0 0 0 ...
    0 1 1 1 1 1 0 0 0 0 0 0 0 ...
    0 0 0 0 0 0 0 0 0 0 0 0 0 ...
    .............................

    shape = (19200, 10800)
    """
    points = [[1, 1], [5, 5], [5, 1]]
    result = fill_polygon(19200, 10800, points)

    assert result[0].shape == (19200, 10800)
    assert (0 in result[0][0][1:6]) == True
    assert (0 in [result[0][1][1]]) == False
    assert (0 in result[0][2][1:2]) == False
    assert (0 in result[0][3][1:3]) == False
    assert (0 in result[0][4][1:4]) == False
    assert (0 in result[0][5][1:5]) == False
    assert (0 in result[0][6][1:6]) == True
