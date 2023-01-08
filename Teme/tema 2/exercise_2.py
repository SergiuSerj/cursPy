"""varianta unu"""

# number_added = int(input("Enter some text: "))
# if number_added % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")


"""varianta doi cu definitie"""

def check_even_odd(number_added):
    if number_added % 2 == 0:
        print(f"The number {number_added} is even.")
    else:
        print(f"The number {number_added} is odd.")

number_added = int(input("Enter some number: "))
check_even_odd(number_added)
