class Libreria():
    def __init__(self,articulo,precioCompra,tipo,marca):
        self.articulo =articulo 
        self.precioCompra=precioCompra
        self.tipo=tipo
        self.marca=marca
        self.precioVenta=""

    @staticmethod
    def RecibirDatos():
         print(" Registro de datos")
         print("*********************")
         #Valida que ingrese una opción valida
         while True:
            articulo=input("Nombre del articulo: Cuaderno(C) Lapices(L) ")
            if articulo.upper()=='C' or  articulo.upper()=='L':
                if articulo.upper()=='C':
                    articulo="Cuaderno"
                else:
                    articulo="Lapices"

                break
            else:
                print("Escribe una opción valida")
         precioCompra=float(input("Precio de compra:  "))

         #Le asigna el valor a la variable tipo según la opción que se ingreso anteriormente
         if articulo.upper() =='CUADERNO':
            tipo=input("Tipo de cuaderno: 1)-50 hojas 2)-100 hojas ")
            if tipo=="1":
                tipo="50 hojas"
            else:
                tipo="100 hojas"
         else:
             tipo=input("Tipo de Lapices: 1)-Grafito 2)- colores ")
             if tipo=="1":
                tipo="Grafito"
             else:
                tipo="Colores"
        #Le asigna el valor a la variable marca según la opción que se almaceno en la variable articulo
         marca = "Hojitas" if articulo.upper() == "CUADERNO" else "Rayas"

         libreria1 = Libreria(articulo, precioCompra, tipo, marca)
         libreria1.PRECIOVENTA()
         return libreria1
    #Calcula el precio de venta 
    def PRECIOVENTA(self):
        self.precioVenta = self.precioCompra *1.30
    
    def MostrarDatos(self):
        print(" Impresión de datos")
        print("*********************")
        print('Articulo: ',self.articulo)
        print('Tipo: ',self.tipo) 
        print('Marca: ',self.marca)
        print('Precio de compra: ',self.precioCompra)
        print('Precio de venta: ',self.precioVenta)


Registro1 = Libreria.RecibirDatos()
Registro2 = Libreria.RecibirDatos()
Registro1.MostrarDatos()
Registro2. MostrarDatos()






        
        


         
          
