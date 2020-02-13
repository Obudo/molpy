# Import package, test suite, and other packages as needed
from molpy.util import distance as dist
import pytest


@pytest.mark.parametrize("point1,point2,bench", [
    ([0, 1], [0, 0], 1),
    ([1, 0, 1, 0], [0, 1, 0, 1], 2),
    ([2.236, 2.236], [0, 0], 3.162),
])
def test_distance(point1, point2, bench):
    assert dist(point1, point2) == pytest.approx(bench, abs=1e-3)


def test_distance_failure():
    assert dist([0], [3]) != 5
