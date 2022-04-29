#Ejercicio 2

def string_capitalize(palabra):
    auxiliar=""
    inicio_palabra=True             
    for j in palabra:
        if j==" ":
            auxiliar=auxiliar+j
            inicio_palabra=True
        else:
            if inicio_palabra:
                auxiliar=auxiliar+j.upper()
                inicio_palabra=False 
            else:
                auxiliar=auxiliar+j.lower()
    return print(auxiliar)

string_capitalize('tengo que terminar esto antes del viernes porque estoy ocupado')

##############################################################################