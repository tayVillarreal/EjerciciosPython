#Entrada de datos 

nombre = input('Cual es tu nombre? \r\n') #\r\n es para el salto de linea

print(f'Hola {nombre}')

#Leer datos que serán numeros

edad= input('Cual es tu edad? \r\n')
#convertir edad (string) a int
edad = int(edad)

if edad >= 18:
    print('Ya puedes votar')
else:
    print ('Aún no puedes votar')    

# Mezclarlo con operadores
#Numero par
numero = input ('Agrega un numero \r\n')
numero = int(numero)

if numero % 2 == 0:
    print(f'El numero {numero} es par')
else:
    print(f'El numero {numero} es impar')  



