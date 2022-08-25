from directed_graph import *

def clone_rec(root,graph,nodes_completed):
    if not root:
        return None
    
    # Creating new vertex/node
    pNew = Node(root.data)
    
    # Using hashmap to keep track of visited nodes
    nodes_completed[root] = pNew
    
    # Adding new vertex in the graph
    graph.add_vertex_in_nodes(pNew)
    
    # Iterate over each neighbor of the current vertex/node
    for p in root.neighbors:
        x = nodes_completed.get(p)
        if not x:
            # If node is not visited call recursive function to create vertex
            pNew.neighbors.append(clone_rec(p,graph,nodes_completed))
        else:
            # If not is visited just add it to neighbors of current vertex
            pNew.neighbors.append(x)
    
    return pNew

def clone(graph):
    # Hashmap to keep record of visited nodes
    nodes_completed = {}

    # Creating new graph
    clone_graph = DirectedGraph()

    if not graph.nodes:
        return None
    else:
        clone_rec(graph.nodes[0], clone_graph, nodes_completed)

    # return deep copied graph
    return clone_graph

"""
Solution
    We use depth-first traversal and create a copy of each node while traversing the graph. 
    To avoid getting stuck in cycles, we use a hashtable to store each visited node. And we
    do not revisit nodes that exist in the hashtable. The hashtable key is a node in the 
    original graphm and its value is the corresponding node in the cloned graph.

    For the above graph, let's assume the root is node 0. So, we'll start with 0.

    We will start our traversal from node 0
    We will create a new node 0 and add the
    entry(0,0') in the hashtable

    Now we'll move to the first neighbor of 0
    node 2. We'll create a new node 2', and add
    entry (2,2') in hashtable. 2 has only one 
    neighbor 0 which is already in hashtable,
    so it will be skipped in this step.

    No we'll move on to 2nd neighbor of node 0
    node 3. We'll create a new node 3', and add
    entry (3,3') in hashtable. 3 has only one 
    neighbor2 which is already in hashtable, so it will
    be skipped in this step.

    No we'll move on to 3rd neighbor of node 0
    node 4. We'll create a new node 4', and add 
    entry (4,4') in hashtable. 4 has three neigh-
    -bors {0,1,3}. Nodes 0 and 3 are already in hashtable,
    so they will be skipped. However node 1 is still not 
    in hashtable.

    Now we'll move to node 1 which is neighbor of 4.
    We'll create a new node 1'. Only neighbor of this
    node is node 2 which is already in hashtable.

Time Complexity
    The time complexity of this solution is linear, O(N).

Space Complexity
    The space complexity of this solution is linear, O(N) where n is
    the number of vertices in the graph.

    **We can have at most n entries in the hash table, so the worst-case
    space complexity is O(N)**

"""