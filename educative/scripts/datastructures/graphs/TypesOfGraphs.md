# Types of Graphs
There are two common types of graphs:
1. Undirected 
2. Directed
   
# Undirected Graph
In an undirected graph, the edges are bi-directional. For e.g., an ordered pair(2,3) shows that there exists an edge between vertex 2 and 3 without any specific direction. You can go from vertex 2 to 3 or from 3 to 2.

Let's calculate the maximum number of edges for an undirected graph. We are denoting an edge between vertex a and b as (a,b). So, the maximum possible edges of a graph with n vertices will be all possible pairs of vertices of that graph, assuming that there are no self-loops.

If a graph has n vertices, then there are C(n,2) possible pairs of vertices according to Combinatorics. Solving C(n,2) by binomial coefficients gives us n(n-1)/2. Hence, there are n(n-1)/2 maximum possible edges in an undirected graph.

