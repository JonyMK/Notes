# Nivel 2

# Diga o que faz a instrução i.to_bytes e explique a diferença entre byteorder='big' e
# byteorder='little'
# R: A função "i.to_bytes" vai tornar os números de i até n em bytes.
#    O byteorder='big' vai ordenar os números mais significativos a esquerda
#    enquanto o byteorder='little' irá ordena-los a direita.

# Explique o que faz o programa
# R: O programa vai escrever em dois ficheiros os números de i até n em bytes
#    com as duas ordenações mencionadas anteriormente.

# Abra os ficheiros outBig.bin e outLittle.bin e verifique a forma como estão representados os
# inteiros. Aceda ao site HexEd.it para abrir os ficheiros e, no menu configurações, altere o
# número de bytes por linha para 4. Verifique como está representado o número 1024 em
# cada um dos ficheiros.
# R: No ficheiro outBig que contem os números cujos algarismos mais significativos
# estão no inicio o número 1024 é representado por 00 00 09 04 e no ficheiro outLittle
# é representado por 09 04 00 00

if __name__ == '__main__':
    n = 10000
    with open('outBig.bin', 'wb') as file:
        for i in range(n):
            file.write(i.to_bytes(4, byteorder='big', signed=False))
    with open('outLittle.bin', 'wb') as file:
        for i in range(n):
            file.write(i.to_bytes(4, byteorder='little', signed=False))