import pytest
import os

from course_2.week_3.median_maintenance import median_maintenance
from helpers.test_setup import get_fixtures


current_path = os.path.dirname(os.path.realpath(__file__))
fixtures = get_fixtures(current_path, keys=["in", "out"])


class TestMedian:
    @pytest.mark.parametrize(
        "fixture",
        [
            pytest.param(fixture, id=fixture_name)
            for fixture_name, fixture in fixtures.items()
        ],
    )
    def test_median(self, fixture):

        array = fixture["in"].rstrip().split("\n")
        array = [int(i) for i in array]

        result = median_maintenance(array)

        assert (sum(result) % 10000) == int(fixture["out"].rstrip())
