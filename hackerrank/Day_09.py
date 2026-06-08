#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def factorial(n):
    """
    Calculate the factorial of a given non-negative integer.

    Problem Statement:
    ------------------
    Given an integer `n`, compute its factorial.

    The factorial of a number is the product of all positive integers
    less than or equal to that number.

    Mathematical Definition:
    ------------------------
    n! = n × (n - 1) × (n - 2) × ... × 2 × 1

    Special Case:
    -------------
    0! = 1

    Examples:
    ---------
    Input: 5
    Output: 120
    Explanation:
        5! = 5 × 4 × 3 × 2 × 1 = 120

    Input: 0
    Output: 1

    Approach:
    ---------
    - Initialize a variable `result` with 1.
    - Iterate from 1 to n.
    - Multiply `result` by each number in the range.
    - Return the final product.

    Time Complexity:
    ----------------
    O(n)

    Space Complexity:
    -----------------
    O(1)

    Parameters:
    -----------
    n : int
        A non-negative integer whose factorial is to be calculated.

    Returns:
    --------
    int
        The factorial of n.
    """
    
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


if __name__ == '__main__':
    n = int(input("Enter a non-negative integer: ").strip())

    result = factorial(n)

    print("The factorial of", n, "is", result)