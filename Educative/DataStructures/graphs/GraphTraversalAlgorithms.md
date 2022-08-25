# Graph Traversal Algorithms

# Types of graph traversals

Graph traversal means visiting every vertex in the graph. There are two basic techniques used for graph traversal:

1. Breadth First Search (BFS)
2. Depth First Search (DFS)

In order to understand these algorithms, we will have to view graphs from a slightly different perspective.
Any traversal needs a starting point, but a graph does not have a linear structure like lists or stacks. So how do we give graph traversal a better sense of direction?
This is where the concept of levels is introduced. Take any vertex as the starting point. This is the lowest level in your search. The next level consists of all the vertices adjacent to the starting vertex. A level higher would mean the vertices adjacent to the nodes at the lower level.
With this is in mind, let's begin our discussion on the two graph traversal algorithms.


1. Breadth First search
   1. The BFS algorithm earns its name because it grows breadth-wise. All the nodes at a certain level are traversed before moving on to the next level. 
   2. The level wise expansion ensures that for any starting vertex, you can reach all others, one level at a time.
   
2. Depth first traversal
   1. The DFS algorithm is the opposite of BFS in the sense that it grows depth-wise
   2. Starting from any node, we keep moving to an adjacent node until we reach the farthest level. Then we move back to the starting point and pick another adjacent node. Once again, we prove to the farthest level and move back. This process continues until all nodes are visisted.



