from collections import defaultdict
from itertools import chain
from typing import Dict, List, Tuple, Union


def kosaraju(graph: List[Tuple]) -> Union[Dict, List, Dict]:
    """
    TODO: DEBUG - 11 of 68 test cases are failing
    Kosaraju's algorithm to detect strongly connected components

    https://en.wikipedia.org/wiki/Kosaraju%27s_algorithm

    Parameters
    ----------
    graph : list
        adjecent nodes as tuple

    Returns
    -------
    ssc
        strongly connected component. key: initial node, value: number of nodes
    ssc_node
        starting node for a ssc
    node_position : dict
            node position on the original graph
    """

    def prepare_graph(temp_graph: List) -> Union[Dict, Dict]:
        """
        prepare graph to an adjacency list and revert it

        Parameters
        ----------
        graph : list
            adjecent nodes as tuple

        Returns
        -------
        original
            original graph as adjacency list
        reversed_graph
            reversed graph as adjacency list
        """
        original_graph = defaultdict(list)
        reversed_graph = defaultdict(list)

        for edge in graph:
            original_graph[edge[0]].append(edge[1])
            reversed_graph[edge[1]].append(edge[0])

        return original_graph, reversed_graph

    def create_positional_graph(graph: Dict, node_position: Dict) -> Dict:
        """
        Calculate new graph from the node positions calculated by DFS on reversed graph

        Parameters
        ----------
        graph : dict
            original graph with adjacent node list
        node_position : dict
            node with the position on the reversed graph

        Returns
        -------
        positional_graph
            graph with node position from the reversed path
        """
        positional_graph = {}

        for node_1, adj_nodes in graph.items():
            positional_graph[node_position[node_1]] = [
                node_position[node_2] for node_2 in adj_nodes
            ]

        return positional_graph

    def dfs_loop(graph: Dict) -> Union[Dict, List, Dict]:
        """
        DFS loop for calculating ssc (topological sort)


        Parameters
        ----------
        graph : dift
            graph as adjacency list

        Returns
        -------
        ssc
            strongly connected component. key: initial node, value: number of nodes
        ssc_node
            starting node for a ssc
        node_position : dict
                node position on the original graph
        """
        nodes = list(set(chain(*graph.values())) | set(graph.keys()))

        def dfs(graph, _node):
            """
            Depth-first search recursive implementation

            Parameters
            ----------
            graph : list
                adjecent nodes as tuple
            _node :
            """

            nonlocal visited, ssc, counter, node_positions

            if _node not in visited:

                visited.add(_node)

                ssc[node] = ssc.get(node, 0) + 1

                for n in graph[_node]:
                    dfs(graph, n)

                counter += 1
                node_positions[_node] = counter

        counter = 1
        ssc_node = []
        ssc = {}
        node_positions = {}
        visited = set()

        for node in nodes[::-1]:

            if node not in visited:
                ssc_node.append(node)
                dfs(graph, node)

        return ssc, ssc_node, node_positions

    original_graph, reversed_graph = prepare_graph(graph)

    # compute position for each node on the reversed graph
    _, _, node_position = dfs_loop(reversed_graph)

    positional_graph = create_positional_graph(original_graph, node_position)

    # compute the identity of each node's strongly connected component
    return dfs_loop(positional_graph)
