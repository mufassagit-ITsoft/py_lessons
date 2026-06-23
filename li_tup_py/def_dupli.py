list_a = [1, 1, 2, 3, 4, 4]

def dupli_elem(list_a):
    sort_li = sorted(list_a)
    set_li = list(set(sort_li))
    return set_li

print(dupli_elem(list_a))