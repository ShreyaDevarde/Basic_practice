def summation_prime(num):
    """
    Problem:
    --------
    Check whether a given number is a Prime Number.

    A Prime Number is a number that:
    - Is greater than 1
    - Has exactly two factors: 1 and itself

    Examples:
    ----------
    2  -> Prime
    3  -> Prime
    5  -> Prime
    7  -> Prime
    9  -> Not Prime (divisible by 3)
    15 -> Not Prime (divisible by 3 and 5)

    Parameters:
    -----------
    num : int
        The number that needs to be checked.

    Returns:
    --------
    bool
        True  -> If the number is prime
        False -> If the number is not prime

    Solution / Logic:
    -----------------
    Step 1:
        Numbers less than 2 are not prime.
        Therefore return False.

    Step 2:
        Check whether the number is divisible by any value
        from 2 up to the square root of the number.

        Why only up to the square root?

        Example:
            num = 49

            Factors:
            1 × 49
            7 × 7

            √49 = 7

            If a factor exists larger than 7, a matching
            factor smaller than 7 must already exist.

            Therefore checking beyond the square root
            is unnecessary.

    Step 3:
        If any number divides num exactly
        (remainder becomes 0), then the number
        is not prime.

    Step 4:
        If no divisor is found, return True.

    Time Complexity:
    ----------------
    O(√n)

    Space Complexity:
    -----------------
    O(1)
    """

    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


"""
Main Program
============

Problem Statement:
------------------
Find the sum of all prime numbers below 2,000,000.

Example:
--------
Prime numbers below 10:
    2, 3, 5, 7

Sum:
    2 + 3 + 5 + 7 = 17

Approach:
---------
1. Start from 2 because:
   - 0 and 1 are not prime numbers.

2. Iterate through every number below 2,000,000.

3. For each number:
   - Call summation_prime().
   - If it returns True, add the number to total.

4. After all numbers are checked,
   print the final sum.

Dry Run:
--------
Suppose count = 10

Iteration 1:
    i = 2
    Prime? Yes
    total = 2

Iteration 2:
    i = 3
    Prime? Yes
    total = 5

Iteration 3:
    i = 4
    Prime? No
    total = 5

Iteration 4:
    i = 5
    Prime? Yes
    total = 10

Iteration 5:
    i = 6
    Prime? No
    total = 10

Iteration 6:
    i = 7
    Prime? Yes
    total = 17

Final Answer for count=10:
    17

Expected Output for count=2,000,000:
------------------------------------
142913828922

Time Complexity:
----------------
Prime check for one number:
    O(√n)

Checking all numbers up to N:
    O(N√N)

For N = 2,000,000 this is computationally expensive.

Better Solution:
----------------
The Sieve of Eratosthenes can solve the same problem
much faster with approximately:

    O(N log log N)

and is the preferred approach for finding all primes
within a large range.
"""

count = 2000000
total = 0

for i in range(2, count):
    if summation_prime(i):
        total += i

print("Result:", total)