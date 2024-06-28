# Answers to Lesson 2

# Exercise 1: Variables and Data Types
print("\r\n1.1 Create variables for your favorite book title, author, and publication year.")
favorite_title = "To Kill a Mockingbird"
favorite_author = "Harper Lee"
favorite_year = 1960
print(favorite_title)
print(favorite_author)
print(favorite_year)


print("\r\n1.2 Print each variable and its data type.")
print(favorite_title, type(favorite_title))
print(favorite_author, type(favorite_author))
print(favorite_year, type(favorite_year))


# Exercise 2: Basic Operators
print("\r\n2.1 Calculate the total number of books you plan to read this year (use addition).")
books_planned = 5 + 3 + 7
print(books_planned)


print("\r\n2.2 Check if the publication year of your favorite book is before 2000.")
is_classic = favorite_year < 2000
print(is_classic)


print("\r\n2.3 Combine conditions to check if the book is a classic and has a high rating.")
high_rating = 4.8
is_classic_high_rating = is_classic and (high_rating >= 4.5)
print(is_classic_high_rating)


# Exercise 3: String Manipulation


print("\r\n3.1 Create a string with your favorite book's title and author.")
book_info = f"{favorite_title} by {favorite_author}"
print(book_info)


print("\r\n3.2 Convert the title to uppercase and the author to lowercase.")
uppercase_title = favorite_title.upper()
lowercase_author = favorite_author.lower()
print(uppercase_title)
print(lowercase_author)


print("\r\n3.3 Replace any spaces in the title with underscores.")
title_with_underscores = favorite_title.replace(" ", "_")
print(title_with_underscores)


# Exercise 4: Lists and List Comprehensions


print("\r\n4.1 Create a list of your top 5 favorite books.")
favorite_books = ["To Kill a Mockingbird", "1984", "Pride and Prejudice", "The Great Gatsby", "Moby Dick"]
print(favorite_books)


print("\r\n4.2 Add a new book to the list and then remove one.")
favorite_books.append("War and Peace")
favorite_books.remove("Moby Dick")
print(favorite_books)


print("\r\n4.3 Sort the list and print it.")
favorite_books.sort()
print(favorite_books)


print("\r\n4.4 Use a list comprehension to create a list of book titles in uppercase.")
uppercase_books = [book.upper() for book in favorite_books]
print(uppercase_books)