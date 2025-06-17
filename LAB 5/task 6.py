array = [1,-5, 0, 3, -4]
for i in range(len(array)):
    if array[i] > 0:
        array[i] = -array[i]
    else:
        array[i] = abs(array[i])
print(array)