# MY solution; passed all test cases
from Graph import Graph
from Queue import MyQueue

def is_tree_helper(g,visited,source):
    queue = MyQueue()
    visited[source] = True
    queue.enqueue((source,-1))

    while queue.is_empty() is False:
        (v,parent) = queue.deqeue()
        connected_vertex = g.array[v].head_node
        while connected_vertex:
            if visited[connected_vertex.data] is False:
                visited[connected_vertex.data] = True
                queue.enqueue(connected_vertex.data)
            elif connected_vertex.data != parent:
                # We found a connected visited vertex that is not a parent -> cycle found
                return True
            connected_vertex = connected_vertex.next_element
    # no cycle found after traversal
    return False


def is_tree(g):
    visited = [False] * g.vertices

    if is_tree_helper(g,visited,0):
        return False
    for i in range(len(visited)):
        if visited[i] == False:
            return False
    return True

"""
Time Complexity
    O(V + E), same as BFS or DFS algorithms.
"""