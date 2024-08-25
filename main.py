# Task 1: Assigning values to variables and printing them along with their types.

# Assigning values to variables
name = "S M Ali Zaidi"  
age = 37  
height = 1.89  
is_student = True  

# Printing the values and their types
print("Name:", name, "| Type:", type(name))
print("Age:", age, "| Type:", type(age))
print("Height:", height, "| Type:", type(height))
print("Is Student:", is_student, "| Type:", type(is_student))

# Task 2: Perform arithmetic operations on user-input numbers

# Function to get a valid number from the user
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Prompting the user to enter two numbers
num1 = get_number("Enter the first number: ")
num2 = get_number("Enter the second number: ")

# Performing basic arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handling division separately to avoid division by zero
if num2 != 0:
    division = num1 / num2
else:
    division = "undefined (division by zero)"

# Printing the results
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")


# Task 3: Classify user's age into categories

# Function to get a valid age from the user
def get_age(prompt):
    while True:
        try:
            age = int(input(prompt))
            if age < 0:
                print("Age cannot be negative. Please enter a valid age.")
            else:
                return age
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Prompting the user to enter their age
age = get_age("Enter your age: ")

# Classifying the user's age into categories
if 0 <= age <= 12:
    age_group = "Child"
elif 13 <= age <= 19:
    age_group = "Teenager"
elif 20 <= age <= 64:
    age_group = "Adult"
elif age >= 65:
    age_group = "Senior"
else:
    age_group = "Invalid age range"

# Printing the age group
print(f"You are classified as: {age_group}")
