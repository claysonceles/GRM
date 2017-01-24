


d = open("NCCU.csv")

for line in d:
	pair = line.split(" ")
	i = int(pair[0])
	j = int(pair[1])
	temp = int(pair[2]) - 1418767200
	print(str(i)+" "+str(j)+" "+str(temp)+" "+str(1));
