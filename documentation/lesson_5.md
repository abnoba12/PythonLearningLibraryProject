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
- The try-except block is used to catch and handle exceptions in the library application, such as when a book is not found.

**Examples:**
```python
# Basic error handling with try-except
def get_book_by_title(title, books):
    try:
        for book in books:
            if book['title'] == title:
                return book
        raise ValueError("Book not found")
    except ValueError as e:
        print(f"Error: {e}")

books = [
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932}
]

get_book_by_title("The Great Gatsby", books)
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
def add_book(book, books):
    try:
        if not isinstance(book, dict):
            raise TypeError("Book must be a dictionary")
        books.append(book)
    except TypeError as e:
        print(f"Error: {e}")
    else:
        print("Book added successfully")
    finally:
        print("Execution completed.")

books = []

add_book({"title": "1984", "author": "George Orwell", "year": 1949}, books)
add_book("Not a dictionary", books)
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
def check_book_year(year):
    if year < 1450 or year > 2024:
        raise ValueError("Year must be between 1450 and 2024")
    return "Year is valid."

try:
    print(check_book_year(2025))
except ValueError as e:
    print(f"Error: {e}")

# Creating a custom exception
class BookError(Exception):
    pass

def check_book_title(title):
    if not title:
        raise BookError("Title cannot be empty")

try:
    check_book_title("")
except BookError as e:
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
    try:
        result = divide(x, y)
        print(result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

if __name__ == "__main__":
    main()
```

**Further Reading:**
- [Debugging in Visual Studio Code](https://code.visualstudio.com/docs/editor/debugging) on Visual Studio Code Docs

## Exercises

**Exercise 1: Basic Error Handling**
1. Update add_book to use a try-except block to handle errors when the title or author is missing/blank.

**Exercise 2: Catching Specific Exceptions**
1. Create a function that can take a list of book as input and print each book's details. Use try-except blocks to handle invalid input and type errors.

**Exercise 3: Raising Exceptions**
1. Write a function that takes a book as input and checks if it's year contains only numbers. Raise a custom exception if the year contains any other characters.

**Exercise 4: Debugging with VS Code**
1. Use the VS Code debugger to debug the provided example code. Set breakpoints, inspect variables, and step through the code to identify and fix the division by zero error.

## Summary

By the end of Lesson 5, students should be comfortable with handling errors and exceptions in Python and using the VS Code debugger to troubleshoot and fix issues in their code. They will understand how to use try-except blocks to catch and handle specific exceptions, how to use else and finally clauses, how to raise exceptions, including custom exceptions, and how to effectively use debugging tools in VS Code. These skills are essential for writing robust and error-tolerant programs and for efficiently troubleshooting and resolving issues during development, especially within the context of building a library application.
