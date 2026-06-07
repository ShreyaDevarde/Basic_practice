def triangle_number(n):
    """
    Calculate the nth triangular number.

    A triangular number is the sum of all natural numbers from 1 to n.

    Formula:
        T(n) = n * (n + 1) // 2

    Args:
        n (int): Position of the triangular number.

    Returns:
        int: The nth triangular number.

    Example:
        >>> triangle_number(5)
        15
    """
    return n * (n + 1) // 2


def count_divisors(n):
    """
    Count the total number of positive divisors of a given number.

    The function iterates only up to the square root of n for efficiency.
    For every divisor found, its complementary divisor is also counted.

    Example:
        n = 12
        Divisors = [1, 2, 3, 4, 6, 12]
        Total divisors = 6

    Args:
        n (int): Positive integer whose divisors are to be counted.

    Returns:
        int: Total number of divisors of n.

    Example:
        >>> count_divisors(12)
        6
    """
    count = 0

    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:

            # Perfect square case
            if i * i == n:
                count += 1
            else:
                count += 2

    return count


# Find the first triangular number with more than 500 divisors
num = 1

while True:
    tri = triangle_number(num)

    if count_divisors(tri) > 500:
        print("The first triangle number is:", tri)
        break

    num += 1