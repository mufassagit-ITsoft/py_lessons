a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]
result = []

for elem in a:
    if elem in b:
        result.append(elem)
print(result)

# alternative solution
set_a = set(a)
set_b = set(b)
result2 = set_a.intersection(set_b)
list_result = list(result2)
print(list_result)
