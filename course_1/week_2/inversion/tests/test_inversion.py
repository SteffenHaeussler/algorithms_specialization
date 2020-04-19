import pytest
import os

from course_1.week_2.inversion import sort_and_count
from helpers.test_setup import get_fixtures


current_path = os.path.dirname(os.path.realpath(__file__))
fixtures = get_fixtures(current_path)


class TestCountInversion:
    @pytest.mark.parametrize(
        "fixture",
        [
            pytest.param(fixture, id=fixture_name)
            for fixture_name, fixture in fixtures.items()
        ],
    )
    def test_count_inversion(self, fixture):

        array = [int(i) for i in fixture["in"].split("\n") if i != ""]
        test_result = fixture["out"].rstrip()

        _, count = sort_and_count(array)

        assert str(count) == test_result
