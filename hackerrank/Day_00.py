"""
stdin and stdout in Python

stdin (Standard Input):
- stdin is the input stream used by a program to receive data.
- By default, input comes from the keyboard.
- In Python, input() reads from stdin.
- For faster input (large data), sys.stdin.readline() is used.

Example:
x = input()

stdout (Standard Output):
- stdout is the output stream used to display results.
- By default, output is shown on the screen.
- In Python, print() writes to stdout.
- For faster output, sys.stdout.write() is used.

Example:
print(x)

Flow:
stdin → Program → stdout

stdin = data enters program
stdout = results leave program
"""
# Read a full line of input from stdin and save it to our dynamically typed variable, input_string.
input_string = input()

# Print a string literal saying "Hello, World." to stdout.
print('Hello, World.')

# TODO: Write a line of code here that prints the contents of input_string to stdout.
print(input_string)
