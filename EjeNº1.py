import random
# iniciamos con una lista vacia

matriz = []
for i in range(5):
    fila = []
    for j in range(5):
        fila.append(random.randint(0, 9))
    matriz.append(fila)

# imprime la matriz que acabamos de crear
for fila in matriz:
    print(fila)

col_suma = []

for i in range(5):
    col_sum = 0
    for j in range(5):
        col_sum += matriz[i][j]
    col_suma.append(col_sum)

print(col_suma)

# imprime por consola el munero mayor dentro de la lista
print(max(col_suma))

fila_suma = [sum(fila) for fila in matriz]
print(fila_suma)

# imprime por consola el numero menor dentro de la lista
print(min(fila_suma))