from random import randint
from collections import namedtuple
from datetime import datetime
import networkx as nx
import numpy
import random

import group_lib as gl
import time_lib as tl
import sys
import os
n_nodes = 2000
dataset = "./prox.csv"

if len(sys.argv) != 4:
	print "Wrong arguments."
	print "Usage: python protocolo.py 'origin_node' 'destination_node'"
	print "Exiting..."
	exit()

time_init = int(sys.argv[3])

W_lim = 600
k_clique = 3


k = int(sys.argv[1])#random.randint(1,75) #49 #18 pior caso
l = int(sys.argv[2])#random.randint(1,75) #5 #30 pior caso

origin = k
dest = l

encounters = [[] for x in range(n_nodes)]
global_rank = [0 for x in range(n_nodes)]
labels = [[] for x in range(n_nodes)]

f = open(dataset)
dia_ant = 0

#for line in f:
#	pair = line.split(" ")
#	i = int(pair[0])
#	j = int(pair[1])
#	time = int(pair[2])
#	duration = int(pair[3])
#	dia = time / (24*3600)

#	if(i!=j):
#		if(dia != dia_ant):
#			dia = dia_ant
#			encounters = [[] for x in range(2000)]
#		if(not(j in encounters[i])):
#			encounters[i] = encounters[i] + [j]
#			global_rank[i] += 1;
#		if(not(i in encounters[j])):
#			encounters[j] = encounters[j] + [i]
#			global_rank[j] += 1;

print("oi")

group_and_time = gl.cstruct()
group_births_list = []

periodicity_vector = [0 for x in range(30000)]

evolution_rates = [[] for x in range(24)]

reaching_time = [-1 for y in range(n_nodes)]
have_message = [False for y in range(n_nodes)]

have_message[origin] = True
reaching_time[origin] = 0

G= nx.Graph()

for i in range(0,n_nodes):
	for j in range(0,n_nodes):
		if(i!=j):
			G.add_edge(i,j,weight=0);

f = open(dataset)

start_capture_hour = 0
zero_hour = 3600*24*7*3 + time_init*3600

groups_last_hour = []

dia_ant =0

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

strategy = 0

transmission = 0
route = []

arrived = False
arrival = -1

difuse_once = False

labels = [[] for x in range(n_nodes)]

difusion_flag = True 

dia_ant = 0 
hora_ant = 0

#labels_txt = open("./protocolo_vt/labels"+str(time_init)+".txt","w")
#groups_txt = open("./protocolo_vt/groups"+str(time_init)+".txt","w")

for line in f:
	pair = line.split(" ")
	i = int(pair[0])
	j = int(pair[1])
	time = int(pair[2])
	duration = int(pair[3])
	dia = time / (24*3600)
	hora = time / (3600)

	i2 = i
	j2 = j

	if i == j:
		continue;
	
	if(dia == dia_ant and hora == hora_ant):
		G[i][j]['weight'] = G[i][j]['weight'] + duration
	else:
		print(hora)
		#next hour
		hora_ant = hora
		dia_ant = dia
		G_aux = G
		#######Reseting G (hour graph)
		G=nx.Graph()

		for i in range(1,n_nodes):
			for j in range(0,n_nodes):
				if(i!=j):
					G.add_edge(i,j,weight=0);
		#######End of: Reseting G (hour graph)#########

		#######Removing Edges that are not social######		
		for i in range(0,n_nodes):
			for j in range(i,n_nodes):
				if(i!=j):
					if(G_aux[i][j]['weight'] < W_lim):
						G_aux.remove_edge(i,j)
					#if(G_day[i][j]['weight'] < W_lim):
						#G_day[i][j]['weight'] = 0

		#graph_list.append(G_aux)

		cls = nx.find_cliques(G_aux)
		communities = list(nx.k_clique_communities(G_aux,k_clique ,cliques = cls))
		groups_last_hour = list(communities)
		gl.checkPeriodicity2(group_births_list, list(communities), time, G_aux,labels)
		#print(len(group_births_list))
################ routing test #########################################################
enc_t = open("g_meetings.csv","w")
	
for gr in group_births_list:	
	if(len(gr.encounter)<=1):
		enc_t.write(str(-1)+" ")
	else:
		flag = True
		for enc in range(1,len(gr.encounter)):
			value = (gr.encounter[enc] - gr.encounter[enc-1])/3600
			if value > 1:
				enc_t.write(str(value)+" ")
				flag = False
		if flag:
			enc_t.write(str(-1)+" ")
	enc_t.write("\n")
	enc_t.flush()
enc_t.close()

enc_t = open("g_members.csv","w")

for gr in group_births_list:	
	for enc in range(0,len(gr.group)):
		value = gr.group[enc]
		enc_t.write(str(value)+" ")
	enc_t.write("\n")
	enc_t.flush()
enc_t.close()

exit();		


