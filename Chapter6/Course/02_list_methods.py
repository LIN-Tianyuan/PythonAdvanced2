name_list = ['Leo', 'Lucas', 'Laurent']
# trouver l'indice de l'élément spécifié
print(name_list.index('Laurent'))   # 2
# Insertion d'un élément
name_list.insert(1, 'Kevin')
print(name_list)    # ['Leo', 'Kevin', 'Lucas', 'Laurent']
print(len(name_list))

my_list = [1, 2, 3]
# modifier la valeur d'un élément
my_list[0] = 5
print(my_list)
