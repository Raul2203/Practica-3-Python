#Ejercicio 7

from math import factorial

filas=int(input("Ingrese cantidad de filas: "))

def triangulo_pascal(n):
    for i in range(n):
        for j in range(n-i+1):
            print(end=" ")
        
        for j in range(i+1):
            number=(factorial(i)//(factorial(j)*factorial(i-j)))
            print(number,end=" ")
        
        print()

triangulo_pascal(filas)

##############################################################################