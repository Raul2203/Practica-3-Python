#Ejercicio 6

lista_de_datos=str(input('Ingrese todas las notas: '))
listado=[]
aux=""
try:
    for i in lista_de_datos:
        if i!=",":
            aux=aux+i
        if i==lista_de_datos[len(lista_de_datos)-1]:
            listado.append(int(aux))
        if i==",":
            listado.append(int(aux))
            aux=""    
    print(listado)

except:
    for i in lista_de_datos:
        if i.isalpha():
            print("Error en los datos")
            break

##############################################################################
