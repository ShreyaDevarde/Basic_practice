#!/bin/python3

"""
Problem: Difference Between Sum of Squares and Square of Sum

Objective:
Find the difference between:
1. The sum of the squares of the first N natural numbers.
2. The square of the sum of the first N natural numbers.

Formula:
- Sum of Squares:
  1² + 2² + 3² + ... + N²

- Square of Sum:
  (1 + 2 + 3 + ... + N)²

The program calculates the absolute difference between these two values.

Example:
For N = 10
- Sum of Squares = 385
- Square of Sum = 3025
- Difference = 2640
"""

import math


def square_diff(n):
    """
    Calculate the difference between the sum of squares
    and the square of the sum of the first N natural numbers.

    Parameters:
    n (int): The range of natural numbers.

    Returns:
    int: Absolute difference between:
         - sum of squares
         - square of sum
    """

    sum_square = 0
    square_sum = 0
    sum_s = 0

    for i in range(1, n + 1):
        sum_square += math.pow(i, 2)
        sum_s += i

    square_sum += math.pow(sum_s, 2)

    difference = abs(sum_square - square_sum)

    return int(difference)


n = 100
print("Result:", square_diff(n))