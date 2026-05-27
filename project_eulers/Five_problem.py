def find_gcd(a, b):
    """
    Calculate the Greatest Common Divisor (GCD) of two numbers.

    The GCD of two numbers is the largest number that divides both
    numbers without leaving a remainder.

    This function uses a simple trial division approach:
    - It checks all numbers from 1 up to the smaller of the two numbers.
    - If a number divides both 'a' and 'b', it is a common divisor.
    - The largest such number is returned as the GCD.

    Parameters:
    a (int): First positive integer
    b (int): Second positive integer

    Returns:
    int: The greatest common divisor of a and b
    """
    smallest = a if a < b else b
    gcd = 1

    for i in range(1, smallest + 1):
        if a % i == 0 and b % i == 0:
            gcd = i

    return gcd


def smallest_multiple(n):
    """
    Find the smallest positive number that is evenly divisible
    by all numbers from 1 to n.

    Problem Explanation:
    --------------------
    We need a number that can be divided by every number from 1 to n
    without leaving any remainder.

    This is equivalent to finding the Least Common Multiple (LCM)
    of all numbers from 1 to n.

    Approach:
    ---------
    - Start with 'multiple = 1'
    - Iterate from 1 to n
    - For each number 'i', update the multiple using:
        LCM(a, b) = (a * b) // GCD(a, b)
    - We use our custom 'find_gcd' function to avoid built-in functions

    Why this works:
    ---------------
    - Multiplying directly would create very large numbers
    - Dividing by GCD removes common factors
    - This ensures we get the smallest possible multiple

    Parameters:
    n (int): The upper limit (inclusive)

    Returns:
    int: The smallest number divisible by all numbers from 1 to n
    """
    multiple = 1

    for i in range(1, n + 1):
        gcd = find_gcd(multiple, i)
        multiple = (multiple * i) // gcd

    return multiple


# Main execution
if __name__ == "__main__":
    """
    Entry point of the program.

    Calls the smallest_multiple function with n = 20
    and prints the result.
    """
    result = smallest_multiple(20)
    print("Answer:", result)