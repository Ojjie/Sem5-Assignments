from queue import PriorityQueue

def rec_DFS_Traversal(cost, curr, goals, l):
	#print("at node cur: ",curr)
	#print("l: ",l)
	if(curr in goals):
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

def rec_A_star_Traversal(cost, heuristic, start_point, goals, queue):
	if(queue.empty() == True):
		return []
	front = queue.get()
	path_len = len(front[2])-1
	current_node = front[2][path_len]
	if(current_node in goals):							#if a path that ends with a goal node is at the top of the queue it is the optimal solution
		return front[2]
	for i in range(1,len(cost[0])):
		if(cost[current_node][i] > 0 and i not in front[2]):
			path_cost = front[1] + cost[current_node][i]
			new_path = front[2][:]
			new_path.append(i)
			queue.put([(path_cost + heuristic[i]),path_cost,new_path])
	return rec_A_star_Traversal(cost, heuristic, start_point, goals, queue)

#check on this later

def A_star_Traversal(cost, heuristic, start_point, goals):
	queue = PriorityQueue()
	queue.put([0,0,[start_point]])
	return rec_A_star_Traversal(cost, heuristic, start_point, goals, queue)


def rec_UCS_Traversal(cost, start_point, goals, queue):
	if(queue.empty() == True):
		return []
	#print("front of queue: ",front)
	front = queue.get()
	path_len = len(front[1])-1
	current_node = front[1][path_len]
	#print("current node: ",current_node)
	if(current_node in goals):							#if a path that ends with a goal node is at the top of the queue it is the optimal solution
		#print("goal found")
		return front[1]
	for i in range(1,len(cost[0])):
		if(cost[current_node][i] > 0 and i not in front[1]):
			path_cost = front[0] + cost[current_node][i]
			new_path = front[1][:]
			new_path.append(i)
			queue.put([path_cost,new_path])
	return rec_UCS_Traversal(cost, start_point, goals, queue)

#check on this later

def UCS_Traversal(cost, start_point, goals):
	queue = PriorityQueue()
	queue.put([0,[start_point]])
	return rec_UCS_Traversal(cost, start_point, goals, queue)


def tri_traversal(cost, heuristic, start_point, goals):
	l = []
	t1 = DFS_Traversal(cost, start_point, goals)
	#t2 = UCS_Traversal()
	t3 = A_star_Traversal(cost, heuristic, start_point, goals)
	#l.append(t1)
	#l.append(t2)
	'''l.append(t3)
	return l'''
	print(t1)
	print(t3)

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


#tri_traversal(cost, heuristic, 1, [6,7,10])
