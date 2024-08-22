class Dispositivos():
    def __init__(self, dispositivo, modelo, ram, almacenamiento, tamñoPantalla, precioCompra):
        self.marca="PHR"
        self.dispositivo=dispositivo
        self.modelo=modelo
        self.ram=ram
        self.almacenamiento=almacenamiento
        self.tamñoPantalla=tamñoPantalla
        self.precioCompra=precioCompra
        self.precioVenta=0

    #Calcula el precio de venta utilizando el precio de compra
    def  calcularPrecioVenta(self):
        self.precioVenta=self.precioCompra*1.7

    @staticmethod
    #almacena los datos ingresados por el usuario
    def RecibirDatos():
        #Se asegura que el usuario ingrese un dato valido
        while True:
            dispositivo = input("Ingrese el dispositivo: a-Celular, b-Tablet, c-Portatiles ")
            if dispositivo.upper()=='A' or  dispositivo.upper()=='B'or  dispositivo.upper()=='C':
                #el if almacena el nombre completo del dispositivo que el usuario ha seleccionado
                if dispositivo.upper()=='A':
                    dispositivo="Celular"
                elif  dispositivo.upper()=='B':
                    dispositivo="Tablet"

                else:
                    dispositivo="Portatiles"
                #Se rompe el ciclo  while cuando se valida que el dato es una de las tres opciones y continua con las siguientes entradas de datos

                break
            else:
                print("Escribe una opción valida") #Imprime este print cuando el usuario ingresa  un dato invalido

        modelo = input("Ingrese el modelo del dispositivo: ")
        ram = int(input("Ingrese la cantidad de RAM del dispositivo: "))
        almacenamiento = int(input("Ingrese el almacenamiento del dispositivo: "))
        tamñoPantalla = int(input("Ingrese el tamaño de la pantalla del dispositivo: "))
        precioCompra = int(input("Ingrese el precio de compra del dispositivo: $"))
        dispositivo_x= Dispositivos( dispositivo, modelo, ram, almacenamiento, tamñoPantalla, precioCompra)
        return dispositivo_x
    def imprimirDatos(self):
        print("Dispositivo: ",self.dispositivo)
        print("Marca: ",self.marca)
        print("Modelo: ", self.modelo)
        print("RAM: ", self.ram, "GB")
        print("Almacenamiento:  ", self.almacenamiento,"GB")
        print("Tamaño de pantalla: ",self.tamñoPantalla," pulgadas")
        print("Precio de compra: $",self.precioCompra)
        print("Precio de venta: $",self.precioVenta)

dispositivo1 = Dispositivos.RecibirDatos()
dispositivo1.calcularPrecioVenta() 
dispositivo1.imprimirDatos()

