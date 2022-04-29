
def sumar(a,b):
    try:
        print("La suma es:",float(a)+float(b))
    except:
        if str(a).isnumeric!=False or str(b).isnumeric!=False: 
            print("Ingrese valores numericos para la suma")

def resta(a,b):
    try:
        print("La resta es:",float(a)-float(b))
    except:
        if str(a).isnumeric!=False or str(b).isnumeric!=False: 
            print('Ingrese valores numericos para la resta')

def producto(a,b):
    try:
        print("El producto es:",float(a)*float(b))
    except:
        if str(a).isnumeric!=False or str(b).isnumeric!=False: 
            print("Ingrese valores numericos para el producto")

def division(a,b):
    try:
        print("La division es:",float(a)/float(b))
    except:
        
        if b=="0" or b=="" or b=="00":
            print('Division entre 0')
            
        elif str(a).isnumeric!=False or str(b).isnumeric!=False: 
            print("Ingrese valores numericos para la division")
        
        


