# Lesson 2: Core Python Concepts

## Objective
The objective of this lesson is to cover core Python concepts, including variables, data types, basic operators, string manipulation, and lists and list comprehensions. By the end of this lesson, students will have a solid understanding of these foundational concepts and be able to apply them in their Python programs.

## Key Points

1. **Variables and Data Types**
   - Introduction to variables and data types in Python.
   - Understanding the different data types: integers, floats, strings, and booleans.
   - Variable naming conventions.

2. **Basic Operators**
   - Arithmetic operators: addition, subtraction, multiplication, division, modulus, exponentiation, and floor division.
   - Comparison operators: equal to, not equal to, greater than, less than, greater than or equal to, and less than or equal to.
   - Logical operators: and, or, not.

3. **String Manipulation**
   - String creation and basic operations.
   - String slicing and indexing.
   - Common string methods: upper(), lower(), strip(), replace(), and split().

4. **Lists and List Comprehensions**
   - Introduction to lists: creation, indexing, and slicing.
   - Common list methods: append(), remove(), pop(), and sort().
   - List comprehensions: creating lists using loops and conditions.

## Lesson Content

### 1. Variables and Data Types

**Discussion Points:**
- Variables are used to store data values.
- Data types define the type of value a variable can hold.
- Python is dynamically typed, meaning you don't need to declare the data type.

**Examples:**
```python
# Variables and data types
title = "1984"  # string
author = "George Orwell"  # string
year = 1949  # integer
rating = 4.6  # float
is_fiction = True  # boolean

print(title, type(title))
print(author, type(author))
print(year, type(year))
print(rating, type(rating))
print(is_fiction, type(is_fiction))
```

**Further Reading:**
- [Python Variables](https://www.w3schools.com/python/python_variables.asp) on W3Schools
- [Python Data Types](https://www.w3schools.com/python/python_datatypes.asp) on W3Schools

### 2. Basic Operators

**Discussion Points:**
- Arithmetic operators perform mathematical operations.
- Comparison operators compare two values.
- Logical operators combine conditional statements.

**Examples:**
```python
# Arithmetic operators
total_books = 20 + 15  # addition
average_rating = (4.5 + 4.6 + 4.8) / 3  # division
years_since_published = 2021 - year  # subtraction

# Comparison operators
is_classic = year < 2000
is_high_rating = rating >= 4.5

# Logical operators
is_classic_high_rating = is_classic and is_high_rating

print(total_books, average_rating, years_since_published)
print(is_classic, is_high_rating, is_classic_high_rating)
```

**Further Reading:**
- [Python Operators](https://www.w3schools.com/python/python_operators.asp) on W3Schools

### 3. String Manipulation

**Discussion Points:**
- Strings are sequences of characters.
- Strings can be manipulated using slicing, indexing, and methods.

**Examples:**
```python
# String manipulation
full_title = f"{title} by {author}"
uppercase_title = title.upper()
lowercase_author = author.lower()
stripped_title = "  1984  ".strip()
replaced_title = title.replace("1984", "Nineteen Eighty-Four")
split_author = author.split()

print(full_title)
print(uppercase_title)
print(lowercase_author)
print(stripped_title)
print(replaced_title)
print(split_author)
```

**Further Reading:**
- [Python Strings](https://www.w3schools.com/python/python_strings.asp) on W3Schools

### 4. Lists and List Comprehensions

**Discussion Points:**
- Lists are used to store multiple items in a single variable.
- Lists are ordered, changeable, and allow duplicate values.
- List comprehensions provide a concise way to create lists.

**Examples:**
```python
# Lists
books = ["1984", "Brave New World", "Fahrenheit 451"]
books.append("The Handmaid's Tale")
books.remove("Brave New World")
popped_book = books.pop()
books.sort()

print(books)
print(popped_book)

# List comprehensions
upper_books = [book.upper() for book in books]
books_with_year = [(book, year) for book in books]

print(upper_books)
print(books_with_year)
```

**Further Reading:**
- [Python Lists](https://www.w3schools.com/python/python_lists.asp) on W3Schools
- [Python List Comprehensions](https://www.w3schools.com/python/python_lists_comprehension.asp) on W3Schools

## Exercises

**Exercise 1: Variables and Data Types**
1. Create variables for your favorite book title, author, and publication year.
2. Print each variable and its data type.

**Exercise 2: Basic Operators**
1. Calculate the total number of books you plan to read this year (use addition).
2. Check if the publication year of your favorite book is before 2000.
3. Combine conditions to check if the book is a classic and has a high rating.

**Exercise 3: String Manipulation**
1. Create a string with your favorite book's title and author.
2. Convert the title to uppercase and the author to lowercase.
3. Replace any spaces in the title with underscores.

**Exercise 4: Lists and List Comprehensions**
1. Create a list of your top 5 favorite books.
2. Add a new book to the list and then remove one.
3. Sort the list and print it.
4. Use a list comprehension to create a list of book titles in uppercase.

## Summary

By the end of Lesson 2, students should be comfortable with the core concepts of Python, including variables, data types, operators, string manipulation, and lists. These foundational skills will be crucial for the more advanced topics covered in later lessons.
