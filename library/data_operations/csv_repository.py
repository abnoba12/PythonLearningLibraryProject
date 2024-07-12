# csv_repository.py

import csv

filename = "library_books.csv"

# Function to add a book to a CSV file
def add_book(title, author, year):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([title, author, year])

# Function to list books from a CSV file
def list_books():
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if(row != None):
                print(row)

# Function to update book year in a CSV file
def update_book_year(title, new_year):
    books = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == title:
                books.append([row[0], row[1], new_year])
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
