"""
list2 = []
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in my_list:
    if i % 2 == 0:
        list2.append(i)
print(f"Une boucle for retire les numéro pairs de la liste {my_list} "
      f"et forme une nouvelle liste {list2}.")
"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = []
i = 0
while i < 10:
    if my_list[i] % 2 == 0:
        list2.append(my_list[i])
    i = i + 1
print(f"Une boucle for retire les numéro pairs de la liste {my_list} "
      f"et forme une nouvelle liste {list2}.")