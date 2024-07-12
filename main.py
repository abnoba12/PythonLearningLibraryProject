# Answers to Lesson 3

# Exercise 1: Function Definition and Calling
print("\n\rExercise 1: Function Definition and Calling")

# 1. Define a function `remove_book` that takes a title as a parameter and removes the corresponding book from a list.
print("\n\r1. Define a function remove_book:")

def remove_book(book_list, title):
    for book in book_list:
        if book['title'] == title:
            book_list.remove(book)
            return f"Book '{title}' removed."
    return f"Book '{title}' not found."

# 2. Call the `remove_book` function with different book titles.
print("\n\rCalling remove_book with different book titles:")

books = [
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925}
]

print(remove_book(books, "1984"))
print(books)
print(remove_book(books, "The Catcher in the Rye"))
print(books)




# Exercise 2: Parameters and Return Values
print("\n\rExercise 2: Parameters and Return Values")

# 1. Define a function `update_book_year` that takes a title and a new year as parameters and updates the year of the book with the given title.
print("\n\r1. Define a function update_book_year:")

def update_book_year(book_list, title, new_year):
    for book in book_list:
        if book['title'] == title:
            book['year'] = new_year
            return f"Year updated for book '{title}' to {new_year}."
    return f"Book '{title}' not found."

# 2. Define a function `list_books` that returns a list of all book titles in the library.
print("\n\r2. Define a function list_books:")

def list_books(book_list):
    return [book['title'] for book in book_list]

# Test the functions
books = [
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932}
]

print(update_book_year(books, "1984", 1950))
print(books)
print(update_book_year(books, "The Great Gatsby", 1925))
print(books)
print("List of book titles:", list_books(books))


# Exercise 3: Importing and Organizing Code into Modules
# This library comes from ./library/data_operations/book_operations.py that you need to make
# main.py
from library.data_operations.book_operations import add_book, remove_book, update_book_year, list_books, find_book_by_title

books = [
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932}
]

# Add a book
add_book(books, "The Great Gatsby", "F. Scott Fitzgerald", 1925)
print("Books after adding 'The Great Gatsby':", books)

# Remove a book
print(remove_book(books, "1984"))
print("Books after removing '1984':", books)

# Update the year of a book
print(update_book_year(books, "Brave New World", 1950))
print("Books after updating year:", books)

# List all books
print("List of book titles:", list_books(books))

# Find a book by title
print("Find book by title 'Brave New World':", find_book_by_title(books, "Brave New World"))
