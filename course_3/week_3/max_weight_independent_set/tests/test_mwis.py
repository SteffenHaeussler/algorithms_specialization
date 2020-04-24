from typing import List
import pytest
import os

from course_3.week_3.max_weight_independent_set._mwis import mwis
from helpers.test_setup import get_fixtures

current_path = os.path.dirname(os.path.realpath(__file__))
fixtures = get_fixtures(current_path, keys=["in", "out"])


class TestMWIS:
    @pytest.mark.parametrize(
        "fixture",
        [
            pytest.param(fixture, id=fixture_name)
            for fixture_name, fixture in fixtures.items()
        ],
    )
    def test_mws(self, fixture):

        checks = [1, 2, 3, 4, 17, 117, 517, 997]

        array = fixture["in"].rstrip().split('\n')
        array = [int(i) for i in array]

        result = mwis(array)

        string = ""
        for i in checks:
            if i in result:
                string += "1"
            else:
                string += "0"

        assert string == fixture["out"].rstrip()
