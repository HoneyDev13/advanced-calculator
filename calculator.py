import math

# Basic arithmetic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def power(x, y):
    return x ** y

def modulus(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x % y

# Advanced operations
def square_root(x):
    if x < 0:
        return "Error! Cannot take square root of a negative number."
    else:
        return math.sqrt(x)

def logarithm(x, base):
    if x <= 0 or base <= 0 or base == 1:
        return "Error! Invalid input for logarithm."
    else:
        return math.log(x, base)

def factorial(n):
    if not isinstance(n, int) or n < 0:
        return "Error! Factorial is only defined for non-negative integers."
    else:
        return math.factorial(n)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

# Main function to run the calculator
def main():
    while True:
        print("\nAdvanced Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Modulus")
        print("7. Square Root")
        print("8. Logarithm")
        print("9. Factorial")
        print("10. Sine")
        print("11. Cosine")
        print("12. Tangent")
        print("13. Exit")
        choice = input("Enter your choice (1/2/3/4/5/6/7/8/9/10/11/12/13): ")

        if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '10', '11', '12'):
            num1 = float(input("Enter first number: "))
            if choice in ('7', '8', '10', '11', '12'):  # These operations work with one number
                print(globals()[f"{choice}_"](num1))
            else:
                num2 = float(input("Enter second number: "))
                print(globals()[f"{choice}_"](num1, num2))

        elif choice == '9':
            num = int(input("Enter a non-negative integer: "))
            print(factorial(num))

        elif choice == '13':
            print("Exiting the calculator.")
            break

        else:
            print("Invalid input. Please choose a valid option.")

# Run the calculator
if __name__ == "__main__":
    main()
