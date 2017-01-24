try:
    import matplotlib.pyplot as plt
except:
    raise

import networkx as nx
import time_lib as tl
import random
import sys

n_nodes = 2000

if len(sys.argv) != 5:
	print "Wrong arguments."
	print "Usage: python protocolo.py 'origin_node' 'destination_node' 0" 
	print "Exiting..."
	exit()

time_init = int(sys.argv[4])*3600

#zero_hour = 3600*24*7*3 + time_init*3600
zero_hour = time_init

dataset = sys.argv[3]
f = open(dataset)

have_message = [False for x in range(-100,n_nodes)]

origin = int(sys.argv[1])
dest = int(sys.argv[2])

have_message[origin] = True
transmission = 0

cont_1=0
cont_3=0
cont_6=0
cont_12=0
cont_24=0
cont_48=0
cont_96=0
cont_1w=0
cont_2w=0
cont_3w=0
cont_6w=0

f = open(dataset)
ttl = 24*7*3
for line in f:
	pair = line.split(" ")
	i = int(pair[0])
	j = int(pair[1])
	time = int(pair[2])
	if (time >= zero_hour):
		if(have_message[i] and not(have_message[j])):
			transmission +=1;
			have_message[j] = True;
			if (((time-zero_hour) / 3600) <= 1):
				cont_1+=1;
			if (((time-zero_hour) / 3600) <= 3):
				cont_3+=1;
			if (((time-zero_hour) / 3600) <= 6):
				cont_6+=1;
			if (((time-zero_hour) / 3600) <= 12):
				cont_12+=1;
			if (((time-zero_hour) / 3600) <= 24):
				cont_24+=1;
			if (((time-zero_hour) / 3600) <= 48):
				cont_48+=1;
			if (((time-zero_hour) / 3600) <= 96):
				cont_96+=1;
			if (((time-zero_hour) / 3600) <= 24*7):
				cont_1w+=1;
			if (((time-zero_hour) / 3600) <= 24*14):
				cont_2w+=1;
			if (((time-zero_hour) / 3600) <= 24*21):
						cont_3w+=1;	
			if (((time-zero_hour) / 3600) <= 24*42):
						cont_6w+=1;	
		if(have_message[j] and not(have_message[i])):
			transmission +=1;
			have_message[i] = True;
			if (((time-zero_hour) / 3600) <= 1):
				cont_1+=1;
			if (((time-zero_hour) / 3600) <= 3):
				cont_3+=1;
			if (((time-zero_hour) / 3600) <= 6):
				cont_6+=1;
			if (((time-zero_hour) / 3600) <= 12):
				cont_12+=1;
			if (((time-zero_hour) / 3600) <= 24):
				cont_24+=1;
			if (((time-zero_hour) / 3600) <= 48):
				cont_48+=1;
			if (((time-zero_hour) / 3600) <= 96):
				cont_96+=1;
			if (((time-zero_hour) / 3600) <= 24*7):
				cont_1w+=1;
			if (((time-zero_hour) / 3600) <= 24*14):
				cont_2w+=1;
			if (((time-zero_hour) / 3600) <= 24*21):
				cont_3w+=1;
			if (((time-zero_hour) / 3600) <= 24*42):
						cont_6w+=1;

	#print(have_message[dest],transmission,int((timestamp-zero_hour).total_seconds() / 3600))
	#print(origin,dest)
	if(have_message[dest]):
		print(str(origin)+","+ str(dest)+","+str(have_message[dest])+","+str(transmission)+","+str((time-zero_hour) / 3600))
		break
	if(((time-zero_hour) / 3600) > 42*24):
		print(str(origin)+","+ str(dest)+","+str(have_message[dest])+","+str(transmission)+","+str(-1))
		break
#print(local_rank)

if True:				
	f1 = open("f_1h.txt","a")
	f1.write(str(cont_1))
	f1.write("\n")
	f1 = open("f_3h.txt","a")
	f1.write(str(cont_3))
	f1.write("\n")
	f1 = open("f_6h.txt","a")
	f1.write(str(cont_6))
	f1.write("\n")
	f1 = open("f_12h.txt","a")
	f1.write(str(cont_12))
	f1.write("\n")
	f1 = open("f_24h.txt","a")
	f1.write(str(cont_24))
	f1.write("\n")
	f1 = open("f_48h.txt","a")
	f1.write(str(cont_48))
	f1.write("\n")
	f1 = open("f_96h.txt","a")
	f1.write(str(cont_96))
	f1.write("\n")
	f1 = open("f_1w.txt","a")
	f1.write(str(cont_1w))
	f1.write("\n")
	f1 = open("f_2w.txt","a")
	f1.write(str(cont_2w))
	f1.write("\n")
	f1 = open("f_3w.txt","a")
	f1.write(str(cont_3w))
	f1.write("\n")
	f1 = open("f_6w.txt","a")
	f1.write(str(cont_6w))
	f1.write("\n")



