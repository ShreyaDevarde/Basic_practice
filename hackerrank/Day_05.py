"""
Program: Multiplication Table Generator

Description:
    This program takes an integer input from the user and prints
    the multiplication table of that number from 1 to 10.

Input:
    A single integer value.

Output:
    The multiplication table of the given integer in the format:
    <number> x <multiplier> = <result>

Example:
    Input:
        5

    Output:
        5 x 1 = 5
        5 x 2 = 10
        ...
        5 x 10 = 50
"""

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    # Read an integer input from the user
    n = int(input().strip())

    # Generate and print the multiplication table from 1 to 10
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")