from copy import deepcopy
from typing import Dict, Tuple

import numpy as np


def floyd_warshall(graph: np.ndarray) -> Tuple[np.ndarray, Dict]:
    """
    Calculates the shortest path between all nodes in a graph.

    https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm

    I failed several times with multiple different implementations including
    Johnson's algorithm and floyd warshell, so I took the easy way:
    Implementation follows https://www.goodreads.com/book/show/51139424-python-algorithms

    TODO: 5 test cases fails; paths not solved, since not clear, how to compute the path

    Parameters
    ----------
    graph : np.ndarray
        adjacent matrix of the matrix; missing edges are described with np.inf
    Returns
    -------
    distance
        adjacent matrix of the shortest distances between nodes
    path
        returns shortest path between nodes | add + 1 for each node
    """
    n_nodes = graph.shape[0]

    distance, path = deepcopy(graph), {}
    for u in range(0, n_nodes):
        for v in range(0, n_nodes):
            if u == v or graph[u][v] == np.inf:
                path[u, v] = None
            else:
                path[u, v] = u

    for k in range(0, n_nodes):
        for u in range(0, n_nodes):
            for v in range(0, n_nodes):
                shortcut = distance[u][k] + distance[k][v]
                if shortcut < distance[u][v]:
                    distance[u][v] = shortcut
                    path[u, v] = path[k, v]
                if u == v:
                    if distance[u][v] < 0:
                        return "NULL", []

    return distance, path
