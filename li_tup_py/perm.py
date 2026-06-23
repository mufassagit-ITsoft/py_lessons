import itertools

items = ['A', 'B', 'C']
perm_lists = list(itertools.permutations(items))
print(perm_lists)

for perm in perm_lists:
    # perm by itself is a tuple, as permutations produce tuples.
    # when casting it to a list, the tuple becomes a list.
    print(perm)
    print(list(perm))