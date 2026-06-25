set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

def set_int(set1, set2):
    int_set = set1.intersection(set2)
    return int_set

print(set_int(set1, set2))