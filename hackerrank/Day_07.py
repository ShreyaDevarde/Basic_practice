"""
Problem:
    Given an array of N integers, print the elements in reverse order
    as a single line of space-separated integers.

Input:
    - The first line contains an integer N, representing the number of elements.
    - The second line contains N space-separated integers.

Output:
    - Print the array elements in reverse order on a single line,
      separated by spaces.

Approach:
    - Read the array elements from input.
    - Reverse the array using Python slicing (arr[::-1]).
    - Convert each element to a string and join them with spaces.
    - Print the reversed sequence.

Example:
    Input:
        4
        1 4 3 2

    Output:
        2 3 4 1

Time Complexity:
    O(N)

Space Complexity:
    O(N)
"""
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    print("Result:", ' '.join(map(str, arr[::-1])))