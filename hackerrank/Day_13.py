"""
Problem: Day 13 - Abstract Classes (HackerRank 30 Days of Code)

Objective:
Learn how to work with abstract classes and abstract methods in Python.

Given:
- An abstract class Book containing:
    - title
    - author
    - abstract method display()

Task:
Create a subclass MyBook that:
1. Inherits from Book.
2. Adds a price attribute.
3. Implements the abstract display() method.

The display() method should print:
Title: <title>
Author: <author>
Price: <price>

Approach:
1. Create MyBook as a subclass of Book.
2. Use super().__init__() to initialize title and author.
3. Store the price in the constructor.
4. Override the abstract display() method and print all
   required book details.

Concepts Covered:
- Abstract Classes
- Abstract Methods
- Inheritance
- Method Overriding
- super() Function

Time Complexity:
O(1)

Space Complexity:
O(1)
"""
from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass


#Write MyBook class
class MyBook(Book):

    def __init__(self, title, author, price):
        super().__init__(title, author)
        self.price = price

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)


title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()