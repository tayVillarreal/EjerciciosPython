#Constructor

class Restaurant:

    def __init__ (self, nombre, categoria, precio):
        self.nombre = nombre #Atributo
        self.categoria = categoria
        self.precio = precio

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio} \r\n')    

#Instancia de una clase
restaurant = Restaurant('Pizza', 'Italiana', 90) #Esto vendria siendo un objeto        
restaurant.mostrar_informacion() #Metodo

restaurant2 = Restaurant('Burger', 'Americana', 30) #Esto vendria siendo un objeto        
restaurant2.mostrar_informacion() #Metodo
