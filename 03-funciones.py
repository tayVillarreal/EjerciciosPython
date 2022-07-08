def informacion(lenguaje, puesto = 'desconocido' ):
   print(f'aprendo {lenguaje} y soy {puesto}')

informacion('python', 'programador')
informacion('java')


#Funciones 2


def informacion_2(nombre):
   return nombre

empleado = informacion_2('Juan')   

print(empleado)

#Metodos

nombre = "Tay"

print( nombre.upper())
#imprime TAY
