"""
Module: prime_factors.py

Description:
------------
This module provides a utility function to compute the set of unique
prime factors of a given positive integer using an optimized approach.

Approach:
---------
1. Remove all factors of 2 (smallest prime).
2. Check only odd numbers up to sqrt(n).
3. If remaining n > 2, it is a prime factor.

Time Complexity:
----------------
O(√n)

Space Complexity:
-----------------
O(k), where k is the number of unique prime factors.

Example:
--------
>>> prime_factors_unique(28)
{2, 7}
"""


def prime_factors_unique(n: int) -> set[int]:
    """
    Returns the set of unique prime factors of a given integer.

    Parameters:
    -----------
    n : int
        A positive integer whose prime factors are to be found.

    Returns:
    --------
    set[int]
        A set containing unique prime factors of n.

    Raises:
    -------
    ValueError:
        If n is less than 2.

    Example:
    --------
    >>> prime_factors_unique(600851475143)
    {71, 839, 1471, 6857}
    """

    if n < 2:
        raise ValueError("Input must be an integer greater than 1.")

    factors = set()

    # Handle factor 2 separately
    while n % 2 == 0:
        factors.add(2)
        n //= 2

    # Check odd factors
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            factors.add(factor)
            n //= factor
        factor += 2

    # If remaining n is a prime number > 2
    if n > 2:
        factors.add(n)

    return factors


if __name__ == "__main__":
    number = 600851475143
    result = prime_factors_unique(number)
    print(f"Unique prime factors of {number}: {result}")