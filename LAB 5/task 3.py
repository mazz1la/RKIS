import random

numbers = [random.randint(1, 100) for i in range(55)]

even_numbers = []
odd_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

even_numbers.sort()

print("Отсортированные четные числа:", even_numbers)