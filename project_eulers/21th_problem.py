"""
Problem Statement:
Evaluate the sum of all amicable numbers under 10,000.

Definition:
Let d(n) be the sum of the proper divisors of n (all positive divisors
excluding n itself).

If:
    d(a) = b
    d(b) = a
and a ≠ b,

then a and b are called an amicable pair, and both numbers are
considered amicable numbers.

Example:
The proper divisors of 220 are:
    1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110

Their sum is:
    d(220) = 284

The proper divisors of 284 are:
    1, 2, 4, 71, 142

Their sum is:
    d(284) = 220

Since:
    d(220) = 284
    d(284) = 220
    220 ≠ 284

(220, 284) is an amicable pair.

Objective:
Find all amicable numbers less than 10,000 and calculate their total sum.

Solution Approach:
1. Create a function `sum_of_divisors(n)` to calculate the sum of
   proper divisors of a number.
2. Iterate through numbers from 2 to 9,999.
3. For each number:
   - Find its partner using d(n).
   - Verify that d(partner) equals the original number.
   - Ensure the pair is not a perfect number (partner ≠ number).
4. Use a set to track already processed amicable numbers and avoid
   counting pairs multiple times.
5. Add both members of each amicable pair to the running total.
6. Print all discovered amicable pairs and the final sum.

Expected Result:
The sum of all amicable numbers under 10,000 is:

    31626
"""
def sum_of_divisors(n):
    total = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total


visited = set()
total = 0   

for num in range(2, 10000):
    if num not in visited:
        partner = sum_of_divisors(num)

        if partner != num and sum_of_divisors(partner) == num:
            print(num, partner)
            
            total += num + partner   
            
            visited.add(num)
            visited.add(partner)

print("Sum of all amical numbers:", total)