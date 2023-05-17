# threads Múltiplos

# 2.1 - Explique a estratégia seguida neste algoritmo
#       R : O programa cria duas threads para executar o algoritmo de contagem descrescente, sendo que uma thread fica com uma
#       metade e a outra thread fica com a metade restante. Mas mesmo com a criação das duas threads não existe paralelismo pois
#       a segunda thread só inicia o seu funcionamento após a primeira thread acabar a sua função atráves do uso do "join",
#       desta maneira não existem nenhum momento em que ambas estejam a trabalhar ao mesmo momento.
# 2.2 - Compara o resultado obtido, neste código, com o obtido no código do nível 1. Apresente uma explicação.
#       R : O resultado obtido é pior ao do nível 1 porque continua a ser programação sequencial (não existe paralelismo,
#       como explicado no 2.1.) e agora o programa têm de gastar recursos e tempo a mudar de thread,
#       aumentado o tempo necessário.

import time
from threading import Thread

COUNT = 50000000


def contar_decrescente(ls, li):
    while ls > li:
        ls -= 1


inicio = time.time()

thread_1 = Thread(target=contar_decrescente, args=(COUNT, COUNT // 2,))
thread_2 = Thread(target=contar_decrescente, args=(COUNT // 2, 0,))

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

fim = time.time()

print(f'Tempo em segundos: {fim - inicio}')
