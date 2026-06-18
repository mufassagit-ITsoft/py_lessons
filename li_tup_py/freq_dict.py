a = ["a", "a", "b", "c", "a", "b", "A", "A", "B", "C"]
b = [1, 2, 3, 4, 3, 2, 1, 2]

output = {}

for elem in a:
    if elem not in output:
        output[elem] = 1
    else:
        output[elem] += 1

print(f"list = {output}")