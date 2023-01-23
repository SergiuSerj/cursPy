import csv
import datetime
import operator
from datetime import datetime

"""Adaugare categorii"""
# def adaugare_categorii()
#     with open("categorii.txt", "a") as file:
#         while True:
#             categorie = input("introduceti o categorie de taskuri. tastati enter pentru a incheia: ")
#             if categorie == "":
#                 break
#             else:
#                 file.write(categorie)
#
# adaugare_categorii()

"""Adaugare taskuri"""
def check_category(category):
    with open("categorii.txt", "r") as file:
        while True:
            line = file.readline().strip()
            if line == category:
                return True
            if not line:
                print("Categoria nu se gasete!Incercati din nou! ")
                break
        return False

def check_date(date):
    try:
        datetime.datetime.strptime(date, '%d.%m.%Y')
        return True
    except ValueError:
        print('Formatul datei trebuie sa fie sub forma ZZ.LL.AAAA')
        return False

def add_task():
    with open('taskuri.csv', 'a', newline="") as file:
        while True:
            category = input('Introduceti o categorie: ').strip()
            if category == '':
                break
            if check_category(category):
                pass
            else:
                continue
            tasks = input('Introduceti un task. Tastati enter pentru a incheia: ')
            if tasks == '':
                break
            while True:
                end_date = input('Introduceti o data limita: ')
                if check_date(end_date):
                    break
            responsible = input('Introduceti o persoana responsabila: ')
            if responsible == '':
                break

            # if tasks == '' or end_date == '' or responsible == '' or category == '':
            if '' in [tasks, end_date, responsible, category]:
                break
            csv_writer = csv.writer(file, delimiter=',')
            csv_writer.writerow([tasks, end_date, responsible, category]) # fara [] itereaza litera cu litera separata prin delimiter
            next_task = input('Introduceti un alt task? (Y/N)')
            if next_task.lower() == 'n':
                break


"""Elemnte sortare"""
def sortare_alfabetica_as(referinta):
    with open("taskuri.csv", "r") as sort:
        data = csv.reader(sort)
        data_sort = list(data)
        data_sort.sort(key=lambda x: x[referinta].lower())
        for y in data_sort:
            print(" ".join(y))
        return None

def sortare_alfabetica_des(referinta):
    with open("taskuri.csv", "r") as sort:
        data = csv.reader(sort)
        data_sort = list(data)
        data_sort.sort(key=lambda x: x[referinta].lower(), reverse=True)
        for y in data_sort:
            print(" ".join(y))
        return None

def sortare():
    print("Criteriile disponibile sunt: \n"
          "1. sortare ascendentă task\n"
          "2. sortare descendentă task\n"
          "3. sortare ascendentă data\n"
          "4. sortare descendentă data\n"
          "5. sortare ascendentă persoana responsabilă\n"
          "6. sortare descendentă persoană responsabilă\n"
          "7. sortare ascendentă categorie\n"
          "8. sortare descendentă categorie")
    while True:
        sortare = input("introduceti o varianta sau apasati  Enter pentru a merge mai departe! ")
        if sortare == "1":
            sortare_alfabetica_as(0)
            break
        if sortare == "2":
            sortare_alfabetica_des(0)
            break
        if sortare == "3":
            with open('taskuri.csv', 'r') as file:
                reader = csv.reader(file)
                data = list(reader)
                data.sort(key=lambda x: datetime.strptime(x[1], '%d.%m.%Y'))
                for x in data:
                    print(" ".join(x))
            break
        if sortare == "4":
            with open('taskuri.csv', 'r') as file:
                reader = csv.reader(file)
                data = list(reader)
                data.sort(key=lambda x: datetime.strptime(x[1], '%d.%m.%Y'), reverse=True)
                for x in data:
                    print(" ".join(x))
            break
        if sortare == "5":
            sortare_alfabetica_as(2)
            break
        if sortare == "6":
            sortare_alfabetica_des(2)
            break
        if sortare == "7":
            sortare_alfabetica_as(3)
            break
        if sortare == "8":
            sortare_alfabetica_des(3)
            break
        if sortare == "":
            break
        else:
            print("Alegerea introdusa este gresita: ")
            continue


while True:
    print("MENIU: \n"
          "1. Liste date\n"
          "2. Sortare\n"
          "3. Filtrare\n"
          "4. Adaugarea unui nou task in lista initiala\n"
          "5. Editare detalii task\n"
          "6. Stergerea unui task din lista initiala")
    menu_input = input("Alegeti o varianta: ")
    if menu_input == "1":
        with open("taskuri.csv", "r") as sort:
            data = csv.reader(sort)
            data_sort = list(data)
            data_sort.sort(key=lambda x: x[3].lower())
            for y in data_sort:
                print(" ".join(y))
            continue
    if menu_input == "2":
        sortare()
        continue
    if menu_input == "3":
        # urmeaza sa o construiesc printr-o functie
        continue
    if menu_input == "4":
        add_task()
        continue
    if menu_input == "5":
       # urmeaza sa o construiesc printr-o functie
        continue
    if menu_input == "6":
        # urmeaza sa o construiesc printr-o functie
        continue


