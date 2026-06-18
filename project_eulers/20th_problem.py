"""
Problem Statement:
Find the sum of the digits in the factorial of 100.

A factorial of a number n (denoted as n!) is the product of all positive
integers from 1 to n. For example:

    10! = 10 × 9 × 8 × ... × 2 × 1 = 3628800

The task is to compute 100! and determine the sum of all digits
present in the resulting number.

Approach:
1. Calculate the factorial of 100 using iterative multiplication.
2. Extract each digit of the factorial using modulo (%) and integer
   division (//) operations.
3. Accumulate the extracted digits to compute their total sum.
4. Print the factorial value and the final digit sum.

Expected Output:
- The value of 100!
- The sum of the digits of 100!, which is 648.
"""
num = 100
fact  = 1
sum = 0
for i in range(1, num + 1):
    fact *= i  
print(fact)  
while fact > 0:
    sum += fact % 10  
    fact //= 10      
print("Sum will be:",sum) 