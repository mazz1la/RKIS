strings = ['apple', 'soccer', '1234555', 'https://moodle', 'snake', 'https://pampam']
print("Список до изменения", strings)
i = 0
while i <len(strings):
    if not strings[i].startswith("https://"):
        del strings [i]
    else:
        i += 1
print("Список после изменения:", strings)