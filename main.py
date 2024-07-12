# Answers to Lesson 4

# ./main.py
print("\n\rExercise 3: User Input Handling")

# 1. Write a prompt that asks for a list of numbers as input and prints out if each number is positive, negative, or zero using the function from Exercise 1.
# Use try-except blocks to handle invalid input and type errors.
print("\n\r1. Prompt for a list of numbers and check if each number is positive, negative, or zero:")

def check_number(number):
    if number > 0:
        return "The number is positive"
    elif number == 0:
        return "The number is zero"
    else:
        return "The number is negative"

user_input = input("Enter a list of numbers separated by spaces: ")
numbers = user_input.split()
for num in numbers:
    try:
        number = int(num)
        print(check_number(number))
    except ValueError:
        print(f"Invalid input: {num} is not a number")

# 2. Write a program that takes a string as input and checks if it is a palindrome (a word that reads the same backward as forward).
print("\n\r2. Check if a string is a palindrome:")

def is_palindrome(s):
    return s == s[::-1]

user_input = input("Enter a string: ")
if is_palindrome(user_input):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")





print("\n\rExercise 4: Implementing a Menu-Driven Interface")

# 1. Create a menu-driven program that allows the user to perform different library operations that were created in lesson 3 in file "./library/data_operations/book_operations.py".
# Through this menu and prompts we need to allow users to "add_book", "remove_book", "update_book_year", "list_books", and "find_book_by_title".

from library.data_operations.book_operations import add_book, remove_book, update_book_year, list_books, find_book_by_title

books = []

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Update Book Year")
        print("4. List Books")
        print("5. Find Book by Title")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = int(input("Enter book year: "))
            add_book(books, title, author, year)
            print(f"Book added: {title}, {author}, {year}")
        elif choice == '2':
            title = input("Enter book title to remove: ")
            print(remove_book(books, title))
        elif choice == '3':
            title = input("Enter book title to update: ")
            new_year = int(input("Enter new year: "))
            print(update_book_year(books, title, new_year))
        elif choice == '4':
            print("List of books:")
            for title in list_books(books):
                print(title)
        elif choice == '5':
            title = input("Enter book title to find: ")
            book = find_book_by_title(books, title)
            if book:
                print(f"Found book: {book}")
            else:
                print("Book not found")
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main menu
main_menu()