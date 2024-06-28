# Answers to Lesson 5

# Exercise 1: Basic Error Handling
print("\n\rExercise 1: Basic Error Handling")

# Write a program that takes two numbers as input and prints their division. Use a try-except block to handle division by zero errors.
print("\n\r1. Division of two numbers with error handling for division by zero:")
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
    print(f"The result of the division is: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid numbers.")


# Exercise 2: Catching Specific Exceptions
print("\n\rExercise 2: Catching Specific Exceptions")

# Write a program that takes a list of numbers as input and prints the square of each number. Use try-except blocks to handle invalid input and type errors.
print("\n\r1. Print the square of each number in a list with error handling:")
try:
    numbers = input("Enter a list of numbers separated by spaces: ").split()
    numbers = [float(num) for num in numbers]
    for num in numbers:
        print(f"The square of {num} is {num ** 2}")
except ValueError:
    print("Error: Please enter valid numbers.")


# Exercise 3: Raising Exceptions
print("\n\rExercise 3: Raising Exceptions")

# Write a function that takes a string as input and checks if it contains only letters. Raise a custom exception if the string contains non-letter characters.
print("\n\r1. Check if a string contains only letters and raise a custom exception if it contains non-letter characters:")

class NonLetterError(Exception):
    pass

def check_only_letters(input_string):
    if not input_string.isalpha():
        raise NonLetterError("The string contains non-letter characters.")
    return "The string contains only letters."

try:
    input_string = input("Enter a string: ")
    result = check_only_letters(input_string)
    print(result)
except NonLetterError as e:
    print(f"Error: {e}")


# Exercise 4: Debugging with VS Code
print("\n\rExercise 4: Debugging with VS Code")

# Use the VS Code debugger to debug the provided example code. Set breakpoints, inspect variables, and step through the code to identify and fix the division by zero error.

print("\n\r1. Debug the provided example code:")

def divide(a, b):
    return a / b

def main():
    x = 10
    y = 0
    try:
        result = divide(x, y)
        print(result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

if __name__ == "__main__":
    main()

# To debug this code in Visual Studio Code:

# Set a breakpoint by clicking in the gutter next to the line number where result = divide(x, y) is.
# Open the Run and Debug view by clicking the Debug icon in the Activity Bar.
# Click the Run and Debug button, or press F5 to start debugging.
# Step through the code, inspect variables, and use the debug console to troubleshoot the issue.