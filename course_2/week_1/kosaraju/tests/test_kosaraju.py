import pytest
import os
import sys

from course_2.week_1.kosaraju import kosaraju
from helpers.test_setup import get_fixtures


sys.setrecursionlimit(50000)


current_path = os.path.dirname(os.path.realpath(__file__))
fixtures = get_fixtures(current_path)


class TestStronglyConectedCompounds:
    @pytest.mark.parametrize(
        "fixture",
        [
            pytest.param(fixture, id=fixture_name)
            for fixture_name, fixture in fixtures.items()
        ],
    )
    def test_strongly_conected_compounds(self, fixture):

        graph, test_result = prepare_fixture(fixture)

        ssc, _, _ = kosaraju(graph)

        counter = sorted(ssc.values(), reverse=True)[:5]

        if len(counter) < 5:
            counter += [0] * (5-len(counter))

        assert counter == test_result


def prepare_fixture(fixture):

    _input = fixture["in"].rstrip().split('\n')
    _input = [i.split(' ')[:2] for i in _input]
    _input = [[int(i) for i in j] for j in _input]
    _input = [tuple(i) for i in _input]

    _output = fixture["out"].rstrip()
    _output = _output.split(',')
    _output = [int(i) for i in _output]

    return _input, _output
