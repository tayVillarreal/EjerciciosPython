#While = se ejecuta mientras una condicion sea verdadera
pregunta = 'Agrega un numero y te dire si es par \r\n'
pregunta += ' (Escribe "cerrar" para salir de la aplicacion)\r\n'

preguntar = True
while preguntar:

    numero = input(pregunta)
    
    if numero == 'cerrar':
        preguntar= False
    else:
        numero = int(numero)

        if numero % 2 == 0:
                print(f'El numero {numero} es par')
        else:
                print(f'El numero {numero} es impar')

# While como for, siempre añadirle un incremento para evitar bucles infinitos

numero = 0

while numero <= 10:
    print (numero)
    numero += 1 #Incremento

#If dentro del while



