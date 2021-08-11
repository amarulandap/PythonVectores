from vector import vector
import random
import math

"""Esta funcion invierte un número, osea, 3456 invertido sería 6543"""

def invierteNumero(n): 
    nunu = 0
    m = n
    while m > 0:
        digito = m % 10
        nunu = nunu * 10 + digito
        m = m // 10
    return nunu
    
"""Esta función retorna el primer digito de el número x"""
def comienzaCon(x):
    pd = x
    while pd > 9:
        pd = pd // 10
    return pd

"""Funcion que contiene la solución al problema que será calificado"""
def solucion():
    """Se genera aleatoriamente un número entero entre 15 y 30"""
    n = random.randint(15,30)
    """A 's' se le asigna un 0, esta variable va ser donde se almacena la suma como esta descrito en el enunciado"""
    s = 0 
    """Se crea un objeto vector que tiene como tamaño el valor n"""
    vec4 = vector(n)
    """Usamos un ciclo para llenar el vector con número del 1 al 99999"""
    for i in range(1, n + 1):
        """Se genera aleatoriamente un número entero entre 1 y 99999"""
        vec4.V[i] = random.randint(1,99999)
        """Se actualiza el valor de la primera posición del vector indicando cuantas posiciones
        son usadas (En este caso es igual al tamaño del vector)"""
        vec4.V[0] = n
    """Usamos un ciclo para recorrer el vector"""
    for i in range(1, vec4.V[0] + 1):
        """En la variable 'nunu' sea almacena el numero invertido de la posición i del vector"""
        nunu = invierteNumero(vec4.V[i])
        """Se pregunta si al invertir el numero sige siendo el mismo(capicua) o si el numero compienza por un dígito par"""
        if vec4.V[i] == nunu or comienzaCon(vec4.V[i]) % 2 == 0:
            """Se realiza la suma de la suma acumulada
            con el dato en la posición i"""
            s += vec4.V[i]
    """Se retornan los objetos requeridos para efectuar la
    calificación de la solución"""
    return vec4, s, n

def imprimeVector(vector, mensaje="vector sin nombre: \t"):
    print("\n", mensaje, end="        ")
    for i in range(1, vector.V[0] + 1):
        print(vector.V[i], end=", ")
        if i % 30 == 0:
            print("\n                      ", end="")
    print()


v, suma, datos = solucion()
imprimeVector(v,"Vector creado: ")

print("\nVector de: ",datos, "datos")
print("La suma de los capicua y los que inician por par es: ",suma)




