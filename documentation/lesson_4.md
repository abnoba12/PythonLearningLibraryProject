# Lesson 4: Control Structures

## Objective
The objective of this lesson is to teach students how to use control structures in Python, including conditional statements and loops. By the end of this lesson, students will understand how to control the flow of their programs using if-else statements and different types of loops.

## Key Points

1. **If-Else Statements**
   - Introduction to conditional statements.
   - Syntax of if, elif, and else statements.
   - Nested if statements.

2. **While Loops**
   - Introduction to while loops.
   - Loop control with break and continue.
   - Infinite loops and how to avoid them.

3. **For Loops**
   - Introduction to for loops.
   - Iterating over sequences (lists, strings, etc.).
   - Loop control with break and continue.
   - Using the range() function.

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
x = 10
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")
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

### 3. For Loops

**Discussion Points:**
- A for loop iterates over a sequence (e.g., list, string).
- The range() function generates a sequence of numbers.
- The break statement exits the loop prematurely.
- The continue statement skips the current iteration and moves to the next iteration.

**Examples:**
```python
# For loops
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Using range()
for i in range(5):
    print(i)

# Using break
for i in range(5):
    if i == 3:
        break
    print(i)

# Using continue
for i in range(5):
    if i == 3:
        continue
    print(i)
```

**Further Reading:**
- [Python For Loops](https://www.w3schools.com/python/python_for_loops.asp) on W3Schools

## Exercises

**Exercise 1: If-Else Statements**
1. Write a program that checks if a number is positive, negative, or zero.
2. Write a program that assigns grades based on marks: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

**Exercise 2: While Loops**
1. Write a while loop that prints numbers from 1 to 10.
2. Write a program that uses a while loop to calculate the sum of numbers from 1 to 100.

**Exercise 3: For Loops**
1. Write a for loop that iterates over a list of numbers and prints only the even numbers.
2. Write a program that uses a for loop and the range() function to print the first 10 multiples of 3.

## Summary

By the end of Lesson 4, students should be comfortable with using control structures in Python, including if-else statements and loops (while and for). These structures are essential for controlling the flow of a program and making decisions based on conditions. Understanding and using control structures effectively will enable students to write more complex and dynamic Python programs.
