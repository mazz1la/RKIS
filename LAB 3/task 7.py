def check_digits(input_number):
    digit_string = str(input_number)
    for idx in range(len(digit_string) - 1):
        if digit_string[idx] < digit_string[idx + 1]:
            return "Цифры числа не расположены по убыванию."
        elif digit_string[idx] == digit_string[idx + 1]:
            return "Цифры числа расположены по убыванию."
    return "Цифры числа расположены по убыванию."
result = check_digits(input("Введите число: "))
print(result)