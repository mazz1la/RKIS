input_x = int(input("Введите число, чтобы узнать есть ли он в массиве: "))
for i in range(10):
    if i == input_x:
        print("Число содержится в массиве")
        break
else:
    print("Число не содержится в массиве")