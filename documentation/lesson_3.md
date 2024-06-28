# Lesson 3: Functions and Modules

## Objective
The objective of this lesson is to teach students how to define and use functions in Python, and how to organize code into modules. By the end of this lesson, students will understand how to create reusable code blocks and structure their projects using modules.

## Key Points

1. **Function Definition and Calling**
   - What is a function and why use them?
   - Defining a function using the `def` keyword.
   - Calling a function.
   - Function parameters and return values.

2. **Parameters and Return Values**
   - Positional and keyword arguments.
   - Default parameter values.
   - Returning values from functions.

3. **Importing and Organizing Code into Modules**
   - What is a module?
   - Creating and importing modules.
   - Using `import` statements to include modules.
   - Organizing code for better readability and maintenance.

## Lesson Content

### 1. Function Definition and Calling

**Discussion Points:**
- Functions are reusable blocks of code that perform a specific task.
- Functions help in organizing code, making it more readable and maintainable.

**Examples:**
```python
# Function definition
def greet(name):
    print(f"Hello, {name}!")

# Function calling
greet("Alice")
greet("Bob")
```

**Further Reading:**
- [Python Functions](https://www.w3schools.com/python/python_functions.asp) on W3Schools

### 2. Parameters and Return Values

**Discussion Points:**
- Functions can take parameters (arguments) to work with different inputs.
- Functions can return values using the `return` statement.

**Examples:**
```python
# Function with parameters and return value
def add(a, b):
    return a + b

result = add(3, 5)
print(result)

# Function with default parameter values
def greet(name, message="Hello"):
    print(f"{message}, {name}!")

greet("Alice")
greet("Bob", "Hi")
```

**Further Reading:**
- [Python Function Arguments](https://www.w3schools.com/python/python_functions_arguments.asp) on W3Schools
- [Python Return Values](https://www.w3schools.com/python/gloss_python_function_return.asp) on W3Schools

### 3. Importing and Organizing Code into Modules

**Discussion Points:**
- A module is a file containing Python code that can be imported and used in other Python files.
- Modules help in organizing code by separating it into different files based on functionality.

**Examples:**
```python
# utils.py
def add(a, b):
    return a + b

def greet(name, message="Hello"):
    print(f"{message}, {name}!")
```

```python
# main.py
from utils import add, greet

result = add(3, 5)
print(result)

greet("Alice")
greet("Bob", "Hi")
```

**Further Reading:**
- [Python Modules](https://www.w3schools.com/python/python_modules.asp) on W3Schools
- [Python import Statement](https://www.programiz.com/python-programming/modules#import) on Programiz

## Exercises

**Exercise 1: Function Definition and Calling**
1. Define a function `multiply` that takes two numbers as parameters and prints their product.
2. Call the `multiply` function with different sets of numbers.

**Exercise 2: Parameters and Return Values**
1. Define a function `is_even` that takes a number as a parameter and returns `True` if the number is even, `False` otherwise.
2. Define a function `square` that takes a number as a parameter and returns its square.

**Exercise 3: Importing and Organizing Code into Modules**
1. Create a module `math_utils.py` and define functions `add`, `subtract`, `multiply`, and `divide`.
2. Import the `math_utils` module in a new file `main.py` and use the functions defined in the module.

## Summary

By the end of Lesson 3, students should be comfortable with defining and using functions in Python, understanding function parameters and return values, and organizing their code into modules for better readability and maintainability. These skills are essential for writing clean, efficient, and reusable code.
