#Diga o que faz cada uma das seguintes instruções:
# q = Queue() -> Cria uma queue
# q.put(valor) -> Coloca um valor na queue
# valor = q.get() -> Remove e retorna um valor da queue
# conn_pai, conn_filho = Pipe() -> Cria uma pipe
# conn.send(['Olá', 'mundo', 'abril', 2022]) -> Envia os valores para o conn_filho
# conn.recv() -> Devolve os valores que estão no conn_filho
# conn.close() -> Fecha a conexão

from multiprocessing import Process, Queue, Pipe
import os
import random

def funcao_comunicacao_queue(q):
    print(f"\tEstou na função funcao_comunicacao_queue e sou o processo {os.getpid()}")
    valor = random.randint(1, 10)
    q.put(valor)

def funcao_comunicacao_pipe(conn):
    print(f"\tEstou na função funcao_comunicacao_pipe e sou o processo {os.getpid()}")
    conn.send(['Olá', 'mundo', 'abril', 2022])
    conn.close()

if name == 'main':
    print(f"processo principal {os.getpid()}")
    # utilizando queue
    q = Queue()
    processo_1 = Process(target=funcao_comunicacao_queue, args=(q,))
    processo_1.start()
    valor = q.get()
    print(f"valor recebido: {valor}")
    processo_1.join()
    # utilizando pipe
    conn_pai, conn_filho = Pipe()
    processo_2 = Process(target=funcao_comunicacao_pipe, args=(conn_filho,))
    processo_2.start()
    valor = conn_pai.recv()
    print(f"valor recebido: {valor}")
    processo_2.join()