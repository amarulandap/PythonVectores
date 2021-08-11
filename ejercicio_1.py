# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 18:02:07 2021

@author: Andres Marulanda
"""

"""Elabore un programa en Python que genere un entero entre 15 y 30; luego, 
   construya un objeto de la clase vector tal como la definida en el curso con tamaño el número generado. 
   Luego, llene el vector con números enteros entre 1 y 29 generados aleatoriamente. Haga una copia del vector generado. 
   Con el vector copiado, elabore un programa en Python que intercambie el mayor dato con el menor dato.  
   Si el menor dato aparece más de una vez intercambie la primera ocurrencia, igualmente, si el mayor dato aparece más de una vez 
   intercambie la última ocurrencia.  
   Para obtener el resultado de su evaluación escriba su programa en el método solucion(). 
   Dicho método debe retornar respectivamente el vector construido inicialmente y el vector modificado con base en el enunciado.
   En otras palabras, la última instrucción del método solución, sería:

       return nombreDelVectorCreado, nombreDelVectorModificado               

    Si el vector creado se llamó vec1 y el vector modificado se llamó vec1mod, sería:

        return vec1, vec1mod"""
    

from vector import vector
import random
#import math

def mayor(vector):
    mayor = 1
    for i in range(2, vector.V[0]+1):
        if vector.V[i] >= vector.V[mayor]:
            mayor = i
            
    return mayor
            
def menor(vector):
    menor = 1
    for i in range(2, vector.V[0]+1):
        if vector.V[i] < vector.V[menor]:
            menor = i
            
    return menor

def intercambiar(vector,a,b):
    aux = vector.V[a]
    vector.V[a] = vector.V[b]
    vector.V[b] = aux
    
    return vector
    
def imprimeVector(vector, mensaje="vector sin nombre: \t"):
    print("\n", mensaje, end="        ")
    for i in range(1, vector.V[0] + 1):
        print(vector.V[i], end=", ")
        if i % 30 == 0:
            print("\n                      ", end="")
    print()

def solucion():
    
    n = random.randint(15,30)
    
    vec1 = vector(n)
    vec2 = vector(n)
    vec1mod = vector(n)
    
    vec1.V[0] = n
    for i in range(1, vec1.V[0]):
        vec1.V[i] = random.randint(1,29)
    
    vec2.V[0] = n
    for i in range(1, vec2.V[0] + 1):    
        vec2.V[i] = vec1.V[i]
    
    
    may = mayor(vec1)
    print(may)
    men = menor(vec1)
    print(men)
    
    vec1mod = intercambiar(vec2,may,men)
    
    return vec1, vec1mod
    
v, v1 = solucion()
imprimeVector(v, "Vector creado: ")
imprimeVector(v1, "Vector modificado")

    
        
    
            
        