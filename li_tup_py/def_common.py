list_a = [4, 5, 6]
list_b = [1, 2, 3]

def common_num(list_a, list_b):
    common_li = []
    for num in list_a:
        if num in list_b:
            common_li.append(num)
    return common_li
print(common_num(list_a, list_b))