#Array o como se lo conoce en Python "List"

lenguajes = ['Python', 'Java', 'C', '.Net']

print(lenguajes)

#Los array comienzan con la posicion 0
print(lenguajes[0])

#Ordenar los elementos
lenguajes.sort()
print(lenguajes)

#Acceder a un elemento dentro de un texto
aprendiendo = f'Estoy aprendiendo {lenguajes[3]}'
print(aprendiendo)

#Modificando valores de un arreglo
lenguajes[2] = 'PHP'
print(lenguajes)

#Agregar elemento al Array
lenguajes.append('Ruby')
print(lenguajes)

#Eliminar un elemento del array
del lenguajes[2]
print(lenguajes)

#Eliminar un elemento de un array 
lenguajes.pop() #Elimina el ultimo elemento
print(lenguajes)

lenguajes.pop(0) #Elimina el elemento especifico
print(lenguajes)

#Eliminar por nombre
lenguajes.remove('C')
print(lenguajes)

