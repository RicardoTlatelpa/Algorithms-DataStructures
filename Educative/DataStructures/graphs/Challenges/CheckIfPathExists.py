"""
Check if path exists between two vertices

Problem statement:
    You have to implement the check_path() function. It takes a source vertex and a destnation vertex
    and tells us whether or not a path exists between the two.
"""

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

def check_path(g,source,destination):
    visited = [False] * g.vertices
    stack = MyStack()
    stack.push(source)
    visited[source] = True

    while not stack.is_empty():
        p = stack.pop()
        if p == destination:
            return True
        current_node = g.array[p].head_node
        while current_node:
            if visited[current_node.data] is False:
                stack.push(current_node.data)
                visited[current_node.data] = True
            current_node = current_node.next_element
    return False