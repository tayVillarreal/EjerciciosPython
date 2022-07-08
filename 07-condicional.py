#Revisar si una condicion es igual a
balance = 500

if balance > 0:
    print('Puedes pagar')

#Else

if balance >= 0:
    print('Puedes pagar')
else:
    print('No tienes saldo')  

#Likes
likes = 200
if likes ==200:
    print('Excelente, 200 likes')    

#If revisa si la condicion es diferente
lenguaje = 'PHP'
if not lenguaje == 'Python':
    print('Es distinto')    

#Evaluar un Boolean
usuario_autonticado = True

if usuario_autonticado:
    print('Acceso al sistema')
else:
    print('Debes iniciar sesión')    

#Evaluar un elemento de una lista
lenguajes = ['Python', 'Java', 'C', '.Net']
if 'PHP' in lenguajes:
    print('PHP si existe')
else:
    print('No esta en la lista')    

 #If anidados
usuario_autonticado = True
usuario_admin = True

if usuario_autonticado:
    if usuario_admin:
        print('Acceso Total')
    else:    
        print('Acceso al sistema')
else:
    print('Debes iniciar sesión')   

#Ejemplo con elif
ocupacion = 'Jubilado'

if ocupacion == 'Estudiante':
    print('Tiene 50% de Descuento')
elif ocupacion == 'Jubilado':
    print('Tiene 75% de Descuento')    
else:
    print('Debes pagar el 100%')

#Condicionales con For

for lenguaje in lenguajes:
    if lenguaje == 'Python':
        print(lenguaje.upper())
    else:
        print(lenguaje)
       