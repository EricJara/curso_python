numbers = {1:"uno", 2:"dos", 3:"tres"}
print(numbers)
print(numbers[2])
information = {"Nombre": "Eric",
               "Apellido": "Jara",
               "Edad": 29,
               "DNI": 75059196,
               "Altura":1.68}
print(information)
del information["Edad"] # Funcion de eliminar edad del diccionario
print(information)
claves = information.keys()
print(claves) # Imprime el nombre de las columnas de la lista
print(type(claves))
values = information.values()
print(values) # Imprime los valores que existe en las columnas de la lista
pairs = information.items() # Imprime solo los pares de la lista
print(pairs)
Contactos = {"Eric":{"Nombre": "Eric",
               "Apellido": "Jara",
               "Edad": 29,
               "DNI": 75059196,
               "Altura":1.68},
               "Melissa":{"Nombre": "Melissa",
               "Apellido": "Jara",
               "Edad": 24,
               "DNI": 71521185,
               "Altura":1.58}}

print(Contactos["Melissa"])