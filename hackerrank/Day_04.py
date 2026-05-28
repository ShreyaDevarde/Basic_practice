class Person:
    """ A class is a blueprint for creating objects.

    An instance is an individual object created from the class.
    Each instance stores its own separate data using instance variables.
    """
    """
    Represents a person with age-related behaviors.

    This class demonstrates the use of:
    - Instance variables
    - Constructors
    - Object methods
    - Conditional logic

    Attributes:
        initialAge (int):
            Stores the current age of the person.
    """

    def __init__(self, initialAge):
        """
        Initialize a Person object.

        Args:
            initialAge (int):
                The starting age of the person.

        Behavior:
            - Stores the given age.
            - If the age is negative, prints a warning message
              and sets age to 0.
        """

        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
            self.initialAge = 0
        else:
            self.initialAge = initialAge

    def amIOld(self):
        """
        Determine and print the age category of the person.

        Categories:
            - Young: age < 13
            - Teenager: 13 <= age < 18
            - Old: age >= 18
        """

        if self.initialAge < 13:
            print("You are young.")

        elif 13 <= self.initialAge < 18:
            print("You are a teenager.")

        else:
            print("You are old.")

    def yearPasses(self):
        """
        Increase the person's age by 1 year.

        This method simulates the passing of one year.
        """

        self.initialAge += 1


# Driver Code
t = int(input("Enter number of test cases: "))

for i in range(t):

    age = int(input("Enter age: "))

    # Create object (instance) of Person class
    p = Person(age)

    p.amIOld()

    # Simulate passing of 3 years
    for j in range(3):
        p.yearPasses()

    p.amIOld()

    print()