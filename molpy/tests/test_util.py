# Import package, test suite, and other packages as needed
import molpy
import pytest

@pytest.mark.parametrize("point1,point2,bench", [
    ([0,1], [0,0], 1),
    ([1,0,1,0], [0,1,0,1], 2),
])
def test_distance(point1, point2, bench):
    assert molpy.util.distance(point1, point2) == bench
