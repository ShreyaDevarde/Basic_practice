"""
Problem: Sum of multiples of 3 or 5

Description:
Calculate the sum of all natural numbers below 1000
that are divisible by 3 or 5.

Approach:
- Iterate from 1 to 999
- Check if number is divisible by 3 or 5
- Add it to total sum

Time Complexity: O(n)
Space Complexity: O(1)
"""
def sum_of_multiples(limit):
    total = 0
    for i in range(1, limit):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total


if __name__ == "__main__":
    result = sum_of_multiples(1000)
    print("Sum of multiples of 3 or 5 below 1000:",result)