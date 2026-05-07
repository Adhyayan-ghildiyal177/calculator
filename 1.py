num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid operator")
num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /, %, **, //): ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)

elif op == "-":
    print(num1 - num2)

elif op == "*":
    print(num1 * num2)

elif op == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Cannot divide by zero")

elif op == "%":
    print(num1 % num2)   # remainder

elif op == "**":
    print(num1 ** num2)  # power

elif op == "//":
    print(num1 // num2)  # floor division

else:
    print("Invalid operator")
while True:
    # your calculator code here
    
    choice = input("Do you want to continue? (yes/no): ")
    if choice.lower() != "yes":
        break
while True:

    print("\n===== CALCULATOR =====")

    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /, %, **, //): ")
        num2 = float(input("Enter second number: "))

        if op == "+":
            result = num1 + num2

        elif op == "-":
            result = num1 - num2

        elif op == "*":
            result = num1 * num2

        elif op == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                print("Cannot divide by zero")
                continue

        elif op == "%":
            result = num1 % num2

        elif op == "**":
            result = num1 ** num2

        elif op == "//":
            result = num1 // num2

        else:
            print("Invalid operator")
            continue

        print("Answer =", result)

    except ValueError:
        print("Please enter valid numbers")

    choice = input("\nDo you want to continue? (yes/no): ")

    if choice.lower() != "yes":
        print("Calculator closed")
        break