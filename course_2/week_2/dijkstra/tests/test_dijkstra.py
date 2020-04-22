import pytest
import os

from course_2.week_2.dijkstra import dijkstra
from helpers.test_setup import get_fixtures


current_path = os.path.dirname(os.path.realpath(__file__))
fixtures = get_fixtures(current_path, keys=["in", "out", "path"])


class TestDijksta:
    @pytest.mark.parametrize(
        "fixture",
        [
            pytest.param(fixture, id=fixture_name)
            for fixture_name, fixture in fixtures.items()
        ],
    )
    def test_dijkstra(self, fixture):

        graph, test_result, test_distances, test_path = prepare_data(fixture)

        distances, path = dijkstra(graph)

        for node in test_result:
            if node not in test_path:
                continue

            assert distances[node] == test_distances[node]
            assert path[node] == test_path[node]


def prepare_data(fixture):

    graph = {}
    test_distances = {}

    test_graph = fixture["in"].rstrip().split('\n')
    test_graph = [i.split('\n')[0].split('\t') for i in test_graph]

    for edges in test_graph:
        node = int(edges[0])
        graph[node] ={}
        for edge in edges[1:]:
            node_2, length = edge.split(',')
            graph[node][int(node_2)] = int(length)

    test_result = fixture["out"].rstrip()
    test_result = [int(i) for i in test_result.split(",")]

    test_path = fixture["path"].rstrip().split('\n')
    test_path = [i.split(" => path => ") for i in test_path]
    test_path = [[j.split(",") for j in i] for i in test_path]
    test_path = {int(i[0][0]): [int(j) for j in i[1]] for i in test_path}

    for node in test_result:
        distance = 0

        if node not in test_path:
            continue

        path = test_path[node]

        for idx in range(1, len(path)):
            edges = graph[path[idx - 1]]
            distance += edges[path[idx]]

        test_distances[node] = distance

    return graph, test_result, test_distances, test_path
