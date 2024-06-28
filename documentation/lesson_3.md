# Lesson 3: Functions and Modules

## Objective
The objective of this lesson is to teach students how to define and use functions in Python, and how to organize code into modules within the context of building a library application. By the end of this lesson, students will understand how to create reusable code blocks and structure their projects using modules.

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
- Functions can be used to perform operations related to managing the library's book collection.

**Examples:**
```python
# Function definition
def add_book(title, author, year):
    print(f"Book added: {title}, {author}, {year}")

# Function calling
add_book("1984", "George Orwell", 1949)
add_book("Brave New World", "Aldous Huxley", 1932)
```

**Further Reading:**
- [Python Functions](https://www.w3schools.com/python/python_functions.asp) on W3Schools

### 2. Parameters and Return Values

**Discussion Points:**
- Functions can take parameters (arguments) to work with different inputs.
- Functions can return values using the `return` statement.
- Use functions to retrieve information about books or perform operations on book data.

**Examples:**
```python
# Function with parameters and return value
def find_book_by_title(title, book_list):
    for book in book_list:
        if book['title'] == title:
            return book
    return None

books = [
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932}
]

result = find_book_by_title("1984", books)
print(result)

# Function with default parameter values
def add_book(title, author, year=2023):
    print(f"Book added: {title}, {author}, {year}")

add_book("The Great Gatsby", "F. Scott Fitzgerald")
```

**Further Reading:**
- [Python Function Arguments](https://www.w3schools.com/python/python_functions_arguments.asp) on W3Schools
- [Python Return Values](https://www.w3schools.com/python/gloss_python_function_return.asp) on W3Schools

### 3. Importing and Organizing Code into Modules

**Discussion Points:**
- A module is a file containing Python code that can be imported and used in other Python files.
- Modules help in organizing code by separating it into different files based on functionality, such as book operations and user interactions.

**Examples:**
```python
# book_operations.py
def add_book(title, author, year):
    print(f"Book added: {title}, {author}, {year}")

def find_book_by_title(title, book_list):
    for book in book_list:
        if book['title'] == title:
            return book
    return None
```

```python
# main.py
from book_operations import add_book, find_book_by_title

books = [
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932}
]

add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
book = find_book_by_title("1984", books)
print(book)
```

**Further Reading:**
- [Python Modules](https://www.w3schools.com/python/python_modules.asp) on W3Schools
- [Python import Statement](https://www.programiz.com/python-programming/modules#import) on Programiz

## Exercises

**Exercise 1: Function Definition and Calling**
1. Define a function `remove_book` that takes a title as a parameter and removes the corresponding book from a list.
2. Call the `remove_book` function with different book titles.

**Exercise 2: Parameters and Return Values**
1. Define a function `update_book_year` that takes a title and a new year as parameters and updates the year of the book with the given title.
2. Define a function `list_books` that returns a list of all book titles in the library.

**Exercise 3: Importing and Organizing Code into Modules**
1. Create a module `library_utils.py` and define functions `add_book`, `remove_book`, `update_book_year`, and `list_books`.
2. Import the `library_utils` module in a new file `main.py` and use the functions defined in the module to manage a list of books.

## Summary

By the end of Lesson 3, students should be comfortable with defining and using functions in Python, understanding function parameters and return values, and organizing their code into modules for better readability and maintainability. These skills are essential for writing clean, efficient, and reusable code, especially when managing a library application.
