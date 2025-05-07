width = int(input("Введите ширину прямоугольника: "))
length = int(input("Введите длину прямоугольника: "))
square_side = int(input("Введите сторону квадрата: "))

def calculate_area_ratio():
    rectangle_area = width * length
    square_area = square_side * square_side
    area_ratio = rectangle_area / square_area
    return area_ratio

result = int(calculate_area_ratio())
print(f"Количество квадратов которые можно вырезать: {result}")