import itertools

list_a = [1, 2, 3]

def perm_li(list_a):
    poss_li = itertools.permutations(list_a)
    return list(poss_li)
print(perm_li(list_a))

for items in perm_li(list_a):
    print(list(items))

