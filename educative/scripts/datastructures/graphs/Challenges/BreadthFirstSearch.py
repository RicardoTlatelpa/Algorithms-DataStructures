"""
Problem Statement
    You have to implement the Breadth First Search traversal. We have already covered the logic behind this algorith.
    All that's left to do is to flesh it out in code.
    To solve this problem, all the previously implemented data structures will be available to us.

    Input
        A directed graph in the form an adjacnecy list and integer indicating the starting vertex number.

    Output 
        A string containing the vertices of the graph listed in the correct order of traversal.
"""

from Graph import Graph
from Queue import MyQueue

# Create Queue => queue = MyQueue()
# Functions of Queue => enqueue(int), dequeue(), size(), front(), is_empty()
# Create Stack => stack = MyStack()

# Breadth First Traversal of Graph g from source vertex
def bfs_traversal_helper(g, source, visited):
    result = ""
    # Create Queue(implemented in previous lesson) for Breadth First Traversal
    # and enqueue source in it
    queue = MyQueue()
    queue.enqueue(source)
    visited[source] == True # Mark as visited

    while not queue.is_empty():
        # Dequeue a vertex/node from queue and add it to result
        current_node = queue.deqeue()
        result += str(current_node)
        # Get adjacent vertices to the current_node from the list,
        # and if they are not already visited then enqueue them in the Queue
        temp = g.array[current_node].head_node
        while temp is not None:
            if not visited[temp.data]:
                queue.enqueue(temp.data)
                visited[temp.data] = True # Visit the current Node
            temp = temp.next_element
    
    return result, visited


def bfs_traversal(g,source):
    result = ""
    #queue = MyQueue()
    num_of_vertices = g.vertices

    if num_of_vertices is 0:
        return result
    # A list to hold the history of visited nodes
    # Make a node visisted whenver you enqueue it into queue
    visited = []
    for i in range(num_of_vertices):
        visited.append(False)
    # Start from source
    result, visited = bfs_traversal_helper(g, source, visited)
    # visit remaining nodes
    for i in range(num_of_vertices):
        if not visited[i]:
            result_new, visited = bfs_traversal_helper(g,i,visited)
            result += result_new
    return result


"""
Solution: Using Queues

For this solution, we will use the queue data structure that we studied earlier. bfs_traversal 
calls the helper function bfs_traversal_helper on every vertex which is not visited. Starting
from the source vertext which is 0, we insert the vertex into the queue. To keep track of where
we have already traversed, every vertex inserted into the queue is marked visisted in the 
visited list.

The result string will be our returning variable. The value of a node is appended to result when it 
is dequeued from the queue. For each node that is dequeued, its adjacent nodes are added to the queue 
if they have not been visited.

The first in first out structure of the queue ensures that the graph is traversed one level at a time.

Time Complexity

Since this algorithm traverses the whole graph once, its time complexity is O(V + E).
"""