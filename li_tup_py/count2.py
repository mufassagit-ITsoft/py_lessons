list_1 = []
count = 0

for char in range(len(list_1)):
    if list_1[char] > 3:
        count += 1

print(count)

#alternate solution, optimal

count2 = sum(1 for elem in list_1 if elem > 3)
print(count2)
