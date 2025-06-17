C = input("Введите символ C: ")
A = ["voleball", "football", "basketball", "alpha", "arena"]
count = 0
for word in A:
    if len(word) > 1 and word.startswith(C) and word.endswith(C):
        count += 1

print("Список слов:", A)
print(f"Количество слов, начинающихся и заканчивающихся на '{C}': {count}")