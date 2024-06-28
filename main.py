# Answers to Lesson 3

# Exercise 1: Function Definition and Calling
print("\n\rExercise 1: Function Definition and Calling")

# Define a function multiply that takes two numbers as parameters and prints their product.
def multiply(a, b):
    print(a * b)

# Call the multiply function with different sets of numbers
print("Calling multiply(2, 3):")
multiply(2, 3)  # Output: 6

print("\n\rCalling multiply(4, 5):")
multiply(4, 5)  # Output: 20

print("\n\rCalling multiply(7, 8):")
multiply(7, 8)  # Output: 56


# Exercise 2: Parameters and Return Values
print("\n\rExercise 2: Parameters and Return Values")

# Define a function is_even that takes a number as a parameter and returns True if the number is even, False otherwise.
def is_even(number):
    return number % 2 == 0

# Define a function square that takes a number as a parameter and returns its square.
def square(number):
    return number ** 2

# Test the is_even function
print("Testing is_even function:")
print("is_even(4):", is_even(4))  # Output: True
print("is_even(7):", is_even(7))  # Output: False

# Test the square function
print("\n\rTesting square function:")
print("square(3):", square(3))  # Output: 9
print("square(5):", square(5))  # Output: 25


# Exercise 3: Importing and Organizing Code into Modules
print("\n\rExercise 3: Importing and Organizing Code into Modules")


# Pulled from file ./library/math_utils.py
from library.math_utils import add, subtract, multiply, divide

# Test the add function
print("Testing add function:")
print("add(10, 5):", add(10, 5))  # Output: 15

# Test the subtract function
print("\n\rTesting subtract function:")
print("subtract(10, 5):", subtract(10, 5))  # Output: 5

# Test the multiply function
print("\n\rTesting multiply function:")
print("multiply(10, 5):", multiply(10, 5))  # Output: 50

# Test the divide function
print("\n\rTesting divide function:")
print("divide(10, 5):", divide(10, 5))  # Output: 2.0
print("divide(10, 0):", divide(10, 0))  # Output: "Cannot divide by zero"
