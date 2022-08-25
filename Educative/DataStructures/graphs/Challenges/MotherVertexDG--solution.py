"""
Solution: Last finished vertex
"""
from Graph import Graph
from Stack import MyStack

def find_mother_vertex(g):
    visited = [False] * (g.vertices)
    last_v = 0
    for i in range(g.vertices):
        if not visited[i]:
            perform_DFS(g,i,visited)
            last_v = i
    # Depth first search until we visited all the nodes
    # While storing the last vertex we performed dfs on

    # restart visited and assume mother vertex is last_v
    # perform DFS as last_v as the source

    visited = [False]*(g.vertices)
    perform_DFS(g,last_v,visited)
    # if all elements visited return the source else return -1
    if any(not i for i in visited):
        return -1
    else:
        return last_v

# recursive dfs function
def perform_DFS(g,node,visited):
    visited[node] = True
    temp = g.array[node].head_node
    while temp:
        if not visited[temp.data]:
            perform_DFS(g,temp.data,visited)
        temp = temp.next_element

"""
This solution is based on Korarju's Strongly connected Component Algorithm.
Initially, we run the DFS on the whole graph in a loop. The DFS ensures that all
the nodes in the graph are visited. If the graph is disconnected, the visited
list will still have some vertices which haven't been set to True.

The theory is taht the last vertex visited in the recursive DFS will be the 
mother vertex. This is because, at the last vertex, all slots in visited would
be True(DFS only stops when all nodes are visited). Hence, we keep track of
this last vertex using last_v.

Then, we reset the visited list and run the DFS only on last_v. If it visits all nodes,
it is a mother vertex. Otherwise, a mother vertex does not exist. The only limitation
in this algorithm is that it can detect one mother vertex, even if others exist.

Time complexity
The DFS of the whole graphs works in O(V+E). If a mother vertex does exists, the second DFS
takes O(V+E) as well. Therefore, the complete time complexity for this algorithm is
O(V+E).
"""