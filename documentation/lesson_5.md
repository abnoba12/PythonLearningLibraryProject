# Lesson 5: Error Handling and Debugging

## Objective
The objective of this lesson is to teach students how to handle errors and exceptions in Python, and how to use the debugger in Visual Studio Code (VS Code) to debug their programs. By the end of this lesson, students will understand how to use try-except blocks to manage errors gracefully, raise exceptions, and use the VS Code debugger to troubleshoot and fix issues in their code.

## Key Points

1. **Introduction to Error Handling**
   - Importance of error handling.
   - Common types of errors in Python.
   - Using try-except blocks to catch and handle exceptions.

2. **Catching Specific Exceptions**
   - How to catch specific types of exceptions.
   - Using multiple except blocks.
   - The else and finally clauses.

3. **Raising Exceptions**
   - How to raise exceptions using the `raise` keyword.
   - Creating custom exceptions.

4. **Debugging with VS Code**
   - Introduction to debugging.
   - Setting breakpoints.
   - Running the debugger.
   - Inspecting variables and the call stack.
   - Stepping through code.

## Lesson Content

### 1. Introduction to Error Handling

**Discussion Points:**
- Errors and exceptions are common in programming and can cause programs to crash.
- Error handling allows you to manage errors gracefully and continue the execution of the program.
- The try-except block is used to catch and handle exceptions.

**Examples:**
```python
# Basic error handling with try-except
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
```

**Further Reading:**
- [Python Try Except](https://www.w3schools.com/python/python_try_except.asp) on W3Schools

### 2. Catching Specific Exceptions

**Discussion Points:**
- You can catch specific types of exceptions to handle different errors in different ways.
- Multiple except blocks can be used to catch different exceptions.
- The else block executes if no exceptions are raised.
- The finally block executes regardless of whether an exception is raised or not.

**Examples:**
```python
# Catching specific exceptions and using else and finally
try:
    x = int(input("Enter a number: "))
    y = 10 / x
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
else:
    print(f"Result: {y}")
finally:
    print("Execution completed.")
```

**Further Reading:**
- [Handling Multiple Exceptions](https://realpython.com/python-exceptions/#handling-multiple-exceptions) on Real Python

### 3. Raising Exceptions

**Discussion Points:**
- You can raise exceptions using the `raise` keyword to indicate that an error has occurred.
- Custom exceptions can be created by subclassing the built-in Exception class.

**Examples:**
```python
# Raising exceptions and creating custom exceptions
def check_age(age):
    if age < 18:
        raise ValueError("Age must be at least 18.")
    return "Age is valid."

try:
    print(check_age(15))
except ValueError as e:
    print(f"Error: {e}")

# Creating a custom exception
class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom error.")
except CustomError as e:
    print(f"Caught custom error: {e}")
```

**Further Reading:**
- [Raising Exceptions](https://www.programiz.com/python-programming/exception-handling#raise) on Programiz

### 4. Debugging with VS Code

**Discussion Points:**
- Debugging is the process of identifying and fixing bugs in your code.
- VS Code provides powerful debugging tools that can help you troubleshoot and fix issues.

**Steps:**
1. **Setting Breakpoints:**
   - Click in the gutter next to the line number where you want to set a breakpoint.
   - A red dot will appear, indicating a breakpoint is set.

2. **Running the Debugger:**
   - Open the Run and Debug view by clicking the Debug icon in the Activity Bar on the side of the VS Code window.
   - Click the Run and Debug button, or press F5 to start debugging.
   - Choose the appropriate debug configuration for Python.

3. **Inspecting Variables and Call Stack:**
   - Use the VARIABLES section in the Debug view to inspect the values of variables at the current breakpoint.
   - Use the CALL STACK section to see the sequence of function calls that led to the current breakpoint.

4. **Stepping Through Code:**
   - Use the Step Over (F10), Step Into (F11), and Step Out (Shift+F11) buttons to navigate through your code.
   - Step Over runs the next line of code.
   - Step Into enters any function calls on the current line.
   - Step Out continues execution until the current function returns.

**Examples:**
```python
# Example code to debug
def divide(a, b):
    return a / b

def main():
    x = 10
    y = 0
    result = divide(x, y)
    print(result)

if __name__ == "__main__":
    main()
```

**Further Reading:**
- [Debugging in Visual Studio Code](https://code.visualstudio.com/docs/editor/debugging) on Visual Studio Code Docs

## Exercises

**Exercise 1: Basic Error Handling**
1. Write a program that takes two numbers as input and prints their division. Use a try-except block to handle division by zero errors.

**Exercise 2: Catching Specific Exceptions**
1. Write a program that takes a list of numbers as input and prints the square of each number. Use try-except blocks to handle invalid input and type errors.

**Exercise 3: Raising Exceptions**
1. Write a function that takes a string as input and checks if it contains only letters. Raise a custom exception if the string contains non-letter characters.

**Exercise 4: Debugging with VS Code**
1. Use the VS Code debugger to debug the provided example code. Set breakpoints, inspect variables, and step through the code to identify and fix the division by zero error.

## Summary

By the end of Lesson 5, students should be comfortable with handling errors and exceptions in Python and using the VS Code debugger to troubleshoot and fix issues in their code. They will understand how to use try-except blocks to catch and handle specific exceptions, how to use else and finally clauses, how to raise exceptions, including custom exceptions, and how to effectively use debugging tools in VS Code. These skills are essential for writing robust and error-tolerant programs and for efficiently troubleshooting and resolving issues during development.
