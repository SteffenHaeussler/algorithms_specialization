import heapq
from typing import Dict, Tuple


def dijkstra(graph: Dict, start: int = 1) -> Tuple[Dict, Dict]:
    """
    Dijkstra implementation with heap
    This implementation calculates the shortest path to all nodes

    https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

    Parameters
    ----------
    graph : dict
        graph with neighbor's and distance as a dict
    start : initial node

    Returns
    -------
    distances
        distance from start node to all other nodes
    path
        path from start node to all other nodes
    """

    path = {node: [start] for node in graph}
    distances = {node: 100000 for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:

        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor_node, distance in graph[current_node].items():
            distance = current_distance + distance

            if distance < distances[neighbor_node]:
                distances[neighbor_node] = distance
                path[neighbor_node] = path[current_node] + [neighbor_node]
                heapq.heappush(priority_queue, (distance, neighbor_node))

    return distances, path
