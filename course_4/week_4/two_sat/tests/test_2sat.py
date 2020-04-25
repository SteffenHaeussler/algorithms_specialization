import pytest
import os

from course_4.week_4.two_sat import two_sat
from helpers.test_setup import get_fixtures


current_path = os.path.dirname(os.path.realpath(__file__))
fixtures = get_fixtures(current_path, keys=["in", "out"])


class TestTwoSat:
    @pytest.mark.parametrize(
        "fixture",
        [
            pytest.param(fixture, id=fixture_name)
            for fixture_name, fixture in fixtures.items()
        ],
    )
    def test_two_sat(self, fixture):


        edges, n_var = prepare_input(fixture)

        success = two_sat(edges, n_var)

        assert success == int(fixture["out"].rstrip())


def prepare_input(fixture):

    edges = []

    graph = fixture["in"].rstrip().split("\n")

    n_var = int(graph[0])

    for edge in graph[1:]:
        nodes = [int(node) for node in edge.split()]
        edges.append((-nodes[0], nodes[1]))
        edges.append((-nodes[1], nodes[0]))

    return edges, n_var
