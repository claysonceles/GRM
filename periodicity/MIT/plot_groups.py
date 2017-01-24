
try:
    import matplotlib.pyplot as plt
except:
    raise

from random import randint
from collections import namedtuple
from datetime import datetime
import networkx as nx
import numpy
import random
#import pso

sms_flag = 0

dataset = "./prox.csv"
sms_dataset = "../../../SocialEvolution/sms_.csv"
start_date = 'Sun Sep 16 16:05:15 +0000 2012'
end_date = 'Sun Sep 17 23:55:20 +0000 2012'
"2007-09-05 14:02:11"

p_init = 0.8

def __datetime(date_str):
	return datetime.strptime(date_str, '"%Y-%m-%d %H:%M:%S')

#start = __datetime(start_date)
#end = __datetime(end_date)

#delta = end - start
#print delta  # prints: 1 day, 7:50:05
#print delta.total_seconds()  # prints: 114605.0

def group_match(l1,l2):
	if(len(l1)==0):
		return 0;
	n_matching_groups = 0
	for i in l1:
		for j in l2:
			matches = list(set(i).intersection(j))
			if(len(matches) > len(i)/2.0):
				n_matching_groups += 1
				break
	return(100*(n_matching_groups*1.0)/(1.0*len(l1)))
				
def int_to_weekday(day):
	to_week = {}
	to_week[1] = "monday"
	to_week[2] = "tuesday"			
	to_week[3] = "wednesday"
	to_week[4] = "thursday"
	to_week[5] = "friday"
	to_week[6] = "saturday"
	to_week[7] = "sunday"
	return to_week[day]

def weekday_to_int(weekday):
	to_int = {}
	to_int["monday"] = 1 
	to_int["tuesday"] = 2 			
	to_int["wednesday"] = 3
	to_int["thursday"] = 4
	to_int["friday"] = 5
	to_int["saturday"] = 6
	to_int["sunday"] = 7
	return to_int[weekday]

def hour_persistance_ratio(day_groups):
	pers_list = []	#persistance list
	for i in range(0 , 22):
		pers_list.append(group_match(day_groups[i],day_groups[i+1]))
	return pers_list;

def group_corr(g1,g2):
	#####computing union of g1 and g2 nodes#### 
	union_list = set(g1).union(g2)
	###########################################
	#####computing intersection of g1 and g2 nodes#### 
	intersection_list = set(g1).intersection(g2)
	##################################################
	return((len(intersection_list)*1.0)/len(union_list))


def group_track(g1,g2):
	#####computing union of g1 and g2 nodes#### 
	union_list = set(g1).union(g2)
	###########################################
	#####computing intersection of g1 and g2 nodes#### 
	intersection_list = set(g1).intersection(g2)
	##################################################
	if((len(intersection_list)*1.0)/len(union_list) < 0.9):
		return 0;
	else:
		if(len(g1)==len(g2)):
			return(2);
		if(len(g1)>len(g2)):
			return(-1);
		if(len(g1)<len(g2)):
			return(1);
			
def group_evolution(group_list1,group_list2):
	class cstruct:
		unchanged = 0
		growth = 0
		contract = 0
		birth = 0
		death = 0
	e = cstruct()
	
	if(len(group_list1)==0):
		e.birth = len(group_list2)
		return e
	if(len(group_list2)==0):
		e.death = len(group_list1)
		return e
		
	matched_groups1=[]
	matched_groups2=[]
	for i in group_list1:
		for j in group_list2:
			t = group_track(i,j);
			if(t!=0):
				matched_groups1.append(i);
				matched_groups2.append(j);
				if(t==-1):
					e.contract+=1;
				if(t==1):
					e.growth+=1;
				if(t==2):
					e.unchanged+=1;
	e.birth = len(group_list2)-len(matched_groups2)
	e.death = len(group_list1)-len(matched_groups1)
	return e;


def GSCF(graph,group):	##Sum of group internal edge-weights divided by total sum of group nodes' edge-weights
	w_in = 0;
	w_out = 0;
	for node in group:
		neighbor_iter = nx.all_neighbors(graph,node)
		for neighbor in neighbor_iter:
			if(neighbor in group):
				w_in += graph[node][neighbor]['weight']
				#print("in: "+ str(graph[node][neighbor]['weight']))
			else:
				w_out += graph[node][neighbor]['weight']
				#print("out: "+ str(graph[node][neighbor]['weight']))
	w_in = w_in/2; #because edges from inside the group are considered one time for each node, thus, counted twice instead of once.
	return ((1.0*w_in)/(w_in+w_out));	

def AGICT_AGSCF(groups):
#	print("oi"+str(randint(0,10)))
	AGICT_AGSCF_list = []
	for i in groups:
		ICT_list = [];
		GSCF_list = [];
		for j in range(len(i.reencounters)):
			ICT_list = ICT_list + [[(i.reencounters[j])[0]]];
			GSCF_list = GSCF_list + [[(i.reencounters[j])[1]]];
		#print(GSCF_list)
		if(len(ICT_list)==0):
			continue;
		else:
			#AGICT = numpy.mean(ICT_list)*numpy.std(ICT_list)
			AGICT = numpy.mean(ICT_list)/len(ICT_list)
			if(AGICT == 0):
				print(len(ICT_list))
		if(len(GSCF_list)==0):
			continue;
		else:	
			print(GSCF_list)
			AGSCF = numpy.mean(GSCF_list)
			print(AGSCF)
		AGICT_AGSCF_list = AGICT_AGSCF_list + [[len(GSCF_list),AGSCF,AGICT,numpy.mean(i.stability)]]
		#print(AGICT,AGSCF)
	return(AGICT_AGSCF_list)

def predict(groups,time_in_past,acceptable_dev):
	return;
		
class cstruct:
	group = []
	time = datetime.strptime('"2008-10-03 00:00:00', '"%Y-%m-%d %H:%M:%S')
	encounters = []
	stability = [0]
	GSCF = []
	duration = []
	ICT = []
	last_enc = datetime.strptime('"2008-10-03 00:00:00', '"%Y-%m-%d %H:%M:%S')
	reenc_prob=[p_init];
group_and_time = cstruct()

group_births_list = []
periodicity_vector = [0 for x in range(30000)]

def checkPeriodicity(group_births_list, hour_groups_list, current_timestamp):
	for x_group in hour_groups_list:
		group = list(x_group)
		achou = 0
		for i in range(len(group_births_list)):
			#print(group)
			#print(group_births_list[i].group)
			if(group_track(group_births_list[i].group,group)!=0):
				achou = 1
				group_births_list[i].group = group
				tp = current_timestamp - group_births_list[i].time
				periodicity_vector[int(tp.total_seconds())/3600] += 1
				#print(int(tp.total_seconds())/3600)
				break;
		if(achou==0):
			g_and_t = cstruct()
			g_and_t.group = group
			g_and_t.time = current_timestamp
			group_births_list.append(g_and_t)

def checkPeriodicity2(group_births_list, hour_groups_list, current_timestamp,graph):
	for x_group in hour_groups_list:
		group = list(x_group)
		achou = 0
		for i in range(len(group_births_list)):
			if(group_track(group_births_list[i].group,group)!=0):
				achou = 1
				group_births_list[i].stability = group_births_list[i].stability + [group_corr(group,group_births_list[i].group)]
				#print(int((current_timestamp - group_births_list[i].last_enc).total_seconds()) == 3600)
				if(int((current_timestamp - group_births_list[i].last_enc).total_seconds()) == 3600):
					group_births_list[i].duration = group_births_list[i].duration + [group_births_list[i].duration[-1]+1]
				else:
					group_births_list[i].duration = group_births_list[i].duration + [1]
				prob = group_births_list[i].prob[-1]
				prob = prob*0.98**(int((current_timestamp - group_births_list[i].encounter[-1]).total_seconds()/3600) -1)
				prob = prob*0.80**(int((current_timestamp - group_births_list[i].encounter[-1]).total_seconds()/3600) -1)
				#print(prob)
				group_births_list[i].GSCF = group_births_list[i].GSCF + [GSCF(graph,group)]
				tp = current_timestamp - group_births_list[i].time
				group_births_list[i].group = group
				group_births_list[i].last_enc = current_timestamp
				group_births_list[i].ICT = group_births_list[i].ICT + [(current_timestamp - group_births_list[i].encounter[-1]).total_seconds()/3600]
				group_births_list[i].prob = group_births_list[i].prob + [prob + (1-prob)*p_init]
				periodicity_vector[int(tp.total_seconds())/3600] += 1
				group_births_list[i].encounter = group_births_list[i].encounter + [current_timestamp]
				break;
		if(achou==0):
			g_and_t = cstruct()
			g_and_t.group = group
			g_and_t.encounter = [current_timestamp]
			g_and_t.time = current_timestamp
			g_and_t.GSCF = [GSCF(graph,group)]
			g_and_t.duration = [1]
			g_and_t.ICT = [0]
			g_and_t.prob = [p_init]
			g_and_t.last_enc = current_timestamp
			group_births_list.append(g_and_t)

def temp_mean(lista):
	mean = 0;
	for i in range(len(lista)):
		mean += lista[i]*0.5**(len(lista) - i)
	return mean;

evolution_rates = [[] for x in range(24)]

sms = [[0 for y in range(85)] for x in range(85)]

reaching_time = [[-1 for y in range(85)] for x in range(85)]
have_message = [[False for y in range(85)] for x in range(85)]
#origin = random.randint(1,80)
for origin in range(85):
	have_message[origin][origin] = True
	reaching_time[origin][origin] = 0

labels = []

#for i in range(0,40):
#	labels.append("#"+str(hex(randint(0,pow(2,24)-1))[2:]))
#	print(labels[i])
labels = {}
labels[0] = "red"
labels[1] = "blue"
labels[2] = "yellow"
labels[3] = "white"
labels[4] = "pink"
labels[5] = "green"
labels[6] = "orange"
labels[7] = "purple"
labels[8] = "gray"
labels[9] = "black"

W_lim = 2
k_clique = 3

G= nx.Graph()
G_day = nx.Graph()

for i in range(0,85):
	for j in range(0,85):
		if(i!=j):
			G.add_edge(i,j,weight=0);
			G_day.add_edge(i,j,weight=0);

f2 = open(sms_dataset)

f = open(dataset)
out = open("./daily_group_persistece.csv","w")

out.write("0h,1h,2h,3h,4h,5h,6h,7h,8h,9h,10,11h,12h,13h,14h,15h,16h,17h,18h,19h,20h,21h,22h,23h\n")
out.write("day.1,0") 
groups_last_hour = []
groups_day_ant = []
dia_ant = '"2008-10-03'
hora_ant = '00'
week_day = 5
graph_list = []
day_groups =  []
num_day = 1;
aux=0

start_capture_hour = __datetime('"2008-11-03 00:00:00')
zero_hour1 = __datetime('"2008-11-03 00:00:00')
zero_hour2 = __datetime('"2008-12-03 00:00:00')
zero_hour3 = __datetime('"2009-01-03 00:00:00')
zero_hour4 = __datetime('"2009-02-03 00:00:00')
zero_hour5 = __datetime('"2009-03-03 00:00:00')
zero_hour6 = __datetime('"2009-04-03 00:00:00')
zero_hour7 = __datetime('"2009-05-03 00:00:00')
zero_hour = __datetime('"2009-06-03 00:00:00')
zero_hour9 = __datetime('"2009-07-03 00:00:00')
zero_hour10 = __datetime('"2009-08-03 00:00:00')
zero_hour11 = __datetime('"2009-09-03 00:00:00')
zero_hour12 = __datetime('"2009-10-03 00:00:00')

timestamp = __datetime('"2008-10-03 00:00:00')
sms_timestamp = __datetime('"2008-10-03 00:00:00')
difusion_flag = True 

g_size = open("./groups_size_per_hour.csv","w")
g_size.write("0h,1h,2h,3h,4h,5h,6h,7h,8h,9h,10,11h,12h,13h,14h,15h,16h,17h,18h,19h,20h,21h,22h,23h\n")
g_size.write("day.1,0") 
for line in f:
	pair = line.split()
	i = int(pair[0])
	j = int(pair[1])
	i2 = i
	j2 = j
	dia = pair[2]
	hora = pair[3][0:2]
	timestamp = __datetime(dia + " " + hora + ":00:00")

	while int((sms_timestamp - timestamp).total_seconds()) < 0:
		l = f2.readline();
		pair = l.split()
		if len(pair)<5:
			break
		sms_source = int(pair[4])
		sms_dest = int(pair[0])
		sms_dia = pair[1]
		sms_hora = pair[2][0:2]
		sms_timestamp = __datetime(dia + " " + hora + ":00:00")
		sms[sms_source][sms_dest] = 1
		#print(sms_source,sms_dest,sms_dia,sms_hora)

	if(dia == dia_ant and hora == hora_ant):
		G[i][j]['weight'] = G[i][j]['weight'] + 1
		G_day[i][j]['weight'] = G_day[i][j]['weight'] + 1
	else:
		if(dia != dia_ant):
			##next day
			aux=0
			num_day+=1
			out.flush()
			out.write("\nday."+str(num_day))
			g_size.write("\nday."+str(num_day))
			for i in range(0,85):
				for j in range(i+1,85):
					if(G_day[i][j]['weight'] < W_lim):
						G_day.remove_edge(i,j)

			day_groups = [list(i) for i in set(map(tuple, day_groups))]	#removendo grupos duplicados
			day_groups = sorted(day_groups,key=lambda tam: len(tam), reverse = False)	#ordenando pelo tamanho dos grupos, decrescente

			#print("grupos do dia")
			#print day_groups
			#print(len(day_groups))
			
			G_day = nx.Graph()

			for i in range(1,85):
				for j in range(0,85):
					if(i!=j):
						G_day.add_edge(i,j,weight=0);
			day_groups = []
			if(week_day == 7):
				week_day = 1
			else:
				week_day+=1;
			#print(int_to_weekday(week_day))

		#next hour
		hora_ant = hora
		dia_ant = dia
		G_aux = G
		#######Reseting G (hour graph)
		G=nx.Graph()

		for i in range(1,85):
			for j in range(0,85):
				if(i!=j):
					G.add_edge(i,j,weight=0);
		#######End of: Reseting G (hour graph)#########

		#######Removing Edges that are not social######
		for i in range(0,85):
			for j in range(i,85):
				if(i!=j):
					if(G_aux[i][j]['weight'] < W_lim):
						G_aux.remove_edge(i,j)
					#if(G_day[i][j]['weight'] < W_lim):
						#G_day[i][j]['weight'] = 0

		graph_list.append(G_aux)

		cls = nx.find_cliques(G_aux)
		communities = list(nx.k_clique_communities(G_aux,k_clique ,cliques = cls))
		#print(dia_ant,hora_ant)
		#print(list(communities))
		ge = group_evolution(groups_last_hour,list(communities))
		evolution_rates[int(hora_ant)].append(ge)
		#print(ge.unchanged,ge.birth,ge.death,ge.growth,ge.contract)
		groups_last_hour = list(communities)
		checkPeriodicity2(group_births_list, list(communities), timestamp,G_aux)
		
		list(communities)
		l = len(list(communities))
		###########################################3
		avg_group_size = 0
		for i in list(communities):
			avg_group_size += len(i);
		if(l!=0):
			avg_group_size = (1.0*avg_group_size)/l;
		g_size.write(","+str(avg_group_size));
		###########################################3
		day_groups = day_groups + list(communities)
		
		match_ratio = group_match([list(i) for i in list(groups_day_ant)],[list(i) for i in list(day_groups)])
		
		out.write(","+str(match_ratio))
		aux+=1
		#print(aux)
		groups_day_ant = list(communities)

enc_t = open("g_meetings.csv","w")
	
for gr in group_births_list:	
	if(len(gr.encounter)<=1):
		enc_t.write(str(-1)+" ")
	else:
		flag = True
		for enc in range(1,len(gr.encounter)):
			value = int((gr.encounter[enc] - gr.encounter[enc-1]).total_seconds()/3600)
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


