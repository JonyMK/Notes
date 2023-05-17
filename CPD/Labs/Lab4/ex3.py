# Diga o que faz o programa
# O programa calcula os primeiros 10 termos da série de Fibonacci e retorna o tempo
# que demorou para os calcular.

# O que é um dicionário em Python
# É uma estutura de dados do tipo coleção que permite armazenar objetos (chave:valor).


# Coloque como comentário as instruções mostrar_dicionario(dicionario_fibonacci), altere
# para 10000 o valor da qtd_valores e execute o programa. Explique a diferença de
# desempenho observada.

# A primeira forma tem uma complexidade O(n^2) pois é um ciclo que dentro dele chama uma função O(n)
# dentro de um próprio ciclo for na função, desta maneira O(n) a chamar uma função O(n), ficando quadrátrica.
# No entanto a segunda forma têm complexidade O(n), desta maneira com quantos mais valores trabalhar com, mais eficiente
# é em relação à primeira forma, mesmo tendo de ir ao dicionário ler os dados. No entanto, se os valores fossem menores,
# a primeira forma é provalvelmente mais rápida.
#


import time


def fibonacci(n):
    a, b = 0, 1
    for item in range(n):
        a, b = b, a + b
    return a


def preencher_dicionario_fibonacci_v1(dicionario, qtd):
    for i in range(qtd):
        dicionario[i + 1] = fibonacci(i + 1)


def preencher_dicionario_fibonacci_v2(dicionario, qtd):
    for i in range(qtd):
        if i <= 2:
            dicionario[i] = 1
        else:
            dicionario[i] = dicionario[i - 1] + dicionario[i - 2]


def mostrar_dicionario(dicionario):
    for n in dicionario.keys():
        print(f'Fib({n}) = {dicionario[n]}')


if __name__ == '__main__':
    qtd_valores = 10000
    inicio = time.time()
    dicionario_fibonacci = {}
    preencher_dicionario_fibonacci_v1(dicionario_fibonacci, qtd_valores)
    tempo = time.time() - inicio
    print(f'{tempo:.10f}s para calcular os primeiros {qtd_valores} termos da série de Fibonacci de forma sequencial')
    # print(dicionario_fibonacci)
    # mostrar_dicionario(dicionario_fibonacci)
    inicio = time.time()
    dicionario_fibonacci = {}
    preencher_dicionario_fibonacci_v2(dicionario_fibonacci, qtd_valores)
    tempo = time.time() - inicio
    print(f'{tempo:.10f}s para calcular os primeiros {qtd_valores} termos da série de Fibonacci de forma sequencial')
    # mostrar_dicionario(dicionario_fibonacci)
