import pytest
import os
import sys

from course_3.week_4.knapsack import knapsack
from helpers.test_setup import get_fixtures

current_path = os.path.dirname(os.path.realpath(__file__))
fixtures = get_fixtures(current_path, keys=["in", "out"])


class TestKnapsck:
    @pytest.mark.parametrize(
        "fixture",
        [
            pytest.param(fixture, id=fixture_name)
            for fixture_name, fixture in fixtures.items()
        ],
    )
    def test_knapsack(self, fixture):

        array = fixture["in"].rstrip().split('\n')

        max_weight = int(array[0].split(' ')[0])
        num_items = int(array[0].split(' ')[1])

        array = [item.split(' ') for item in array[1:]]
        array = [tuple(int(i) for i in item) for item in array]
        array.insert(0, (0,0))

        sys.setrecursionlimit(50000)
        weight, packed_items = knapsack(array, max_weight)

        if weight != int(fixture["out"].rstrip()):
            breakpoint()

        assert weight == int(fixture["out"].rstrip())
