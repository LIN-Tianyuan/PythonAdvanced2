name = {"Python", "666", "Python", "y6"}
print(name)

print("----------")
my_set = {"Leo", "Laurent"}
my_set.add("Kevin")
print(my_set)
print("----------")
my_set.remove("Leo")
print(my_set)
print("----------")
element = my_set.pop()
print("Deleted: " + element)
print(my_set)
print("----------")
my_set.clear()
print(my_set)
print("----------")
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.difference(set2)
print(f"set1 : {set1}")
print(f"set2 : {set2}")
print(f"set3 : {set3}")
print("----------")
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set1.difference_update(set2)
print(f"set1 : {set1}")
print(f"set2 : {set2}")
print("----------")
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.union(set2)
print(f"set1 : {set1}")
print(f"set2 : {set2}")
print(f"set3 : {set3}")
print("----------")
set1 = {1, 2, 3}
print(len(set1))
print("----------")
for i in set1:
    print(i)