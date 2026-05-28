#!/bin/python3

"""
Problem: Conditional Statements (Weird / Not Weird)

Introduction to Conditional Statements:
--------------------------------------
Conditional statements in Python are used to make decisions in a program.
They allow the program to execute different blocks of code based on whether
a condition is True or False.

Python provides three main conditional keywords:
- if   : checks the first condition
- elif : checks multiple additional conditions
- else : runs when none of the above conditions are True

Syntax:
-------
if condition:
    # code runs if condition is True
elif condition:
    # code runs if previous condition is False
else:
    # code runs if all conditions are False

These conditions usually involve:
- Comparison operators (==, !=, >, <, >=, <=)
- Logical operators (and, or)

------------------------------------------------------------

Problem Description:
-------------------
Given an integer N, perform the following conditional actions:

1. If N is odd → print "Weird"
2. If N is even and in the range 2 to 5 → print "Not Weird"
3. If N is even and in the range 6 to 20 → print "Weird"
4. If N is even and greater than 20 → print "Not Weird"

------------------------------------------------------------

Approach:
---------
- Use modulus operator (%) to check if a number is odd or even
- Apply conditional statements (if-elif-else) to check ranges
- Print the result based on the matching condition

------------------------------------------------------------

Input:
------
An integer N

Output:
-------
Print "Weird" or "Not Weird" based on the conditions
"""

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    # Read input
    N = int(input().strip())

    # Apply conditional logic
    if N % 2 != 0:
        print('Weird')

    elif N % 2 == 0 and 2 <= N <= 5:
        print('Not Weird')

    elif N % 2 == 0 and 6 <= N <= 20:
        print('Weird')

    elif N % 2 == 0 and N > 20:
        print('Not Weird')