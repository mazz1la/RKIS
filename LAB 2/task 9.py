def comparison():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    if a > b:
        print(f"Наибольшим является {a}")
    elif b > a:
        print(f"Наибольшим является {b}")
    else:
        print("Числа равны, введите другие")
comparison()