# Simple Command Line Calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    else:
        return a / b

print("🧮 Simple Command Line Calculator 🧮")
print("Operations: +  -  *  /")
print("Type 'exit' to quit the calculator.\n")

while True:
    user_input = input("Enter calculation (e.g., 5 + 3): ")

    if user_input.lower() == 'exit':
        print("Calculator closed. Goodbye!")
        break

    try:
        parts = user_input.split()
        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])

        if operator == '+':
            print("Result:", add(num1, num2))
        elif operator == '-':
            print("Result:", subtract(num1, num2))
        elif operator == '*':
            print("Result:", multiply(num1, num2))
        elif operator == '/':
            print("Result:", divide(num1, num2))
        else:
            print("Invalid operator! Use +, -, *, or /.")

    except (IndexError, ValueError):
        print("Invalid input format! Use format like: 8 * 2")
