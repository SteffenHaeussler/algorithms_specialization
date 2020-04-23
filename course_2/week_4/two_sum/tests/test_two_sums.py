import pytest
import os

from course_2.week_4.two_sum import two_sum
from helpers.test_setup import get_fixtures

current_path = os.path.dirname(os.path.realpath(__file__))
fixtures = get_fixtures(current_path, keys=["in", "out"])


class TestTwoSum:
    @pytest.mark.parametrize(
        "fixture",
        [
            pytest.param(fixture, id=fixture_name)
            for fixture_name, fixture in fixtures.items()
        ],
    )
    def test_two_sum(self, fixture):

        array = fixture["in"].rstrip().split("\n")
        array = [int(i) for i in array]

        result = two_sum(array)

        assert result == int(fixture["out"].rstrip())
