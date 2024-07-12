# book_operations.py

def add_book(book_list, title, author, year):
    book = {
        "title": title,
        "author": author,
        "year": year
    }
    book_list.append(book)
    return book_list

def remove_book(book_list, title):
    for book in book_list:
        if book['title'] == title:
            book_list.remove(book)
            return f"Book '{title}' removed."
    return f"Book '{title}' not found."

def update_book_year(book_list, title, new_year):
    for book in book_list:
        if book['title'] == title:
            book['year'] = new_year
            return f"Year updated for book '{title}' to {new_year}."
    return f"Book '{title}' not found."

def list_books(book_list):
    return [book['title'] for book in book_list]

def find_book_by_title(book_list, title):
    for book in book_list:
        if book['title'] == title:
            return book
    return None
