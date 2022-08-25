"""
Problem statement:
    Implement the find_min() function which will take a directed graph and two vertices, A and B. The
    result will be the shortest path from A to B.

    Remember, the shortest path will contain the minimum number of edges.

Input:
    A directed graph, a Avert A and a vertex B
Output:
    Returns number of edges in the shortest path between A and B.


Pseudocode:
    - Use a Queue data structure for Breadth First Search algorithm
    - While traversing through the adjacent vertices
        -keep track of every level with a flagNode
            -only increment level when flag node is in the front of the queue
        -when destination is found, return currentLevel
        -else continue traversing, if front is flagNode, dequeue flagNode and add to back of queue

I saw the graph and every vertex's adjacent vertices as next levels, and keep track of these 
levels will give me an accurate level of where the destination was found, if the destination
can be found in the graph.
"""
from Graph import Graph
from Queue import MyQueue
from Node import Node

def find_min_helper(g,source,destination,visited):
    current_level = 0 
    queue = MyQueue()
    visited[source] = True
    flagNode = Node(None)
    
    queue.enqueue(source)
    queue.enqueue(flagNode)
    while queue.is_empty() is False:
        vertex = queue.deqeue()
        
        # Do not dequeue yet, until we added adjacent vertices to queue
        if queue.front() is flagNode: 
            current_level += 1
        
        # traverse through connected vertices (adjacent)
        connected_vertex = g.array[vertex].head_node
        while connected_vertex:
            if connected_vertex.data == destination:
                return current_level
            if visited[connected_vertex.data] == False:
                visited[connected_vertex.data] = True
                queue.enqueue(connected_vertex.data)
            connected_vertex = connected_vertex.next_element
        current_level += 1
        
        # set flagNode for accurate current level tracker
        if queue.front() is flagNode:
            queue.deqeue()
            queue.enqueue(flagNode)
    return -1 # after BFS, if destination was never found, return -1    

def find_min(g,source,destination):
    visited = [False] * g.vertices
    return find_min_helper(g,source,destination,visited)
