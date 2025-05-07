def calc(a,b):
    if a % b == 0:
        print("Делится")
    else:
        print("Не делится")
    return a % b == 0
calc(20,5)