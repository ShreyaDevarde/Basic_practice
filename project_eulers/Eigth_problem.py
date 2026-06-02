"""
Problem: Largest Product in a Series

Description:
Given a very large number represented as a string, find the greatest product
that can be obtained from 13 consecutive digits.

Why is the number stored as a string?
- The number contains thousands of digits.
- Storing it as a string allows us to easily access individual digits
  using indexing without worrying about integer size limitations.

Approach:
1. Initialize a variable `max_prod` to store the maximum product found so far.
2. Define `digit = 13` because we need to examine groups of 13 consecutive digits.
3. Use a sliding window approach:
   - Start from the first digit.
   - Take 13 consecutive digits at a time.
   - Calculate the product of those 13 digits.
4. Compare the calculated product with `max_prod`.
   - If the current product is larger, update `max_prod`.
5. Continue until all possible groups of 13 consecutive digits have been checked.
6. Print the largest product found.

Example:
For the number "12345" and digit length 2:

Possible groups:
- "12" -> 1 × 2 = 2
- "23" -> 2 × 3 = 6
- "34" -> 3 × 4 = 12
- "45" -> 4 × 5 = 20

Largest product = 20

Time Complexity:
- O(n * k)
  where:
    n = length of the number string
    k = number of consecutive digits (13)
- For every starting position, we calculate the product of 13 digits.

Space Complexity:
- O(1)
  Only a few variables are used regardless of input size.

Expected Output:
23514624000
(The largest product of 13 consecutive digits in the given series.)
"""

num = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

max_prod = 0
digit = 13

for i in range(len(num) - digit + 1):
    product = 1

    # Calculate the product of the current 13-digit window
    for j in range(digit):
        product *= int(num[i + j])

    # Update maximum product if a larger one is found
    if product > max_prod:
        max_prod = product

print("Maximum product:", max_prod)