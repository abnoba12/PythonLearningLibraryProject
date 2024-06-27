import csv
from library.book import Book
from library.data_operations.base_operations import BaseOperations

class CsvOperations(BaseOperations):

    def create_book(self, title, author, year):
        books = self.read_books()
        books.append(Book(title, author, year))
        self.save_books(books)

    def read_books(self):
        books = []
        try:
            with open('data/books.csv', 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    books.append(Book(row[0], row[1], int(row[2])))
        except FileNotFoundError:
            pass
        return books

    def update_book(self, old_title, new_title, new_author, new_year):
        books = self.read_books()
        for book in books:
            if book.title == old_title:
                book.update(new_title, new_author, new_year)
                break
        self.save_books(books)

    def delete_book(self, title):
        books = self.read_books()
        books = [book for book in books if book.title != title]
        self.save_books(books)

    def save_books(self, books):
        with open('data/books.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Author", "Year"])
            for book in books:
                writer.writerow([book.title, book.author, book.year])
