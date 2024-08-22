class Autos:
    def __init__(self, marca, modelo, año, color, transmision, precioCompra, tipo):
        self.cantidad_ruedas = 4
        self.capacidad = "5 pasajeros"
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.transmision = transmision
        self.precioCompra = precioCompra
        self.precioVenta = 0
        self.tipo = tipo
#Se utiliza para ir almacenando los datos de los autos en las variables que corresponden
    @staticmethod
    def RecibirDatos():
        print("******Registrar auto*******")
        marca = input("Ingrese la marca del auto: ")
        modelo = input("Ingrese el modelo del auto: ")
        año = int(input("Ingrese el año del auto: "))
        color = input("Ingrese el color del auto: ")
        transmision = input("Ingrese la transmisión del auto: ")
        precioCompra = float(input("Ingrese el precio de compra del auto: $"))
        tipo = input("Ingrese el tipo del auto (Importado o Nacional): ")
       
        
        return Autos(marca, modelo, año, color, transmision, precioCompra, tipo)
#Aquí se realiza la impresión de la información del auto registrado

    def MostrarDatos(self):
        print("******Datos del auto*******")
        print("La marca del auto es:", self.marca)
        print("El modelo del auto es:", self.modelo)
        print("El año del auto es:", self.año)
        print("El color del auto es:", self.color)
        print("La transmisión del auto es:", self.transmision)
        print("El precio de compra del auto es: $", self.precioCompra)
        print("El tipo del auto es:", self.tipo)
        print("La cantidad de ruedas del auto es:", self.cantidad_ruedas)
        print("La capacidad del auto es:", self.capacidad)
        print("El precio de venta del auto es: $", self.precioCompra * 1.4)


auto1 = Autos.RecibirDatos()
auto1.MostrarDatos()

            

