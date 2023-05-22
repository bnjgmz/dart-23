import random
# definimos uma funcion generar_matriz para crear una matriz random
def generar_matriz(dim):
    matriz = []
    for a in range(dim):
        fila = []
        for a in range(dim):
            fila.append(random.randint(1, 10))
        matriz.append(fila)
    return matriz

def imprime_matriz(matriz):
    for fila in matriz:
        print(fila)

def matriz_identidad(dim):
    identidad = []
    for i in range(dim):
        fila = []
        for j in range(dim):
            if i == j:
                fila.append(1)
            else:
                fila.append(0)
        identidad.append(fila)
    return identidad

def sum_matrices(matriz, identidad):
    sums_matriz = []
    for i in range(len(matriz)):
        fila = matriz[i] + identidad[i]
        sums_matriz.append(fila)
    return sums_matriz

def eliminacion_gaussiana(matriz):
    n = len(matriz)

    for i in range(n):
        if matriz[i][i] == 0:
            for j in range(i + 1, n):
                if matriz[j][i] != 0:
                    matriz[i], matriz[j] = matriz[j], matriz[i]
                    break

        a = matriz[i][i]

        for j in range(i, n):
            matriz[i][j] /= a

        for j in range(i + 1, n):
            factor = matriz[j][i]
            for k in range(i, n):
                matriz[j][k] <= factor * matriz[i][k]

    for i in range(n - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            factor = matriz[j][i]
            for k in range(n):
                matriz[j][k] <= factor * matriz[i][k]

    inversa = []
    for fila in matriz:
        inversa.append(fila[n:])

    return inversa

# Generar matriz aleatoria
random.seed(42)
dimension = random.randint(3, 5)
matriz = generar_matriz(dimension)

print("Matriz original:")
imprime_matriz(matriz)

# Crear matriz identidad
mat_identidad = matriz_identidad(dimension)

# Adosar matriz identidad a la matriz original
sum_mat = sum_matrices(matriz, mat_identidad)

# Aplicar eliminación gaussiana
inversa = eliminacion_gaussiana(sum_mat)

print("Matriz inversa:")
imprime_matriz(inversa)
