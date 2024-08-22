class Estudiantes:
    def __init__(self, nombre, edad, grado, notas):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.notas = notas

    def obtenerPromedio(self):
        if len(self.notas) > 0:
            return sum(self.notas) / len(self.notas)
        return 0
    
    def imprimir_info(self):
        print("*********************************+")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Grado: {self.grado}")
        print(f"Notas: {self.notas}")
        print(f"Promedio: {self.obtenerPromedio():.2f}")

    @staticmethod
    def obtenerDatos():
        nombre = input("Ingrese el nombre del estudiante: ")
        edad = int(input("Ingrese la edad del estudiante: "))
        grado = input("Ingrese el grado del estudiante: ")
        notas = []

        while True:
            nota = input("Ingrese una nota del estudiante (escriba 'salir' para terminar): ")
            if nota.lower() == "salir":
                break
            elif nota.replace('.', '', 1).isdigit():  
                notas.append(float(nota))
            else:
                print("Nota inválida, por favor ingrese un valor numérico.")

        return Estudiantes(nombre, edad, grado, notas)


estudiante1 = Estudiantes.obtenerDatos()


estudiante1.imprimir_info()

