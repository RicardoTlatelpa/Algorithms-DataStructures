from Graph import Graph
from Stack import MyStack

# Test Graph
g = Graph(6)

g.add_edge(2,3)
g.add_edge(3,1)
g.add_edge(4,1)
g.add_edge(4,0)
g.add_edge(5,0)
g.add_edge(5,2)

def topological_sort_h(source,visited,g):
    stack = MyStack()
    visited[source] = True
    stack.push(source)
    while stack.is_empty() is False:
        vertex = stack.pop()
        current_node = g.array[vertex].head_node
        print("DFS, vertex: ",vertex)
        # traverse adjacent vertices
        while current_node:
            if visited[current_node.data] is False:
                stack.push(current_node.data)
                visited[current_node.data] = True
            current_node = current_node.next_element
    

def topological_sort(graph):    
    numOfVertices = graph.vertices
    visited = [False] * numOfVertices
    for i in range(numOfVertices):
        if visited[i] is False:
            topological_sort_h(i,visited, graph)

#topological_sort(g)

# Geeks for Geeks solution
def tl_sort_rec(g,v,visited,stack):
    visited[v] = True
    # visit all adjacent nodes
    current_node = g.array[v].head_node
    while current_node:
        if visited[current_node.data] == False:
            tl_sort_rec(g,current_node.data,visited,stack)
        current_node = current_node.next_element
    stack.push(v)

def tl_sort(g):
    numOfVertices = g.vertices
    visited = [False]*numOfVertices
    stack = MyStack()

    # iterate through all the vertices that have not been visited
    for i in range(numOfVertices):
        if visited[i] == False:
            tl_sort_rec(g,i,visited,stack)
    
    print(stack.stack_list[::-1])

tl_sort(g)


"""
Topological sort summary
    1.Visiting every vertex that exists in the graph
        2.exhaust adjacent vertices and pass operation to adjacent vertices
            3.Once a vertex is reached where it is exhausted, vertex is added to stack and the recursive call returns 
    4. return reverse stack
    1. Imagine an adjacency list:
    stack = []
    visited = [False,False,False,False,False,False]
    0: Null
    1: Null
    2: 3
    3: 1 
    4: 0
    5: 0 2
    
    We will be visiting every vertex
    0, 1, 2, 3, 4, 5

    2. 
    visited[0] = True
    [True,False,False,False,False,False]
    3.Are the adjacent vertices exhausted?
    For zero yes, so we append to stack and function call ends, 0
    [0]
    visited[1] = True
    [True,True,False,False,False,False]
    3.Are the adjacent vertices exhausted?
    For vertex yes, so we append to stack and function call ends, 1
    [0,1]
    visited[2] = True
    [True,True,True,False,False,False]
    3.Are the adjacent vertices exhausted?
    No, 
        visited[3] = True
        [True,True,True,True,False,False]
        Are the adjacent vertices exhausted?
        No,
            visited[1] has been visited 
        3.adjacent vertex traversal ends
        append to stack, 3
        [0,1,3]
        function call ends
    3.adjacent vertex traversal ends
    append to stack, 2
    [0,1,3,2]
    function call ends

    visited[4] = True
    [True,True,True,True,True,False]
    adjacent traversal begins
        adjacent vertex has been visited
    3.adjacent traversal ends
    append to stack, 4
    [0,1,3,2,4]
    function call ends
    
    visited[5] = True
    [True,True,True,True,True,True]
    Adjacent traversal begins
        adjacent vertices have been visited, no recursive calls
    3.Adjacent traversal ends
    append to stack, 5
    [0,1,3,2,4,5]
    function call ends
    
    4. return reverse stack [0,1,3,2,4,5] = [5,4,2,3,1,0]

"""