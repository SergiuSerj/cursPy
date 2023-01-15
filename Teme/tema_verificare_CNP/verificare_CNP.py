"""Verificare CNP"""

CNP = int
list_number_str = []
list_number = int
cifra_de_control = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
suma_control = []
luna = {"01": "Ianuarie", "02": "Februari", "03": "Martie", "04": "Aprilie", "05": "Mai", "06": "Iunie", "07": "Iulie",
        "08": "August", "09": "Septembrie", "10": "Octombrie", "11": "Noiembrie", "12": "Decembrie"}
luna_introdusa = ""
anul = ""
sexul_persoanei = ""
result = int

def validare():
    print("CNP CORECT!")
    print(f" Sunteti nascut in {introducere_date[5:7]}, luna {luna} , anul {anul}. \n Sexul dumneavoastra este {sexul_persoanei}")

while True:
    introducere_date = input("introduceti CNP-ul dumneavoastra: \n")
    if introducere_date.isdigit() and len(introducere_date) == 13:
        for x in introducere_date:
            list_number_str.append(x)
            # print(list_number_str)
            # print(type(introducere_date))
        list_number = [eval(i) for i in list_number_str]
        # print(list_number)
        # print(type(list_number))
        for l1, l2 in zip(cifra_de_control, list_number):
            suma_control.append(l1*l2)
        # print(suma_control)
        result = sum(suma_control)
        # print(result)
        # print(list_number[-1])
    else:
        print("CNP incorect!")
        continue
    if result % 11 == list_number[-1] or 10:
        if list_number[0] < 9:
            if list_number[0] % 2 == 0:
                sexul_persoanei = "Feminin"
            else:
                sexul_persoanei = "Masculin"
        elif list_number[0] == 9:
            sexul_persoanei = "strain"
        else:
            print("Prima cifra este incorecta!")
    else:
        print("Numarul introdus nu corespunde cifrei de control!")
        continue
    if str(introducere_date[3:5]) in luna:
        indicativ = str(introducere_date[3:5])
        # print(type(indicativ))
        luna = luna.get(indicativ)
        # print(luna)
    else:
        print("Luna Incorecta")
        continue
    if list_number[0] in range(8):
        terminatie_an = str(introducere_date[1:3])
        if list_number[0] == 1 or list_number[0] == 2:
            anul = f"19{terminatie_an}"
        elif list_number[0] == 3 or list_number[0] == 4:
            anul = f"18{terminatie_an}"
        elif list_number[0] == 5 or list_number[0] == 6:
            anul = f"20{terminatie_an}"
        elif list_number[0] == 7 or list_number[0] == 8 or list_number[0] == 9:
            anul = f"secolul 20, 19{terminatie_an}"
        # print(type(anul))
    validare()
    break

#  Mai am de cosmetizat putin si cred pot reusi sa il fac mai curat