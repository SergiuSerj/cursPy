import csv
import datetime

# task_list = []
# with open('Task.csv', 'a') as csv_file:  # am creat fisierul csv si capetele de tabel
#     csv_writer = csv.writer(csv_file, delimiter=',')
#     csv_writer.writerow(['task', 'date', 'responsible', 'category'])

# with open('Categorie.txt', 'w') as file:
#     file.write("cumparaturi")


# ---> VALIDARE CATEGORIE, pentru cazul adaugarii unei categorii noi
def add_category(new):
    """Adauga o noua categorie"""

    with open('Categorie.txt','a') as file:
        file.write(new)
def category_duplicate(category):
    """Verifica daca o categorie se afla deja in fisier / daca este unica (noua) sau exista deja"""
    with open("Categorie.txt", 'r') as file:
        for line in file:
            if category in line:
                return True
    return False

# ---> VALIDARE CATEGORIE, pentru cazul adaugarii unui task nou
def category_exists(category):
    """Verifica daca exista categoria in fisier
    parcurgand linie cu linie fisierul .txt
    ---> Pentru ADAUGARE UNUI NOU TASK """

    with open('Categorie.txt', 'r') as file:
        while True:
            line = file.readline()
            if line.strip() == category:
                return True
            if not line:
                break
        return False
def validate_category(category):
    """Verifica daca s-a introdus o categorie valida
    si solicita un nou input pana cand aceasta este introdusa"""

    while category_exists(category) == False:
        print("---> Categoria nu este disponibila!")
        category = input("Introduceti o categorie existenta: ")

    return category


# ---> VALIDARE DATA
def validate_date(date_input):
    """Verifica daca o data respecta
    formatul cerut si RETURNEAZA true/false"""
    try:
        check_date = datetime.datetime.strptime(date_input, "%d.%m.%Y %H:%M")
        return True
    except ValueError:
        return False
def correct_date():
    """Verifica daca data introdusa este incorecta si
    solicita o alta valoare pana cand se introduce una valida,
    fara sa reia codul de la inceput cerand celelalte elemente
    RETURNEAZA data corecta, care va fi adaugata in fisier"""

    while True:  # cat timp data introdusa este invalida
        print("---> Data invalida. Exemplu data valida: 10.03.2023 12:30.")
        date = input("Introduceti data DD.MM.YYYY HH:MM: ")
        if validate_date(date):  # daca a introdus o valoare valida
            return date


# ---> SORTARI PER OPTIUNE
def sort_as_task():
    """Sorteaza fisierul ascendent in functie de task folosind o lista intermediara.
    Modificarile se fac in fisier si se afiseaza pentru utilizator"""

    with open('Task.csv', 'r') as csv_reader:
        rows = csv.reader(csv_reader, delimiter=',')
        list_rows = []
        for row in rows:
            if row != []:
                list_rows.append(row)

        list_rows.sort()
        with open('Task.csv', 'w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            for row in list_rows:
                csv_writer.writerow([row[0], row[1], row[2], row[3]])

        print("---> ACTUALIZARE FISIER: <---")
        with open('Task.csv', 'r') as csv_reader:
            rows = csv.reader(csv_reader, delimiter=',')
            for row in rows:
                if row != []:
                    print(row)
def sort_des_task():
    """Sorteaza fisierul descendent in functie de task folosind o lista intermediara.
        Modificarile se fac in fisier si se afiseaza pentru utilizator"""

    with open('Task.csv', 'r') as csv_reader:
        rows = csv.reader(csv_reader, delimiter=',')
        list_rows = []
        for row in rows:
            if row != []:
                list_rows.append(row)

        list_rows.sort(reverse=True)
        with open('Task.csv', 'w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            for row in list_rows:
                csv_writer.writerow([row[0], row[1], row[2], row[3]])

        print("---> ACTUALIZARE FISIER: <---")
        with open('Task.csv', 'r') as csv_reader:
            rows = csv.reader(csv_reader, delimiter=',')
            for row in rows:
                if row != []:
                    print(row)
def sort_as_resp():
    """Sorteaza fisierul ascendent in functie de responsabil folosind o lista intermediara.
        Modificarile se fac in fisier si se afiseaza pentru utilizator"""

    with open('Task.csv', 'r') as csv_reader:
        rows = csv.reader(csv_reader, delimiter=',')
        list_rows = []
        for row in rows:
            if row != []:
                list_rows.append(row)

        list_rows.sort(key = lambda x: x[2])
        with open('Task.csv', 'w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            for row in list_rows:
                csv_writer.writerow([row[0], row[1], row[2], row[3]])

        print("---> ACTUALIZARE FISIER: <---")
        with open('Task.csv', 'r') as csv_reader:
            rows = csv.reader(csv_reader, delimiter=',')
            for row in rows:
                if row != []:
                    print(row)
def sort_des_resp():
    """Sorteaza fisierul descendent in functie de responsabil folosind o lista intermediara.
       Modificarile se fac in fisier si se afiseaza pentru utilizator"""

    with open('Task.csv', 'r') as csv_reader:
        rows = csv.reader(csv_reader, delimiter=',')
        list_rows = []
        for row in rows:
            if row != []:
                list_rows.append(row)

        list_rows.sort(key=lambda x: x[2], reverse=True)
        with open('Task.csv', 'w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            for row in list_rows:
                csv_writer.writerow([row[0], row[1], row[2], row[3]])

        print("---> ACTUALIZARE FISIER: <---")
        with open('Task.csv', 'r') as csv_reader:
            rows = csv.reader(csv_reader, delimiter=',')
            for row in rows:
                if row != []:
                    print(row)
def sort_as_category():
    """Sorteaza fisierul ascendent in functie de categorie folosind o lista intermediara.
       Modificarile se fac in fisier si se afiseaza pentru utilizator"""

    with open('Task.csv', 'r') as csv_reader:
        rows = csv.reader(csv_reader, delimiter=',')
        list_rows = []
        for row in rows:
            if row != []:
                list_rows.append(row)

        list_rows.sort(key=lambda x: x[3])
        with open('Task.csv', 'w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            for row in list_rows:
                csv_writer.writerow([row[0], row[1], row[2], row[3]])

        print("---> ACTUALIZARE FISIER: <---")
        with open('Task.csv', 'r') as csv_reader:
            rows = csv.reader(csv_reader, delimiter=',')
            for row in rows:
                if row != []:
                    print(row)
def sort_des_category():
    """Sorteaza fisierul descendent in functie de categorie folosind o lista intermediara.
       Modificarile se fac in fisier si se afiseaza pentru utilizator"""

    with open('Task.csv', 'r') as csv_reader:
        rows = csv.reader(csv_reader, delimiter=',')
        list_rows = []
        for row in rows:
            if row != []:
                list_rows.append(row)

        list_rows.sort(key = lambda x: x[3], reverse=True)
        with open('Task.csv', 'w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            for row in list_rows:
                csv_writer.writerow([row[0], row[1], row[2], row[3]])

        print("---> ACTUALIZARE FISIER: <---")
        with open('Task.csv', 'r') as csv_reader:
            rows = csv.reader(csv_reader, delimiter=',')
            for row in rows:
                if row != []:
                    print(row)
def sort_as_date():
    """Sorteaza fisierul ascendent in functie de data folosind o lista intermediara.
       Modificarile se fac in fisier si se afiseaza pentru utilizator"""

    with open('Task.csv', 'r') as csv_reader:
        rows = csv.reader(csv_reader, delimiter=',')
        list_rows = []
        for row in rows:
            if row != []:
                list_rows.append(row)

        list_rows.sort(key=lambda row: datetime.datetime.strptime(row[1], '%d.%m.%Y %H:%M'))

        with open('Task.csv', 'w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            for row in list_rows:
                csv_writer.writerow([row[0], row[1], row[2], row[3]])

        print("---> ACTUALIZARE FISIER: <---")
        with open('Task.csv', 'r') as csv_reader:
            rows = csv.reader(csv_reader, delimiter=',')
            for row in rows:
                if row != []:
                    print(row)
def sort_des_date():
    """Sorteaza fisierul descendent in functie de data folosind o lista intermediara.
       Modificarile se fac in fisier si se afiseaza pentru utilizator"""

    with open('Task.csv', 'r') as csv_reader:
        rows = csv.reader(csv_reader, delimiter=',')
        list_rows = []
        for row in rows:
            if row != []:
                list_rows.append(row)

        list_rows.sort(key=lambda row: datetime.datetime.strptime(row[1], '%d.%m.%Y %H:%M'),reverse=True)
        with open('Task.csv', 'w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            for row in list_rows:
                csv_writer.writerow([row[0], row[1], row[2], row[3]])

        print("---> ACTUALIZARE FISIER: <---")
        with open('Task.csv', 'r') as csv_reader:
            rows = csv.reader(csv_reader, delimiter=',')
            for row in rows:
                if row != []:
                    print(row)
def sort_it():
        """Aplica functiile de sortare, in functie de nevoile utilizatorului.
       Modificarile se vor face in fisier si se vor afisa pentru utilizator."""
        print("Sortari disponibile:")
        print("a. ascendenta task\nb. descendenta task")
        print("c. ascendenta data\nd. descendenta data")
        print("e. ascendenta responsabil\nf. descendenta responsabil")
        print("g. ascendenta categorie\nh. descendenta categorie")
        opt_sort = input("---> Alege optiunea dorita pentru sortare: ")

        if opt_sort == 'a':
            sort_as_task()
        elif opt_sort == 'b':
            sort_des_task()
        elif opt_sort == 'c':
            sort_as_date()
        elif opt_sort == 'd':
            sort_des_date()
        elif opt_sort == 'e':
            sort_as_resp()
        elif opt_sort == 'f':
            sort_des_resp()
        elif opt_sort == 'g':
            sort_as_category()
        elif opt_sort == 'h':
            sort_des_category()
        else:
            print("---> Optiune incorecta!")
            sort_it()


# ---> FILTRARI PER OPTIUNE
def filter_task(element):
    """Identifica particularitatile unui task ales de utilizator"""

    with open('Task.csv','r') as csv_reader:
        rows = csv.reader(csv_reader, delimiter = ',')
        print(f'{element.upper()} are urmatoarele particularitati:')
        for row in rows:
            if element in row:
                print(f'Data limita:{row[1]}, Responsabil:{row[2]}, Categorie:{row[3]}')
def filter_resp(element):
    """Identifica particularitatile unui responsabil ales de utilizator"""

    with open('Task.csv','r') as csv_reader:
        rows = csv.reader(csv_reader, delimiter = ',')
        print(f'{element.upper()} are urmatoarele task-uri active:')
        for row in rows:
            if element in row:
                print(f'Task:{row[0]}, Data limita:{row[1]}, Categorie:{row[3]}')
def filter_category(element):
    """Identifica particularitatile unei categorii alese de utilizator"""

    with open('Task.csv','r') as csv_reader:
        rows = csv.reader(csv_reader, delimiter = ',')
        print(f'In categoria {element.upper()} se afla urmatoarele task-uri:')
        for row in rows:
            if element in row:
                print(f'Task:{row[0]}, Data limita:{row[1]}, Responsabil:{row[2]}')
def filter_date(element):
    """Identifica task-urile cu deadline in ziua si ora aleasa"""

    with open('Task.csv','r') as csv_reader:
        rows = csv.reader(csv_reader, delimiter = ',')
        print(f'Pe data de {element} este dealine-ul pentru:')
        for row in rows:
            if element in row:
                print(f'Task:{row[0]}, Responsabil:{row[2]}, Categorie:{row[3]}')
def filter_it():
    """Filtreaza fisierul in functie de o optiune aleasa de utilizator"""

    print("---> Filtrari disponibile:")
    print("a. dupa task\nb. dupa data\nc. dupa responsabil\nd. dupa categorie")
    opt_filter = input("---> Alege optiunea dorita pentru filtrare: ")
    if opt_filter == 'a':
        element_filter = input("Introduceti task-ul: ")
        filter_task(element_filter)
    if opt_filter == 'b':
        element_filter = input("Introduceti data si ora: ")
        filter_date(element_filter)
    elif opt_filter == 'c':
        element_filter = input("Introduceti numele responsabilului (Exemplu: Andrei): ")
        filter_resp(element_filter)
    elif opt_filter == 'd':
        element_filter = input("Introduceti numele categoriei: ")
        filter_category(element_filter)


# Exit -> Enter, Evitarea duplicatelor, FUNCTIE PENTRU TASK NOU
def check_exit(element):  # functie cu scop simbolic pentru a oferi context in cod
    """Verifica daca un input este gol
    si iese din loop in acest caz,
    RETURNEAZA true cand se face exit"""
    if element == '':
        return True  #  nu vor mai fi introduse alte elemente
def unique_task(task_input):
    """Verifica daca un task se afla deja in fisier / daca este unic (nou) sau exista deja"""

    with open("Task.csv", 'r') as csv_file:
        rows = csv.reader(csv_file, delimiter = ',')
        list_rows = []
        for row in rows:
            if row != []:
                list_rows.append(row)

        for row in list_rows:
            if row[0] == task_input:
                return False
        return True
def input_task():
    """Adauga unul sau mai multe task-uri in fisier"""

    while True:
        print("Apasati ENTER pentru a incheia procesul de adaugare.")

        category = input("Introduceti categoria: ")
        if check_exit(category):
            break
        category= validate_category(category)

        task = input("Introduceti task: ")
        if check_exit(task):
            break
        while unique_task(task) == False:  # cat timp un task se afla deja in fisier
            print("---> Task-ul exista deja in fisier!")
            task = input("Introduceti task: ")  # se cere un nou task

        date = input("Introduceti data DD.MM.YYYY HH:MM: ")
        if check_exit(date):
            break  # in acest caz utilizator a renuntat la a mai introduce date
        elif validate_date(date) == False:
            date = correct_date()  # preluam data care a fost validata

        responsible = input("Introduceti un responsabil: ")
        if check_exit(responsible):
            break


        with open('Task.csv', 'a') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter = ',')
            csv_writer.writerow([task,date,responsible, category])


# EDITARE TASK
def edit_task():
    old_task = input("Task-ul ce va fi modificat: ")

    with open("Task.csv", 'r') as csv_file:
        rows = csv.reader(csv_file, delimiter=',')
        list_rows = []
        for row in rows:
            if row != []:
                list_rows.append(row)

        no_task = True  # am presupus ca nu exista task-ul

        for row in list_rows:
            if row[0].strip() == old_task:
                no_task = False  # faptul ca task-ul nu exista este Fals
                print(f"Status initial: {row}")
                change = input("a. modific data limita\nb. modific responsabil\nc. modific categorie\nd. modific denumirea task-ului\nAlegere: ")
                if change == 'a':
                    row[1] = input("Introduceti data DD.MM.YYYY: ")
                    if validate_date(row[1]) == False:
                        row[1] = correct_date()  # preluam data care a fost validata
                elif change == 'b':
                    row[2] = input("Introduceti un nou responsabil: ")
                elif change == 'c':
                    row[3] = input("Introduceti noua categorie: ")
                    validate_category(row[3])
                elif change == 'd':
                    row[0] = input("Introduceti noul task: ")
        if no_task == False:  # daca a fost facuta modificarea in fisier (pentru ca a gasit task-ul)
            with open('Task.csv', 'w') as csv_file:
                csv_writer = csv.writer(csv_file, delimiter=',')
                for row in list_rows:
                    csv_writer.writerow([row[0], row[1], row[2], row[3]])

            print("---> ACTUALIZARE FISIER: <---")
            with open('Task.csv', 'r') as csv_reader:
                rows = csv.reader(csv_reader, delimiter=',')
                for row in rows:
                    if row != []:
                        print(row)
        else:
            print("Task-ul introdus nu exista in fisier.")
            edit_task()


# ---> STERGERE TASK
def delete_task():
    with open("Task.csv", 'r') as csv_file:
        del_task = input("Task-ul ce va fi eliminat: ")
        no_task = True  # am presupus ca nu exista task-ul
        with open("Task.csv", 'r') as csv_file:
            rows = csv.reader(csv_file, delimiter=',')
            list_rows = []
            for row in rows:
                if row != []:
                    list_rows.append(row)

        for row in list_rows:
            if row[0].strip() == del_task:
                list_rows.remove(row)
                no_task = False  # faptul ca task-ul nu exista este Fals

        if no_task == False:  # daca a fost facuta modificarea in fisier (pentru ca a gasit task-ul)
            with open('Task.csv', 'w') as csv_file:
                csv_writer = csv.writer(csv_file, delimiter=',')
                for row in list_rows:
                    csv_writer.writerow([row[0], row[1], row[2], row[3]])

            print("---> ACTUALIZARE FISIER: <---")
            with open('Task.csv', 'r') as csv_reader:
                rows = csv.reader(csv_reader, delimiter=',')
                for row in rows:
                    if row != []:
                        print(row)
        else:
            print("Task-ul introdus nu exista in fisier.")
            delete_task()

# MAIN APP
def menu():
    """Ruleaza proceduri asupra unui fisier CSV"""

    user_needs = True
    while user_needs:
        print("---> ORGANIZAREA RESPONSABILITATILOR <---")
        print("1. Listare Date\n2. Sortare\n3. Filtrare\n4. Adaugare Task\n5. Editare Task\n6. Stergere Task\n7. Adaugare Categorie")
        option = input("---> Alege optiunea dorita: ")
        if option == '1':
            sort_as_category()
        elif option == '2':
            sort_it()
            print("\n")
        elif option == '3':
            filter_it()
            print("\n")
        elif option == '4':
            print("---> Incepem procesul de adaugare Task:")
            input_task()
            print("\n")
        elif option == '5':
            edit_task()
        elif option == '6':
            delete_task()
        elif option =='7':
            new_category = input("---> Adaugati o noua categorie: ")
            while category_duplicate(new_category) == True:  # cat timp noua categorie e duplicat
                print("Categoria exista deja in fisier!")
                new_category = input("---> Adaugati o noua categorie: ")
            add_category(new_category)
        else:
            print("Introduceti o optiune de la 1 -> 7.")
            menu()

menu()




