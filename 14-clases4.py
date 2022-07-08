#Herencias

class Restaurant:

    def __init__ (self, nombre, categoria, precio):
        self.nombre = nombre #Atributo
        self.categoria = categoria 
        self.__precio = precio #Default: public
        #PROTECTED se le pone un _ antes del atributo y se puede acceder dentro de la clase
        #PRIVATE se le pone __ antes y no se puede acceder o modificar, solo a travez de un metodo como Get and Set

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.__precio} \r\n')    

    #GETTERS Y SETTERS - Get = Obtiene un valor, SET = Agrega un valor o lo modifica
    def get_precio(self):
        print(self.__precio)

    def set_precio(self, precio):
        self.__precio = precio    

#Instancia de una clase
restaurant = Restaurant('Pizza', 'Italiana', 90) #Esto vendria siendo un objeto        
restaurant.mostrar_informacion() #Metodo
restaurant.set_precio(29) #modificamos el precio con el metodo set
restaurant.get_precio() #llamamos a la funcion get para traer el precio


restaurant2 = Restaurant('Burger', 'Americana', 30) #Esto vendria siendo un objeto        
restaurant2.mostrar_informacion() 
restaurant2.set_precio(79)
restaurant2.get_precio()


# Crear una clase hijo del Restaurante

class Hotel(Restaurant):
    def __init__ (self, nombre, categoria, precio):
        super().__init__(nombre, categoria, precio)

hotel = Hotel ('Hotel POO', '5 Estrellas', 200)
hotel.mostrar_informacion()        


