#Kahns Algorithm
# First step, determine the indegere of each vertex
# O(V+E)
# Second step, start with vertices that have an ind of 0
# traverse these nodes and remove their connection to 
# adjacent nodes
# When finished, add explored vertex to final ans


def kahn(adj_list, N):
    indegree = [0] * (N+1)
    for i in range(N+1):
        for adjNode in adj_list[i]:
            indegree[adjNode]+=1
    ans = []
    queue = []
    for i in range(len(indegree)):
        if indegree[i] == 0:
            queue.append(i)
    while(len(queue) != 0):
        deq = queue.pop(0)
        ans.append(deq)
        for node in adj_list[deq]:
            indegree[node]-=1
            if indegree[node] == 0:
                queue.append(node)
    return ans

print(kahn([
    [],
    [],
    [3],
    [1],
    [0,1],
    [0,2]
    ],5))
