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
import math

elif op == "sqrt":
    print(math.sqrt(num1))
1. Add
2. Subtract
3. Multiply
...