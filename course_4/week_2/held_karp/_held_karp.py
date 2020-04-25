from functools import lru_cache

import numpy as np


def held_karp(cities):
    """
    Standing on the shoulders of giants. Blatently copied from
    https://github.com/norvig/pytudes/blob/master/ipynb/TSP.ipynb
    , since his pytudes, blog posts and especially his book is an amazing source
    of guidance. His work helped me a lot on my path of the last years.

    The Held-Karp shortest tour of this set of cities.
    For each end city C, find the shortest segment from A (the start) to C.
    Out of all these shortest segments, pick the one that is the shortest tour."""

    A = cities[0]
    shortest_segment.cache_clear()
    return shortest_tour(
        shortest_segment(A, cities[1:idx] + cities[idx + 1 :], C)
        for idx, C in enumerate(cities[1:], 1)
    )


def shortest_tour(tours):
    return min(tours, key=tour_length)


@lru_cache(None)
def shortest_segment(A, Bs, C):
    "The shortest segment starting at A, going through all Bs, and ending at C."
    if not Bs:
        return [A, C]
    else:
        return min(
            (
                shortest_segment(A, Bs[:idx] + Bs[idx + 1 :], B) + [C]
                for idx, B in enumerate(Bs)
            ),
            key=segment_length,
        )


def segment_length(segment):
    "The total of distances between each pair of consecutive cities in the segment."
    # Same as tour_length, but without distance(tour[0], tour[-1])
    return sum(distance(segment[i], segment[i - 1]) for i in range(1, len(segment)))


def distance(A, B):
    return np.sqrt((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2)


def tour_length(tour):
    """The total of distances between each pair of consecutive cities in the tour.
    This includes the last-to-first, distance(tour[-1], tour[0])"""
    return sum(distance(tour[i - 1], tour[i]) for i in range(len(tour)))
