"""A simple command-line calculator application.

This application allows users to perform basic arithmetic operations
such as addition, subtraction, multiplication, and division.
"""

def add(x_val, y_val):
    """
    Add two numbers.

    Parameters
    ----------
    x_val : float
        The first number.
    y_val : float
        The second number.

    Returns
    -------
    float
        The sum of x_val and y_val.
    """
    return x_val + y_val


def subtract(x_val, y_val):
    """
    Subtract two numbers.

    Parameters
    ----------
    x_val : float
        The number to subtract from.
    y_val : float
        The number to subtract.

    Returns
    -------
    float
        The difference between x_val and y_val.
    """
    return x_val - y_val


def multiply(x_val, y_val):
    """
    Multiply two numbers.

    Parameters
    ----------
    x_val : float
        The first number.
    y_val : float
        The second number.

    Returns
    -------
    float
        The product of x_val and y_val.
    """
    return x_val * y_val


def divide(x_val, y_val):
    """
    Divide one number by another.

    Parameters
    ----------
    x_val : float
        The dividend.
    y_val : float
        The divisor.

    Returns
    -------
    float or str
        The result of the division, or an error message if dividing by zero.
    """
    if y_val == 0:
        return "Error: Cannot divide by zero."
    return x_val / y_val


def main():
    """
    Run the calculator interface.

    Prompts the user to select an arithmetic operation and input two numbers.
    Displays the result of the chosen operation.
    """
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
