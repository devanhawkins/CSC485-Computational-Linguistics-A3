corpus=[['otters hurried '],['whales hurried carefully for otters among fish by otters'],['seals placed seals onto seals'],['whales hurried whales beside fish by fish for whales'],['seals placed seals among whales onto seals'],['otters we admire placed otters onto whales'],['otters we admire swam carefully onto whales'],['otters placed seals onto otters'],['otters among seals advanced toward whales'],['otters placed seals onto otters'],['seals among whales placed seals onto seals onto otters onto whales'],['whales placed fish beside whales onto whales by whales'],['seals among fish swam by otters'],['fish beside seals onto whales swam carefully by fish by whales beside whales beside fish'],['otters hurried for whales'],['otters we admire hurried otters onto otters for fish'],['seals placed happily whales onto fish beside whales'],['seals swam carefully onto otters'],['fish by seals placed whales onto seals onto fish beside otters'],['seals swam by fish'],['otters hurried for seals'],['otters among seals hurried fish beside seals onto otters among whales for whales beside whales'],['otters onto fish hurried whales for fish'],['seals among whales hurried happily'],['whales hurried happily fish for fish'],['seals swam '],['otters onto otters hurried carefully whales for whales'],['fish advanced beside fish'],['whales advanced '],['seals we love placed otters onto fish'],['seals hurried carefully whales for otters onto otters'],['whales by otters hurried for otters'],['otters swam onto whales'],['fish swam by whales'],['fish swam '],['otters swam carefully by fish'],['seals we love hurried for fish by whales by whales'],['seals placed whales beside whales beside fish onto seals'],['whales advanced otters among whales toward whales'],['whales advanced toward fish']]

pos={"fish":"N","whales":"N","seals":"N","otters":"N","we":"N","swam":"V","hurried":"V","placed":"V","advanced":"V","love":"V","admire":"V","carefully":"Adv","happily":"Adv","by":"P","onto":"P","toward":"P","beside":"P","for":"P","among":"P"}


true_w_count=0
total_w_count=0
total_s_count=0
true_s_count=0
n_p_true_count=0
v_p_true_count=0
for sentence in corpus:
	s=sentence[0].split()
	for x in range(len(s)):
		if s[x]=="whales":
			total_w_count+=1
		if s[x]=="advanced":
			total_s_count+=1
		#check for v,p tuple
		if (x+1<len(s) and pos[s[x+1]]=="N") or (x+2<len(s) and pos[s[x+2]]=="N" and pos[s[x+1]]!="V"):
			#have a n2
			if pos[s[x]]=="P" and s[x]!="of":
				#have non off prep
				v=None
				if (x-1>=0 and pos[s[x-1]]=="V"):
					v=s[x-1]
				elif (x-2>=0 and pos[s[x-2]]=="V" and pos[s[x-1]]!="N"):
					v=s[x-2]
				if v!=None:
					print v, " ", s[x]
					if v=="advanced":
						true_s_count+=1
						if s[x]=="for":
							v_p_true_count+=1
		#check for n,p tuple
		#n2 is the first noun to occur within the 
		if (x+1<len(s) and pos[s[x+1]]=="N") or (x+2<len(s) and pos[s[x+2]]=="N" and pos[s[x+1]]!="V"):
			#n is the first noun to occur within K left of p
			n=None
			if (x-1>=0 and pos[s[x-1]]=="N"):
				n=s[x-1]
			elif (x-2>=0 and pos[s[x-2]]=="N"):
				n=s[x-2]
			if n!=None:
				#no verb occurs within K words to left of p
				if (x-1<0 or pos[s[x-1]]!="V") and (x-2<0 or pos[s[x-2]]!="V"):
					#p is no of
					if pos[s[x]]=="P" and s[x]!="of":
						print n, " ", s[x]
						if n=="whales":
							true_w_count+=1
							if s[x]=="for":
								n_p_true_count+=1


print "Total-whale: %d vs True-whale: %d" % (total_w_count,true_w_count)

print "Total-swam: %d vs True-swam: %d" % (total_s_count,true_s_count)

print "v_p_true: %d , n_p_true %d" % (v_p_true_count,n_p_true_count)