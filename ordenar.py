def ordenacao(L,N):
	for j in range(0,N-1):
		for i in range(0, N-1):
			if L[i] > L[i+1]:
				aux = L[i]
				L[i]=L[i+1]
				L[i+1]=aux
L = [1,3,4,5,7,8,9,6,6,6]
ordenacao(L, 10)
print L	
	
