numbers = [1,2,3,4,5,9,10,-5, -15, -16,-17, -1]
positive_nums = []

for num in numbers:
    if num > 0:
        positive_nums.append(num)

print("Исходный массив:", numbers)
print("Только положительные числа:", positive_nums)