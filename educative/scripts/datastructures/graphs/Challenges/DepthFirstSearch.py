from Stack import MyStack
from Graph import Graph

def dfs_traversal_helper(g,source,visited):
    result = "" # result string that we want as the end result
    stack = MyStack() # Stack datastructure for depth first search traversal
    # Since the source node is being added to stack, we can say it's visited
    stack.push(source)
    visited[source] = True
    while stack.is_empty() is not True:
        p = stack.pop()
        # popped off values are added to result string
        result += str(p)
        # iterate through linked list(children) of node we removed
        # If there are any
        current_node = g.array[p].head_node
        while current_node:
            # Every node we come across in the linked list will be visited
            # and added to stack for further traversal of graph
            # Make sure we only iterate through unvisited nodes
            if visited[current_node.data] is False:
                stack.push(current_node.data)
                visited[current_node.data] = True
            current_node = current_node.next_element

    return result,visited


def dfs_traversal(g,source):
    result = ""
    visited = [] #list tracking visited nodes in graph
    # Initialize visited list, False representing nodes have not been visited
    for i in range(g.vertices):
        visited[i] = False
    
    # First call to dfs_traversal_helper, updates result and visited values
    result,visited = dfs_traversal_helper(g,source,visited)

    # Iterate through rest of vertices in graph, only non visited

    for i in range(g.vertices):
        if visited[i] is False:
            result_new, visited = dfs_traversal_helper(g,i,visited)
            result += result_new

    return result

"""
The approach is verys imilar ot that of the BFS solution. However, instead
of a queue, we use a stack since it follows the last in first out approach.
We will see how that is useful here.

dfs_traversal calls the helper function dfs_traversal_helper on every vertex
which is not visited. Starting from source which is 1, each node is pushed 
into the stack. Whenever a node is popped, it is added to the result. Nodes
are marked visited whenever they are pushed. Now we can understand why we need
the stack because it keeps popping out the new adjacent nodes(gives you a node
at a new level) instead of returning the previous nodes that we pushed in.

Time complexity
Like the BFS, this algorithm traverse the whole list once. Hence, it's 
time complexity is O(V+E)
"""