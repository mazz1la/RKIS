list = ["level", "book", "match", "python"]
def change(list):
    list[0], list[-1] = list[-1], list[0]
    return list
print(change(list))