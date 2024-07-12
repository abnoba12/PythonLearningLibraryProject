# book_operations.py

book_list = [
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932}
]

# Exercise 1: Basic Error Handling
def add_book(title, author, year):
    try:
        if not title or not author:
            raise ValueError("Both title and author are required.")
        book = {
            "title": title,
            "author": author,
            "year": year
        }
        book_list.append(book)
        return f"Book added: {title}, {author}, {year}"
    except ValueError as e:
        return f"Error: {e}"
    
# Sample usage
# books = []
# print(add_book(books, "1984", "George Orwell", 1949))
# print(add_book(books, "", "George Orwell", 1949))
# print(add_book(books, "Brave New World", "", 1932))
# print("Books list:", books)




# Exercise 2: Catching Specific Exceptions
def print_book_details():
    try:
        for book in book_list:
            if not isinstance(book, dict) or 'title' not in book or 'author' not in book or 'year' not in book:
                raise TypeError("Each book must be a dictionary with 'title', 'author', and 'year' keys.")
            print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")
    except TypeError as e:
        print(f"Error: {e}")

# Sample usage
# books = [
#     {"title": "1984", "author": "George Orwell", "year": 1949},
#     {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932},
#     "Invalid Book"
# ]
# print_book_details(books)




# Exercise 3: Raising Exceptions
class InvalidYearError(Exception):
    pass

def check_book_year(book):
    year = book.get('year', '')
    if not str(year).isdigit():
        raise InvalidYearError("The year must contain only numbers.")
    return "Year is valid."

# Sample usage
# books = [
#     {"title": "1984", "author": "George Orwell", "year": 1949},
#     {"title": "Brave New World", "author": "Aldous Huxley", "year": "Nineteen Thirty-Two"}
# ]
# try:
#     print(check_book_year(books[0]))
#     print(check_book_year(books[1]))
# except InvalidYearError as e:
#     print(f"Error: {e}")


def remove_book(title):
    for book in book_list:
        if book['title'] == title:
            book_list.remove(book)
            return f"Book '{title}' removed."
    return f"Book '{title}' not found."

def update_book_year(title, new_year):
    for book in book_list:
        if book['title'] == title:
            book['year'] = new_year
            return f"Year updated for book '{title}' to {new_year}."
    return f"Book '{title}' not found."

def list_books():
    return [book['title'] for book in book_list]

def find_book_by_title(title):
    for book in book_list:
        if book['title'] == title:
            return book
    return None
