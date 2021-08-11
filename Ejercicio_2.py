# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 19:30:51 2021

@author: Andres Marulanda
"""

""" Elabore un programa en Python que genere un entero entre 15 y 30;
luego, construya un objeto de la clase vector tal como la definida en el curso, 
con tamaño el número generado inicialmente. 
Luego, llene el vector con números enteros entre 1 y 99 generados aleatoriamente. Después, 
haga una copia del vector generado. 
Con el vector copiado elabore un programa en Python que intercambie los datos así: 
El primero con el penúltimo, el segundo con el último, el tercero con el trasantepenúltimo, 
el cuarto con el antepenúltimo y así sucesivamente.
Cada dato se debe intercambiar solo una vez.
Para obtener el resultado de su evaluación escriba su programa en el método solucion(). 
Dicho método debe retornar respectivamente el vector construido inicialmente y el vector modificado con base en el enunciado.
En otras palabras, la última instrucción del método solución, sería:
return nombreDelVectorCreado, nombreDelVectorModificado               
Si el vector creado se llamó vec2 y el vector modificado se llamó vec2mod, sería:
return vec2, vec2mod"""

from vector import vector
import random

def intercambiar_pos(vector):
    i = 1
    j = vector.V[0]
    while i <= vector.V[0] // 2:
        aux = vector.V[i]
        vector.V[i] = vector.V[j]
        vector.V[j] = aux
        i += 1
        j -= 1
    return vector        
        
        
def solucion():
    
    n = random.randint(15,30)
    
    vec2 = vector(n)
    vec2A = vector(n)
    vec2mod = vector(n)
    
    vec2.V[0] = n
    for i in range(1, vec2.V[0]+1):
        vec2.V[i] = random.randint(1,99)
        
    vec2A.V[0] = n
    for i in range(1, vec2A.V[0]+1):
        vec2A.V[i] = vec2.V[i]
        
        
    vec2mod = intercambiar_pos(vec2A)
    
    return vec2, vec2mod

def imprimeVector(vector, mensaje="vector sin nombre: \t"):
    print("\n", mensaje, end="        ")
    for i in range(1, vector.V[0] + 1):
        print(vector.V[i], end=", ")
        if i % 30 == 0:
            print("\n                      ", end="")
    print()
    
v, v1 = solucion()
imprimeVector(v, "Vector original: ")
imprimeVector(v1, "Vector modificado: ")

   
    