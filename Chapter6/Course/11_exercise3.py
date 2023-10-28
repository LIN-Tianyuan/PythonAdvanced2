name_string = "fruit friend apple"
count = name_string.count("fr")
print("Il y a " + str(count) + " fr dans la chaîne fruit fruit friend apple.")

new_name_string = name_string.replace(" ", "|")
print("La chaîne fruit friend apple est remplacée par un espace et "
      "le résultat est " + new_name_string + ".")

name_list = new_name_string.split("|")
print(f"Le résultat de la division de la châine fruit friend apple par | est {name_list}.")