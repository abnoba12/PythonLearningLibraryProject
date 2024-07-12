# Lesson 7: Classes, Interfaces, and Data Storage

## Objective
The objective of this lesson is to teach students how to define and use interfaces in Python, understand the concepts of classes and objects, implement methods and attributes, create a menu-driven interface around CRUD operations, and switch between file-based (text and CSV) and database-based data storage in the context of the library application. By the end of this lesson, students will understand how to use interfaces to abstract different data storage implementations and toggle between them seamlessly.

## Key Points

1. **Classes and Objects**
   - Introduction to classes and objects.
   - Creating a class.
   - Creating objects from a class.
   - Understanding constructors.
   - Introduction to encapsulation.

2. **Methods and Attributes**
   - Defining methods and attributes in a class.
   - Understanding instance methods and class methods.
   - Using `self` to access instance attributes and methods.
   - Passing by reference vs. passing by value in Python.
   - Access control: public and private methods.

3. **Introduction to Interfaces**
   - What is an interface?
   - Importance of using interfaces in programming.
   - How to define and use interfaces in Python.

4. **Implementing Interfaces for CRUD Operations**
   - Defining a CRUD interface.
   - Implementing the CRUD interface for text file storage.
   - Implementing the CRUD interface for CSV file storage.
   - Implementing the CRUD interface for database storage.

5. **Switching Between Different Data Storages**
   - Using a factory pattern to select the data storage method.
   - Configuration file to set the desired storage type.
   - Updating the main menu to toggle between different storage methods.

## Lesson Content

### 1. Classes and Objects

**Discussion Points:**
- A class is a blueprint for creating objects (instances).
- An object is an instance of a class.
- Classes encapsulate data and functions that operate on that data.
- A constructor is a special method that is automatically called when an object is created. It initializes the object's attributes.
- Encapsulation refers to bundling data and methods that operate on the data within one unit, like a class, and restricting access to some of the object's components.

**Examples:**
```python
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

# Creating an object from the Book class
book1 = Book("1984", "George Orwell", 1949)
print(book1.title, book1.author, book1.year)
```

**Further Reading:**
- [Python Classes and Objects](https://www.w3schools.com/python/python_classes.asp) on W3Schools
- [Python Constructors](https://www.geeksforgeeks.org/constructors-in-python/) on GeeksforGeeks
- [Encapsulation in Python](https://www.programiz.com/python-programming/object-oriented-programming) on Programiz

### 2. Methods and Attributes

**Discussion Points:**
- Methods are functions defined within a class.
- Attributes are variables defined within a class.
- The `self` keyword is used to refer to instance attributes and methods from within the class.
- In Python, arguments are passed by assignment, which is essentially a mix of passing by reference and passing by value.
- Access control in Python is achieved through naming conventions: a single underscore (`_`) for protected members and a double underscore (`__`) for private members.

**Examples:**
```python
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"

# Creating an object and calling a method
book1 = Book("1984", "George Orwell", 1949)
print(book1.display_info())

# Passing by reference example
def update_year(book, new_year):
    book.year = new_year

update_year(book1, 1950)
print(book1.display_info())

# Access control example
class Book:
    def __init__(self, title, author, year):
        self.__title = title  # private attribute
        self.author = author
        self.year = year

    def display_info(self):
        return f"Title: {self.__title}, Author: {self.author}, Year: {self.year}"

    def set_title(self, title):
        self.__title = title

book1 = Book("1984", "George Orwell", 1949)
print(book1.display_info())
book1.set_title("Animal Farm")
print(book1.display_info())
```

**Further Reading:**
- [Python Methods](https://www.w3schools.com/python/python_methods.asp) on W3Schools
- [Pass by Reference or Value](https://realpython.com/python-pass-by-reference/) on Real Python
- [Access Modifiers in Python](https://www.tutorialsteacher.com/python/public-private-protected-modifiers) on TutorialsTeacher

### 3. Introduction to Interfaces

**Discussion Points:**
- An interface is a blueprint for classes that defines methods without implementing them.
- Interfaces ensure that different classes provide the same set of methods, allowing them to be used interchangeably.
- In Python, interfaces can be implemented using abstract base classes (ABCs) from the `abc` module.

**Examples:**
```python
from abc import ABC, abstractmethod

class CRUDInterface(ABC):
    @abstractmethod
    def add_book(self, title, author, year):
        pass

    @abstractmethod
    def list_books(self):
        pass

    @abstractmethod
    def update_book_year(self, title, new_year):
        pass

    @abstractmethod
    def remove_book(self, title):
        pass
```

**Further Reading:**
- [Abstract Base Classes in Python](https://docs.python.org/3/library/abc.html) on Python.org

### 4. Implementing Interfaces for CRUD Operations

**Discussion Points:**
- Implement the CRUD interface for text file storage.
- Implement the CRUD interface for CSV file storage.
- Implement the CRUD interface for database storage.

**Examples:**
**Text Repository Implementation:**
```python
class TextRepository(CRUDInterface):
    def __init__(self, filename):
        self.filename = filename

    def add_book(self, title, author, year):
        with open(self.filename, "a") as file:
            file.write(f"Title: {title}, Author: {author}, Year: {year}\n")

    def list_books(self):
        with open(self.filename, "r") as file:
            for line in file:
                print(line.strip())

    # Other methods...
```

**CSV Repository Implementation:**
```python
import csv

class CSVRepository(CRUDInterface):
    def __init__(self, filename):
        self.filename = filename

    def add_book(self, title, author, year):
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([title, author, year])

    def list_books(self):
        with open(self.filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"Title: {row[0]}, Author: {row[1]}, Year: {row[2]}")

    # Other methods...
```

### 5. Switching Between Different Data Storages

**Discussion Points:**
- Use a factory pattern to create the appropriate repository instance based on configuration.
- Read the configuration file to determine which storage method to use.

**Examples:**
```python
import json

class RepositoryFactory:
    @staticmethod
    def get_repository():
        with open("config.json", "r") as file:
            config = json.load(file)
            storage_type = config["storage_type"]
            if storage_type == "text":
                return TextRepository("library_books.txt")
            elif storage_type == "csv":
                return CSVRepository("library_books.csv")
            else:
                raise ValueError(f"Unknown storage type: {storage_type}")
```

**Further Reading:**
- [Factory Pattern](https://refactoring.guru/design-patterns/factory-method) on Refactoring Guru
- [JSON in Python](https://www.w3schools.com/python/python_json.asp) on W3Schools

## Exercises

**Exercise 1: Classes and Objects**
1. Create a `Book` class with `title`, `author`, and `year` attributes. Instantiate an object of this class.

**Exercise 2: Methods and Attributes**
1. Add a method to the `Book` class that returns a formatted string with the book's details.

**Exercise 3: Defining an Interface**
1. Define a CRUD interface using an abstract base class.

**Exercise 4: Implementing the Interface for Text Storage**
1. Implement the CRUD interface for text file storage.

**Exercise 5: Implementing the Interface for CSV Storage**
1. Implement the CRUD interface for CSV file storage.

**Exercise 6: Switching Between Storage Methods**
1. Implement a factory pattern to switch between text and CSV storage based on a configuration file.
2. Update the main menu to use the repository instance created by the factory.

## Summary

By the end of Lesson 7, students should be comfortable with defining and using interfaces in Python, understanding and using classes and objects, implementing methods and attributes, implementing interfaces for different data storage methods, and switching between these storage methods using a factory pattern. These skills are essential

 for writing flexible, maintainable, and scalable code, particularly in the context of managing a library's book collection.