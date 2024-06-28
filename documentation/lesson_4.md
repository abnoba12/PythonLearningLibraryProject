# Lesson 4: Control Structures and Menu-Driven Interface

## Objective
The objective of this lesson is to implement a menu-driven interface using conditional statements and loops. By the end of this lesson, students will understand how to use if-else statements, while loops, and handle user input to create interactive programs.

## Key Points

1. **If-Else Statements**
   - Introduction to conditional statements.
   - Syntax of if, elif, and else statements.
   - Nested if statements.

2. **While Loops**
   - Introduction to while loops.
   - Loop control with break and continue.
   - Infinite loops and how to avoid them.

3. **User Input Handling**
   - Using the input() function to take user input.
   - Converting input to appropriate data types.
   - Validating user input.

4. **Implementing a Menu-Driven Interface**
   - Combining if-else statements and while loops.
   - Creating a main menu function.
   - Handling user choices to perform different actions.

## Lesson Content

### 1. If-Else Statements

**Discussion Points:**
- Conditional statements allow you to execute code based on certain conditions.
- The if statement evaluates a condition and executes code if the condition is true.
- The elif (else if) statement evaluates additional conditions if the previous conditions were false.
- The else statement executes code if all previous conditions were false.

**Examples:**
```python
# If-else statements
choice = 2
if choice == 1:
    print("You selected option 1")
elif choice == 2:
    print("You selected option 2")
else:
    print("Invalid choice")
```

**Further Reading:**
- [Python If...Else](https://www.w3schools.com/python/python_conditions.asp) on W3Schools

### 2. While Loops

**Discussion Points:**
- A while loop repeats a block of code as long as a condition is true.
- The break statement exits the loop prematurely.
- The continue statement skips the current iteration and moves to the next iteration.

**Examples:**
```python
# While loops
count = 0
while count < 5:
    print(count)
    count += 1

# Using break
count = 0
while count < 5:
    if count == 3:
        break
    print(count)
    count += 1

# Using continue
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)
```

**Further Reading:**
- [Python While Loops](https://www.w3schools.com/python/python_while_loops.asp) on W3Schools

### 3. User Input Handling

**Discussion Points:**
- The input() function allows you to take input from the user.
- Input is returned as a string, so it may need to be converted to other data types.
- Validating user input ensures that the program handles unexpected or incorrect input gracefully.

**Examples:**
```python
# User input handling
user_input = input("Enter a number: ")
try:
    number = int(user_input)
    print(f"You entered the number: {number}")
except ValueError:
    print("Invalid input. Please enter a valid number.")
```

**Further Reading:**
- [Python User Input](https://www.w3schools.com/python/python_user_input.asp) on W3Schools

### 4. Implementing a Menu-Driven Interface

**Discussion Points:**
- A menu-driven interface allows users to interact with the program by selecting options from a menu.
- Combining if-else statements and while loops can create an interactive menu.
- Handling user choices involves performing different actions based on the selected option.

**Examples:**
```python
# Implementing a menu-driven interface

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Option 1")
        print("2. Option 2")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("You selected Option 1")
        elif choice == '2':
            print("You selected Option 2")
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main menu
main_menu()
```

**Further Reading:**
- [Python Control Flow](https://docs.python.org/3/tutorial/controlflow.html) on Python.org

## Exercises

**Exercise 1: If-Else Statements**
1. Write a program that checks if a number is positive, negative, or zero.
2. Write a program that assigns grades based on marks: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

**Exercise 2: While Loops**
1. Write a while loop that prints numbers from 1 to 10.
2. Write a program that uses a while loop to calculate the sum of numbers from 1 to 100.

**Exercise 3: User Input Handling**
1. Write a program that takes a list of numbers as input and prints the square of each number. Use try-except blocks to handle invalid input and type errors.
2. Write a program that takes a string as input and checks if it is a palindrome (a word that reads the same backward as forward).

**Exercise 4: Implementing a Menu-Driven Interface**
1. Create a menu-driven program that allows the user to perform different mathematical operations (addition, subtraction, multiplication, division) based on their choice. Ensure that the program handles invalid choices and division by zero errors.

## Summary

By the end of Lesson 4, students should be comfortable with using control structures in Python, including if-else statements and loops (while and for), and handling user input. They will also learn to implement a menu-driven interface, which is essential for creating interactive programs. Understanding and using these control structures effectively will enable students to write more complex and dynamic Python programs.
