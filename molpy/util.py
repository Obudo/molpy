import numpy as np

def distance(point1, point2):
    a = np.asarray(point1)
    b = np.asarray(point2)
    retval = np.linalg.norm(a -  b)
    return retval
