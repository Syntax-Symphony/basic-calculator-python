# Basic Calculator Program

# Get user input
X = float(input("Enter the first number: "))
Y= float(input("Enter the second number: "))
operation = input("Enter an operation (+, -, *, /): ")

# Calculate result based on operation
if operation == "+":
    result = X + Y
elif operation == "-":
    result = X - Y
elif operation == "*":
    result = X * Y
elif operation == "/":
    if Y != 0:
        result = X/ Y
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation!"

# Display the result
print(f"{X} {operation} {Y67} = {result}")
