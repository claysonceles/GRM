


d = open("swim.csv")

for line in d:
	pair = line.split(" ")
	i = int(pair[0])
	j = int(pair[1])
	temp = int(pair[2])-200112
	dur = int(pair[2]) - int(pair[3])
	print(str(i)+" "+str(j)+" "+str(temp)+" "+str(dur));
