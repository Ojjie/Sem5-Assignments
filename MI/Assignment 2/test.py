def rec_DFS_Traversal(cost, curr, goals, l):
	#print("at node cur: ",curr)
	#print("l: ",l)
	if(curr in goals):
		#print("reached goal")
		l.append(curr)
		return True
	else:
		path = l[:]
		path.append(curr)
		for i in range(1,len(cost[curr])):
			if(cost[curr][i] > 0 and i not in l):
				if(rec_DFS_Traversal(cost, i, goals, path) == True):
					#print("recursive call found goal")
					for node in path[(len(l)):(len(path))]:
						l.append(node)
					#print("path after finding goal: ",l)
					return True
		return False

def DFS_Traversal(cost, start_point, goals):
	l=[]
	found = rec_DFS_Traversal(cost, start_point, goals, l)
	return l
	


def UCS_Traversal():
	l=[]
	return l

def A_star_Traversal():
	l=[]
	return l

def tri_traversal(cost, heuristic, start_point, goals):
	l = []
	visited = [0]*len(cost[0])
	t1 = DFS_Traversal(cost, start_point, goals)
	'''t2 = UCS_Traversal()
	t3 = A_star_Traversal()
	l.append(t1)
	l.append(t2)
	l.append(t3)
	return l'''
	print(t1)

cost = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
			[0, 0, 5, 9, -1, 6, -1, -1, -1, -1, -1],
			[0, -1, 0, 3, -1, -1, 9, -1, -1, -1, -1], 
			[0, -1, 2, 0, 1, -1, -1, -1, -1, -1, -1],
			[0, 6, -1, -1, 0, -1, -1, 5, 7, -1, -1],
			[0, -1, -1, -1, 2, 0, -1, -1, -1, 2, -1],
			[0, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1],
			[0, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1],
			[0, -1, -1, -1, -1, 2, -1, -1, 0, -1, 8],
			[0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 7],
			[0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0]]
heuristic = [0, 5, 7, 3, 4, 6, 0, 0, 6, 5, 0]


tri_traversal(cost, heuristic, 1, [6,7,10])
