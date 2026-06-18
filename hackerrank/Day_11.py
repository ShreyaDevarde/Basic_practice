"""
Problem: 2D Arrays - DS (HackerRank 30 Days of Code, Day 11)

Given a 6×6 2D array, calculate the maximum hourglass sum.

An hourglass in a 2D array is defined as:

a b c
  d
e f g

The hourglass sum is:
a + b + c + d + e + f + g

Approach:
1. Read the 6×6 array.
2. Iterate through all possible hourglass starting positions
   (0 ≤ row ≤ 3, 0 ≤ col ≤ 3).
3. Compute the sum of the 7 elements forming each hourglass.
4. Track the maximum hourglass sum encountered.
5. Print the maximum sum.

Time Complexity:
O(16) ≈ O(1)
(Only 16 hourglasses exist in a 6×6 array.)

Space Complexity:
O(1)
"""
#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input("Enter the array:").rstrip().split())))

    max_sum = -63  # Minimum possible hourglass sum (-9 * 7)

    for i in range(4):
        for j in range(4):
            hourglass_sum = (
                arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
                + arr[i + 1][j + 1]
                + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            )

            max_sum = max(max_sum, hourglass_sum)

    print(max_sum)