set1 = {1, 2, 3, 4, "adam", "nimoy"}
set2 = {4, 5, 6, "adam"}

intersection = set1.intersection(set2)

print(intersection)

#alternate solution
intersection2 = set()

for elem in set1:
    if elem in set2:
        intersection2.add(elem)

print(intersection2)
