import timeit
import numpy as np

rnd = np.random
measurements = [1000, 10000, 100000, 1000000, 10000000, 20000000]
bwRAM = []
for n in measurements:
    vetor = rnd.randint(1000, size=n)
    melhorTempo = 9999999  # Um valor muito grande
    for i in range(3):  # Efetua 3 medições de tempo e mostra a melhor
        print(f"Medição {i + 1} para {n} elementos...")
        starttime = timeit.default_timer()
        soma = 0.0
        for j in range(n):
            soma += vetor[j]
        tempo = timeit.default_timer() - starttime  # 1.1 - Cálculo do tempo de demora a somar os elementos do vetor
        print(f"\t {tempo} segundos")
        if tempo < melhorTempo:
            melhorTempo = tempo
        print(f"Melhor tempo da soma para {n} elementos: {melhorTempo} segundos")
    bwRAM.append(n * 4 / melhorTempo / (1024 * 1024))
    print(f"Largura de banda da RAM: {n * 4 / melhorTempo / (1024 * 1024):.2f} Mega Bytes por segundo")
    print(vetor.dtype)
# 1.2 - O 1024*1024 é utilizado para converter em Mega bytes, sendo o primeiro 1024 em kilo, e o segundo em mega.
# O número de tentativas é depois divido pelo melhor tempo e depois pela unidade de megabyte. 
# print(f"Largura de banda da RAM: {n * 4 / melhorTempo / (1024 * 1024):.2f} Mega Bytes por segundo")
for u in bwRAM:
    print(f"Largura de banda da RAM: {u:.2f} Mega Bytes por segundo")
print(f"Largura de banda média da RAM: {sum(bwRAM)/len(bwRAM):.2f} Mega Bytes por segundo")