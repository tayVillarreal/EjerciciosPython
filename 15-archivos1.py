#Leer archivos
def app():

    #with open* se abre y se cierra de manera automatica
    with open('archivo.txt') as archivo: #No le pasamos otro parametro por que por defaul viene con R que es de lectura
        for contenido in archivo:
            print(contenido)

app()   