from Graph import Graph

def detect_cycle(g):
    visited = [False] * g.vertices
    rec_node_stack = [False] * g.vertices
    for node in range(g.vertices):
        if detect_cycle_rec(g,node,visited,rec_node_stack):
            return True
    return False

def detect_cycle_rec(g,node,visited,rec_node_stack):
    # Node was already in recursion stack. Cycle found
    if rec_node_stack[node]:
        return True
    # It has been visited before the recursion
    if visited[node]:
        return False
    # Mark current node as visited 
    # add to recursion stack

    visited[node] = True
    rec_node_stack[node] = True
    head_node = g.array[node].head_node
    while head_node is not None:
        adjacent = head_node.data
        if detect_cycle(g,adjacent,visited,rec_node_stack):
            return True
        head_node = head_node.next_element
    # remove the node from the recursive call
    rec_node_stack[node] = False
    return False

"""
So basically we visit every vertex and call a helper function on it
the vertex gets marked as visited, and its respective reucrsive node stack gets marked as visited too until
its edges are visited, then the recursive_node_stack marks the source back to false.

At this point, every edge has been visited and the recursive stack marks the source as false, and marks
every edge that was visited as false

On every source of the graph, its edges are visited in the helper function, and those children are called recursively on
to check if they have been visited before. 
If they have then there is no point in visiting them
if they are marked as true on the recursive node stack, then a cycle has been found, the call stack collapses(pops off) 
and returns true

We are basically just visiting every vertex and its edges recursively, and using another visited list, to see if we find
any self loops starting from the source

"""