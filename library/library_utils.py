# library_utils.py

def add_book(title, author, year, book_list):
    book_list.append({"title": title, "author": author, "year": year})
    print(f"Book added: {title}, {author}, {year}")

def remove_book(title, book_list):
    for book in book_list:
        if book['title'] == title:
            book_list.remove(book)
            print(f"Book removed: {title}")
            return
    print(f"Book not found: {title}")

def update_book_year(title, new_year, book_list):
    for book in book_list:
        if book['title'] == title:
            book['year'] = new_year
            print(f"Updated book year: {title} to {new_year}")
            return
    print(f"Book not found: {title}")

def list_books(book_list):
    return [book['title'] for book in book_list]
