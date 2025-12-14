operator = input("Enter an operator (+ - * /): ")
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter yout second number: "))


if operator == "+":
    result = round((num1 + num2),2)
    print(f"Addition is: {result}")
elif operator == "-":
    result = round((num1 - num2),2)
    print(f"Subtract is: {result}")
elif operator == "*":
    result = round((num1 * num2),2)
    print(f"Multiply is: {result}")
elif operator == "/":
    result = round((num1 / num2),2)
    print(f"Divide is: {result}")
else:
    print(f"{operator} is not correct operator")