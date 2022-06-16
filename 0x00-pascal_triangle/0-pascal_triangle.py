#!/usr/bin/python3

"""
Returns a list if n <= 0
You can assume n will always be an integer
"""


def pascal_triangle(n):
    """
    print a list that will make a triangle
    """
    triangle = []
    row = []
    result = []
    if n <= 0:
        return []
    for i in range(0, n + 1):
        row = [j > 0 and j < i - 1 and i > 2 and result[j - 1] +
               result[j] or 1 for j in range(0, i)]
        result = row
        triangle += [row]
    return triangle[1:]
