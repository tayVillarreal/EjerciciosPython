class Restaurant:

    def agregar_restaurant(self, nombre):
        self.nombre = nombre #Atributo
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}')    

#Instancia de una clase
restaurant = Restaurant() #Esto vendria siendo un objeto        
restaurant.agregar_restaurant('Pizzeria') #Metodo
restaurant.mostrar_informacion()

restaurant2 = Restaurant() 
restaurant2.agregar_restaurant('Hamburguesa')
restaurant2.mostrar_informacion()

