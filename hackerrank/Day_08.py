"""
Problem: Phone Book Lookup Using a Dictionary

Problem Statement:
------------------
You are given a list of people's names along with their phone numbers.
Your task is to store this information in a phone book and then answer
a series of lookup queries.

For each query:
    - If the person's name exists in the phone book, print their
      name and phone number in the format:
          name=phoneNumber
    - If the person's name does not exist, print:
          Not found

Input Format:
-------------
1. The first input contains an integer n, representing the number of
   entries in the phone book.

2. The next n lines each contain:
       name phoneNumber

3. After the phone book entries, an unknown number of queries follow.
   Each query consists of a single name.

4. Input ends when there is no more data to read (EOF - End of File).

Example Input:
--------------
3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry

Example Output:
---------------
sam=99912222
Not found
harry=12299933

Approach:
---------
1. Read the number of phone book entries.
2. Create an empty dictionary called `phone_book`.
3. Store each name as the key and the corresponding phone number as
   the value.
4. Continuously read query names until the end of input.
5. For each query:
      - Check whether the name exists in the dictionary.
      - If found, print the name and phone number.
      - Otherwise, print "Not found".
6. Use a try-except block to handle EOFError, which indicates that
   there are no more queries to process.

Why Dictionary?
---------------
A dictionary provides very fast lookups using keys.

Example:
    phone_book = {
        "sam": "99912222",
        "tom": "11122222"
    }

Searching for a name in a dictionary takes approximately O(1) time,
making it ideal for phone book applications.

Time Complexity:
----------------
Building the phone book: O(n)

Query lookup:
O(1) per query on average

Overall:
O(n + q)

where:
    n = number of phone book entries
    q = number of queries

Space Complexity:
-----------------
O(n)

because all phone book entries are stored in the dictionary.
"""
n = int(input("Enter the number of entries in the phone book: "))

phone_book = {}

for _ in range(n):
    name, number = input().split()
    phone_book[name] = number

while True:
    try:
        query = input()
        if query in phone_book:
            print(query + "=" + phone_book[query])
        else:
            print("Not found")
    except EOFError:
        break


