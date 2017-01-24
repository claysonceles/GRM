import sys

dataset = sys.argv[1]
f = open(dataset)

n_nodes = 1200

contacts = [[[] for x in range(n_nodes)] for x in range(n_nodes)]
cont = 0

for line in f:
	if cont%100000==0:
		print cont
	cont+=1	
	pair = line.split(" ")
	i = int(pair[0])
	j = int(pair[1])
	time = int(pair[2])
	duration = int(pair[3])
	if i > j:
		aux = i
		i = j
		j = aux
	
	contacts[i][j] = contacts[i][j] + [time]

f = open("ict.csv","w")
for i in range(n_nodes):
	print i
	for j in range(i,n_nodes):
		for k in range(len(contacts[i][j])-1):
			f.write(str(contacts[i][j][k+1] - contacts[i][j][k])+"\n")
	f.flush()
f.close()

