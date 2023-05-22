import numpy as np

def verificar_propiedad(matriz):
    # convierte la matriz en un array de numpy
    matriz = np.array(matriz)

    # Calcula la matriz inversa de la matriz
    matriz_inversa = np.linalg.inv(matriz)

    # Calcula el producto de la matriz y su inversa
    producto = np.dot(matriz, matriz_inversa)

    # Crea la matriz identidad de la misma forma que la matriz original
    matriz_identidad = np.eye(matriz.shape[0])

    # Compara el producto con la matriz identidad
    if np.array_equal(producto, matriz_identidad):
        return print("La propiedad A * A^-1 = I se cumple.")
    else:
        return print("La propiedad A * A^-1 = I no se cumple.")
    

A = [[1, 2], [3, 4]]
es_id = verificar_propiedad(A)
print(es_id)