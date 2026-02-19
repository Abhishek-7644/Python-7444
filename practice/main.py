a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

import calculator
while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiply")
    print("4. Divide")

    choice = int(input("Please enter choice: "))
    if choice == 1:
        print(calculator.sum(a, b))

    elif choice == 2:   
        print(calculator.sub(a, b))

    elif choice == 3:
        print(calculator.multiply(a, b))

    elif choice == 4:
        print(calculator.divide(a, b))
        break

    else:
        print("Invalid choice")
