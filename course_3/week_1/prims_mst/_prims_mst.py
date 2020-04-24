import heapq
from typing import Dict, List, Tuple


def prims_mst(graph: Dict) -> Tuple[List, List]:
    """
    Calculates the minimal spanning tree of a graph

    https://en.wikipedia.org/wiki/Prim%27s_algorithm

    Parameters
    ----------
    graph : list
        adjecent graph with key = node_1 and list of (node_2, weight)
        G = (V_1: [(V_2, Cost), (V_3, Cost)])

    Returns
    -------
    tree
        edges with weights of the minimal spanning tree
    weights
        list of weights of the edges for the minimal spanning tree
    """
    heap = []
    visited = set()
    tree = []
    weights = []

    current_node = 1
    visited.add(current_node)

    for edge in graph[current_node]:

        heapq.heappush(heap, (edge[1], edge[0], current_node))

    while heap:
        weight, next_node, previous_node = heapq.heappop(heap)

        if next_node in visited:
            continue

        visited.add(next_node)

        tree.append(tuple((previous_node, next_node, weight)))
        weights.append(weight)

        for edge in graph[next_node]:

            heapq.heappush(heap, (edge[1], edge[0], next_node))

    return tree, weights
