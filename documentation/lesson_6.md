# Lesson 6: File Handling and CRUD Operations

## Objective
The objective of this lesson is to teach students how to handle files in Python and perform basic CRUD (Create, Read, Update, Delete) operations. By the end of this lesson, students will understand how to open, read, write, and close files, as well as how to manipulate data in files using CRUD operations.

## Key Points

1. **Introduction to File Handling**
   - Importance of file handling.
   - Different modes for opening files.
   - Using the open(), read(), write(), and close() functions.

2. **Reading and Writing Files**
   - Reading from files.
   - Writing to files.
   - Using with statements for better resource management.

3. **Basic CRUD Operations**
   - Creating and writing data to files.
   - Reading and displaying data from files.
   - Updating data in files.
   - Deleting data from files.

## Lesson Content

### 1. Introduction to File Handling

**Discussion Points:**
- File handling is essential for many applications that need to read from or write to files.
- Files can be opened in different modes: read ('r'), write ('w'), append ('a'), and more.
- Properly opening and closing files is crucial to avoid resource leaks.

**Examples:**
```python
# Opening and closing a file
file = open("example.txt", "w")
file.write("Hello, World!")
file.close()

# Using with statement to handle files
with open("example.txt", "r") as file:
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
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a test file.\n")

# Reading from a file
with open("example.txt", "r") as file:
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
filename = "example.txt"
create_file(filename, "Hello, World!\n")
print(read_file(filename))

update_file(filename, "This is an update.\n")
print(read_file(filename))

delete_file(filename)
```

**Further Reading:**
- [Python File Methods](https://www.programiz.com/python-programming/file-operation) on Programiz

## Exercises

**Exercise 1: Introduction to File Handling**
1. Write a program to open a file in write mode and write some text to it. Then, open the same file in read mode and display its content.

**Exercise 2: Reading and Writing Files**
1. Write a program that writes a list of strings to a file, each string on a new line. Then, read the file line by line and print each line.

**Exercise 3: Basic CRUD Operations**
1. Create a program that performs the following operations on a text file:
   - Create and write initial data to the file.
   - Read and display the data.
   - Update the file by appending new data.
   - Delete the file.

## Summary

By the end of Lesson 6, students should be comfortable with handling files in Python and performing basic CRUD operations. They will understand how to open, read, write, and close files using different methods and how to manage file resources efficiently. These skills are essential for applications that need to persist data between runs or manipulate data stored in files.
