from time_lib import *
import math

class cstruct:
	glabel = -1
	group = []
	time = datetime.strptime('"2008-10-03 00:00:00', '"%Y-%m-%d %H:%M:%S')
	encounters = []
	stability = [0]
	GSCF = []
	duration = []
	ICT = []
	last_enc = datetime.strptime('"2008-10-03 00:00:00', '"%Y-%m-%d %H:%M:%S')

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
	if((len(intersection_list)*1.0)/len(union_list) <= 0.9):
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

def checkPeriodicity2(group_births_list, hour_groups_list, current_timestamp,graph,labels):
	for x_group in hour_groups_list:
		group = list(x_group)
		achou = 0
		for i in range(len(group_births_list)):
			if(group_track(group_births_list[i].group,group)!=0):
				for elem in group:
					if(not(i in labels[elem])):
						labels[elem] = labels[elem] + [i]
				achou = 1
				group_births_list[i].stability = group_births_list[i].stability + [group_corr(group,group_births_list[i].group)]
				#print(int((current_timestamp - group_births_list[i].last_enc).total_seconds()) == 3600)
				if(current_timestamp - group_births_list[i].last_enc <= 3600):
					group_births_list[i].duration = group_births_list[i].duration + [group_births_list[i].duration[-1]+1]
				else:
					group_births_list[i].duration = group_births_list[i].duration + [1]

				group_births_list[i].GSCF = group_births_list[i].GSCF + [GSCF(graph,group)]
				tp = current_timestamp - group_births_list[i].time
				group_births_list[i].group = group
				group_births_list[i].last_enc = current_timestamp
				group_births_list[i].ICT = group_births_list[i].ICT + [(current_timestamp - group_births_list[i].last_enc)/3600]
				group_births_list[i].encounter = group_births_list[i].encounter + [current_timestamp]
				break;
		if(achou==0):
			g_and_t = cstruct()
			g_and_t.glabel = len(group_births_list)
			g_and_t.group = group
			g_and_t.encounter = [current_timestamp]
			g_and_t.time = current_timestamp
			g_and_t.GSCF = [GSCF(graph,group)]
			g_and_t.duration = [1]
			g_and_t.ICT = [0]
			g_and_t.last_enc = current_timestamp
			group_births_list.append(g_and_t)

			for elem in group:
				labels[elem] = labels[elem] + [len(group_births_list)]

def groupsGraph(group_births_list):
	G= nx.Graph()
	maxi = 0
	for i in range(len(group_births_list)):
		if len(group_births_list[i].encounter) > maxi:
			maxi = len(group_births_list[i].encounter)
		G.add_node(group_births_list[i].glabel,members = group_births_list[i].group,encounters = len(group_births_list[i].encounter))
	nodes = nx.get_node_attributes(G,"encounters")
	for i in nodes:
		G.node[i]["encounters"] = 1-math.exp(-1*7*(1.0*G.node[i]["encounters"])/21)

	for i in range(len(group_births_list)):
		for j in range(i,len(group_births_list)):
			if(i!=j):
				a = group_births_list[i].group
				b = group_births_list[j].group
				matches = set(a).intersection(b)
				if len(group_births_list[i].group) > len(group_births_list[j].group):
					size = len(group_births_list[i].group)
				else:
					size = len(group_births_list[j].group)
				if len(matches) != 0:
					g1 = G.node[group_births_list[i].glabel]["encounters"]
					g2 = G.node[group_births_list[i].glabel]["encounters"]
					G.add_edge(group_births_list[i].glabel,group_births_list[j].glabel,weight=-numpy.log((1.0*len(matches)/size)* g1 * g2))
					#print (i,j,-numpy.log((1.0*len(matches)/size)* g1 * g2))
	return G


def groupsGraph2(groups,freq):
	G= nx.Graph()
	maxi = 0
	for i in range(len(groups)):
		if freq[i] > maxi:
			maxi = freq[i]
		G.add_node(i,members = groups[i],encounters = freq[i])
	nodes = nx.get_node_attributes(G,"encounters")
	for i in nodes:
		G.node[i]["encounters"] = 1.0*G.node[i]["encounters"]/maxi
	for i in range(len(groups)):
		for j in range(i,len(groups)):
			if(i!=j):
				a = groups[i]
				b = groups[j]
				matches = set(a).intersection(b)
				if len(groups[i]) > len(groups[j]):
					size = len(groups[i])
				else:
					size = len(groups[j])
				if len(matches) != 0:
					g1 = G.node[i]["encounters"]
					g2 = G.node[j]["encounters"]
					G.add_edge(i,j,weight=-numpy.log((1.0*len(matches)/size)* g1 * g2))

	return G


def computeMostProbPath(groups_graph,orig,dest):
	prob = 1
#	if(not(groups_graph.has_node(orig) and groups_graph.has_node(dest))):
#		print("a")
#		return([0,[]])		
	if(not(nx.has_path(groups_graph,source=orig,target=dest))):
		return([0,[]])
	path = nx.shortest_path(groups_graph,source=orig,target=dest,weight="weight")
#	if(len(path) == 1):
#		prob = 
	for i in range(len(path)-1):
		prob *= numpy.exp(groups_graph[path[i]][path[i+1]]['weight']*(-1))
	return([prob,path])

def ocComputeMostProbPath(groups_graph,orig,dest):
	prob = 1
#	if(not(groups_graph.has_node(orig) and groups_graph.has_node(dest))):
#		print("a")
#		return([0,[]])		
	if(not(nx.has_path(groups_graph,source=orig,target=dest))):
		return([0,[]])
	path = nx.shortest_path(groups_graph,source=orig,target=dest,weight="weight")
#	if(len(path) == 1):
#		prob = 
	for i in range(len(path)-1):
		prob *= numpy.exp(groups_graph[path[i]][path[i+1]]['weight']*(-1))
	return([prob,path])


def belong(groups,route,index):
	for g in groups:
		if (g in route):
			if route.index(g) >= index:
				return True
	return False
	
def belong_o(groups,route,index):
	for g in groups:
		if (g in route):
				return True
	return False


