from vector import vector
import random
import math


#INICIE COMPLETANDO LA FUNCIÓN SOLUCIÓN
def solucion():
    
    a = random.randint(15,30)
    v = vector(a)
    
    for i in range(1, a+1):
        
        """Completa el llenado de cada casilla, el número debe ser entero y 
        aleatorio entre 1 y 9999.
        Sugerencia, usa random.randint"""
        v.V[i] = random.randint(1,9999)
        
        """Como el número es aleatorio entre 1 y 9999, habrá UNA (1) nueva casilla
        ocupada, por lo tanto, se debe ir alterando en UNO (1) la posición 0 del vector
        cada vez que se llene una casilla"""
        v.V[0] += 1

    
    """Creamos una variable s, donde guardaremos la suma de los números 
    que son primos o que comienzan por dígito impar"""
    s = 0
    
    """Recorramos todas las casilla del vector (Desde la posición 1)
    Complete los límites de la función range:"""
    for i in range(1, v.V[0]+1):
        
        """Si el número guardado en la posición i es primo o comienza por dígito impar
        SÚMELO a la variable s
        Complete el siguiente condicional, para que sume solo los números primos
        o números que empiecen por dígito impar:"""
        if es_primo(v.V[i]) or comienza_digito_impar(v.V[i]):
            s += v.V[i]
            
    return v, s

def es_primo(n):
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    i = 3
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i +=2
        
    return True
    

def comienza_digito_impar(n):
    
    """Complete la siguiente línea, que sirve para guardar el primer dígito de n en una variable llamada d"""
    d = str(int(n))[0] 
    
    """d guarda un valor de tipo texto, completa la siguiente línea para cambiar el tipo de la variable d a entero"""
    d = int(str(d))
    
    if d % 2 == 1:
        return True
    return False


def imprimeVector(vector, mensaje="vector sin nombre: \t"):
    print("\n", mensaje, end="        ")
    for i in range(1, vector.V[0] + 1):
        print(vector.V[i], end=", ")
        if i % 30 == 0:
            print("\n                      ", end="")
    print()
    
"""Las siguientes líneas le permitirán probar su solución al presionar el botón de ejecutar"""
a, suma = solucion()
imprimeVector(a, 'Original')
print("Suma: ", suma)