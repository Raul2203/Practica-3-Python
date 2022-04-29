#Ejercicio 4

l=float(input("Ingrese el largo del rectangulo: "))
w=float(input("Ingrese el ancho del rectangulo: "))

class RECTANGULO:
    def __init__(self,largo,ancho) -> None:
        self.large=largo
        self.wide= ancho
        pass

    def area(self):
        Area=self.large*self.wide
        return Area

rectangulo1=RECTANGULO(l,w)

print(f"El area del rectangulo es: {rectangulo1.area()}")

##############################################################################