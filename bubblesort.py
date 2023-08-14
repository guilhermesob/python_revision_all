
def trocar (seq,i):
    tmp = seq[i]
    seq[i] = seq[i+1]
    seq[i+1] = tmp

sequencia = [10,5,20,1,4]
troca=1
while troca:
	troca=0
	i=0
	for i in range(0,len(sequencia)-1):
		if sequencia[i]>sequencia[i+1]:
		    trocar(sequencia,i)
		    troca=1
print(sequencia)
