import pytest
import os

from course_3.week_1.prims_mst import prims_mst
from helpers.test_setup import get_fixtures

current_path = os.path.dirname(os.path.realpath(__file__))
fixtures = get_fixtures(current_path, keys=["in", "out"])


class TestMST:
    @pytest.mark.parametrize(
        "fixture",
        [
            pytest.param(fixture, id=fixture_name)
            for fixture_name, fixture in fixtures.items()
        ],
    )
    def test_mst(self, fixture):

        adj_matrix = prepare_input(fixture)

        _, weights = prims_mst(adj_matrix)

        assert sum(weights) == int(fixture["out"].rstrip())


def prepare_input(fixture):

    graph = fixture["in"].rstrip().split("\n")
    n_nodes, n_edges = int(graph[0].split(" ")[0]), int(graph[0].split(" ")[1])

    graph = [[int(node) for node in edge.split(" ")] for edge in graph[1:]]
    node_1 = {edge[0]: [] for edge in graph}
    node_2 = {edge[1]: [] for edge in graph}

    for edge in graph:
        node_1[edge[0]].append(tuple((edge[1], edge[2])))
        node_2[edge[1]].append(tuple((edge[0], edge[2])))

    adj_matrix = {}

    for node in range(1, n_nodes + 1):
        temp_1, temp_2 = [], []

        if node in node_1:
            temp_1 = node_1[node]

        if node in node_2:
            temp_2 = node_2[node]

        adj_matrix[node] = temp_1 + temp_2

    return adj_matrix
