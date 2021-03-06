'''
author Elvis Soares Gomes
codigo disponivel em github.com/vinci011235/python
'''
def multiplicar(matrizA, matrizB):
	quantL = len(matrizA) #linha
	quantC = len(matrizA[0]) #quantos elementos na linha (coluna)
	quantLB = len(matrizB) #linha da segunda matriz
	multi = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] #vetor que recebera o produto
	
	# i numeros de linha
	# j numeros de coluna
	# k move nas colunas de A e linhas de B
	#multi recebe a soma das multiplicaçao de cada elemento
	for i in range(quantL):
		for j in range(quantC):
			aux = 0
			for k in range(quantLB):
				aux += matrizA[i][k] * matrizB[k][j]
			multi[i][j] = aux
	return multi

#multiplica todas as posições por 2
def multiplicarA(matrizX):
	quantL = len(matrizX)
	quantC = len(matrizX[0])
	multi2a = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

	for i in range(quantL):
		for j in range(quantC):
			multi2a[i][j] = matrizX[i][j] * 2

	return multi2a

#soma o retorno das 2 funções acima
def soma(y,z):
	quantL = len(y)
	quantC = len(z[0])
	soma = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	for i in range(quantL):
		for j in range(quantC):
			soma[i][j] = y[i][j] + z[i][j]
	return soma

if __name__ == '__main__':
	a = [[3,5,1,6],[6,2,0,9],[7,3,5,4],[10,4,2,1]]
	b = [[6,2,8,3],[9,1,3,4],[3,3,4,4],[8,7,0,6]]
	print 'matriz A: \n',a
	print '------------------------\n'
	print 'matriz B: \n',b
	print '------------------------\n'
	print 'A x B: \n'
	print multiplicar(a,b)
	print '------------------------\n'
	print '2 x A: \n'
	print multiplicarA(a)
	print '------------------------\n'
	print 'A X B + 2A \n'
	print soma(multiplicar(a,b),multiplicarA(a))
	print '------------------------\n'
