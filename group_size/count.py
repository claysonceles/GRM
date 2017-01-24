
f = open("groups_dt.csv")

for line in f:
	pair = line.split(" ")
	print(len(pair)-1)
