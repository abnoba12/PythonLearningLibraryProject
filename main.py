# Answers to Lesson 4

# Exercise 1: If-Else Statements
print("\n\rExercise 1: If-Else Statements")

# 1. Write a program that checks if a number is positive, negative, or zero.
print("\n\r1. Check if a number is positive, negative, or zero:")
number = 7
if number > 0:
    print("The number is positive")
elif number == 0:
    print("The number is zero")
else:
    print("The number is negative")

# 2. Write a program that assigns grades based on marks: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).
print("\n\r2. Assign grades based on marks:")
marks = 85
if marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f"The grade is {grade}")


# Exercise 2: While Loops
print("\n\rExercise 2: While Loops")

# 1. Write a while loop that prints numbers from 1 to 10.
print("\n\r1. Print numbers from 1 to 10:")
count = 1
while count <= 10:
    print(count)
    count += 1

# 2. Write a program that uses a while loop to calculate the sum of numbers from 1 to 100.
print("\n\r2. Calculate the sum of numbers from 1 to 100:")
sum_numbers = 0
number = 1
while number <= 100:
    sum_numbers += number
    number += 1
print(f"The sum of numbers from 1 to 100 is {sum_numbers}")


# Exercise 3: User Input Handling
print("\n\rExercise 3: User Input Handling")

# 1. Write a program that takes a list of numbers as input and prints the square of each number. Use try-except blocks to handle invalid input and type errors.
print("\n\r1. Print the square of each number in a list with error handling:")
try:
    numbers = input("Enter a list of numbers separated by spaces: ").split()
    numbers = [float(num) for num in numbers]
    for num in numbers:
        print(f"The square of {num} is {num ** 2}")
except ValueError:
    print("Error: Please enter valid numbers.")

# 2. Write a program that takes a string as input and checks if it is a palindrome (a word that reads the same backward as forward).
print("\n\r2. Check if a string is a palindrome:")
def is_palindrome(s):
    return s == s[::-1]

user_input = input("Enter a string: ")
if is_palindrome(user_input):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")


# Exercise 4: Implementing a Menu-Driven Interface
print("\n\rExercise 4: Implementing a Menu-Driven Interface")

# 1. Create a menu-driven program that allows the user to perform different mathematical operations (addition, subtraction, multiplication, division) based on their choice. Ensure that the program handles invalid choices and division by zero errors.
print("\n\r1. Menu-driven program for mathematical operations:")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            print(f"Result: {add(a, b)}")
        elif choice == '2':
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            print(f"Result: {subtract(a, b)}")
        elif choice == '3':
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            print(f"Result: {multiply(a, b)}")
        elif choice == '4':
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            print(f"Result: {divide(a, b)}")
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main menu
main_menu()
