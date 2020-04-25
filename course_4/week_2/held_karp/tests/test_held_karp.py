import pytest
import os

from math import floor

from course_4.week_2.held_karp import held_karp, tour_length
from helpers.test_setup import get_fixtures


current_path = os.path.dirname(os.path.realpath(__file__))
fixtures = get_fixtures(current_path, keys=["in", "out"])


class TestHeldKarp:
    @pytest.mark.parametrize(
        "fixture",
        [
            pytest.param(fixture, id=fixture_name)
            for fixture_name, fixture in fixtures.items()
        ],
    )
    def test_held_karp(self, fixture):

        cities = fixture["in"].rstrip().split("\n")
        n_cities = int(cities[0])
        cities = [city.split(" ") for city in cities[1:]]
        cities = tuple(tuple(float(coord) for coord in coords) for coords in cities)

        if n_cities < 17:
            shortest_tour = held_karp(cities)
            distance = tour_length(shortest_tour)

            assert floor(distance) == int(fixture["out"].rstrip())
