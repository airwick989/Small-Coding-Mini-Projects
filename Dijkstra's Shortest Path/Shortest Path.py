import heapq

MAX_LENGTH_CONSTRAINT = 100000  #Maximum possible edge length constraint

def shortestReach(nodecount, edges, start):
    
    new_edges = []
    for node_to_others in range(nodecount):        
        skeleton = []
        for i in range(nodecount):
            skeleton.append(MAX_LENGTH_CONSTRAINT)
        new_edges.append(skeleton)
    #Make a list of edge lengths from node of index in list to all other nodes (nested 
    #list). Make lengths the max constraint by default
    #Reason we're not using the list of edges provided is to avoid the duplicate edges
    #problem
    
    for edge in edges:
    
        head = edge[0]
        tail = edge[1]
        length = edge[2]
        #Get the head, tail, and length of every edge
        
        if length < new_edges[head - 1][tail - 1]:
            new_edges[head - 1][tail - 1] = length
        if length < new_edges[tail - 1][head - 1]:
            new_edges[tail - 1][head - 1] = length
        #For the corresponding index of a head and tail node in the the list of edges, 
        #IF the current edge being added is shorter than the one already stored in the 
        #list, append it. Otherwise, keep the edge length already in the list.
        #This is to handle duplicate edges, was a MASSIVE pain before
        
    nodes = []
    for i in range(nodecount):
        nodes.append(-1)
    #Make a list of lengths to nodes
    #Set all nodes to unvisited, -1
    
    #####################################################################################
    #Everything after is basically where the shortest path finding begins
    
    heap = []
    heapq.heappush(heap, (0, start))
    #initialize a heapq called heap
    #Push the starting node and a length to it of 0
    
    while len(heap) > 0:   #Do the following while the heap is not empty
    
        length, node = heapq.heappop(heap) 
        #return the smallest length to a node from heap and the node itself
        
        if nodes[node] == -1:     
        #check if the node has been visited or not
        #if it has already been visited, skip iteration and get next smallest
        #length to a node. If not visited, do following.
        
            nodes[node] = length
            #If the node has not yet been visited, assign its corresponding length to
            #it from the start node to its correct position in the list of nodes. 
            
            for next_node in range(nodecount):  #Do the following for every node
            
                if new_edges[node][next_node] != MAX_LENGTH_CONSTRAINT and nodes[next_node] == -1:
                    heapq.heappush(heap, (length+new_edges[node][next_node], next_node))
                #If the length to a next node from the current node of interest 
                #is not the max constraint and it is unvisited, push it to the heapq
                #along with an updated total path length starting from start node 
            
    nodes.pop(start) #remove beginning node to conform with output format
    return nodes


n = 4
edges = [[1, 2, 24], 
            [1, 4, 20], 
            [3, 1, 3], 
            [4, 3, 12]]
s = 1

distances_from_s = shortestReach(n, edges, s-1)
print(distances_from_s)