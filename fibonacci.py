'''
Sequencia Fibonacci
'''
#Menu
def menu():
	print '1 - calcular fibonacci'
	print '2 - sair'
	op = int(raw_input(': '))
	return op
'''
Calcula sequencia
n1 -> 0 + 1 = 0
n2 -> 1 - 1 = *0

n1 -> 1 + 0 = 1
n2 -> 1 - 0 = *1

n1 -> 1 + 1 = 2
n2 -> 2 - 1 = *1
'''
def fibonacci(n1,n2,t):
	for x in range(0, t):
		n1 = n1 + n2
		n2 = n1 - n2
		print n2
	print '-------------'
#Chama menu e verifica o retorno
if __name__ == '__main__':
	while (menu() != 2):
		n = int(raw_input('Quantos numeros\n:'))
		print '-------------'
		fibonacci(0,1,n)