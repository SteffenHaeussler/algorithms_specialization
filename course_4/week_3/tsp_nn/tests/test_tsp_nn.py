import pytest
import os

from math import floor

from course_4.week_2.held_karp import tour_length
from course_4.week_3.tsp_nn import tsp_nn
from helpers.test_setup import get_fixtures


current_path = os.path.dirname(os.path.realpath(__file__))
fixtures = get_fixtures(current_path, keys=["in", "out"])


class TestTspNN:
    @pytest.mark.parametrize(
        "fixture",
        [
            pytest.param(fixture, id=fixture_name)
            for fixture_name, fixture in fixtures.items()
        ],
    )
    def test_tsp_nn(self, fixture):

        cities = fixture["in"].rstrip().split("\n")
        n_cities = int(cities[0])

        if n_cities <= 10000:
            cities = [city.split(" ") for city in cities[1:]]
            cities = tuple(
                tuple(float(coord) for coord in coords[1:]) for coords in cities
            )

            nearest_neighbors = tsp_nn(cities)
            distance = tour_length(nearest_neighbors)

            assert floor(distance) == int(fixture["out"].rstrip())
