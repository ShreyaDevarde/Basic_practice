def pythagorean_triplet():
    """
    Find the unique Pythagorean triplet (a, b, c) for which:

        a² + b² = c²
        a + b + c = 1000

    Problem Statement:
        A Pythagorean triplet consists of three positive integers
        (a, b, c) that satisfy the Pythagorean theorem:

            a² + b² = c²

        Given that the sum of the triplet is 1000, determine the
        product a × b × c.

    Approach:
        1. Iterate through possible values of 'a'.
        2. Iterate through possible values of 'b' where b > a.
        3. Calculate 'c' using:

               c = 1000 - a - b

        4. Check whether the triplet satisfies:

               a² + b² = c²

        5. Return the product a × b × c when the valid triplet is found.

    Returns:
        int:
            Product of the Pythagorean triplet satisfying the conditions.

    Example:
        Triplet:
            a = 200
            b = 375
            c = 425

        Product:
            200 × 375 × 425 = 31875000

    Time Complexity:
        O(n²)

    Space Complexity:
        O(1)
    """

    for a in range(1, 1000):
        for b in range(a + 1, 1000):
            c = 1000 - a - b

            if a**2 + b**2 == c**2:
                return a * b * c


print("The product of the Pythagorean triplet is:", pythagorean_triplet())