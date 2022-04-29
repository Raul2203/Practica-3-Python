import random

def num_ale():
    numero_al=random.randint(1,100)
    return numero_al

def input_num():
    a=True
    while (a):
        numero=int(input("Ingrese un numero del 1 al 100: "))
        if 1<=numero<=100:
            a=False
    return numero

def comparacion(numero_al, numero):
    if (numero==numero_al):
        print('Felicidades, ganaste')
    
    elif (numero!=numero_al):
        print(f'Perdiste, el numero era: {numero_al}') 
        print('Intentalo de nuevo ;v')
