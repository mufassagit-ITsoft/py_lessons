list_a = [1, 2, 3, 4]

def second_val(list_a):
    if len(list_a) == 0 or len(list_a) == 1:
        return None
    else:
        max_val1 = max(list_a)
        list_a.remove(max_val1)
        max_val2 = max(list_a)