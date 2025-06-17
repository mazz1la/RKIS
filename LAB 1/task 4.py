def cout_it(sequence):
    numbers = {}
    for num in sequence:
        cur_num = int(num)
        if cur_num in numbers.keys():
            numbers[cur_num] += 1
        else:
            numbers[cur_num] = 1
    first_num = -1
    first_cout = 0
    second_num = -1
    second_cout = 0
    third_num = -1
    third_cout = 0
    for k, v in numbers.items():
        if v >= first_cout:
            first_num, second_num, third_num = k, first_num, second_num
            first_cout, second_cout, third_cout = v, first_cout, second_cout
    return {first_num: first_cout, second_num: second_cout, third_num: third_cout}

print(cout_it("213125345342"))