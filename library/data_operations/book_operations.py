# ./library/data_operations/book_operations.py

# Function to add a book
def add_book(book_list, title, author, year):
    book = {
        "title": title,
        "author": author,
        "year": year
    }
    book_list.append(book)
    return book_list

# Function to remove a book
def remove_book(book_list, title):
    book_to_remove = None
    for book in book_list:
        if book["title"] == title:
            book_to_remove = book
            break
    if book_to_remove:
        book_list.remove(book_to_remove)
    return book_list

# Function to update the year of a book
def update_book_year(book_list, title, new_year):
    for book in book_list:
        if book["title"] == title:
            book["year"] = new_year
            break
    return book_list

# Function to list all books
def list_books(book_list):
    return [book["title"] for book in book_list]

# Function to find a book by title
def find_book_by_title(book_list, title):
    for book in book_list:
        if book["title"] == title:
            return book
    return None

# Sample usage
# books = []
# add_book(books, "1984", "George Orwell", 1949)
# add_book(books, "Brave New World", "Aldous Huxley", 1932)
# print("Books after adding:", books)

# remove_book(books, "1984")
# print("Books after removing 1984:", books)

# update_book_year(books, "Brave New World", 1950)
# print("Books after updating year:", books)

# print("List of book titles:", list_books(books))

# print("Find book by title 'Brave New World':", find_book_by_title(books, "Brave New World"))
