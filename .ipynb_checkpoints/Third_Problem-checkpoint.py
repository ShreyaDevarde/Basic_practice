def prime_factors_unique(n: int) -> set[int]:
    factors = set()

    while n % 2 == 0:
        factors.add(2)
        n //= 2

    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            factors.add(factor)
            n //= factor   
        factor += 2

    if n > 2:
        factors.add(n)

    return factors

print(prime_factors_unique(600851475143))
