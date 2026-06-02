"""
Problem:
--------
You are given multiple strings. For each string, separate the characters
based on their index positions:

1. Characters at even indexes (0, 2, 4, 6, ...)
2. Characters at odd indexes (1, 3, 5, 7, ...)

Then print:
    even-indexed characters + space + odd-indexed characters

Note:
-----
Python uses zero-based indexing.

Example:
--------
Input:
2
Hacker
Rank

Output:
Hce akr
Rn ak

Explanation:
------------
String: "Hacker"

Index:      0 1 2 3 4 5
Character:  H a c k e r

Even Index Characters:
    H, c, e
    Result = "Hce"

Odd Index Characters:
    a, k, r
    Result = "akr"

Output:
    Hce akr

------------------------------------------------------------

Approach:
---------
1. Read the number of test cases.
2. For each test case:
    a. Read the string.
    b. Create two empty lists:
       - even_index
       - odd_index
    c. Traverse the string using enumerate().
       enumerate() provides:
           - index position
           - character
    d. If index is even, store character in even_index.
    e. Otherwise, store character in odd_index.
3. Convert both lists into strings using "".join().
4. Print the even-indexed characters and odd-indexed characters.

------------------------------------------------------------

Dry Run:
--------
Input String:
    "Python"

Index:      0 1 2 3 4 5
Character:  P y t h o n

Iteration 1:
    i = 0
    char = 'P'
    0 % 2 == 0
    even_index = ['P']

Iteration 2:
    i = 1
    char = 'y'
    odd_index = ['y']

Iteration 3:
    i = 2
    char = 't'
    even_index = ['P', 't']

Iteration 4:
    i = 3
    char = 'h'
    odd_index = ['y', 'h']

Iteration 5:
    i = 4
    char = 'o'
    even_index = ['P', 't', 'o']

Iteration 6:
    i = 5
    char = 'n'
    odd_index = ['y', 'h', 'n']

Final:
    even_index = "Pto"
    odd_index  = "yhn"

Output:
    Pto yhn

------------------------------------------------------------

Time Complexity:
----------------
Let n be the length of the string.

For each string:
    O(n)

Since every character is visited exactly once.

------------------------------------------------------------

Space Complexity:
-----------------
O(n)

Because two lists are used to store the characters
from the original string.

------------------------------------------------------------

Concepts Used:
--------------
1. input()
2. for loop
3. enumerate()
4. if-else condition
5. List append()
6. String join()
7. String indexing
"""

t = int(input())

for _ in range(t):
    s = input().strip()
    even_chars = s[::2]
    odd_chars = s[1::2]

    print("Result:", even_chars, odd_chars)
