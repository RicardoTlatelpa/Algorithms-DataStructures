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

>>Adjacency List of Undirected Graph g1<<
| 0 | => [ 3 ] -> [ 2 ] -> [ 1 ] -> None
| 1 | => [ 0 ] -> None
| 2 | => [ 0 ] -> None
| 3 | => [ 4 ] -> [ 0 ] -> None
| 4 | => [ 5 ] -> [ 3 ] -> None
| 5 | => [ 4 ] -> None

After visiting source 0

visited[True,True,True,True,False,False]

(3,0),(2,0),(1,0) = queue

dequeue (3,0) = (v,parent)

(2,0),(1,0) = queue

adjacent list of 3 = [4,0]
for u in range(adjacency list of vertex 3):
    if not visited[4]:
        visited[4] = True
        queue.enqueue((u,v)) # (4,3),(2,0),(1,0)
    elif u != parent # false because we met the first case of not being visited

first iteration finished, visited 4 now we're at index 1

if not visited[0] # false, 0 is visited

elif u != parent is similar to saying 0 != 0 which is false

visited[True,True,True,True,True,False]

So we move on to this queue
(4,3),(2,0),(1,0) = queue
deqeue = (v,parent) = (4,3)
(2,0),(1,0) = queue

adjacency list of 4 = [5,3]
for u in range(adjacency list of vertex 4):
    if not visited[5] # true statement
        visited[5] = True
        queue.enqueue((5,4)) # 
first iterastion finished, visited 5 @idx 0 now we're at index 1
    if not visited[3] # 3 has been visited
    elif u != parent; 3 != 3 # false statement so we finish loop

queue = (5,4),(2,0),(1,0)
dequeue = (5,4) = (v,parent)
queue = (2,0),(1,0)
adjacency list of vertex 5 = [4]
for u in range(adjacency list of vertex 5):
    if visited[4] is false # node has been visited
    else if 
    u != parent, u is 4 and it does equal the parent 4 
loop ends

dequeue = (2,0) = (v,parent)
adjacency list of 2 = [0]
loop through adcancey list of 2
    0 has been visited
    0 does equal parent(0)
loop ends

dequeue = (1,0) = (v,parent)
adjacency list of 1 = [0]
loop through adjacency list of 1
    0 has been visited
    0 does equal parent(0)
loop ends

queue is empty, while loop ends

# no cross edges found
return False

In layman's terms, if we traverse through an array and come across a vertex 
that has connected vertices that have been visited, and if any connected
vertex does not equal the parent of the current vertex, then a cycle has 
been found.

A non cyclic undirected graph:
    when traversed, any unvisited connected vertices are allowed, 
    or a vertex that connects to the parent of the current vertex.

    if a visited vertex is connected to a vertex that is not the parent,
    that is a detection of a cycle. 
    Because then the connected vertex can either be a pointer to itself
    or to a visited vertex that creates a cycle we don't want to find in
    a non-cyclic graph

A non cyclic directed graph:
    When traversed, any unvisted connected vertices are allowed

    if a visited vertex is connected to a vertex that is not unique
    then a cycle has been found.


visited = [True,True,True,False,False,False]
(4,3)
4 => [1,0] = adjacency list
loop through adjacency list of vertex 4 with parent 3


"""

