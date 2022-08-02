"""
Solution
    A spanning tree of a connected, undirected graph is a subgraph that is a tree and connects all the vertices.
    One graph can have many different spanning trees. A graph with n vertices has a spanning tree with n - 1 edges.

    A weight can be assigned to each edge of the graph. The weight of a spanning tree is the sum of weight of all 
    the edges of the spanning tree. A minimum spanning tree (MST) for a connected, weighted, and an undirected
    graph is a spanning tree with a weight less than or equal to the weight of every other spanning tree.

    We find the minimum spanning treee of a graph using Prim's algorithm. This algorithm builds the tree one vertex
    at a time, starting from any arbitrary vertex. At each step, it adds the minimum weight edge from the constructed
    tree to a vertex from the remaining vertices of the input graph.

    The algorithm is as follows:
        1. Initialize the MST with an arbitrary vertex from the graph
        2. Find the edge with the minimum weight from the constructed graph
        3. Add that edge and vertex to the MST
        4. Repeat steps 2-3 until alll the vertices have added to the MST
    
    The time complexity to find the minimum weight edge is O(N^2). However, it can be improved further by 
    using heaps to find the minimum weight edge.

    Let's take an example graph and find its minimum spanning tree using the above algorithm:
"""


def find_min_spanning_tree(graph):
    graphMST = Graph([],[])

    vertex_count = 0
    current = graph.g[0]
    current.visited = True
    vertex_count += 1

    #Iterate over all vertices because MST should contain all vertices
    while vertex_count < len(graph.g):
        smallest = None
        # iterate over edges
        # Pick an edge which is not visited and has minimum weight
        for i in range(len(graph.e)):
            if graph.e[i].visited == False:
                if graph.e[i].src.visited and graph.e[i].dest.visited == False:
                    if smallest == None or graph.e[i].weight < smallest.weight:
                        smallest = graph.e[i]
        smallest.visited = True
        smallest.dest.visited = True
        vertex_count += 1

        # Construct the remaining MST using the smallest weight edge
        # populate the edges of mst
        if smallest:
            graphMST.e.append(Edge(smallest,weight,smallest,visited,smallest.src, smallest.dest))
    return graphMST
