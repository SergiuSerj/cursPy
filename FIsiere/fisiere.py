"""import fisiere"""
# "r" - citeste si nu adauga
# "w" - scrie in fisier si daca nu este il creaza si ruleaza in continuare pana il inchid
#     - daca este scris, sterge si  il rescrie
# "a" - adauga scris
# "r+" - citeste si scrie

"mod1"
# file = open("data.txt", "w")
# file.write("SERGIU")
# file.close()

"mod2"

# file = open("data.txt", "w")
# try:
#     file.write("Sergiu")
# finally:
#     file.close()

"mod3"
# with open ("data2.txt", "w") as variabila_temporara:
#     variabila_temporara.write("e vara")

"""citire din fisier"""

"mod 1"
# with open("data.txt", "r") as variabila:
#     for line in variabila.readlines():
#         print(line)

"mod 2"

with open("data.txt", "r") as variabila:
    while True:
        line = variabila.readlines()

