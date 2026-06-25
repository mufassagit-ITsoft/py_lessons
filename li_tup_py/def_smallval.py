list_a = [1, 2, 3, 4]

def small_val(list_a):
    if len(list_a) == 0 or len(list_a) == 1:
        return None
    else:
        min_val1 = min(list_a)
        list_a.remove(min_val1)
        min_val2 = min(list_a)
print(small_val(list_a))