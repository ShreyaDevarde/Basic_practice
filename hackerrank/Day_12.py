"""
Problem: Day 12 - Inheritance (HackerRank 30 Days of Code)

Objective:
Demonstrate inheritance by creating a Student class that extends
the Person class.

The Person class contains:
- firstName
- lastName
- idNumber

The Student class should:
1. Inherit all properties and methods from Person.
2. Store a list of test scores.
3. Calculate the student's grade based on the average score.

Grade Scale:
90 - 100 : O (Outstanding)
80 - 89  : E (Exceeds Expectations)
70 - 79  : A (Acceptable)
55 - 69  : P (Poor)
40 - 54  : D (Dreadful)
0  - 39  : T (Troll)

Approach:
1. Use inheritance to derive Student from Person.
2. Call the parent constructor using super().
3. Store the scores list in the Student object.
4. Calculate the average score.
5. Return the corresponding grade according to the grading scale.

Concepts Covered:
- Inheritance
- Constructors
- super() function
- Method implementation in derived classes

Time Complexity:
O(n), where n is the number of scores.

Space Complexity:
O(n), for storing the scores list.
"""
class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):

    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        avg = sum(self.scores) / len(self.scores)

        if 90 <= avg <= 100:
            return 'O'
        elif 80 <= avg < 90:
            return 'E'
        elif 70 <= avg < 80:
            return 'A'
        elif 55 <= avg < 70:
            return 'P'
        elif 40 <= avg < 55:
            return 'D'
        else:
            return 'T'


line = input("Enter firstname lastname and IDnumber:").split()
firstName = line[0]
lastName = line[1]
idNum = line[2]

numScores = int(input("Enter num of Scores:"))
scores = list(map(int, input("Enter Scores:").split()))

s = Student(firstName, lastName, idNum, scores)

s.printPerson()
print("Grade:", s.calculate())