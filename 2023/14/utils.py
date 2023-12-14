import numpy

def rotate_matrix(matrix, clockwise=False):
    return numpy.rot90(matrix) if clockwise else numpy.rot90(matrix, k=1, axes=(1, 0))
