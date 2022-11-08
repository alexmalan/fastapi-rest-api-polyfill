"""
Scanline algorithm for polygon filling.
"""
import math

import numpy as np

from .utils import bubblesort


class EdgeTable:
    """
    Class for the list of nodes.
    """
    def __init__(self, max_y):
        self.list = []
        for i in range(0, max_y):
            self.list.append(None)

    def add(self, scanline, node):
        """
        Add a node to the list.

        Parameters
        ----------
        scanline : int
            Scanline to add the node to.
        node : Node
            Node to add to the list.
        """
        if self.list[scanline] is None:
            self.list[scanline] = node
        else:
            actualnode = self.list[scanline]
            while actualnode.nextTA is not None:
                actualnode = actualnode.nextTA
            actualnode.nextTA = node
            node.nextTA = None

    def delete(self, scanline, node):
        """
        Remove a node from the list.

        Parameters
        ----------
        scanline : int
            Scanline to remove the node from.
        node : Node
            Node to remove.
        """
        prevnode = None
        currnode = self.list[scanline]

        if currnode is not None:  # if the node is not null
            while currnode.nextTA is not None:  # while currnode is not the last node
                if currnode == node:
                    if prevnode is None:  # if currnode is first
                        if (
                            currnode.nextTA is not None
                        ):  # if the first node is not last node
                            self.list[scanline] = currnode.nextTA
                    else:  # if is a middle node
                        prevnode.nextTA = currnode.nextTA
                prevnode = currnode
                currnode = currnode.nextTA

            # when its last node
            if currnode == node and currnode.nextTA is None:
                if prevnode is None:  # if it is the first node
                    self.list[scanline] = None
                else:
                    prevnode.nextTA = None

    def first_y(self):
        """
        Returns the first y value in the list.

        Returns
        -------
        int
            First y value in the list.
        """
        for i in range(0, len(self.list)):
            item = self.list[i]
            if item is not None:
                return i

    def isEmpty(self):
        """
        Check if the list is empty.

        Returns
        -------
        bool
            True if the list is empty, False otherwise.
        """
        for item in self.list:
            if item is not None:
                return False
        return True

    def getList(self):
        """
        Return the list of nodes.

        Returns
        -------
        list
            List of nodes.
        """
        return self.list


class EdgeNode:
    """
    Class for the nodes in the list.
    """
    def __init__(self, y_max, x_min, m_numerator, m_denominator, y_min):
        self.y_max = y_max
        self.y_min = y_min
        self.x_min = x_min
        self.m_numerator = m_numerator
        self.m_denominator = m_denominator
        self.nextTA = None

    def slope_inverse(self):
        """
        Returns the inverse of the slope.
        """
        return float(self.m_denominator) / self.m_numerator


def fillTA(TA: EdgeTable, max_y: int, x_points: list, y_points: list):
    """
    Fill the Edge table list with the polygon edges.

    Parameters
    ----------
    TA : EdgeTable
        Edge table list.
    max_y : int
        Maximum y value of the polygon.
    x_points : list
        List of x coordinates of polygon vertices.
    y_points : list
        List of y coordinates of polygon vertices.
    
    Raises
    ------
    ValueError
        If the algorithm fails to fill the Edge Table.
    """
    try:
        for scanline in range(0, max_y):
            # if the y coordinate of the edge is on the scanline
            for i in range(0, len(y_points)):
                # if the y coordinate of the edge is on the scanline
                if scanline == y_points[i]:
                    # find connecting point on the left
                    k = (i - 1) % len(y_points)

                    # if the y coordinate of that point is greater
                    if y_points[k] > y_points[i]:
                        # Add the node with max(current-edge-y, left-connecting-y), current-edge-x, slope numerator and denominator in that scanline
                        TA.add(
                            scanline,
                            EdgeNode(
                                max(y_points[i], y_points[k]),
                                x_points[i],
                                y_points[i] - y_points[k],
                                x_points[i] - x_points[k],
                                min(y_points[i], y_points[k]),
                            ),
                        )

                    # find connecting point on the right
                    k = (i + 1) % len(y_points)

                    # if the y coordinate of that point is greater
                    if y_points[k] > y_points[i]:
                        # Add the node with max(current-edge-y, right-connecting-y), current-edge-x, slope numerator and denominator in that scanline
                        TA.add(
                            scanline,
                            EdgeNode(
                                max(y_points[i], y_points[k]),
                                x_points[i],
                                y_points[i] - y_points[k],
                                x_points[i] - x_points[k],
                                min(y_points[i], y_points[k]),
                            ),
                        )
    except Exception as e:
        raise ValueError(
            f"Failed to fill the Edge Table. Please check the coordinates of the polygon. Message: {e}"
        )

def polyfill(TA: EdgeTable) -> list:
    """
    Fill the polygon.

    Parameters
    ----------
    TA : EdgeTable
        Edge table list.
    
    Returns
    -------
    fill_points: list
        List of points to fill the polygon.

    Raises
    ------
    ValueError
        If the algorithm fails to fill the polygon.
    """
    try:
        # 1. Set y to the smallest value of the y coordinate that is in the TA (first non-empty bucket)
        y = TA.first_y()

        # 2. Initialize the TAA to vacuum
        TAA = []
        fill_points = []

        # 3.Repeat until TA and TA are empty
        while not (len(TAA) == 0 and TA.isEmpty()):
            # a) Move from the TA bucket and to the TAA those edges whose y_min = y (input edges)
            lista_TA = TA.getList()
            for i in range(y, len(lista_TA)):
                item = lista_TA[i]
                if item is not None:
                    node = item
                    while node.nextTA is not None:
                        if node.y_min == y:
                            TAA.append(node)
                            TA.delete(i, node)
                        node = node.nextTA
                    if node.y_min == y:
                        TAA.append(node)
                        TA.delete(i, node)

                # b) Remove from the TAA those entries for which y = y_max
                # (the edges not involved in the next scan line), then sort the TAA on x
                removeList = []
                for node in TAA:
                    if y == node.y_max:
                        removeList.append(node)

                for node in removeList:
                    TAA.remove(node)

                # bubble sort
                bubblesort(TAA)

                # c) Fill in the desired pixels on the scan line and using x-coordinate pairs from the TAA
                i = 0
                for node in TAA:
                    if i % 2 == 0:
                        fill_points.append((int(math.ceil(node.x_min)), y))
                    else:
                        fill_points.append((int(math.floor(node.x_min)), y))
                    i = i + 1

                # d)Increase y by 1 (next scan line)
                y = y + 1

                # e) For each non-vertical edge remaining in the TAA, update x to the new y
                for node in TAA:
                    node.x_min = node.x_min + node.slope_inverse()
        return fill_points
    except Exception as e:
        raise ValueError(f"Failed to fill the polygon. Message: {e}")

def fill_polygon_scanline(xp: list, yp: list) -> "nparray":
    """
    Scanline polygon fill algorithm.

    Parameters
    ----------
    xp : list
        List of x coordinates of polygon vertices.
    yp : list
        List of y coordinates of polygon vertices.
    
    Returns
    -------
    arr: nparray
        List of points to be filled through.
    
    Raises
    ------
    ValueError
        If the algorithm fails to fill the polygon.
    """
    try:
        max_y = max(yp)
        TA = EdgeTable(max_y + 1)
        fillTA(TA, max_y, xp, yp)
        points = polyfill(TA)

        arr = np.zeros((19200, 10800), dtype=np.uint8)
        for i in range(0, len(points) - 1, 2):
            arr[points[i][0] : points[i + 1][0], points[i][1]] = 1

        return arr
    except Exception as e:
        raise ValueError(f"Failed to fill polygon. Message: {e}")
