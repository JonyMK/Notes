from multiprocessing import Process, Queue, Pipe
import os
import random


def func_com_queue_write(q, values):
    q.put(values)
    print(f"\t{values} enviado pelo subprocesso produtor_queue (Process-{os.getpid()})")


def func_com_queue_read(q):
    print(f"\t{q.get()} recebido pelo subprocesso consumidor_queue (Process-{os.getpid()})")


def func_com_pipe_write(conn, values):
    print(f"\t{values} enviado pelo subprocesso produtor_pipe (Process-{os.getpid()})")
    conn.send(values)
    conn.close()


def func_com_pipe_read(conn):
    print(f"\t{conn.recv()} recebido pelo subprocesso consumidor_pipe (Process-{os.getpid()})")
    conn.close()



if __name__ == '__main__':
    names = ["Francisco", "Barros", "Venelin", "Argirov"]
    print(f"processo (MainProcess)-{os.getpid()}")

    # utilizando pipe
    conn_pai, conn_filho = Pipe()
    print("Comunicação com Pipe")
    produtor_pipe = Process(target=func_com_pipe_write, args=(conn_pai, names))
    produtor_pipe.start()
    produtor_pipe.join()
    consumidor_pipe = Process(target=func_com_pipe_read, args=(conn_filho,))
    consumidor_pipe.start()
    consumidor_pipe.join()

    # utilizando queue
    q = Queue()
    produtor_queue = Process(target=func_com_queue_write, args=(q, names))
    print("Comunicação com Queue")
    produtor_queue.start()
    produtor_queue.join()
    consumidor_queue = Process(target=func_com_queue_read, args=(q,))
    consumidor_queue.start()
    consumidor_queue.join()
