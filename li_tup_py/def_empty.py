list_a = [1, 2, 3, 4]

def empty_li(list_a):
    if len(list_a) == 0:
        return "Empty"
    else:
        return "Not Empty"
    
print(empty_li(list_a))