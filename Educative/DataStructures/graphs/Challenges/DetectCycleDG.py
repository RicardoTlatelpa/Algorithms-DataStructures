"""
Problem statement:
The concept of loops or cycles is very common in graph theory. A cycle
exists when you traverse the directed graph and come upon a vertext that
has already been visisted.

You have to implement the detect_cycle function which tells you whether or not
a graph contains a cycle.

graph = {
    0 -> 1
    1 -> 2
    2 -> 0
}
[False,False,False]
[True,False,False]
[True,True,False]

If a child is already visited and is not the head node, then there is a loop, return false
"""
from Queue import MyQueue
from Graph import Graph

def bfs_traversal_helper(g,source,visited):
    result = False
    queue = MyQueue()
    queue.enqueue(source)
    visited[source] = True
    while queue.is_empty() is False:
        p = queue.deqeue()
        current_node = g.array[source].head_node
        while current_node:
            if visited[current_node.data] == False:
                queue.enqueue(current_node.data)
                visited[current_node.data] = True
            if visited[current_node.data] == True and current_node.data != source:
                # found loop
                result = True
            current_node = current_node.next_element

    return result, visited

def detect_cycle(g):
    result = False
    visited = []
    for i in range(g.vertices):
        visited[i] = False
    # Starting vertex is the 0th vertex
    result, visited = bfs_traversal_helper(g,0,visited)
    if result is True:
        return True
    for i in range(1,g.vertices):
        result,visited = bfs_traversal_helper(g,i,visited)
        if result is True:
            return True
    return result
    