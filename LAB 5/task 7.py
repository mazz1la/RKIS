import math
x = int(input("Введите x: "))
y = int(input("Введите y: "))
radius = int(input("Введите радиус: "))

distance = math.sqrt(x**2 + y**2)

if distance <= radius:
    print("Точка принадлежит кругу")
else:
    print("Точка не принадлежит кругу")