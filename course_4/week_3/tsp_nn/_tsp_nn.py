from typing import Sequence, Tuple


import numpy as np


def tsp_nn(cities: Tuple[Sequence[Tuple]]) -> Sequence[Tuple]:
    """
    TSP with nearest neighbor.

    Following the style of norvig's held-karp implementation

    Parameters
    ----------
    cities :
        Tuple of city coordinates as tuple
    Returns
    -------
    tour
        city tour calculated by nearest neighbors
    """
    A = cities[0]
    tour = [A]
    unvisited = set(cities[1:])

    while unvisited:

        A = nearest_neighbor(A, unvisited)
        tour.append(A)
        unvisited.remove(A)

    return tour


def nearest_neighbor(A: Tuple, cities: Tuple[Sequence[Tuple]]) -> Tuple:
    """
    Find nearest neighbot of city A

    Parameters
    ----------
    A :
        coordinates of city A
    cities :
        Tuple of city coordinates as tuple
    Returns
    -------
    tuple
        nearest city from cities towards A
    """
    return min(cities, key=lambda C: distance(A, C))


def distance(A: Tuple, B: Tuple):
    """
    Distance between two cities

    Parameters
    ----------
    A :
        city A
    B :
        city B

    Returns
    -------
    distance
        city distance
    """
    return np.sqrt((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2)
