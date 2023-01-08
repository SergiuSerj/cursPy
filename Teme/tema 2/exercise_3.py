"""varianta unu"""

year = int(input("Introduceti un an: "))

if (year % 400 == 0) or (year %100 != 0) and (year %4 ==0):
    print("Anual introdus este un an bisect")
else:
    print("Anul introdus nu este un an bisesct")

