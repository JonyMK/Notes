import time  

# 3.1 - Diga o que faz o programa
#	R : O programa inicia um loop onde cria 10 ficheiros, de 0 a 9 (na verdade de 1 a 10 devido ao +1).
#	A seguir para cada ficheiro, abre o ficheiro e escreve 1000000 * k (numero do ficheiro) vezes no ficheiro,
#	sendo o k incrementado cada vez que passa para o próximo ficheiro, com o último ficheiro sendo escrito 10000000 vezes.
#	Cada escrita vai ocupar 4 bytes no ficheiro, desta maneira cada ficheiro vai ocupar 1 000 000 * k (número do ficheiro) * 4 bytes
#	Por último indica o tempo que demorou a escrever estes 10 ficheiros.
#	Em resumo, escreve 10 ficherios no disco com tamanhos cada vez maiores.

inicio = time.time() 
for k in range(10):     
	fileName = "fich"+str(k+1)+".dat"     
	with open(fileName, 'wb') as file:
		for i in range((k+1)*1000000):
			file.write(i.to_bytes(4, byteorder='big', signed=False)) 
print(f"Tempo escrita = {time.time()-inicio}")