def sieve(list_num):
    numbers = []
    for num in reversed(list_num):
        if num not in numbers:
            numbers.append(num)
    return tuple(numbers)

list_num = [5, 5, 7, 8, 8, 10, 12, 14, 14, 18, 20]
print(sieve(list_num))