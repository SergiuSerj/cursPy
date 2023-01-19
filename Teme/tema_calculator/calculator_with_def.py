numere = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
semne_operatie = ("+", "-", "*", "/")
result = int

while True:
    numar_x = input("Intrdu primu numar: ").lower()
    if numar_x.isdigit():
        x = int(numar_x)
        if x > 0:
            break
        else:
            continue
    else:
        print("Caracterul introdus nu este corect.")

while True:
    operation = input("Intrdu operatia pe care urmeaza sa o faci: \n")
    if operation in semne_operatie and len(operation) == 1:
        break
    # elif operation == "c":
    else:
        print("Semnul introdus nu este corect: ")

while True:
    numar_y = input("Intrdu al doilea numar: ").lower()
    if numar_y.isdigit():
        y = int(numar_y)
        if y > 0:
            break
        else:
            continue
    else:
        print("Caracterul introdus nu este corect.")


if operation == '+':
    result = x + y
    print(f"Rezulatatul este: {result}")
elif operation == '-':
    result = x - y
    print(f"Rezulatatul este: {result}")
elif operation == '*':
    result = x * y
    print(f"Rezulatatul este: {result}")
elif operation == '/':
    result = x / y
    print(f"Rezulatatul este: {result}")
else:
    print("nu este valid")

























