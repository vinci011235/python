def Busca(L, inicio, fim, X):
	i = (inicio + fim)/2
	if (L[i] == X):
		return i
	if inicio == fim:
		return -1
	else:
		if (L[i] < X):
			return Busca(L, i+1, fim, X)
		else:
			return Busca(L, inicio, i-1, X)

L = [1, 2, 3, 5, 8, 9]
print Busca(L, 0, 5, 9)