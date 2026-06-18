nested_list = [4, [1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = []

for elem in nested_list:
    # verifies if, the element of the list is in a data type.
    # In this case, the lists are an element.
    # The element contains the nest within the elem, that is 
    # also a data type.
    # Therefore, it is instantiated, that the elem contains the 
    # list as a data type. 
    if isinstance(elem, list):
        for nest in elem:
            flat_list.append(nest)
    else:
        flat_list.append(elem)

print(f"flat_list = {flat_list}")

set_list = list(set(flat_list))
print(f"list = {set_list}")