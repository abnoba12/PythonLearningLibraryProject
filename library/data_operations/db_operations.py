import mysql.connector
from library.book import Book
from library.data_operations.base_operations import BaseOperations

class DbOperations(BaseOperations):

    def connect_db(self):
        return mysql.connector.connect(
            host="localhost",
            user="yourusername",
            password="yourpassword",
            database="library"
        )

    def create_book(self, title, author, year):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, author, year) VALUES (%s, %s, %s)", (title, author, year))
        conn.commit()
        conn.close()

    def read_books(self):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT title, author, year FROM books")
        books = [Book(row[0], row[1], row[2]) for row in cursor.fetchall()]
        conn.close()
        return books

    def update_book(self, old_title, new_title, new_author, new_year):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE books SET title=%s, author=%s, year=%s WHERE title=%s", (new_title, new_author, new_year, old_title))
        conn.commit()
        conn.close()

    def delete_book(self, title):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM books WHERE title=%s", (title,))
        conn.commit()
        conn.close()
