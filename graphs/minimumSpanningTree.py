# Implmentation of Prim's Algorithm

'''
Assuming an adjaceny list
where the index is the vertex holding an array of pairs; 
[[(1,2),(2,1)]]
Here vertex 
0 => 1 with a weight of 2
0 => 2 with a weight of 1
'''
import heapq # min_heap from python language needed
def PrimsAlgo(adj_list,V): # such that V is the number of vertices
    pq = [(0,0,-1)] # holding (weight,node,parent)
    visited = [0] * V
    MST = [] # holding the connections of the MST
    MST_SUM = 0
    
    while(len(pq) != 0):
        top_of_heap = heapq.heappop(pq)
        weight,node,parent = top_of_heap[0],top_of_heap[1],top_of_heap[2]
        if visited[node] != 0:
            if parent != -1:
                MST_SUM += weight
                MST.append((node,parent)) # MST connection
            # explore children
            for adj in adj_list[node]:
                (adj_w,adj_v) = adj
                if visited[adj_v]!=1:
                    heapq.heappush(pq,(adj_w,adj_v,node))
# Interpreter gives read error on line 29; python still compiles on terminal




