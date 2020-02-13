import numpy as np


def distance(point1, point2):
    """
    Returns the distance between two points

    Parameters
    ----------
    point1: array_like
        First point
    point2: array_like
        Second point

    Returns
    -------
    float
        The distance between the two points
    """
    a = np.asarray(point1)
    b = np.asarray(point2)
    retval = np.linalg.norm(a - b)
    return retval


def open_xyz(file_location):
    xyz_file = np.genfromtxt(fname=file_location, skip_header=2, dtype='unicode')
    symbols = xyz_file[:, 0]
    coords = (xyz_file[:, 1:])
    coords = coords.astype(np.float)
    return symbols, coords
