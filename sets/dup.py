list_1 = ["a", "a", "b", "c"]

if not list_1:
    print([])
else:
    for char in range(len(list_1)):
        set_list = list(set(list_1))
    print(sorted(set_list))

# alternate solution

set_list2 = list(set(list_1))
print(sorted(set_list2))

# alternate solution 2, optimal
set_list3 = list(dict.fromkeys(list_1))
print(set_list3)