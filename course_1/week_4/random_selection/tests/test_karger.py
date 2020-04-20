import pytest
import os

from course_1.week_4.random_selection import karger
from helpers.test_setup import get_fixtures


current_path = os.path.dirname(os.path.realpath(__file__))
fixtures = get_fixtures(current_path)


class TestRSelect:
    @pytest.mark.parametrize(
        "fixture",
        [
            pytest.param(fixture, id=fixture_name)
            for fixture_name, fixture in fixtures.items()
        ],
    )
    def test_rselect(self, fixture):

        adj_graph = prepare_input(fixture["in"])
        test_result = int(fixture["out"].rstrip())

        result = karger(adj_graph, 100)

        assert result == test_result


def prepare_input(array):

    array = array.split('\n')
    array = [i.split(' ') for i in array if i != '']
    array = [[int(i) for i in j] for j in array]
    array = {i[0]: i[1:] for i in array}

    return array
