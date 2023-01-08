number = int(input("Introduceti un numar:"))

if 0 < number:
    print(f"Numarul {number} este pozitiv ")
elif 0 < number < 10:
    print(f"Numarul {number} este mai mic ca 10")
elif number == 0:
    print(f"Numarul este 0 !")
elif number < 0:
    number = abs(number)
    print(f"Numarul este negativ si l-am transformat in mumarul pozitiv : {number}")


"""Ce se intampla daca nu introduc cifre de la tastatura? Ex: abc :). In rest e foarte bine"""
