import threading
import time

# Explique a diferença no desempenho entre o processamento sequencial e multi-threading.
# Relacione com a instrução sleep.
#   R : Sendo que existem duas ligações, cada ligação têm um sleep de 2 segundos, a sequencial demora 4 segundos + o tempo
#   de processamento. Na multi-threading, ambas as ligações começam paralelamente, ou seja, os 2 segundos de sleep são
#   ao mesmo tempo e não em ordem, desta maneira demora só 2 segundos + o tempo de processamento.
#
# Altere o número de ligações para 20 e analise explique os resultados obtidos
#   R : Na sequencial passa dos 4 segundos para 40 segundos, sendo que mais uma vez para cada ligação têm de esperar o sleep
#   um a um. Na multi-threading continou 2 segundos, devido mais uma vez ao facto de não ser sequencial mas sim todas as ligações
#   realizadas ao mesmo tempo, desta maneira os dois segundos de tempo real é igual para as 20 ligações.

def conecta(): # simula uma ligação remota a um servidor
    print("\tligado")
    time.sleep(2)
    print("\tdesligado")


if __name__ == '__main__':
    numero_de_ligacoes = 20
    inicio = time.time()
    print("Início do processamento sequencial")
    for i in range(numero_de_ligacoes):
        print(f'{i+1}ª ligação')
        conecta()
    fim = time.time()
    print(f'Tempo gasto para realizar {numero_de_ligacoes}ª ligações sequenciais: {fim-inicio}s')

    print("Início do processamento multi-threading")
    # multi-threaded
    threads = []
    inicio = time.time()
    for i in range(numero_de_ligacoes):
        t = threading.Thread(target=conecta)
        threads.append(t)
        t.start()
    for i in range(numero_de_ligacoes):
        threads[i].join()
    fim = time.time()
    print(f'Tempo gasto para realizar {numero_de_ligacoes} ligações multi-threading: {fim - inicio}s')