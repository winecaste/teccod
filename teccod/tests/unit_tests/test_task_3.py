import pytest
import math

from teccod.src.task_3 import Point

@pytest.mark.parametrize("x1, y1, x2, y2, expected_distance", [
    (0, 0, 3, 4, 5),
    (1, 1, 4, 5, 5),
    (3, 3, 3, 3, 0),
    (-3, -3, -3, -3, 0),
    (0, 0, 0, 5, 5),
    (0, 0, 0, -5, 5),
    (0, 0, 5, 0, 5),
    (0, 0, -5, 0, 5),
    (-3, 4, 5, -2, 10)
])
def test_distance_between_points(x1, y1, x2, y2, expected_distance):
    point1 = Point(x1, y1)
    point2 = Point(x2, y2)
    assert math.isclose(point1.distance(point2), expected_distance)





