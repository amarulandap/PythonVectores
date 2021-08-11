#Subprograma de inserción en un vector
def insertar(V, d, pos):
    for i in range(V[0], pos-1, -1):
        V[i+1] = V[i]
    
    V[pos] = d
    V[0] = V[0] + 1


#Subprograma para encontar la posición donde se debe insertar un valor en un vector ordenado
def buscarDondeInsertar(V, d):
    k = 1
    while k <= V[0] and V[k] < d:
        k = k + 1
    return k

#Subprograma para insertar un dato en un vector ordenado
def insertarOrdenado(Vector, dato):
    p = buscarDondeInsertar(Vector, dato)
    insertar(Vector, dato, p)


#Subprograma que retorna la posición del vector en la que está un dato o -1 si no lo encuentra
def buscarDato(V, d):
    i = 1
    while i <= V[0] and V[i] != d:
        i = i + 1
    if i <= V[0]:
        return i
    return -1

#Subprograma que elimina el dato de la posición de un vector y actualiza el nÃºmero de elementos
def borrar(V, i):
    for j in range(i, V[0]):
        V[j] = V[j + 1]
    V[0] = V[0] - 1 



    
#Vector de 20 posiciones, pero solo 10 ocupadas
vector = [10, 3,67,68,91,96,105,112,254,270,300, None, None, None, None, None, None, None, None, None, None]
insertarOrdenado(vector, 15)

p = buscarDato(vector, 96)
borrar(vector, p)