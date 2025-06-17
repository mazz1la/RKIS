try:
    string = int(input("Введите стороку или число: "))
    print(string)
except ValueError:
    print("Ошибка")