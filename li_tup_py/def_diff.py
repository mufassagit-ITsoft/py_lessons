list_a = []
list_b = [1, 3]

def diff_list(list_a, list_b):
    int_list = []
    for num in list_a:
        if num not in list_b:
            int_list.append(num)
    return int_list
print(diff_list(list_a, list_b))
