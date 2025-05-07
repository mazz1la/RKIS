import random
numbers = [random.randint(a: 1, b: 100) for i in range(10)]
min_value = min(numbers)
min_index = numbers.index(min_value)
print("Массив чисел: ", numbers)
print(f'Минимальный элемент коллекции {min_value}')
print("Индекс минимального числа:", min_index)