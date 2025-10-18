while True:  # This means "repeat forever" until we break it
    a = float(input("Enter the first number: "))   # ask the user for first number
    b = float(input("Enter the second number: "))  # ask the user for second number
    operation = input("Enter the operation (+, -, *, /): ")  # ask for operation

    # Check which operation the user chose
    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a * b
    elif operation == '/':
        if b != 0:   # division by zero is not allowed
            result = a / b
        else:
            result = "Error: division by zero is not allowed!"
    else:
        result = "Unknown operation!"

    print("Result:", result)  # show the result

    # Ask user if they want to continue
    choice = input("Do you want to continue? (y / yes): ").lower()

    # If user doesn't type 'y' or 'yes', stop the loop
    if choice not in ("y", "yes"):
        print("Calculator stopped. Goodbye!")
        break