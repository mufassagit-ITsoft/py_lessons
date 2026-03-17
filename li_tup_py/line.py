li_1 = ["a", "b", "c", "d"]

for i in range(len(li_1)):
    print(li_1[i], end=" ")
print("\n")

# alternate solution, optimal

print(*li_1, sep=" ")