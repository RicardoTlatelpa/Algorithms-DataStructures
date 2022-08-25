from Graph import Graph
# We only need Graph for this Question!

def is_tree(g):
    visited = [False] * g.vertices
    # detect cycle in undirected graph
    if check_cycle(g,0,visited,-1):
        return False

    # check how connected graph is
    # the idea is, if the graph is connected it shouldn't have a problem connecting
    # to all nodes from the 0th vertex of the graph
    for i in range(len(visited)):
    # Graph is not connected
        if not visited[i]:
            return False
    # Non-cyclic and connected graph
    return True

def check_cycle(g,node,visited,parent):
    visited[node] = True
    adjacent = g.array[node].head_node
    while adjacent:
        if not visited[adjacent.data]:
            if check_cycle(g,adjacent.data,visited,node):
                return True            
        elif adjacent.data != parent:
            return True
        adjacent = adjacent.next_element

    return False

"""
The logic for this problem is the same as Challenge 3 where you have to detect a cycle in the graph. 
We make a stack (not to be confused with the stack data structure) of vertices in check_cycle(). 
This stack grows recursively (line 31). The only difference is that we keep track of the parent 
vertex since a backward link to the parent does not count as a cycle (undirected graph). If a cycle 
is found in the graph, check_cycle will return True.

At the end of the recursion, visited should be all true and no cycles were found

Time complexity:
    O(V+E) same as BFS or DFS
"""