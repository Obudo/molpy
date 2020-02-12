# Import package, test suite, and other packages as needed
import molpy
import pytest

def test_distance():
    assert molpy.util.distance([0,1], [0,0]) == 1
    assert molpy.util.distance([1,0,1,0], [0,1,0,1]) == 2
