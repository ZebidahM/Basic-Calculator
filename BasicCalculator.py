# Basic Calculator Program

# Step 1: Define operation functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

# Step 2: Map operations to functions in a dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Step 3: Get user input
print("Enter the first number:")
first_number = float(input())

print("Enter the second number:")
second_number = float(input())

print("Enter the operation (+, -, *, /):")
operation = input()

# Step 4: Perform the operation using the dictionary
if operation in operations:
    result = operations[operation](first_number, second_number)
    # Step 5: Display the result
    print(f"The result of {first_number} {operation} {second_number} is {result}")
else:
    print("Invalid operation entered.")

