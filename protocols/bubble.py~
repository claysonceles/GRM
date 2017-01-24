try:
    import matplotlib.pyplot as plt
except:
    raise

import networkx as nx
import time_lib as tl
import random
import sys
import numpy as np
n_nodes = 1200

W_lim = 5*3600
k_clique = 7

nodes_distro = [0 for x in range(n_nodes)]

if len(sys.argv) != 5:
	print "Wrong arguments."
	print "Usage: python protocolo.py 'origin_node' 'destination_node' 'dataset_path' 'withTowers_flag'" 
	print "Exiting..."
	exit()

time_init = 0#int(sys.argv[4])

zero_hour = int(sys.argv[4])*3600 


G=nx.Graph()
for i in range(1,n_nodes):
	for j in range(0,n_nodes):
		if(i!=j):
			G.add_edge(i,j,weight=0);

encounters = [[] for x in range(n_nodes)]
global_rank = [0 for x in range(-60,n_nodes)]
labels = [[] for x in range(n_nodes)]
dataset = sys.argv[3]

withTowers = 0

f = open(dataset)

origin = int(sys.argv[1])
dest = int(sys.argv[2])

dia_ant = 0

for line in f:
	pair = line.split(" ")
	i = int(pair[0])
	j = int(pair[1])
	time = int(pair[2])
	duration = int(pair[3])
	dia = time / (24*3600)

	if(i!=j):
		if(dia != dia_ant):
			dia_ant = dia
			encounters = [[] for x in range(n_nodes)]
		if(not(j in encounters[i])):
			encounters[i] = encounters[i] + [j]
			global_rank[i] += 1;
		if(not(i in encounters[j])):
			encounters[j] = encounters[j] + [i]
			global_rank[j] += 1;
		G[i][j]['weight'] = G[i][j]['weight'] + duration
					###print(G[i][j]['weight'])

			#print("montou grafo")

for i in range(0,n_nodes):
	for j in range(i,n_nodes):
		if(i!=j):
			if(G[i][j]['weight'] < W_lim):
				G.remove_edge(i,j)

cls = nx.find_cliques(G)
communities = list(nx.k_clique_communities(G,k_clique ,cliques = cls))

#print(len(communities))

for c in range(len(list(communities))):
	for i in range(len(labels)):
		if i in list(list(communities)[c]):
			labels[i] = labels[i] + [c]
k=len(list(communities))
for i in range(len(labels)):
	if len(labels[i]) == 0:
		labels[i] = labels[i] + [i + k];
num_labels = len(labels) + k
local_rank = [[0 for y in range(num_labels)] for x in range(n_nodes)]

encounters = [[] for x in range(n_nodes)]
f = open(dataset)
dia_ant = 0

for line in f:
	pair = line.split(" ")
	i = int(pair[0])
	j = int(pair[1])
	time = int(pair[2])
	duration = int(pair[3])
	dia = time / (24*3600)

	if(i!=j):
		if(dia != dia_ant and list(set(labels[i]).intersection(labels[j])) != []):
			l = list(set(labels[i]).intersection(labels[j]))
			for it in l:
				if(not(j in encounters[i])):
					encounters[i] = encounters[i] + [j]
					local_rank[i][it]+=1;
				if(not(i in encounters[j])):
					encounters[j] = encounters[j] + [i]
					local_rank[j][it]+=1;
			dia_ant = dia

have_message = [False for x in range(n_nodes)]

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

#exit()
if withTowers == 1: 
	rg = open("../rg.csv")
	global_rank = [0 for x in range(-60,n_nodes)]
	for line in f:
		pair = line.split(" ")
		indice = int(pair[0])
		valor_rg = int(pair[1])
		global_rank[indice]=valor_rg
		
		
	torres = -1
	while torres > -60:
		global_rank[torres] = 100000000
		torres-=1

if withTowers == 2: 
	torres = -1
	while torres > -60:
		global_rank[torres] = 100000000
		torres-=1

#print("comecou difusao")
f = open(dataset)
ttl = 24*7*6
for line in f:
	pair = line.split(" ")
	i = int(pair[0])
	j = int(pair[1])
	time = int(pair[2])
	duration = int(pair[3])

	if (time >= zero_hour and ((time-zero_hour) / 3600) < ttl):
		if(have_message[i] and not(have_message[j])):
			if(list(set(labels[i]).intersection(labels[dest]))!=[]):
				if(list(set(labels[j]).intersection(labels[dest]))!=[] and local_rank[j][labels[dest][0]] > local_rank[i][labels[dest][0]]):
					transmission +=1;
					nodes_distro[i] += 1
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
					if (((time-zero_hour) / 3600) <= 24*7*6):
						cont_6w+=1;
				else:
					if(j == dest):
						nodes_distro[i] += 1
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
						if (((time-zero_hour) / 3600) <= 24*7*6):
							cont_6w+=1;

			else:
				if(list(set(labels[j]).intersection(labels[dest]))!=[] or global_rank[j] > global_rank[i] or j == dest):
					transmission +=1;
					nodes_distro[i] += 1
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
					if (((time-zero_hour) / 3600) <= 24*7*6):
						cont_6w+=1;
					
		if(have_message[j] and not(have_message[i])):
			if(list(set(labels[j]).intersection(labels[dest]))!=[]):
				if(list(set(labels[i]).intersection(labels[dest]))!=[] and local_rank[i][labels[dest][0]] > local_rank[j][labels[dest][0]]):
					transmission +=1;
					nodes_distro[j] += 1
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
					if (((time-zero_hour) / 3600) <= 24*7*6):
						cont_6w+=1;
				else:
					if(i == dest):
						transmission +=1;
						nodes_distro[j] += 1
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
						if (((time-zero_hour) / 3600) <= 24*7*6):
							cont_6w+=1;
			else:
				if(list(set(labels[i]).intersection(labels[dest]))!=[] or global_rank[i] > global_rank[j] or i==dest):
					transmission +=1;
					nodes_distro[j] += 1
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
					if (((time-zero_hour) / 3600) <= 24*7*6):
						cont_6w+=1;

	if(have_message[dest]):
		print(str(origin)+","+ str(dest)+","+str(have_message[dest])+","+str(transmission)+","+str((time-zero_hour)/ 3600))
		break
	if((time-zero_hour)/ 3600 > ttl):
		print(str(origin)+","+ str(dest)+","+str(have_message[dest])+","+str(transmission)+","+str(-1))
		break
#print(local_rank)

#if int(sys.argv[3])==1:	
#	f_distro = open("distro_protocolo.txt","r")
#else:
#	f_distro = open("distro_bubble.txt","r")

#nodes_distro_old = [0 for x in range(1200)]

#i = 0
#for line in f_distro:
#	value = int(line)
#	if value == -1:
#		break;
#	nodes_distro_old[i] = value
#	i+=1
#f_distro.close()


#if int(sys.argv[3])==1:	
#	f_distro = open("distro_protocolo.txt","w")
#else:
#	f_distro = open("distro_bubble.txt","w")
#for v in range(len(nodes_distro)):
#	f_distro.write(str(nodes_distro[v]+nodes_distro_old[v])+"\n")
#f_distro.close()
if withTowers == 0:
	f1 = open("b_1h.txt","a")
	f1.write(str(cont_1))
	f1.write("\n")
	f1 = open("b_3h.txt","a")
	f1.write(str(cont_3))
	f1.write("\n")
	f1 = open("b_6h.txt","a")
	f1.write(str(cont_6))
	f1.write("\n")
	f1 = open("b_12h.txt","a")
	f1.write(str(cont_12))
	f1.write("\n")
	f1 = open("b_24h.txt","a")
	f1.write(str(cont_24))
	f1.write("\n")
	f1 = open("b_48h.txt","a")
	f1.write(str(cont_48))
	f1.write("\n")
	f1 = open("b_96h.txt","a")
	f1.write(str(cont_96))
	f1.write("\n")
	f1 = open("b_1w.txt","a")
	f1.write(str(cont_1w))
	f1.write("\n")
	f1 = open("b_2w.txt","a")
	f1.write(str(cont_2w))
	f1.write("\n")
	f1 = open("b_3w.txt","a")
	f1.write(str(cont_3w))
	f1.write("\n")
	f1 = open("b_6w.txt","a")
	f1.write(str(cont_6w))
	f1.write("\n")

if withTowers == 1:
	f1 = open("p_1h.txt","a")
	f1.write(str(cont_1))
	f1.write("\n")
	f1 = open("p_3h.txt","a")
	f1.write(str(cont_3))
	f1.write("\n")
	f1 = open("p_6h.txt","a")
	f1.write(str(cont_6))
	f1.write("\n")
	f1 = open("p_12h.txt","a")
	f1.write(str(cont_12))
	f1.write("\n")
	f1 = open("p_24h.txt","a")
	f1.write(str(cont_24))
	f1.write("\n")
	f1 = open("p_48h.txt","a")
	f1.write(str(cont_48))
	f1.write("\n")
	f1 = open("p_96h.txt","a")
	f1.write(str(cont_96))
	f1.write("\n")
	f1 = open("p_1w.txt","a")
	f1.write(str(cont_1w))
	f1.write("\n")
	f1 = open("p_2w.txt","a")
	f1.write(str(cont_2w))
	f1.write("\n")
	f1 = open("p_3w.txt","a")
	f1.write(str(cont_3w))
	f1.write("\n")

if withTowers == 2:
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

