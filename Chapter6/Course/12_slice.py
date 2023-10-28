my_list = [1, 2, 3, 4, 5]
new_list1 = my_list[1:4]
print(new_list1)

new_list2 = my_list[:]
print(new_list2)

new_list3 = my_list[::2]
print(new_list3)

new_list4 = my_list[:4:2]
print(new_list4)

new_list5 = my_list[::-1]
print(new_list5)

new_list6 = my_list[3:1:-1]
print(new_list6)

my_tuple = (1, 2, 3, 4, 5)
my_tuple1 = my_tuple[:1:-2]
print(my_tuple1)
