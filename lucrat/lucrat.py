word = "temperament"
start_letter = word[0]
end_letter = word[-1]
display_word = word

for i in display_word:
    if i == start_letter or i == end_letter:
        continue
    else:
        display_word = display_word.replace(i, '_')

attemps = 6
while attemps > 0:
    print(f"Cuvantul este: {display_word}")
    letter = input("Introduceti litera: ").lower()
    if letter in word.lower():
        for i in word.lower():
            display_word
    else:
        attemps -= 1