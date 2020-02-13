# Import package, test suite, and other packages as needed
import molpy
import pytest
import numpy as np

def test_reader():
    assert molpy.data.look_and_say == molpy.data.reader.look_and_say

@pytest.mark.parametrize(
    "molecule, com, natoms",
    [
        ("water", [9.81833333, 7.60366667, 12.673], 3),
        ("benzene", [-1.4045,0,0], 12),
     ],
)
def test_read_xyz(molecule, com, natoms):
    mol = molpy.data.get_molecule(molecule)
    assert np.allclose(np.mean(mol["geometry"], axis=0), com)
    assert len(mol["geometry"]) == natoms    
    assert len(mol["symbols"]) == natoms
