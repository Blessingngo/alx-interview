#!/usr/bin/env python3

from typing import List

def pascal_triangle(n: int) -> List[list]:
    '''
    Generates Pascal's triangle up to the nth row.
    '''
    if n <= 0:
        return []

    if n == 1:
        return [[1]]

    if n == 2:
        return [[1], [1, 1]]

    triangle = [[1], [1, 1]]

    for i in range(2, n):
        temp = [1]  # Start each row with 1
        for j in range(len(triangle[-1]) - 1):
            a = triangle[-1][j]
            b = triangle[-1][j + 1]
            temp.append(a + b)
        temp.append(1)  # End each row with 1
        triangle.append(temp)

    return triangle
