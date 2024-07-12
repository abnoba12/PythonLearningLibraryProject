# text_repository.py

# Create and write data to a file
filename = "library_books.txt"

def create_file(filename, data):
    with open(filename, "w") as file:
        file.write(data)

# Read and display data from a file
def read_file(filename):
    with open(filename, "r") as file:
        return file.read()

# Function to add a book
def add_book(title, author, year):
    with open(filename, "a") as file:
        file.write(f"Title: {title}, Author: {author}, Year: {year}\n")

# Function to list books
def list_books():
    with open(filename, "r") as file:
        for line in file:
            print(line.strip())

# Function to update book year
def update_book_year(title, new_year):
    lines = []
    with open(filename, "r") as file:
        lines = file.readlines()
    with open(filename, "w") as file:
        for line in lines:
            if title in line:
                parts = line.strip().split(", ")
                parts[-1] = f"Year: {new_year}"
                file.write(", ".join(parts) + "\n")
            else:
                file.write(line)

# Function to remove a book
def remove_book(title):
    lines = []
    with open(filename, "r") as file:
        lines = file.readlines()
    with open(filename, "w") as file:
        for line in lines:
            if title not in line:
                file.write(line)
