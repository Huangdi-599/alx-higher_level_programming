#!/usr/bin/python3
"""
Defines a Pascal's Triangle function.
"""
def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    my_list = [[1]]
    for count in range(1, n):
        row = [1]
        for elem in range(1, count):
            row.append(my_list[count - 1][elem - 1] + my_list[count - 1][elem])
        row.append(1)
        my_list.append(row)
    return my_list
