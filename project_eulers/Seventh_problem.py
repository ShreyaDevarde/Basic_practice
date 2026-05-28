def is_prime(num):
    """
    Check whether a given number is prime or not.

    A prime number is a number greater than 1
    that is divisible only by:
        1 and itself

    Examples:
        Prime Numbers:
            2, 3, 5, 7, 11

        Non-Prime Numbers:
            4, 6, 8, 9, 10

    Logic Used:
    ----------
    1. Numbers less than or equal to 1 are not prime.
    2. Number 2 is the only even prime number.
    3. Any other even number is not prime.
    4. Check only odd divisors from 3 onward.
    5. We only check divisors up to sqrt(num)
       because larger factors would already have
       a smaller corresponding factor.

    Args:
        num (int):
            Number to check for primality.

    Returns:
        bool:
            True  -> if number is prime
            False -> if number is not prime
    """

    if num <= 1:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    i = 3

    while i * i <= num:

        if num % i == 0:
            return False

        i += 2

    return True


"""
Problem Statement
-----------------
Write a Python program to find the 10,001st prime number.

A prime number is a number greater than 1
that has exactly two factors:
    1 and itself

Examples:
    2, 3, 5, 7, 11

Approach
--------
1. Start checking numbers from 2 onward.
2. Use the is_prime() function to check whether
   a number is prime.
3. Maintain a counter to count how many prime
   numbers have been found.
4. Continue until the count reaches 10,001.
5. Print the final prime number.

Variables Used
--------------
num:
    Stores the current number being checked.

count:
    Stores how many prime numbers have been found.

Time Complexity
---------------
Prime checking takes approximately O(sqrt(n))
because divisors are checked only up to sqrt(num).

Concepts Covered
----------------
- Functions
- Loops
- Conditional Statements
- Prime Number Logic
- Mathematical Optimization
- Boolean Returns
"""

num = 1
count = 0

while count < 10001:

    num += 1

    if is_prime(num):
        count += 1

print("10001st Prime Number:", num)