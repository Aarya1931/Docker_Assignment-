# calculator.py
def calculator():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Choose an operation (1/2/3/4): "))
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print(f"The result is: {num1 + num2}")
    elif choice == 2:
        print(f"The result is: {num1 - num2}")
    elif choice == 3:
        print(f"The result is: {num1 * num2}")
    elif choice == 4:
        if num2 != 0:
            print(f"The result is: {num1 / num2}")
        else:
            print("Division by zero is not allowed.")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    calculator()
