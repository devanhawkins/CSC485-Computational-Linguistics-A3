from nltk.corpus import wordnet as wn

root=wn.synset('entity.n.01')

def bfs_mins():
	mins={root:0}
	min_leafs={}
	to_explore=root.hyponyms()
	#print to_explore
	for n in to_explore:
		mins[n]=1
	while len(to_explore)!=0:
		current=to_explore[0]
		to_explore=to_explore[1:]
		kids=current.hyponyms()
		for n in kids:
			if not mins.has_key(n) or mins[n]>(mins[current]+1):
				mins[n]=mins[current]+1
				to_explore.append(n)
		if len(kids)==0:
			min_leafs[current]=mins[current]

	min_examples=[]
	max_examples=[]
	min_sofar=10000
	max_sofar=0
	for key in min_leafs.keys():
		if min_leafs[key]<min_sofar:
			min_sofar=min_leafs[key]
			min_examples=[key]
		elif min_leafs[key]==min_sofar:
			min_examples.append(key)
		if min_leafs[key]>max_sofar:
			max_sofar=min_leafs[key]
			max_examples=[key]
		elif min_leafs[key]==max_sofar:
			max_examples.append(key)
	print min_examples, " ", min_sofar
	print max_examples, " ", max_sofar
	total_nodes=len(mins.keys())
	leaf_nodes=len(min_leafs.keys())
	print "total_nodes from entity:",len(mins.keys())," internal_nodes from entity:", total_nodes-leaf_nodes, " leaf_nodes from entity:",leaf_nodes, " ratio:", leaf_nodes/float(total_nodes)
	#get all nodes not just those rooted at entity
	count=0
	l_count=0
	for n in wn.all_synsets('n'):
		count+=1
		if len(n.hyponyms())==0:
			l_count+=1
	print "Total Nodes: %d , Total leaf Nodes: %d, Ratio: %f" % (count, l_count, float(l_count)/count)
	#return mins,min_leafs


def pairs_comp():
	pairs=[['car','automobile'],
	['gem','jewel'],
	['journey','voyage'],
	['boy','lad'],
	['coast','shore'],
	['asylum','madhouse'],
	['magician','wizard'],
	['midday','noon'],
	['furnace','stove'],
	['food','fruit'],
	['bird','cock'],
	['bird','crane'],
	['tool','implement'],
	['brother','monk'],
	['lad','brother'],
	['crane','implement'],
	['journey','car'],
	['monk','oracle'],
	['cemetery','woodland'],
	['food','rooster'],
	['coast','hill'],
	['forest','graveyard'],
	['shore','woodland'],
	['monk','slave'],
	['coast','forest'],
	['lad','wizard'],
	['chord','smile'],
	['glass','magician'],
	['rooster','voyage'],
	['noon','string']]
	results={}
	for p in pairs:
		max_score=0.0
		for x in wn.synsets(p[0]):
			for y in wn.synsets(p[1]):
				max_score=max(max_score,wn.path_similarity(x,y))
		if not results.has_key(max_score):
			results[max_score]=[]
		results[max_score].append(p)
	keys=results.keys()
	keys.sort()
	keys.reverse()
	for key in keys:
		for res in results[key]:
			print str(res[0])+"-"+str(res[1])+" & "+str(key) + " &  \\\\"
		#print results[key], " " , key


#bfs_mins()
pairs_comp()

