# Revisiting topological sort

def topologicalSort(adjList,N):
    visited = [False] * (N+1) 
    ans,stack = [],[]
    def dfs(v):
        nonlocal visited
        nonlocal stack
        if visited[v] == False:
            visited[v] = True
            for adjNode in adjList[v]:
                dfs(adjNode)
            # explore adjacent nodes
            stack.append(v)
    for i in range(N+1):
        if visited[i] == False:
            dfs(i)
    while(len(stack) != 0):
        ans.append(stack.pop())
    return ans

print(topologicalSort([
    [],
    [],
    [3],
    [1],
    [0,1],
    [0,2]
    ],5))
