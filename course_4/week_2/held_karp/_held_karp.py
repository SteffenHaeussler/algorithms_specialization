from typing import Sequence, Tuple

from functools import lru_cache

import numpy as np


def held_karp(cities: Tuple[Sequence[Tuple]]) -> Tuple[Sequence[Tuple]]:
    """
    Standing on the shoulders of giants. Blatently copied from
    https://github.com/norvig/pytudes/blob/master/ipynb/TSP.ipynb
    , since his pytudes, blog posts and especially his book is an amazing source
    of guidance. His work helped me a lot on my path of the last years.

    The Held-Karp shortest tour of this set of cities.
    For each end city C, find the shortest segment from A (the start) to C.
    Out of all these shortest segments, pick the one that is the shortest tour.

    Parameters
    ----------
    cities :
        Tuple of city coordinates as tuple
    Returns
    -------
    tour
        shortest possible city tour
    """
    A = cities[0]
    shortest_segment.cache_clear()
    return shortest_tour(
        shortest_segment(A, cities[1:idx] + cities[idx + 1 :], C)
        for idx, C in enumerate(cities[1:], 1)
    )


def shortest_tour(tours: Tuple[Sequence[Tuple]]) -> Tuple:
    """
    Returns the shortest tour from multiple tours

    Parameters
    ----------
    tours :
        multiple tours
    Returns
    -------
    tuple
        shortest possible city tour
    """
    return min(tours, key=tour_length)


@lru_cache(None)
def shortest_segment(A: Tuple, Bs: Tuple[Sequence[Tuple]], C: Tuple) -> Tuple:
    """
    Returns shortest segment from A via all Bs to C

    Parameters
    ----------
    A :
        city tour start
    Bs :
        tuple of cities
    C :
        city tour end

    Returns
    -------
    tuple
        shortest possible city segment
    """
    if not Bs:
        return (A, C)
    else:
        return min(
            (
                shortest_segment(A, Bs[:idx] + Bs[idx + 1 :], B) + (C,)
                for idx, B in enumerate(Bs)
            ),
            key=segment_length,
        )


def segment_length(segment: Tuple[Sequence[Tuple]]) -> float:
    """
    Returns the length of the whole segment. It is similiar to tour length

    Parameters
    ----------
    segment :
        segment for distance calculation

    Returns
    -------
    distance
        length of the segment distance
    """
    return sum(distance(segment[i], segment[i - 1]) for i in range(1, len(segment)))


def distance(A: Tuple, B: Tuple) -> float:
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


def tour_length(tour: Tuple[Sequence[Tuple]]) -> float:
    """
    Complete distance of a tour. Including last city to first city

    Parameters
    ----------
    tour :
        tour of cities
    Returns
    -------
    distance
        tour distance
    """
    return sum(distance(tour[i - 1], tour[i]) for i in range(len(tour)))
