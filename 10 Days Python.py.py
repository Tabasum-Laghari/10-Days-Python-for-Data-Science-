# Python Fundamentals Practice
# Day 1 to Day 8
# Name: Tabasum Laghari

# ============================================================
# DAY 1 - Python Basics
# ============================================================

# 1. Print my name
print("Tabasum Laghari")

# 2. Create variables for name, age, and city
name = "Tabasum Laghari"
age = 20
city = "Sakrand"

print("My name is", name, "I am", age, "years old and I live in", city)

# 3. Take user's name using input() and print a greeting
username = input("Enter your name: ")
print("Hello!", username)

# 4. Simple addition, subtraction, and multiplication
num1 = 2
num2 = 3

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)


# ============================================================
# DAY 2 - Operators and Expressions
# ============================================================

# 1. Arithmetic operators
a = 10
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

# 2. Comparison operators
x = 10
y = 20

print(x > y)    # False
print(x < y)    # True
print(x == y)   # False

# 3. Logical operators
print(x > 5 and y < 25)   # True
print(x > 15 or y < 25)   # True
print(not (x == y))       # True

# 4. Assignment operators
c = 10

c += 5
print(c)

c -= 3
print(c)

c *= 2
print(c)

# 5. Parentheses and operator precedence
expr1 = 2 + 3 * 4
expr2 = (2 + 3) * 4

print(expr1)   # 14
print(expr2)   # 20


# ============================================================
# DAY 3 - Conditional Statements
# ============================================================

# 1. Ask the user for marks and display Pass or Fail
marks = float(input("Enter your marks: "))

if marks >= 50:
    print("Pass")
else:
    print("Fail")

# 2. Display grade using if-elif-else
score = float(input("Enter your score: "))

if score >= 80:
    print("Grade: A")
elif score >= 60:
    print("Grade: B")
else:
    print("Grade: C")

# 3. Check whether a number is positive, negative, or zero
number = float(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# 4. Use 'and' to check two conditions
x = 10
y = 20

if x > 5 and y < 25:
    print("Both conditions are true")

# 5. Nested if statement
age = int(input("Enter your age: "))

if age >= 18:
    if age >= 60:
        print("You are a senior citizen.")
    else:
        print("You are an adult.")
else:
    print("You are a minor.")

# 6. Conditional expression
result = "Pass" if marks >= 50 else "Fail"
print(result)


# ============================================================
# DAY 4 - Loops
# ============================================================

# 1. Print numbers from 1 to 10
for i in range(1, 11):
    print(i)

# 2. Print even numbers from 2 to 20
for i in range(2, 21, 2):
    print(i)

# 3. Loop through a word and print each character
word = "Hello"

for char in word:
    print(char)

# 4. While loop: count from 10 down to 1
i = 10

while i > 0:
    print(i)
    i -= 1

# 5. Use break to stop the loop at 5
for i in range(1, 11):
    if i == 5:
        break
    print(i)

# 6. Use continue to skip 5
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# 7. Nested loop: number pattern
for i in range(1, 4):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# ============================================================
# DAY 5 - Data Structures
# ============================================================

# 1. Create a list of 5 fruits
fruits = ["Apple", "Banana", "Dates", "Mango", "Orange"]
print(fruits)

# 2. Add a new item using append()
fruits.append("Pineapple")
print(fruits)

# 3. Remove an item using remove()
fruits.remove("Orange")
print(fruits)

# 4. Create a tuple of 3 colors
colors = ("Red", "Blue", "Green")
print(colors)

# 5. Set automatically removes duplicate values
numbers = {1, 2, 3, 4, 5, 6, 6}
print(numbers)

# 6. Add a number to a set
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
numbers.add(10)
print(numbers)

# 7. Create a dictionary
myself = {
    "name": "Tabasum",
    "age": 19,
    "city": "Sakrand"
}

# 8. Access and print one dictionary value
print(myself["name"])

# 9. Add a new key-value pair
myself["department"] = "24BSIT QUEST SBA"
print(myself)


# ============================================================
# DAY 6 - Strings and Functions
# ============================================================

# 1. Print the first character
name = "Tabasum"
print(name[0])

# 2. Print the last character using negative indexing
print(name[-1])

# 3. Slice the first 3 characters
print(name[0:3])

# 4. Convert a sentence to uppercase
sentence = "My name is Tabasum"
print(sentence.upper())

# 5. Find the length of a string
print(len(name))

# 6. Replace one word in a sentence
print(sentence.replace("Tabasum", "Alice"))

# 7. Function that prints a welcome message
def print_welcome_message():
    print("Welcome!")

print_welcome_message()

# 8. Function that accepts a name as a parameter
def print_name(name):
    print(f"Hello, {name}!")

print_name("Tabasum")

# 9. Function that adds two numbers
def add_numbers(a, b):
    return a + b

print(add_numbers(10, 5))

# 10. Function that returns multiplication result
def multiply_numbers(a, b):
    return a * b

print(multiply_numbers(10, 5))


# ============================================================
# DAY 7 - Functions
# ============================================================

# 1. Function that prints your name
def print_my_name():
    print("My name is Tabasum Laghari")

print_my_name()

# 2. Function that returns the sum of two numbers
def sum_of_two_numbers(a, b):
    return a + b

print(sum_of_two_numbers(10, 5))

# 3. Function with a default parameter
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
greet("Tabasum")

# 4. Check whether a number is even or odd
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(10))

# 5. Find the larger of two numbers
def find_larger(a, b):
    if a > b:
        return a
    else:
        return b

print(find_larger(10, 20))

# 6. Calculate the sum of numbers in a list
def sum_of_list(numbers):
    return sum(numbers)

print(sum_of_list([1, 2, 3, 4, 5]))

# 7. Count characters in a word
def count_characters(word):
    return len(word)

print(count_characters("Python"))

# 8. Calculate factorial using recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))


# ============================================================
# DAY 8 - File Handling and Exception Handling
# ============================================================

# 1. Create a text file and write your name
with open("my_name.txt", "w") as file:
    file.write("My name is Tabasum Laghari")

# 2. Read and print the content of the file
with open("my_name.txt", "r") as file:
    content = file.read()
    print(content)

# 3. Add a new line using append mode
with open("my_name.txt", "a") as file:
    file.write("\nThis is a new line.")

# 4. Read the file again
with open("my_name.txt", "r") as file:
    content = file.read()
    print(content)

# 5. Handle ValueError
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")

# 6. Handle FileNotFoundError
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")

# 7. Handle ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# 8. Use try, except, else, and finally
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
else:
    print(f"You entered: {number}")
finally:
    print("Execution completed.")
