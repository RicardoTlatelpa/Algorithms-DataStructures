# What is a Graph?

When we talk about graphs, whast comes to mind are the conventional graphs used to visualize data. In computer science, the term "graph" has a completely different meaning. It is a data structure used to store and manipulate data.

The graph data structure plays a fundamental role in several applications such as GPS, neural networks, peer-to-peer networks, search engine crawlers, garbage collection (Python), and even social networking websites.

# Graph Structure
A graph is a set of nodes that are connected to each other in the form of a network. First of all, we'll defined the two basic components of a graph.

## Vertex
A vertex is the most essential part of a graph. A collection of vertices forms a graph. In that sense, vertices are similar to linked list nodes.

## Edge
An edge is the link between two vertices. It can be uni-directional or bi-directional depending on your graph. An edge can also have a cost assocated with it(will be discussed in detail later).

# Graph Terminologies
1. Degree of a Vertex: the total number of edges incident on a vertex. There are two types of degrees:
   1. In-degree: the total number of incoming edges of a vertex.
   2. Out-degree: the total number of outgoing edges of a vertex.
2. Parallel Edges: Two unidirected edges are parallel if they have the same end vertices. Two directed edges are parallel if they have the same starting and ending vertices.
3. Self Loop: This occurs when an edge starts and ends on the same vertex.
4. Adjacency: Two vertices are said to be adjacent if there is an edge connecting them directly.

# Representation of Graphs

## Ways to represent a Graph
The two most common ways to represent a graph are:
1. Adjacency Matrix
2. Adjanceny List

## Adjacency Matrix
The adjacency matrix is a two-dimensional matrix where each cell can contain a 0 or 1. If a cell contains 1 there exists an edge between the corresponding vertices e.g,m Matrix[0][1] = 1 shows that an edge exists between vertex 0 and 1. the row and column headings represent the vertices.

In the image, there is a directed graph that has an edge going from vertex 0 to vertex 1, so there is a 1 at Matrix[0][1] in the adjacency matrix. In the case of the unidirected graph, we would have Matrix[1][0] = 1 as well since the edge is bidirectional.
For a directed graph, the usual convention is to think of the rows as sources and the columns as destinations.

For a directed graph, the usual convention is to think of the rows as sources and the columns as destinations.

## Adjancency List

An array of linked lists is used to store all the edges in the graph. The size of the array is equal to the number of vertices in the graph. Each index of the array contains a vertext. This vertex point to a linked list that contains all the vertices connected to this one.

If a new vertex is added to the graph, it is simply added to the array as well.

Note: in an undirected graph an edge is represented with both adjacent nodes having their linked list populated with the corresponding nodes.