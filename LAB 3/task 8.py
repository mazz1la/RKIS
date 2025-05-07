import random
length = random.randint(1, 25)
array = []
num = 3 * length
for i in range(length):
    array.append(num)
    num -= 3
print(f"Рандомный массив: {array}")