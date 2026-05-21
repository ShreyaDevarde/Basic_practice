"""
Problem: Even Fibonacci Numbers

Description:
Find the sum of all even-valued Fibonacci numbers 
that do not exceed a given limit.

Approach:
- Generate Fibonacci sequence iteratively
- Check if each number is even
- Add even numbers to the total sum

Time Complexity: O(n)
Space Complexity: O(1)
"""
def even_fibonacci_sum(limit):
    a, b = 1, 2
    total = 0

    while a < limit:
        if a % 2 == 0:
            total += a
        a, b = b, a + b

    return total


if __name__ == "__main__":
    result = even_fibonacci_sum(4000000)
    print("Sum of even Fibonacci numbers below 4,000,000:", result)