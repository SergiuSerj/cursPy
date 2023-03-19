""" 1 """
# class Example:
#
#     def __init__(self, val=5):
#         self.first = val
#
#     def set_second(self, val=5):
#         self.second = val
#
#
# obj_1 = Example()
# print(obj_1)
# print(obj_1.__dict__)
#
# obj_2 = Example(2)
# print(obj_2)
# print(obj_2.__dict__)
#
# obj_2.third = 5
# print(obj_2.__dict__)
# se pot adauga o alta proprietate la o clasa


""" 2 """
# class Example:
#
#     def __init__(self, val=5):
#         self.__first = val   # privat __
#
#     def set_second(self, val=5):
#         self.second = val
#
#
# obj_1 = Example()
# obj_1.set_second(4)
# print(obj_1._Example__first) #functioneaza sa apelezi valoareqa privata
# # print(obj_1.__first)


""" 3 """

# class Example:
#
#     __counter = 0   #valoare globala se modifica si ramane modificata la fiecare initieliare
#
#     def __init__(self, val=5):
#         self.__first = val
#         # Example.__counter += 1
#         self.__counter += 1
#
#
# obj_1 = Example()
# obj_2 = Example(2)
# obj_3 = Example(4)
#
# print(obj_1.__dict__, obj_1._Example__counter)
# print(obj_2.__dict__, obj_2._Example__counter)
# print(obj_3.__dict__, obj_3._Example__counter)


""" 4 """

# class Example:
#
#     __counter = 0
#
#     def __init__(self, val=1):
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 2
#
# object_1 = Example()
#
# # print(object_1.a)
# # print(object_1.b)
#
# print(hasattr(object_1, "b"))
# print(hasattr(object_1, "a"))

""" 5 """
# class Example:
#
#     __counter = 0
#
#     def __init__(self, val=1):
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 2
#
# object_1 = Example()
# print(getattr(object_1, "a"))

""" 6 """
# class Example:
#     def __init__(self, val):
#         self.val = val
#


""" Mosteniri"""

# class Vehicule:
#     pass
#
# class Masini(Vehicule):
#     pass
#
# class MasiniDeTeren(Masini):
#     pass
#
# print(issubclass(MasiniDeTeren, Vehicule))


"""verificam cu isnstance"""

# class Vehicule:
#     pass
#
# class Masini(Vehicule):
#     pass
#
# class MasiniDeTeren(Masini):
#     pass
#
#
# vehicul_1 = Vehicule()
# masina_1 = Masini()
# masina_de_teren_1 = MasiniDeTeren()
#
# print(isinstance(masina_1, MasiniDeTeren))


""" rescriere de metode """

class SuperClasa:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return  f"Numele meu este {self.name}"

class SubClasa(SuperClasa):
    def __init__(self):
        pass
        super(self, SuperClasa).__init__(self)

