# Import package, test suite, and other packages as needed
import molpy.data as data
import pytest

def test_reader():
    assert data.look_and_say == data.reader.look_and_say 
