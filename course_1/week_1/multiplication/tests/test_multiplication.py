import pytest
import os

from course_1.week_1.multiplication import multiplication
from helpers.test_setup import get_fixtures


current_path = os.path.dirname(os.path.realpath(__file__))
fixtures = get_fixtures(current_path)


class TestMultiplication:
    @pytest.mark.parametrize(
        "fixture",
        [
            pytest.param(fixture, id=fixture_name)
            for fixture_name, fixture in fixtures.items()
        ],
    )
    def test_multiplication(self, fixture):

        number_1, number_2 = fixture["in"].split("\n")
        test_result = fixture["out"].rstrip()

        result = multiplication(int(number_1), int(number_2))

        assert str(result) == test_result
