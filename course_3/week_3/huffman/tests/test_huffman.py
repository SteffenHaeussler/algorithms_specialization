import pytest
import os

from course_3.week_3.huffman import huffman
from helpers.test_setup import get_fixtures

current_path = os.path.dirname(os.path.realpath(__file__))
fixtures = get_fixtures(current_path, keys=["in", "out"])


class TestHuffman:
    @pytest.mark.parametrize(
        "fixture",
        [
            pytest.param(fixture, id=fixture_name)
            for fixture_name, fixture in fixtures.items()
        ],
    )
    def test_huffman(self, fixture):

        array = fixture["in"].rstrip().split("\n")

        nums = int(array[0])
        array = [int(i) for i in array[1:]]

        test_result = fixture["out"].rstrip().split("\n")
        test_result = [int(i) for i in test_result]

        result = huffman(array, nums)

        max_length = len(result[-1])
        min_length = len(result[0])

        assert min_length == test_result[1]
        assert max_length == test_result[0]
