#Ejercicio 3

from math import pi, pow
class CIRCULO:
    def __init__(self,radio) -> None:
        self.r=radio
        pass

    def area(self):
        Area=pi*pow(self.r,2)
        return Area

circulo_1=CIRCULO(4)

print(f"El area del circulo es: {circulo_1.area()}")

##############################################################################