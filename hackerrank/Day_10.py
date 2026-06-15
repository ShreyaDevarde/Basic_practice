#!/bin/python3

"""
Problem: Binary Numbers

Given a decimal (base-10) integer, convert it to its binary (base-2)
representation and determine the maximum number of consecutive 1's
present in the binary number.

Example:
--------
Input:
13

Binary representation of 13:
1101

Consecutive 1's:
11 -> length = 2

Output:
2

Approach:
---------
1. Read the decimal number from the user.
2. Convert the number into binary using Python's bin() function.
3. Remove the '0b' prefix that Python adds to binary numbers.
4. Traverse each digit of the binary string:
   - If the digit is '1', increase the current count.
   - If the digit is '0', reset the count to 0.
5. Keep track of the maximum count encountered.
6. Print the maximum number of consecutive 1's.

Example Walkthrough:
--------------------
Input: 13

Binary: 1101

Iteration:
1 -> count = 1, max_count = 1
1 -> count = 2, max_count = 2
0 -> count = 0
1 -> count = 1

Final Answer: 2
"""

if __name__ == '__main__':

    # Read input number
    n = int(input("Enter the number:").strip())

    # Convert decimal number to binary
    binary_num = bin(n)

    # Remove '0b' prefix
    binary_num = binary_num.replace("0b", "")

    count = 0       # Current consecutive 1's count
    max_count = 0   # Maximum consecutive 1's found

    # Traverse binary digits
    for digit in binary_num:

        if digit == '1':
            count += 1
        else:
            count = 0

        if count > max_count:
            max_count = count

    print("maximum consicutives 1's found:",max_count)