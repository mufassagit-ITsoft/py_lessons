list_a = ['a', 'b', 'c', 'b']
rem_elem = 'd'

def elem_rem(list_a, rem_elem):
    if len(list_a) == 0:
        print("Empty List")
    elif rem_elem not in list_a:
        print("Not Found")
    else:
        new_list = [elem for elem in list_a if elem != rem_elem]
        return new_list

print(elem_rem(list_a, rem_elem))