import pytest
import os

from course_1.week_3.quicksort import quicksort
from helpers.test_setup import get_fixtures


current_path = os.path.dirname(os.path.realpath(__file__))
fixtures = get_fixtures(current_path)


class TestQuickSort:
    @pytest.mark.parametrize(
        "fixture",
        [
            pytest.param(fixture, id=fixture_name)
            for fixture_name, fixture in fixtures.items()
        ],
    )
    def test_quicksort(self, fixture):

        result = []

        array = [int(i) for i in fixture["in"].split("\n") if i != ""]
        test_result = [int(i) for i in fixture["out"].split("\n") if i != ""]

        for flag in ["First", "Last", "Median"]:

            _, cnt = quicksort(array.copy(), FLAG_PIVOT=flag)

            result.append(cnt)

        assert result == test_result
