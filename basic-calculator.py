"""A simple command-line calculator application."""

def add(x_val, y_val):
    """Return the sum of x_val and y_val."""
    return x_val + y_val

def subtract(x_val, y_val):
    """Return the difference between x_val and y_val."""
    return x_val - y_val

def multiply(x_val, y_val):
    """Return the product of x_val and y_val."""
    return x_val * y_val

def divide(x_val, y_val):
    """Return the result of dividing x_val by y_val. Handle division by zero."""
    if y_val == 0:
        return "Error: Cannot divide by zero."
    return x_val / y_val

def main():
    """Main function to run the calculator."""
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice not in ('1', '2', '3', '4'):
        print("Invalid choice")
        return

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    if choice == '1':
        print(f"Result: {add(num1, num2)}")
    elif choice == '2':
        print(f"Result: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Result: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"Result: {divide(num1, num2)}")

if __name__ == "__main__":
    main()
