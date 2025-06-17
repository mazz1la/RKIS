array = [1, 2, 3, 4, 1, 5, 2, 7, 5, 8, 6, 9]

def numbers(array):
    sum_num = 0
    for num in array:
        if num > 0:
            sum_num += num

    min_num = min(array)
    max_num = max(array)
    index_min = array.index(min_num)
    index_max = array.index(max_num)

    start = min(index_min, index_max) + 1
    end = max(index_min, index_max)


    computation_composition = 1
    for i in range(start, end):
        computation_composition *= array[i]

    print(f"Сумма положительных чисел: {sum_num}, Произведение чисел между минимальным и максимальным: {computation_composition}")
numbers(array)