list_menu = [1, 2, 3, 4, 5]
print("1 – Afisare lista de cumparaturi \n"
      "2 – Adaugare element \n"
      "3 – Stergere element \n"
      "4 – Sterere lista de cumparaturi \n"
      "5 - Cautare in lista de cumparaturi")

choise = int(input("Alegeti o varianta: "))

if choise in list_menu:
    if choise == 1:
        print("Afisare lista de cumparaturi")
    elif choise == 2:
        print("Adaugare element")
    elif choise == 3:
        print("Stergere element")
    elif choise == 4:
        print("Sterere lista de cumparaturi")
    elif choise == 5:
        print("Cautare in lista de cumparaturi")
else:
    print("Alegerea nu exista. Reincercati")

"""Ce se intampla daca nu introduc cifre de la tastatura? Ex: abc :). In rest e foarte bine"""
