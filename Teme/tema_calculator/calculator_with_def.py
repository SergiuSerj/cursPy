def calculate():

    operation = input("Enter an operation (+, -, *, /): ")
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))


    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    else:
        result = None

    return result

result = calculate()
if result is not None:
    print("The result is", result)
else:
    print("Invalid input")