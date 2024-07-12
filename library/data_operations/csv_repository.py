import csv

filename = "library_books.csv"

# Function to add a book to a CSV file
def add_book(book):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(book)

# Function to list books from a CSV file
def list_books():
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Function to update book year in a CSV file
def update_book_year(title, new_book):
    books = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == title:
                books.append(new_book)
            else:
                books.append(row)
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(books)

# Function to remove a book from a CSV file
def remove_book(title):
    books = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != title:
                books.append(row)
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(books)
