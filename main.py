# Answers to Lesson 4

# Exercise 1: If-Else Statements
print("\n\rExercise 1: If-Else Statements")

# Write a program that checks if a number is positive, negative, or zero.
print("\n\r1. Check if a number is positive, negative, or zero:")
number = 7
if number > 0:
    print("The number is positive")
elif number == 0:
    print("The number is zero")
else:
    print("The number is negative")

# Write a program that assigns grades based on marks: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).
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

# Write a while loop that prints numbers from 1 to 10.
print("\n\r1. Print numbers from 1 to 10:")
count = 1
while count <= 10:
    print(count)
    count += 1

# Write a program that uses a while loop to calculate the sum of numbers from 1 to 100.
print("\n\r2. Calculate the sum of numbers from 1 to 100:")
sum_numbers = 0
number = 1
while number <= 100:
    sum_numbers += number
    number += 1
print(f"The sum of numbers from 1 to 100 is {sum_numbers}")


# Exercise 3: For Loops
print("\n\rExercise 3: For Loops")

# Write a for loop that iterates over a list of numbers and prints only the even numbers.
print("\n\r1. Print only the even numbers from a list:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print(num)

# Write a program that uses a for loop and the range() function to print the first 10 multiples of 3.
print("\n\r2. Print the first 10 multiples of 3:")
for i in range(1, 11):
    print(3 * i)
