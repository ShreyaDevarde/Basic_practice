"""
Project Euler Problem 14: Longest Collatz Sequence

Problem Statement:
------------------
The following iterative sequence is defined for any positive integer n:

    n → n / 2      if n is even
    n → 3n + 1     if n is odd

Using this rule, starting with 13, the sequence becomes:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

This sequence contains 10 terms.

The Collatz Conjecture states that every positive integer will eventually
reach 1, although this has not been formally proven for all integers.

Task:
-----
Determine which starting number, less than 1,000,000, produces the
longest Collatz sequence.

Approach:
---------
1. Iterate through every starting number from 1 to 1,000,000.
2. For each number:
   - Generate its Collatz sequence by repeatedly applying:
       * n = n // 2  (when n is even)
       * n = 3 * n + 1 (when n is odd)
   - Continue until the sequence reaches 1.
3. Store the generated sequence in a temporary list.
4. Compare the length of the current sequence with the longest sequence
   found so far.
5. If the current sequence is longer, update the longest sequence.
6. After processing all numbers, return the starting number that generated
   the longest sequence.

Key Observation:
----------------
The problem does not ask for the longest value encountered, but rather
the starting number that produces the greatest number of terms before
reaching 1.

Example:
--------
Starting Number: 13

Sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

Length: 10 terms

Expected Result:
----------------
Starting number under one million that produces the longest Collatz sequence:

837799

Time Complexity:
----------------
Approximately O(n × k)

where:
    n = 1,000,000 starting numbers
    k = average Collatz sequence length

Since sequences are recomputed repeatedly, this brute-force approach is
computationally expensive.

Space Complexity:
-----------------
O(m)

where:
    m = length of the longest sequence stored in memory.

Possible Optimization:
----------------------
Use memoization (caching previously computed sequence lengths) to avoid
recalculating the same Collatz chains multiple times. This reduces the
runtime significantly and is the preferred approach for large inputs.
"""
def longest_collatz_sequence(limit):
    longest_length = 0
    starting_number = 0

    for i in range(1, limit):
        n = i
        length = 0

        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            length += 1

        if length > longest_length:
            longest_length = length
            starting_number = i

    return starting_number
if __name__ == "__main__":
    limit = 1000000
    result = longest_collatz_sequence(limit)
    print(f"The starting number under {limit} that produces the longest Collatz sequence is: {result}")