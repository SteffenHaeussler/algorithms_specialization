import pytest
import os

import numpy as np

from course_4.week_1.all_pair_shortest_path import floyd_warshall
from helpers.test_setup import get_fixtures


current_path = os.path.dirname(os.path.realpath(__file__))
fixtures = get_fixtures(current_path, keys=["in", "out", "path"])


class TestAllPairShortestPath:
    @pytest.mark.parametrize(
        "fixture",
        [
            pytest.param(fixture, id=fixture_name)
            for fixture_name, fixture in fixtures.items()
        ],
    )
    def test_all_pair_shortest_path(self, fixture):

        adj_matrix, test_result, test_path = prepare_data(fixture)

        result, path = floyd_warshall(adj_matrix)

        if type(result) == np.ndarray:
            result = int(np.min(result))
            path = {k: v for k, v in path.items() if v is not None}
            min_path = min(path, key=path.get)
            min_path = [i + 1 for i in min_path]

        else:
            min_path = "null"

        assert str(result) == test_result
        # assert min_path == test_path


def prepare_data(fixture):

    test_graph = fixture["in"].rstrip().split("\n")
    test_graph = [i.split(" ") for i in test_graph]

    n_nodes, n_edges = int(test_graph[0][0]), int(test_graph[0][1])
    adj_matrix = np.full((n_nodes, n_nodes), np.inf)

    for i in test_graph[1:]:
        adj_matrix[int(i[0]) - 1, int(i[1]) - 1] = int(i[2])

    test_result = fixture["out"].rstrip()
    test_path = fixture["path"].rstrip()

    if test_result != "NULL":
        test_path = test_path[1:-1].split(",")
        test_path = [int(i) for i in test_path]
    else:
        test_path = "NULL"

    return adj_matrix, test_result, test_path
