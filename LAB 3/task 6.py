def odd_elements():
    entering_elements = input("Введите числа через пробел: ")
    elements = list(map(int, entering_elements.split()))
    product = 1
    for i in range(len(elements)):
        if i % 2 != 0:
            product *= elements[i]
    return product
result = odd_elements()
print("Произведение чисел с нечетными индексами: ", result)