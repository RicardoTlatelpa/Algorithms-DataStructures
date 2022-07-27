"""
Find a Mother vertex in a directed Graph
Problem Statement:
    You have to implement the find_mother_vertex() function which will 
    take a directed graph as an input and find out which vertex is the mother
    vertex in the graph.

    By definition, the mother vertex is a vertex in a graph such that all
    other vertices in a graph can be reached by following a path from that
    vertex. A graph can have multiple mother vertices, but you only need to 
    find one.    
"""
from Queue import MyQueue
from Graph import Graph

def all_visited(visited):
    for i in range(len(visited)):
        if visited[i] == False:
            return False
    return True

def bfs_traversal(g,visited,source):
    queue = MyQueue()
    queue.enqueue(source)
    visited[source] = True
    while queue.is_empty() is False:
        p = queue.dequeue()
        current_node = g.array[p].head_node
        while current_node:
            if not visited[current_node.data]:
                queue.enqueue(current_node.data)
                visited[current_node.data] = True
            current_node = current_node.next_element

    return visited

def find_mother_vertex(g):
    for i in range(g.vertices):
        visited_ = bfs_traversal(g,[False]*g.vertices,i)
        if all_visited(visited_):
            return i
    return -1