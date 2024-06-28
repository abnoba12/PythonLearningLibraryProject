# Answers to Lesson 3

# Exercise 1: Function Definition and Calling
print("\n\rExercise 1: Function Definition and Calling")

# Define a function remove_book that takes a title as a parameter and removes the corresponding book from a list.
print("\n\r1. Define a function remove_book:")
def remove_book(title, book_list):
    for book in book_list:
        if book['title'] == title:
            book_list.remove(book)
            print(f"Book removed: {title}")
            return
    print(f"Book not found: {title}")

# Sample book list
books = [
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932}
]

# Call the remove_book function with different book titles.
print("\n\rCalling remove_book('1984'):")
remove_book("1984", books)
print("\n\rCalling remove_book('The Great Gatsby'):")
remove_book("The Great Gatsby", books)
print(books)



# Exercise 2: Parameters and Return Values
print("\n\rExercise 2: Parameters and Return Values")

# Define a function update_book_year that takes a title and a new year as parameters and updates the year of the book with the given title.
print("\n\r1. Define a function update_book_year:")
def update_book_year(title, new_year, book_list):
    for book in book_list:
        if book['title'] == title:
            book['year'] = new_year
            print(f"Updated book year: {title} to {new_year}")
            return
    print(f"Book not found: {title}")

# Sample book list
books = [
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932}
]

# Define a function list_books that returns a list of all book titles in the library.
print("\n\r2. Define a function list_books:")
def list_books(book_list):
    return [book['title'] for book in book_list]

# Update a book year and list all books
print("\n\rUpdating the year of '1984':")
update_book_year("1984", 1950, books)
print("\n\rListing all books:")
print(list_books(books))


# This library comes from ./library/library_utils that you need to make
from library.library_utils import add_book, remove_book, update_book_year, list_books

# Sample book list
books = [
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932}
]

# Test the add_book function
print("\n\rTesting add_book:")
add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925, books)

# Test the remove_book function
print("\n\rTesting remove_book:")
remove_book("1984", books)

# Test the update_book_year function
print("\n\rTesting update_book_year:")
update_book_year("Brave New World", 1935, books)

# Test the list_books function
print("\n\rTesting list_books:")
print(list_books(books))
