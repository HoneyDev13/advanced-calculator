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

def main():
    while True:
        print("\nAdvanced Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Modulus")
        print("7. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7): ")

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
            print("Exiting the calculator.")
            break

        else:
            print("Invalid input. Please choose a valid option.")

if __name__ == "__main__":
    main()
