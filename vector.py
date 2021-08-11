# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 08:16:23 2021

@author: Andres Marulanda
"""

"""CLASE VECTOR"""

import random

class vector:
    
    def __init__(self,n):
        self.n = n
        self.V = [0]*(n+1)
        
    def construye_vector (self, m, r1, r2=None):
        self.V[0] = m
        for i in range (1, m+1):
            if r2 == None:
                self.V[i] = random.randit(1, r1)
            else:
                self.V[i] = random.randit(r1, r2)
            
    def celdas_usadas (self):
        return self.V[0]

    def tamaño_vector (self):
        return self.n

    def vacio (self):
        if self.V[0] == 0:
            return True
        else:
            return False
        
    def lleno (self):
        if self.V[0] == self.n:
            return True
        else:
            return False
        
    def imprime_vector(self, mensaje="Vector sin nombre"):
        print("\n", mensaje, end="")
        for i in range (1, self.V[0]+1):
            print (self.V[i], end="")
            
    def agregar_dato(self,d):
        if self.lleno():
            return
        self.V[0] = self.V[0]+1
        self.V[self.V[0]] = d
        
    def intercambiar(self,i,j):
        aux = self.V[i]
        self.V[i] = self.V[j]
        self.V[j] = aux
        
    def sumar_datos(self):
        suma = 0
        for i in range(1,self.V[0]+1):
            suma = suma + self.V[i]
            
        return suma()
    
    def ordenar_asc(self):
        for i in range (1, self.V[0]):
            k = i
            for j in range (i+1, self.V[0]+1):
                if self.V[j] < self.V[k]:
                   k = j
            self.intercambiar(i,k)
             
    def ordenar_desc(self):
        for i in range(1, self.V[0]):
            k = i
            for j in range(i+1, self.V[0]+1):
                if self.V[j] > self.V[k]:
                    k = j
                    
            self.intercambiar(i,k)
                
    def mayor(self):
        mayor = 1
        for i in range(2, self.V[0]+1):
            if self.V[i] > self.V[mayor]:
                mayor = i
                
        return mayor
    
    def menor(self):
        menor = 1
        for i in range(2, self.V[0]+1):
            if self.V[menor] > self.V[i]:
                menor = i
        
        return menor
             
    def buscar_dato(self,d):
        i = 1
        while i <= self.V[0] and self.V[i] != d:
            i +=1
            
        if i <= self.V[0]:
            return i
        else:
            return -1

#Vectores ordenados ascendentemente        
    def buscar_insertar(self,d):
        i = 1
        while i <= self.V[0] and d < self.V[i]:
            i = i+1
        return i
    
    def insertar(self,d,i=0):
        if self.lleno():
            print("Vector lleno")
            return
        if i == 0:
            i = self.buscar_insertar(d)
            for j in range(self.V[0]+1, i-1, -1):
                self.V[j] = self.V[j-1]
            self.V[i] = d
            self.V[0] = self.V[0]+1
            
    def borrar_dato_en_posicion(self,i):
        if i > 0 and i <= self.V[0]:
            for j in range(i, self.V[0]+1):
                self.V[j] = self.V[j+1]
            self.V[0] = self.V[0]-1
        else:
            print("posición invalida")

    def borrar_dato(self,d):
        i = self.buscar_dato(d)
        
        if i != -1:
            self.borrar_dato_en_posicion(i)
            

            
            
                
        
                
        
        
    
        
        

        
    
