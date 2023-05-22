import random

# creamos una funcion para crear una matriz
def matriz_1():
    matriz = []
    for _ in range(3):
        fila = []
        for _ in range(3):
            fila.append(random.randint(1, 9))
        matriz.append(fila)
    return matriz

def calcular_determinante(matriz):
    a = matriz[0][0]
    b = matriz[0][1]
    c = matriz[0][2]
    d = matriz[1][0]
    e = matriz[1][1]
    f = matriz[1][2]
    g = matriz[2][0]
    h = matriz[2][1]
    i = matriz[2][2]

    determinate = (a * e * i) + (b * f * g) + (c * d * h) - (c * e * g) - (b * d * i) - (a * f * h)
    return determinate

# Generar una matriz
mat = matriz_1()

# imprimir la matriz
print("matriz 1:")
for fila in mat:
    print(fila)

# Calculamos el determinante
determinante = calcular_determinante(mat)
print("El determinante es:", determinante)