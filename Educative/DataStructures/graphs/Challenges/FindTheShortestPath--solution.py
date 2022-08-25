"""
Once again, breadth first search comes to the rescue. The visited list must be familiar to you by now.
The crux of this algorithm, however, lies in the distance list. For each node, the indexed value in 
distance shows the node's distance from a in terms of the number of edges where a is the source node.

The rest is a simple BFS traversal where the distance is incremented by 1 each time a node is visited.

We are guaranteed to find the shortest distance to b(desination node) because once it has been visited
it won't visited again through the longer path as it has already been marked.

Time complexity
    The algorithm will have the same time complexity as BFS: O(V+E). However, since we stop it as soon
    as we find b, it won't go through the whole list in the average case.

"""
from Queue import MyQueue
from Graph import Graph

def find_min(g,a,b):    
    num_of_vertices = g.vertices
    visited = [False] * num_of_vertices

    distance = [0] * num_of_vertices

    queue = MyQueue()
    queue.enqueue(a)
    visited[a] = True

    while not queue.is_empty():
        current_node = queue.dequeue()

        adjacent = g.array[current_node].head_node
        while adjacent is not None:
            if not visited[adjacent.data] or adjacent.data is b:
                queue.enqueue(adjacent.data)
                visited[adjacent.data] = True
                distance[adjacent.data] = distance[current_node] + 1
                if adjacent.data is b:
                    return distance[b]
            adjacent = adjacent.next_element
    # end of while
    return -1
