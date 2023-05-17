import multiprocessing
import random
from timeit import default_timer as timer

# 4.1 diga o faz cada uma das seguintes instruções:
#       pool = multiprocessing.Pool(processes=numero_CPUs) : Cria um grupo (piscina) de processos, sendo o número de processos
#       criados igual ao números de processadores presentes na máquina a correr o programa.
#       pool.map(createandsort, dimensoes) : Gere os processos criados de maneira a indicar qual a função
#       e os dados a serem utilizados. O map também vai permitir a forma mais eficiente de repartir os dados para
#       demorar o menor tempo possível a acabar o pedido.
# 4.2 Observe o output do programa e realize uma análise crítica dos resultados observados. A
#     análise deverá ter em atenção as dimensões dos vetores, a quantidade de vetores gerados e os
#     tempos observados para a ordenação sequencial e a ordenação utilizando
#      multiprocessamento.
#       R: A ordenação sequencial é mais rápida de início devido ao tamanho do vetor ser menor, desta maneira é mais rápida
#       que a ordenação paralela pois a vantagem de ser paralela é anulada por necessitar de perder tempo a gerir
#       processos. No entanto à medida que o tamanho do vetor aumenta, a paralela começa a ser mais rápida que a sequencial,
#       sendo isto vísivel após 1000000 elementos.

def criar_e_ordenar(n):
    rand = random.Random(50)
    x = [rand.randint(0, 100) for _ in range(n)]
    x.sort()
    return x

if __name__ == "__main__":
    numero_CPUs = multiprocessing.cpu_count()
    print(f'Número de CPUs: {numero_CPUs}')
    vetores_a_gerar = [2, 4, 6, 15]
    dimensoes_dos_vetores = [10 ** 2, 10 ** 3, 10 ** 4, 10 ** 6]
    for numero_de_elementos in dimensoes_dos_vetores:
        print(f'Número elementos do vetor: {numero_de_elementos}')
        for qtd_vetores_a_gerar in vetores_a_gerar:
            print(f'\tQuantidade de vetores a gerar e ordenar: {qtd_vetores_a_gerar}')
            dimensoes = []
            for i in range(qtd_vetores_a_gerar):
                dimensoes.append(numero_de_elementos)
                # dimensoes1 = [d for i in range(qtd_vetores_a_gerar)]
                # print(dimensoes ,dimensoes1)
                # Aplicar a função sequencialmente
                resultado = []
                inicio = timer()
                for d in dimensoes:
                    resultado.append(criar_e_ordenar(d))
                # resultado = [createandsort(d) for d in dimensoes]
                fim = timer()
                print("\t\tTempo para ordenação sequencial: ", fim - inicio)
                # print(resultado)
                # print([createandsort(d) for d in dimensoes])

                # Utilizando multiprocessamento
                pool = multiprocessing.Pool(processes=numero_CPUs)  # Usa o número de cores físicos da sua máquina
                inicio = timer()
                resultado = pool.map(criar_e_ordenar, dimensoes)
                fim = timer()
                print("\t\tTempo para ordenação paralela: ", fim - inicio)
