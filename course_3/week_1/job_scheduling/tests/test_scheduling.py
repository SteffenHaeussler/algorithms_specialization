import pytest
import os

import pandas as pd

from course_3.week_1.job_scheduling import scheduling
from helpers.test_setup import get_fixtures

current_path = os.path.dirname(os.path.realpath(__file__))
fixtures = get_fixtures(current_path, keys=["in", "out"])


class TestScheduling:
    @pytest.mark.parametrize(
        "fixture",
        [
            pytest.param(fixture, id=fixture_name)
            for fixture_name, fixture in fixtures.items()
        ],
    )
    def test_scheduling(self, fixture):

        diff_result, diff_ratio = fixture["out"].rstrip().split("\n")

        job_list = fixture["in"].rstrip().split("\n")
        job_list = [[int(n) for n in job.split(" ")] for job in job_list[1:]]
        job_list = pd.DataFrame(job_list, columns=["weights", "lenghts"])

        diff_weight_length, ratio_weight_length = scheduling(job_list)

        assert diff_weight_length == int(diff_result)
        assert ratio_weight_length == int(diff_ratio)
