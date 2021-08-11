# -*- coding: utf-8 -*-

def busbin(V, d):
    inicio = 1
    fin = V[0]
    
    while inicio <= fin:
        mitad = (inicio + fin ) // 2
        if V[mitad] == d:
            return mitad
        if d < V[mitad]:
            fin = mitad - 1
        else:
            inicio = mitad + 1
            
    return -1


vector = [4,1,4,8,16,17,None,None,None,None]

print("El 1 está en la posición", busbin(vector, 1))
print("El 4 está en la posición", busbin(vector, 4))
print("El 8 está en la posición", busbin(vector, 8))
print("El 16 está en la posición", busbin(vector, 16))
print("El 17 está en la posición", busbin(vector, 17))
print("El 15 está en la posición", busbin(vector, 15))
