"""
Minimum Spanning Tree
    Find the minimum spanning tree of a connected, undirected graph with weighted edges.

Input will be a graph of the form:
    v = 5 
    e = [
        [1,2,1],
        [1,3,1],
        [2,3,2],
        [2,4,3],
        [3,5,3],
        [4,5,2]
    ]

Where v is the number of edges, and e is the set of weighted edges. Each edge is coded
as follows: [source,destination,weight]. Thus, if an edge is coded as [2,4,3], it means
that it goes from node 2 to node 4 and has a weight of 3.

Note: As we consider undirected graphs, the edges are bidirectional.

A minimum spanning tree or minimum weight spanning tree is a subset of the edges of a connected, edge-weighted
undirected graph that connects all the vertices together, without any cycles and with the minimum possible
total edge weight. That is, it is a spanning tree whose sum of edge weight is as small as possible.

More generally, any edge weighted undirected graph (not necessarily connected) has a minimum spanning forest,
which is a union of the minimum spanning trees for its connected components.

So for the given graph I can do breadth first search:

# avoids any loops
visited = {


}

destination is key and its value is [source,destination,weight]

# stores unique minimum edges, no loops
minimum_edges = [None,None,None,None,None] # where each idx is the destination

in order to store correctly, take destination and subtract one to find proper place in list

queue = [[1,2,1]]
    while my queue is not empty
        vertiex,destination,weight = queue.dequeue() // [1,2,1]

"""
