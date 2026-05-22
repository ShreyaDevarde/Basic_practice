"""
Module: data_types_operations.py

Description:
------------
This program demonstrates basic operations on different data types:
integer, float (double), and string.

It performs:
1. Addition of integers
2. Addition of floating-point numbers
3. String concatenation

The program uses predefined variables and user inputs to showcase
type handling and operations in Python.
"""


def perform_operations():
    """
    Reads user input and performs operations on integer, float, and string.

    Operations:
    -----------
    1. Adds a predefined integer with user input integer.
    2. Adds a predefined float with user input float.
    3. Concatenates a predefined string with user input string.

    Predefined Values:
    ------------------
    i : int = 4
    d : float = 4.0
    s : str = 'HackerRank '

    Inputs:
    -------
    A : int
    B : float
    C : str

    Outputs:
    --------
    Prints:
    - Sum of integers
    - Sum of floats
    - Concatenated string

    Example:
    --------
    Input:
        12
        4.0
        is the best place

    Output:
        16
        8.0
        HackerRank is the best place
    """

    i = 4
    d = 4.0
    s = 'HackerRank '

    # Read inputs
    A = int(input())
    B = float(input())
    C = input()

    # Perform operations
    print(i + A)
    print(d + B)
    print(s + C)


if __name__ == "__main__":
    perform_operations()