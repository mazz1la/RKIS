def positive_num():
    array = []
    input_elements = int(input("Введите количество чисел в массиве: "))
    for i in range(input_elements):
        num = int(input("Введите число: "))
        array.append(num)
    counter = 0
    for number in array:
        if number > 0:
            counter += 1
    print("Количество положительных чисел:", counter)

positive_num()