name = 'Alex'
address = 'Paris'
age = 18
height = 1.83
print("Je m'appelle " + name + ". J'habite à " + address + " et j'ai " + str(age) + ' ans.')
print("Je m'appelle %s. J'habite à %s et j'ai %d ans." % (name, address, age))
print("Je m'appelle %s. J'ai %d ans et je mesure %.2f m." % (name, age, height))

print(f"Je m'appelle {name}, J'ai {age} ans et je mesure {height} m.")

print("Le résultat de 1 * 1 est: %d" % (1 * 1))
print(f"Le résultat de 1 * 1 est: {1 * 1}")
print("Le type de chaîne en Python est : %s" %type('chaîne'))