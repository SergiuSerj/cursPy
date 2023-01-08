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


"""Obs.:
- Daca introduc litere acolo unde ar trebui sa am numere, programul ruleaza mai departe. Aici ar fi trebuit sa
ma puna sa reintroduc corect (deci un while).

Pentru a va corecta un numar anterior scrieti litera `C`
Introdu primu numar: a
introdu al doilea numar: d
Introdu o operatie (+, -, *, /): -
Datele introduse nu sunt corecte

- In alta ordine de idei as fi vrut sa am input primul numar dupa care operatie si pe urma al doilea numar. 
- 12 / 0 ... programul crapa. Ar fi trebuit sa am o validare acolo ptr ca nu e posibila impartirea la 0.
- Daca introduc o litera la input operatie, programul este terminat fara validare. Nu ma anunta nimic.

Introdu primu numar: 12
introdu al doilea numar: 4
Introdu o operatie (+, -, *, /): a

Concluzie:
Ar mai fi de imbunatatit aspectele de mai sus.
"""