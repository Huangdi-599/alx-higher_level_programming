#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    array=[]
    for n in matrix:
        m= map(lambda x: x * x, n)
        app = list(m)
        array.append(app)
    return array
