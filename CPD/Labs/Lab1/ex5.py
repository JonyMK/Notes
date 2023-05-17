import timeit
import numpy as np

rnd = np.random
# n define as dimensões da matriz
n = 500
matrix1 = rnd.uniform(0, 499, size=(n, n))
matrix2 = rnd.uniform(0, 499, size=(n, n))
resultMatrix = np.zeros((n, n))

starttime = timeit.default_timer()
resultMatrix = np.matmul(matrix1, matrix2)
print(f"Tempo : {timeit.default_timer() - starttime}")
print(f"Primeiros elementos do vetor resultado: {resultMatrix[0:5]}")
# for i in range(len(matriz)):  # número de linhas da matriz
#    temp = 0
#    for j in range(len(vetor)):  # número de elementos no vetor
#        temp += matriz[i, j] * vetor[i]
#    resultado[i] = temp
# print(f"Tempo 2: {timeit.default_timer() - starttime}")
# print(f"Primeiros elementos do vetor resultado: {resultado[0:5]}")