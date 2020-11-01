'''
def A_star_Traversal(
    #add your parameters 
):
    l = []

    return l

'''
def UCS_Traversal(cost,start_point,goals):
    l = []

    #my code 
    visited = [] #should be a set to avoid duplicate values ?
    path = []  #total traversed path 
    fringe = [] 
    path_cost = {} #to store the cost of a path up till a particular point 
    priority = 0 

    if start == goals:
        #print("reached goal")
        #l.append(path)
        return path 
        return True 

    else:
        #path.append(start_point)
        #path_cost = 0

        frontier = PriorityQueue() #priority queue for elements to be placed in frontier 
        frontier.push((start,path),priority)
        #[(path_cost,path)] #this will basically act as the priority queue 
        path_cost(start) = 0
        visited.append(start)


        while(frontier):
            current_node , current_path = frontier.pop() #to retrieve the current node and path from frontier 


            if current_node == goals:
                return current_path 

            else:
                
                #declare a variable called 'next' to get the children (successors) of the current node - need a separate helper function for that 

                for node in frontier.heap():
                    fringe.append(node[0])

                for states in next: #adds every child to the frontier. 
                    if states[0] not in (key for key in path_cost):
                        frontier.push((states[0], cost + [states[1]]),cost)

                        path_cost(states[0]) = cost 
                        visited.add(states[0])





            '''
            #previous implementation 
            current_path_cost , current_path = frontier.pop() #should it be get for this implementation?
            current_node = current_path[-1]

            visited.append(current_node)

            if(current_node == goals):
                l.append(current_path)

            '''












    return l

'''
def DFS_Traversal(
    #add your parameters 
):
    l = []

    return l

'''

'''
Function tri_traversal - performs DFS, UCS and A* traversals and returns the path for each of these traversals 

n - Number of nodes in the graph
m - Number of goals ( Can be more than 1)
1<=m<=n
Cost - Cost matrix for the graph of size (n+1)x(n+1)
IMP : The 0th row and 0th column is not considered as the starting index is from 1 and not 0. 
Refer the sample test case to understand this better

Heuristic - Heuristic list for the graph of size 'n+1' 
IMP : Ignore 0th index as nodes start from index value of 1
Refer the sample test case to understand this better

start_point - single start node
goals - list of size 'm' containing 'm' goals to reach from start_point

Return : A list containing a list of all traversals [[],[],[]]
1<=m<=n
cost[n][n] , heuristic[n][n], start_point, goals[m]

NOTE : you are allowed to write other helper functions that you can call in the given fucntion
'''

def tri_traversal(cost, heuristic, start_point, goals):
    l = []
'''
    t1 = DFS_Traversal(
    #send whatever parameters you require 
)
'''


    t2 = UCS_Traversal(
    #send whatever parameters you require 
)

'''

    t3 = A_star_Traversal(
    #send whatever parameters you require 
)

'''

    l.append(t1)
    l.append(t2)
    l.append(t3)
    return l
