class Calculator:

    def __init__(self):
        self.operator_1 = self.validate_float(input('Alegeti primul numar: '))
        self.semn = self.validate_sign(input('Alege semnul: '))
        self.operator_2 = self.validate_float(input('Alegeti al doilea numar: '))
        if self.operator_2 == 0 and self.semn == "/":
            self.operator_2 = self.validare_zero_divizare()

    def validate_float(self, operator):
        while not operator.isdigit():
            operator = input("numarul este incorect! Alegeti din nou: ")
        return float(operator)

    def validate_sign(self, semn):
        lista = ["+", "-", "*", "/", "c"]
        while semn not in lista:
            semn = input("introduceti din nou un semn: ")
        return semn



    def validare_zero_divizare(self):
        while self.operator_2 == 0 and self.semn == "/":
            self.operator_2 = self.validate_float(input("Reintroduceti un numar diferit de 0: "))
        return self.operator_2


    def adunare(self):
        return self.operator_1 + self.operator_2

    def scadere(self):
        return self.operator_1 - self.operator_2

    def inpartire(self):
        return self.operator_1 / self.operator_2

    def inmultire(self):
        return self.operator_1 * self.operator_2

    def __str__(self):
        if self.semn == "+":
            return f'{self.operator_1} {self.semn} {self.operator_2} = {self.adunare()}'
        elif self.semn == "-":
            return f'{self.operator_1} {self.semn} {self.operator_2} = {self.scadere()}'
        elif self.semn == "*":
            return f'{self.operator_1} {self.semn} {self.operator_2} = {self.inmultire()}'
        elif self.semn == "/":
            return f'{self.operator_1} {self.semn} {self.operator_2} = {self.inpartire()}'
        else:
            return f"Operatiea nu exista!"

obj_calculator = Calculator()


# object_name = obj_calculator
# class_name = Calculator
# proprity = self_operator1, self_operator2 , semn
# activity = adunare,scadere, inmultire, inpartire

