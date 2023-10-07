'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
write a function to find the number of connected components in an undirected graph.
'''
edges = [[0,1], [1,2], [3,4]]
visited = [False for _ in range(len(edges)+1)]
def dfs(v,adjList):
    if visited[v] == True:
        return
    visited[v] = True
    for adjV in adjList[v]:
        if visited[adjV] != True:
            dfs(adjV, adjList)
    
def countConnectedNodes(edgeList):
    adjList = {}
    
    for (v,e) in edgeList:
        if v not in adjList:
            adjList[v] = [e]
        else:
            adjList[v].append(e)
    ans = 0
    for (vertex) in adjList:
        if visited[vertex] == False:
            ans+=1
            dfs(vertex, adjList)
    return ans

print(countConnectedNodes(edges))
