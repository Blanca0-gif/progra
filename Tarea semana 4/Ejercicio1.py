class mascota():
    def __init__(self,nombre,edad,color,sexo,raza,peso,responsable):
        self.nombre = nombre
        self.edad=edad
        self.color=color
        self.sexo=sexo
        self.raza=raza
        self.peso=peso
        self.responsable=responsable
        self.tamaño=''
        self.estado='NO ATENDIDO'

    def RegistrarMascota(self):
        self.estado='Atendido'
        return self.estado

    def RecibirDatos():
        nombre=input("Nombre del paciente: ")
        edad=int(input("Edad: "))
        color=input("Color: ")
        sexo=input("Sexo: ")
        raza=input("Raza: ")
        peso=float(input("Peso: ")) 
        responsable=input("Nombre del responsable: ")
        print("*****************************")
        print("Datos del paciente: ")
        Mascota1 = mascota(nombre, edad, color, sexo, raza, peso, responsable)
        Mascota1.definirtamaño()
        return Mascota1

    def definirtamaño(self):
        if self.peso >= 10:
            self.tamaño = "Perro grande"

        else:
            self.tamaño="perro pequeño"

    def mostrarDatos(mascota):
        print('Nombre del paciente: ',mascota.nombre)
        print('Edad: ',mascota.edad)
        print('Raza: ',mascota.raza)
        print('Color: ',mascota.color)
        print('Sexo: ',mascota.sexo)
        print('Peso: ',mascota.peso)
        print('Tamaño: ',mascota.tamaño)
        print('Estado: ', mascota.estado)
        print('Responsable: ',mascota.responsable)




nueva_mascota = mascota.RecibirDatos()
estado = nueva_mascota.RegistrarMascota()
nueva_mascota.mostrarDatos()



    
        