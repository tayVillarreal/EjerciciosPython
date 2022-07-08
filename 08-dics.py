#Objetos o diccionarios
cancion = {
    'artista': 'Louis Tomlinson', #Key y valor
    'cancion': 'Walls',
    'lanzamiento' : 2019,
}

#Acceder a los elementos de la lista
print(cancion['artista'])
print(cancion['lanzamiento'])

#Mezclar con un string
artista = cancion['artista']
print(f'Estoy escuchando a {artista}')

#Agregar nuevos valores
cancion['playlist'] = 'Pop'
print(cancion)

#Reemplazar valor existente
cancion['cancion'] = 'Mind'
print(cancion)

#Eliminar un elemento de la lista
del cancion['lanzamiento']
print(cancion)

#Otra forma de acceder a un valor y en caso  de que no exista ponerle un msj
print(cancion.get('pareja', 'no existe ese valor'))


#Iterar en el diccionario

for llave, valor in cancion.items():
    print(llave, valor)

    