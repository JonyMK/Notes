import multiprocessing as mp
from timeit import default_timer as timer

import numpy as np

# 5.1 diga o faz cada uma das seguintes instruções:
#       lista = np.array_split(range(limite_superior), numero_CPUs) - Divide o array principal em vários arrays pelo o número de cores do CPU
#       processo = mp.Process(target=quadrado, args=(lista[i],)) - Cria um novo processo que vai utilizar a função "quadrado" com o argumento de parte da lista de número
#       processos.append(processo) - Adiciona um processo ao array de processos criados
#       processo.start() - Inicia a execução do processo
#       processo.join() - Espera pela finalização do processo
# 5.2 Observe o output do programa e verifique quantos processos foram criados no processamento:
#       Sem pool - 8 Processos
#       Com pool - 8 Processos
# 5.3 Realize uma crítica dos resultados observados quando alterar significativamente o número de
# valores a calcular. A análise deverá ter em atenção a quantidade de valores, o número de
# processos criados e o impacto na performance.
#       R : Com o limite original de 200 é possível logo verificar que a utilização da função map com pool é mais eficiente do que
#       a utilização do ciclo for, com um melhoramente aproximado de 20%. A medida que o valor aumenta (por exemplo limite
#       de 10000) a diferença fica cada vez maior (1.23s vs 0.53s), sendo sempre a utilização da função map mais rápida.

def quadrado(nums):
    pnome = mp.current_process().name
    for num in nums:
        resultado = num * num
        # print(f"Processo {pnome}; o quadrado do número {num} é {resultado}.")

if __name__ == '__main__':
    numero_CPUs = mp.cpu_count()
    processos = []
    limite_superior = 10000
    lista = np.array_split(range(limite_superior), numero_CPUs)
    print('Início do multiprocessamento')
    inicio = timer()
    for i in range(numero_CPUs):
        processo = mp.Process(target=quadrado, args=(lista[i],))
        processos.append(processo)
        processo.start()
    for processo in processos:
        processo.join()
    fim = timer()
    print(f"Multiprocessamento completo em {fim-inicio} segundos")
    print('Início do multiprocessamento com pool')
    pool = mp.Pool(processes=numero_CPUs)
    inicio = timer()
    resultado = pool.map(quadrado, lista)
    fim = timer()
    print(f"Multiprocessamento completo em {fim - inicio} segundos")