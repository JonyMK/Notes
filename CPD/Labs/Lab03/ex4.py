# Diga o que faz o programa.
# R: O que o programa vai fazer é copiar os dados dum ficheiro para outro e retornar o tempo gasto para fazer a operação.
#    Com o processamento sequencial e multi-threaded

# Explique a diferença de desempenho observadas
# R: O processamento multi-thread é mais rápido devido ao programa ser I/O Bound, desta maneira o programa beneficia
#   bastante devido a poder continuar a trabalhar enquanto existem threads à espera de instruções I/O, enquanto que no
#   no modo sequencial a thread fica em modo "blocked" sem haver outra atrás a funcionar entretanto.
import shutil
import time
import threading
if __name__ == '__main__':
    # Versao sequencial
    print("Cópia sequencial de ficheiros")
    inicio = time.time()
    for k in range(10):
        fileName1 = "fich" + str(k + 1) + ".dat"
        fileName2 = "outFich" + str(k + 1) + ".dat"
        shutil.copy(fileName1, fileName2)
    print(f"\tTempo utilizado na cópia sequencial de ficheiros = {time.time()-inicio}")
    # Versao com threads
    print("Cópia multi-threading de ficheiros")
    inicio = time.time()
    threads = []
    for k in range(10):
        fileName1 = "fich" + str(k + 1) + ".dat"
        fileName2 = "outFich" + str(k + 1) + ".dat"
        t = threading.Thread(target=shutil.copy, args=[fileName1, fileName2])
        threads.append(t)
        t.start()
    for i in range(10):
        threads[i].join()
    print(f"\tTempo utilizado na cópia multi-threading de ficheiros = {time.time() - inicio}")