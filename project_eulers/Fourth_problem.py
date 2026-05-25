#!/usr/bin/env python3

"""
Module: Largest Palindrome Product

This module finds the largest palindrome number made from the product
of two 3-digit numbers.
"""


def palindrome(num: int) -> bool:
    """
    Check whether a given number is a palindrome.

    A palindrome is a number that reads the same forward and backward.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is a palindrome, False otherwise.
    """
    return str(num) == str(num)[::-1]


def find_largest_palindrome() -> int:
    """
    Compute the largest palindrome made from the product of two 3-digit numbers.

    Iterates through all possible pairs of 3-digit numbers (100–999),
    calculates their product, and checks if it is a palindrome.

    Returns:
        int: The largest palindrome product found.
    """
    result = 0

    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j

            if palindrome(product):
                result = max(result, product)

    return result


def main() -> None:
    """
    Entry point of the program.

    Calls the function to compute the largest palindrome and prints the result.
    """
    result = find_largest_palindrome()
    print("Result:", result)


if __name__ == "__main__":
    main()