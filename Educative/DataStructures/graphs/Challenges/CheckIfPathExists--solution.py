from more_itertools import adjacent
from Graph import Graph
from Queue import MyQueue
# We only need Graph and Queue for this Question!

def check_path(g,source,dest):
    # BFS to check path between source and dest
    # Keep track of visited vertices
    visited = [False] * (g.vertices)
    
    # Create a queue for BFS
    queue = MyQueue()

    # Enque source and mark it as visited
    queue.enqueue(source)
    visited[source] = True

    # Loop to traverse the whole graph using BFS
    while not queue.is_empty():
        node = queue.deqeue()
        if node is dest:
            return True

        adjacent = g.array[node].head_node
        while adjacent:
            # enqueue adjacent node if it has not been visited
            if not visited[adjacent.data]:
                queue.enqueue(adjacent.data)
                visited[adjacent.data] = True
            adjacent = adjacent.next_element
            
    # Destionation was not found in the search
    return False


"""
This problem can be solved by both DFS and BFS. All we need is a simple traversal 
from source to see if we can reach dest. If the dest value is found, we return True.

Note that we only use the values in the vertices, not the vertices or the linked list objects
themselves. This makes the syntax easier.

Time complexity
    It has the same time complexity as the BFS or DFS algorith: O(V+E)
"""