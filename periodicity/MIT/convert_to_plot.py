


d = open("g_meetings.csv")

dic = {}

for line in d:
	cum = 0		
	pair = line.split(" ")
	for i in range(len(pair)):
		if(pair[i] != '\n'):
			if int(pair[i]) != -1:
				cum += int(pair[i])
				print(cum)
			else:
				cum = 0

