import timeit
import numpy as np

rnd = np.random
# n define as dimensões dos vetores e da matriz
n = 5000
vetor = rnd.uniform(0, 1000, size=n)
matriz = rnd.uniform(0, 1000, size=(n, n))
resultado = np.zeros(n)

## Perguntas
# 3.1 - Na primeira implementação é necessário ler primeiro o número na lista e depois escrever o novo número na mesma lista.
#       Enquanto que na segunda implementação só é necessário escrever na lista após ter guardado o valor na variável temp,
#       desta maneira a segunda implementação é mais rápida que a primeira
# 3.2 - Mesmo com o n tendo valores diferentes é constante que a segunda implementação é mais rápida, a volta dos 30%.

# primeira implementação
starttime = timeit.default_timer()
for i in range(len(matriz)):  # número de linhas da matriz
    for j in range(len(vetor)):  # número de elementos no vetor
        resultado[i] += matriz[i, j] * vetor[i]
print(f"Tempo 1: {timeit.default_timer() - starttime}")
print(f"Primeiros elementos do vetor resultado: {resultado[0:5]}")
# segunda implementação
starttime = timeit.default_timer()
for i in range(len(matriz)):  # número de linhas da matriz
    temp = 0
    for j in range(len(vetor)):  # número de elementos no vetor
        temp += matriz[i, j] * vetor[i]
    resultado[i] = temp
print(f"Tempo 2: {timeit.default_timer() - starttime}")
print(f"Primeiros elementos do vetor resultado: {resultado[0:5]}")
