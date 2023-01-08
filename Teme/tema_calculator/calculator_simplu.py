"""Calculator simplu"""

numere = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
result = int
print("Pentru a va corecta un numar anterior scrieti litera `C`")

number_x = input("Introdu primu numar: ")

number_y = input("introdu al doilea numar: ")
if "c" == number_y:
    number_x = input("introdu dinou primu numar: ")

operation = input("Introdu o operatie (+, -, *, /): ")
if "c" == operation:
    number_y = input("introdu al doilea numar: ")
    operation = input("Introdu o operatie (+, -, *, /): ")

if number_x.isdigit() and number_y.isdigit():
    num1 = int(number_x)
    num2 = int(number_y)
    if operation == '+':
        result = num1 + num2
        print(f"Rezulatatul este: {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"Rezulatatul este: {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"Rezulatatul este: {result}")
    elif operation == '/':
        result = num1 / num2
        print(f"Rezulatatul este: {result}")
else:
    result = None
    print("Datele introduse nu sunt corecte")


