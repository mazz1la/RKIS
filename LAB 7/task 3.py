numbers = [1, 2, 3, 4, 5, 9, 10, -5, -15, -16,-17, -1, 15, 25]
positive_nums = []

for num in numbers:
    if 10 <= num <= 99:
        positive_nums.append(num)

positive_nums.sort()

print("Исходный массив:", numbers)
print("Положительные двузначные числа:", positive_nums)