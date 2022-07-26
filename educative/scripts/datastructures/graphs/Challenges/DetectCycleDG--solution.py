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