#Ejemplo de interador

# #Crear una lista
my_list = [1,2,3,4]

#Obtener el interador
my_ite = iter(my_list)

#Usar el iterador
print(next(my_ite))
print(next(my_ite))
print(next(my_ite))
print(next(my_ite))



#Interar por texto

#Creando la cadena
text = "Hola mundo."

#Creando el iterador
iter_texto = iter(text)

#Iterar en la cadena
for char in iter_texto:
    print(char)



#Iterador para números impares

#Limite
limit = 10

#Crear iterador
odd_iter = iter(range(1, limit+1,2))

#~Usar el iterador
for num in odd_iter:
    print(num)