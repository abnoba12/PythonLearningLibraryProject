# Lesson 6: File Handling and CRUD Operations

## Objective
The objective of this lesson is to teach students how to handle files in Python and perform basic CRUD (Create, Read, Update, Delete) operations within the context of the library application. By the end of this lesson, students will understand how to open, read, write, and close files, as well as how to manipulate data in files using CRUD operations, both in text and CSV formats.

## Key Points

1. **Introduction to File Handling**
   - Importance of file handling in a library application.
   - Different modes for opening files.
   - Using the open(), read(), write(), and close() functions.

2. **Reading and Writing Files**
   - Reading from files.
   - Writing to files.
   - Using with statements for better resource management.

3. **Basic CRUD Operations**
   - Creating and writing data to files (Create).
   - Reading and displaying data from files (Read).
   - Updating data in files (Update).
   - Deleting data from files (Delete).

4. **Using CSV Files**
   - Installing and importing the `csv` library.
   - Performing CRUD operations with CSV files.

## Lesson Content

### 1. Introduction to File Handling

**Discussion Points:**
- File handling is essential for many applications that need to read from or write to files, especially for storing and retrieving book data.
- Files can be opened in different modes: read ('r'), write ('w'), append ('a'), and more.
- Properly opening and closing files is crucial to avoid resource leaks.

**Examples:**
```python
# Opening and closing a file
file = open("library_books.txt", "w")
file.write("Title: 1984, Author: George Orwell, Year: 1949\n")
file.close()

# Using with statement to handle files
with open("library_books.txt", "r") as file:
    content = file.read()
    print(content)
```

**Further Reading:**
- [Python File Handling](https://www.w3schools.com/python/python_file_handling.asp) on W3Schools

### 2. Reading and Writing Files

**Discussion Points:**
- Reading from files using read(), readline(), and readlines() methods.
- Writing to files using write() and writelines() methods.
- The with statement ensures that files are properly closed after their suite finishes, even if an exception is raised.

**Examples:**
```python
# Writing to a file
with open("library_books.txt", "w") as file:
    file.write("Title: 1984, Author: George Orwell, Year: 1949\n")
    file.write("Title: Brave New World, Author: Aldous Huxley, Year: 1932\n")

# Reading from a file
with open("library_books.txt", "r") as file:
    content = file.read()
    print(content)
```

**Further Reading:**
- [Python Read Files](https://www.w3schools.com/python/python_file_open.asp) on W3Schools
- [Python Write/Create Files](https://www.w3schools.com/python/python_file_write.asp) on W3Schools

### 3. Basic CRUD Operations

**Discussion Points:**
- CRUD operations are fundamental for manipulating data stored in files.
- Creating and writing data to files (Create).
- Reading and displaying data from files (Read).
- Updating data in files (Update).
- Deleting data from files (Delete).

**Examples:**
```python
# Create and write data to a file
def create_file(filename, data):
    with open(filename, "w") as file:
        file.write(data)

# Read and display data from a file
def read_file(filename):
    with open(filename, "r") as file:
        return file.read()

# Update data in a file
def update_file(filename, new_data):
    with open(filename, "a") as file:
        file.write(new_data)

# Delete data from a file
def delete_file(filename):
    import os
    os.remove(filename)

# Example usage
filename = "library_books.txt"
create_file(filename, "Title: 1984, Author: George Orwell, Year: 1949\n")
print(read_file(filename))

update_file(filename, "Title: Brave New World, Author: Aldous Huxley, Year: 1932\n")
print(read_file(filename))

delete_file(filename)
```

**Further Reading:**
- [Python File Methods](https://www.programiz.com/python-programming/file-operation) on Programiz

### 4. Using CSV Files

**Discussion Points:**
- CSV (Comma-Separated Values) files are commonly used for storing tabular data.
- The `csv` library in Python provides functionality to read from and write to CSV files.
- Installing and importing the `csv` library.

**Installing the CSV Library:**
Python's `csv` library is built-in, so no installation is needed. Simply import it using:
```python
import csv
```

**Examples:**
```python
import csv

# Create a book and write to a CSV file
def create_book(filename, book):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(book)

# Read and display books from a CSV file
def read_books(filename):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Update book details in the CSV file
def update_book(filename, title, new_book):
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

# Delete a book from the CSV file
def delete_book(filename, title):
    books = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != title:
                books.append(row)
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(books)

# Example usage
filename = "library_books.csv"
create_book(filename, ["1984", "George Orwell", "1949"])
create_book(filename, ["Brave New World", "Aldous Huxley", "1932"])
print("Books after creation:")
read_books(filename)

update_book(filename, "1984", ["1984", "George Orwell", "1950"])
print("Books after update:")
read_books(filename)

delete_book(filename, "Brave New World")
print("Books after deletion:")
read_books(filename)
```

**Further Reading:**
- [Python CSV Module](https://www.w3schools.com/python/python_csv.asp) on W3Schools
- [Reading and Writing CSV Files in Python](https://realpython.com/python-csv/) on Real Python

## Exercises

**Exercise 1: Introduction to File Handling**
1. Write a program to open a file in write mode and write some text to it. Then, open the same file in read mode and display its content.

**Exercise 2: Reading and Writing Files**
1. Create a new file: ./library/data_operations/text_repository.py. Write all code for Exercise 2 in this file.
2. Create a new functions `add_book` that will write a book's details (title, author, year) to a file, each book on a new line. Then make another function `list_books` to read the file line by line and print each book's details.
3. Replace the current `add_book` and `list_books` functions in the main_menu with these two. 

**Exercise 3: Basic CRUD Operations**
1. Write all code for Exercise 3 in ./library/data_operations/text_repository.py
2. Create functions that perform the following operations on a text file storing book details:
   - C: Create and write a new book to the file `add_book`. This was completed in Exercise 2.
   - R: Read and display a list of book data `list_books`. This was completed in Exercise 2.
   - U: Update a single book's year by its title `update_book_year`. Replace the current `update_book_year` in the main menu.
   - D: Delete a single book by its title `remove_book`. Replace the current `remove_book` in the main menu.

**Exercise 4: Using CSV Files**
1. Write all code for Exercise 4 in ./library/data_operations/csv_repository.py
2. Write functions that performs the following CRUD operations on a CSV file storing book details. This is the same as Exercise 3, but for a CSV file this time.:
   - `add_book`: Add a book to the CSV file.
   - `list_books`: Read and display the books from the CSV file.
   - `update_book_year`: Update a book's year in the CSV file.
   - `remove_book`: Remove a book from the CSV file.

## Summary

By the end of Lesson 6, students should be comfortable with handling files in Python and performing basic CRUD operations. They will understand how to open, read, write, and close files using different methods and how to manage file resources efficiently. They will also learn how to work with CSV files, which are commonly used for storing and manipulating tabular data. These skills are essential for applications that need to persist data between runs or manipulate data stored in files, particularly for managing a library's book collection.
