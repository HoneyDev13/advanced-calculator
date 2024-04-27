import math

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
        print("9. Exit")
        choice = input("Enter your choice (1/2/3/4/5/6/7/8/9): ")

        if choice in ('1', '2', '3', '4', '5', '6'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))
            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))
            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))
            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))
            elif choice == '5':
                print(num1, "^", num2, "=", power(num1, num2))
            elif choice == '6':
                print(num1, "%", num2, "=", modulus(num1, num2))

        elif choice == '7':
            num = float(input("Enter a number: "))
            print("sqrt(", num, ") =", square_root(num))

        elif choice == '8':
            num = float(input("Enter a number: "))
            base = float(input("Enter the base: "))
            print("log base", base, "of", num, "=", logarithm(num, base))

        elif choice == '9':
            print("Exiting the calculator.")
            break

        else:
            print("Invalid input. Please choose a valid option.")

if __name__ == "__main__":
    main()
