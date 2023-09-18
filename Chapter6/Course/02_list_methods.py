name_list = ['Leo', 'Lucas', 'Laurent']
# trouver l'indice de l'élément spécifié
# print(name_list.index('Laurent'))   # 2
# Insertion d'un élément
name_list.insert(1, 'Kevin')
# print(name_list)    # ['Leo', 'Kevin', 'Lucas', 'Laurent']
# print(len(name_list))


my_list = [1, 2, 3, 1]
# modifier la valeur d'un élément
# my_list[0] = 5
# ajouter un élément
# my_list.append(4)
# my_list.append([4, 5, 6]) # [1,2,3,[4,5,6]]
# my_list.extend([4, 5, 6]) # [1,2,3,4,5,6]
# supprimer l'élément
# del my_list[0] # [2, 3]
# my_list.pop(0) # [2, 3]
# my_list.remove(1) # [2, 3, 1]
# my_list.clear()
# compter le nombre d'élément dans une liste
# print(my_list.count(1)) # 2
print(len(my_list)) # 4
print(my_list)
