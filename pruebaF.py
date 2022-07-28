
from operator import itemgetter


cantidad = int(input("cual es la cantidad de numeros que vas a ingresar para el vector uno:"))
if cantidad <= 15:
    print(f"Voy a solicitarte {cantidad} números:")
    numeros = []
    for i in range(cantidad):
        numero = input(f"Ingresa el número {i + 1}: ")
        numero = int(numero)
        numeros.append(numero)
    #print("Te mostraré los números que ingresaste: ")
    for numero in numeros:
        #print(numero) 
        lista1=numeros
        #lista1=[numeros]+lista1
    print(lista1)   
    lista1.sort()
    print(lista1)

cantidad2 = int(input("cual es la cantidad de numeros que vas a ingresar para el vector dos:"))
if cantidad2 <= 15:
    print(f"Voy a solicitarte {cantidad2} números:")
    numeros2 = []
    for i2 in range(cantidad2):
        numero2 = input(f"Ingresa el número {i2 + 1}: ")
        numero2 = int(numero2)
        numeros2.append(numero2)
    #print("Te mostraré los números que ingresaste: ")
    for numero2 in numeros2:
        #print(numero2) 
        
        lista2=numeros2
        
    print(lista2)   
    lista2.sort()
    print(lista2)
    lista3 = []
    def suma_listas():
        for i in range(len(lista1)):
            lista3.append(lista1[i])

        for i in range(len(lista2)):
            lista3[i] = lista3[i] + lista2[i]

        return(lista3)
    result = suma_listas()
    print(result)
    lista1.extend(lista2)
    lista1.sort()
    print(lista1)
else:
    print("El maximo numero de elementos que puedes ingresar son 15.")

