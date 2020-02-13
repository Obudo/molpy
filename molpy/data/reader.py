import os
import numpy as np
from ..util import read_xyz

dirname = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(dirname, 'look_and_say.dat')
with open(filename, 'r') as handle:
    look_and_say = handle.read()


def get_molecule(mol_name):
    '''
    Reads a molecule file present as a .xyz file in the data folder

    Parameters
    ----------
    mol_name: string
        Name of the molecule to read. Can be either "water" or "benzene"

    Returns
    -------
    (dict. of strings: numpy array)
        Molecule data, with key "symbols" and "geometry" for the list of atomic symbols and atomic xyz positions respectively
    '''
    data_dirname = os.path.dirname(os.path.abspath(__file__))
    dirname = os.path.join(data_dirname, 'xyz')
    filename = os.path.join(dirname, mol_name + '.xyz')
    sym, coor = read_xyz(filename)
    molecule = {}
    molecule["geometry"] = coor
    molecule["symbols"] = sym
    return molecule
