from queue import PriorityQueue

def rec_DFS_Traversal(cost, curr, goals, l):

	if(curr in goals):
		l.append(curr)
		return True
	else:
		path = l[:]
		path.append(curr)
		for i in range(1,len(cost[curr])):
			if(cost[curr][i] > 0 and i not in l):
				if(rec_DFS_Traversal(cost, i, goals, path) == True):
					for node in path[(len(l)):(len(path))]:
						l.append(node)
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
	current_node = front[1][-1]
	if(current_node in goals):
		return front[1]
	for i in range(1,len(cost[0])):
		if(cost[current_node][i] > 0 and i not in front[1]):
			path_cost = front[2] + cost[current_node][i]
			new_path = front[1][:]
			new_path.append(i)
			queue.put([(path_cost + heuristic[i]),new_path,path_cost])
	return rec_A_star_Traversal(cost, heuristic, start_point, goals, queue)

def A_star_Traversal(cost, heuristic, start_point, goals):
	queue = PriorityQueue()
	queue.put([0,[start_point],0])
	return rec_A_star_Traversal(cost, heuristic, start_point, goals, queue)


def rec_UCS_Traversal(cost, start_point, goals, queue):
	if(queue.empty() == True):
		return []
	front = queue.get()
	current_node = front[1][-1]
	if(current_node in goals):
		return front[1]
	for i in range(1,len(cost[0])):
		if(cost[current_node][i] > 0 and i not in front[1]):
			path_cost = front[0] + cost[current_node][i]
			new_path = front[1][:]
			new_path.append(i)
			queue.put([path_cost,new_path])
	return rec_UCS_Traversal(cost, start_point, goals, queue)

def UCS_Traversal(cost, start_point, goals):
	queue = PriorityQueue()
	queue.put([0,[start_point]])
	return rec_UCS_Traversal(cost, start_point, goals, queue)


def tri_traversal(cost, heuristic, start_point, goals):
	l = []
	t1 = DFS_Traversal(cost, start_point, goals)
	t2 = UCS_Traversal(cost, start_point, goals)
	t3 = A_star_Traversal(cost, heuristic, start_point, goals)
	l.append(t1)
	l.append(t2)
	l.append(t3)
	return l



