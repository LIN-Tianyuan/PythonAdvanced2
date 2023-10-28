name = 'Alex'
print(name[0]) # A
print(name[-1]) # x
print(name.index('l')) # 1
print('----------')

name_string = 'Leo and Laurent'
print(name_string.index('and')) # 4
new_name_string = name_string.replace('Leo', 'Kevin')
print(name_string)
print(new_name_string)

print('----------')
name_list = name_string.split(" ")
print(name_list)

print('----------')
# Suppression des espaces avant et arrière
name_string = '  Leo and Laurent  '
name_strip = name_string.strip()
print(name_strip)

print('----------')
# Suppression de la chaîne spécifiée avant et arrière
name_string = '12Leo and Laurent21'
name_strip = name_string.strip("12")
print(name_strip)

print('----------')
name_string = "Jean-Lucas and Lucas"
print(name_string.count("Lucas"))
print(len(name_string))