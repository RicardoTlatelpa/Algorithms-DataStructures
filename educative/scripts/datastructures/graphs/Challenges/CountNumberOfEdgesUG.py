from Graph import Graph
from Queue import MyQueue
from Stack import MyStack
# You can check the input graph in console tab

# Create Stack => stack = MyStack()
# Functions of Stack => push(int), pop(), top(), is_empty()
# Create Queue => queue = MyQueue()
# Functions of Queue => enqueue(int), dequeue(), size(), front(), is_empty()
# class Graph => {int vertices, linkedList[] array}
# class linkedList => {Node head_node}
# class Node => {int data, Node next_element}

def num_edges_helper(g,source,unique_pairs,visited):
    current_node = g.array[source].head_node
    visited[source] = True
    while current_node:
        tmp = [source]
        if current_node.data != source and visited[current_node.data] == False:
            tmp.append(current_node.data)
            if tmp not in unique_pairs and len(tmp) > 1:
                unique_pairs.append(tmp)
        current_node = current_node.next_element

def num_edges(g):
    visited = [False] * g.vertices
    unique_pairs = []
    for i in range(g.vertices):
        num_edges_helper(g,i,unique_pairs,visited)
    return len(unique_pairs)