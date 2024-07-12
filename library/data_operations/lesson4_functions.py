# ./library/data_operations/lesson4_functions.py
print("\n\rExercise 1: If-Else Statements")

# 1. Write a function that checks if a number is positive, negative, or zero.
print("\n\r1. Write a function that checks if a number is positive, negative, or zero:")

def check_number(number):
    if number > 0:
        return "The number is positive"
    elif number == 0:
        return "The number is zero"
    else:
        return "The number is negative"

# 2. Write a function that returns the first two letters of the author's last name based on the book provided.
print("\n\r2. Write a function that returns the first two letters of the author's last name based on the book provided:")

def author_initials(book):
    author = book.get("author", "")
    last_name = author.split()[-1]
    return last_name[:2] if last_name else ""

# Sample usage
books = [
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932}
]

print(check_number(10))
print(check_number(0))
print(check_number(-5))
print(author_initials(books[0]))
print(author_initials(books[1]))





print("\n\rExercise 2: While Loops")

# 1. Write a function with a while loop that prints numbers from 1 to 10.
print("\n\r1. Write a function with a while loop that prints numbers from 1 to 10:")

def print_numbers():
    count = 1
    while count <= 10:
        print(count)
        count += 1

# 2. Write a function that uses a while loop to calculate the sum of numbers from 1 to 100.
print("\n\r2. Write a function that uses a while loop to calculate the sum of numbers from 1 to 100:")

def sum_numbers():
    total = 0
    number = 1
    while number <= 100:
        total += number
        number += 1
    return total

# Sample usage
print_numbers()
print(f"Sum of numbers from 1 to 100: {sum_numbers()}")
