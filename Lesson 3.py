a = float(input("first number: "))
b = float(input("second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == '+':
    result = a + b
elif operation == '-':
    result = a - b
elif operation == '*':
    result = a * b
elif operation == '/':
    if b != 0:
        result = a / b
    else:
        result = "Error: Division by zero is not allowed!"
else:
    result = "Unknown operation!"

print("Result:", result)



