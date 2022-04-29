#Ejercicio 1

def string_final(frase_1):
    frase=str(frase_1)
    inversa=""
    for i in frase[::-1]:
        inversa=inversa+i
        if (i==" "):
            return print(len(inversa)-1)

string_final("Tengo que terminar esto antes del viernes porque estoy ocupado")

##############################################################################