import os
import numpy as np
from ..util import open_xyz

dirname = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(dirname, 'look_and_say.dat')
with open(filename, 'r') as handle:
    look_and_say  = handle.read()

def get_molecule(mol_name):
    data_dirname = os.path.dirname(os.path.abspath(__file__))
    dirname = os.path.join(data_dirname, 'xyz')
    filename = os.path.join(dirname, mol_name + '.xyz')
    sym, coor = open_xyz(filename)
    molecule = {}
    molecule["geometry"] = coor
    molecule["structure"] = sym
    return molecule
