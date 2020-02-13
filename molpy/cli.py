import argparse
from .data import reader
from .util import distance


def main():
    parser = argparse.ArgumentParser(
        description=
        'A Molecule utility that reads XYZ files and calculates the distance between atoms at index1 and index2.')
    parser.add_argument('filename', type=str, help='The XYZ file to read.')
    parser.add_argument('index1', type=int, help='Index of the first atom.')
    parser.add_argument('index2', type=int, help='Index of the second atom.')

    args = parser.parse_args()

    mol = reader.get_molecule(args.filename)

    atom1 = mol["geometry"][args.index1]
    atom2 = mol["geometry"][args.index2]
    s1 = mol["symbols"][args.index1]
    s2 = mol["symbols"][args.index2]

    print(f"Reading molecule: {args.filename}")
    print(f"Distance between {args.index1}:{s1} and {args.index2}:{s2} = {distance(atom1, atom2):.3f} Å")
