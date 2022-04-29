#Ejercicio 5

class Alumno:
    def __init__(self, nombre, numero_de_registro) -> None:
        self.name=nombre
        self.id=numero_de_registro
        pass

    def display(self):
        print(f"Su nombre es: {self.name}")
        print(f"Codigo de alumno: {self.id}")
        pass

    def setAge(self):
        int(input("Ingrese la edad del estudiante: "))
        pass

    def setNota(self):
        lista=[]
        n=int(input("Cantidad de notas: "))
        for i in range(n):
            dato=int(input(f"Ingrese nota {i+1}: "))
            lista.append(dato)
        print(f"Lista de notas: {lista}")
        pass

alumno_1=Alumno("Raul Fernando","20214009C")
alumno_1.display()
alumno_1.setAge()
alumno_1.setNota()

##############################################################################