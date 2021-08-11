# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 06:54:08 2021

@author: andre
"""

vector = [3, 8, 3, 6]

#añande un elemento al final del vector
vector.append(55)

#elimina ttodos los elementos del vector
#print(vector.clear())

#crea una copia de todo el vector
copia = vector.copy()
#se diferencia de
copia2 = copia
copia2.append(44)
#porque la asignación que hacemos en la instrucción dos líneas antes de esta
#lo que hace, es copiar la referencia, por lo tanto cualquier cosa que yo+
#cambie en copia2 también ocurrirá en copia

#retorna el número de veces  el 4 en el vector
print(vector.count(4))
print(vector.count(3))

#Agrega elementos al final del arreglo
vector.extend([4, 4, 4, 4, 4, 5])

#retorna la posición de la primera ocurrencia del 4 en el vector
print(vector.index(4))

#retorna la posición de la primera ocurrencia del 4 en el vector
print(vector.index(4))

#inserta el elemento 777 en la psición 3
vector.insert(3, 777)

#elimina elementos de la posición 0
vector.pop(0)

#elimina el prmer elemento con el valor 4
vector.remove(4)

#reversa el vector, o sea que lo pone al revés
vector.reverse()

#ordena el vecor de menor a mayor
vector.sort()

#ordena el vecor de mayor a menor
vector.sort(reverse=True)









