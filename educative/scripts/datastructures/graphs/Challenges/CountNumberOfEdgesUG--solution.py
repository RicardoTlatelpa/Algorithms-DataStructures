from Graph import Graph
# We only need Graph for this Question!


def num_edges(g):
    # For undirected graph, just sum up the size of
    # all the adjacency lists for each vertex
    sum = 0
    for i in range(g.vertices):
        temp = g.array[i].head_node
        while temp is not None:
            sum += 1
            temp = temp.next_element

    # Half the total sum as it an undirected graph
    return sum//2 


"""
Nothing too tricky going on here. We simply traverse through the complete adjacency list and count the 
size of each linked list. In an undirected graph, the number of edges is always even as the edges
are bidirectional. Hence, to get the number of bidirectional edges, we half the total sum.

Time complexity:

O(V + E)
"""