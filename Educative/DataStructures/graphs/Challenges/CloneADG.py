"""
Clone a Directed Graph

Statement
    Given the root node of a directed graph, clone this graph by creating its deep copy, such that
    the cloned graph has the same vertices and edges as the original graph.

Example:
    Let's look at the graphs below as an example. If the input graph is G = (V,E) where is a set
    of vertices and E is a set of edges, then the output graph (the cloned graph) is G' = (V', E')
    such that V = V' and E = E'.

**We assume that all vertices are reachable from the root vertex, i.e., we have a connected graph.**

The data we're working with
the graph is just a list of nodes 
Each node has memory of its neighbors 

so in order to traverse through the entire tree, we have to iterate through the vertices
and then iterate through its neighbors

The algorithm at each unexplored vertex, creates a new Node of the current Vertex
and then traverses through its children, looking for the new memory allocated vertex object in the hashtable
if that vertex object is not found in the hashtable, a neighbor is appended recursively

else:
    its newly memory allocated object is appended without any recursive action because that vertex has been explored

"""


from directed_graph import *

def clone_rec(root, nodes_completed, graph):
    if root is None:
        return None
    cloned_vertex = Node(root.data)
    nodes_completed[root] = cloned_vertex

    graph.add_vertex_in_nodes(cloned_vertex)
    # traverse through the original node's neighbors
    # append existing clone to neighbor list
    # else append the the vertex
    for neighbor in root.neighbors:
        existing_clone = nodes_completed.get(neighbor)
        if existing_clone:
            cloned_vertex.neighbors.append(existing_clone)
        else:
            cloned_vertex.neighbors.append(clone_rec(neighbor,nodes_completed,graph))
    
    return cloned_vertex

        

def clone(graph):
    nodes_completed = {}
    clone_graph = DirectedGraph()
    if graph.nodes is None:
        return None
    else:
        clone_rec(graph[0], nodes_completed, graph)
    return clone_graph
