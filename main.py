# Answers to Lesson 5

# Exercise 1: Basic Error Handling
print("\n\rExercise 1: Basic Error Handling")

# 1. Write a program that takes a book title and author as input and adds the book to the library. 
# Use a try-except block to handle errors when the title or author is missing.

print("\n\r1. Adding a book to the library with error handling for missing title or author:")

def add_book_to_library(title, author, books):
    try:
        if not title or not author:
            raise ValueError("Both title and author are required.")
        books.append({"title": title, "author": author})
        print(f"Book added: {title} by {author}")
    except ValueError as e:
        print(f"Error: {e}")

books = []
title = input("Enter the book title: ")
author = input("Enter the book author: ")
add_book_to_library(title, author, books)
print(books)


# Exercise 2: Catching Specific Exceptions
print("\n\rExercise 2: Catching Specific Exceptions")

# 1. Write a program that takes a list of book titles and authors as input and prints each book's details.
# Use try-except blocks to handle invalid input and type errors.

print("\n\r1. Printing book details with error handling for invalid input and type errors:")

def print_book_details(book_list):
    try:
        for book in book_list:
            if not isinstance(book, dict) or 'title' not in book or 'author' not in book:
                raise TypeError("Each book must be a dictionary with 'title' and 'author' keys.")
            print(f"Title: {book['title']}, Author: {book['author']}")
    except TypeError as e:
        print(f"Error: {e}")

book_list = [
    {"title": "1984", "author": "George Orwell"},
    {"title": "Brave New World", "author": "Aldous Huxley"},
    "Invalid Book"
]

print_book_details(book_list)


# Exercise 3: Raising Exceptions
print("\n\rExercise 3: Raising Exceptions")

# 1. Write a function that takes a book title as input and checks if it contains only letters and spaces.
# Raise a custom exception if the title contains any other characters.

print("\n\r1. Checking book title for valid characters and raising a custom exception:")

class InvalidTitleError(Exception):
    pass

def check_book_title(title):
    if not all(char.isalpha() or char.isspace() for char in title):
        raise InvalidTitleError("The title can only contain letters and spaces.")
    return "Title is valid."

try:
    title = input("Enter the book title: ")
    print(check_book_title(title))
except InvalidTitleError as e:
    print(f"Error: {e}")


# Exercise 4: Debugging with VS Code
print("\n\rExercise 4: Debugging with VS Code")

# 1. Use the VS Code debugger to debug the provided example code.
# Set breakpoints, inspect variables, and step through the code to identify and fix the division by zero error.

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
# 1. Set a breakpoint by clicking in the gutter next to the line number where result = divide(x, y) is.
# 2. Open the Run and Debug view by clicking the Debug icon in the Activity Bar.
# 3. Click the Run and Debug button, or press F5 to start debugging.
# 4. Step through the code, inspect variables, and use the debug console to troubleshoot the issue.