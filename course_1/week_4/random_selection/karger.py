import random
import copy


def karger(graph, n):
    """
    Quicksort wrapper

    Parameters
    ----------
    arr : list
        array of distinct integers
    n : int
        number of iterations

    Returns
    -------
    int
        number of cuts
    """

    min_cut = float('inf')
    for _ in range(n):
        data = copy.deepcopy(graph)
        length = contract(data)

        if length < min_cut:
            min_cut = length

    return min_cut


def contract(graph):

    while len(graph) > 2:
        pos_edges = [(node,edge) for node, edges in graph.items() for edge in edges]
        merge_edge = random.choice(pos_edges)
        graph[merge_edge[0]] = graph[merge_edge[0]] + graph[merge_edge[1]]

        del graph[merge_edge[1]]
        graph = {node: [i if i != merge_edge[1] else merge_edge[0] for i in edges] for node, edges in graph.items()}
        graph[merge_edge[0]] = [i for i in graph[merge_edge[0]] if i != merge_edge[0]]

    return [len(i) for i in graph.values()][0]
