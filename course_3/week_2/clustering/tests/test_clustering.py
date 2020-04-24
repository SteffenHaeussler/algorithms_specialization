import pytest
import os

from course_3.week_2.clustering import clustering, find_shortest
from helpers.test_setup import get_fixtures

current_path = os.path.dirname(os.path.realpath(__file__))
fixtures = get_fixtures(current_path, keys=["in", "out"])


class TestClustering:
    @pytest.mark.parametrize(
        "fixture",
        [
            pytest.param(fixture, id=fixture_name)
            for fixture_name, fixture in fixtures.items()
        ],
    )
    def test_mst(self, fixture):

        graph = fixture["in"].rstrip().split('\n')
        nodes = int(graph[0])

        graph = [tuple([int(n) for n in edge.split(' ')]) for edge in graph[1:]]
        graph = sorted(graph, key=lambda x: x[2])

        clusters = clustering(graph, nodes, 4)
        result = find_shortest(graph, clusters)

        assert result == int(fixture["out"].rstrip())
