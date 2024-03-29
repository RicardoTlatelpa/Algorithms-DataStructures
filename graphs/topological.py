#Python program to print topological sorting of a DAG
from collections import defaultdict

#Class to represent a graph
class Graph:
	def __init__(self,vertices):
		self.graph = defaultdict(list) #dictionary containing adjacency List
		self.V = vertices #No. of vertices

	# function to add an edge to graph
	def addEdge(self,u,v):
		self.graph[u].append(v)

	# A recursive function used by topologicalSort
	def topologicalSortUtil(self,v,visited,stack):

		# Mark the current node as visited.
		visited[v] = True

		# Recur for all the vertices adjacent to this vertex
		for i in self.graph[v]:
			if visited[i] == False:
				self.topologicalSortUtil(i,visited,stack)

		# Push current vertex to stack which stores result
		stack.insert(0,v)

	# The function to do Topological Sort. It uses recursive
	# topologicalSortUtil()
	def topologicalSort(self):
		# Mark all the vertices as not visited
		visited = [False]*self.V
		stack =[]

		# Call the recursive helper function to store Topological
		# Sort starting from all vertices one by one
		for i in range(self.V):
			if visited[i] == False:
				self.topologicalSortUtil(i,visited,stack)

		# Print contents of stack
		print (stack)
        
	def viewGraph(self):
		for i in range(self.V):
			print(i, end= ": ")
			for j in self.graph[i]:
				print(j,end=" ")
			print('')
g= Graph(9)
g.addEdge(0, 1);
g.addEdge(0, 4);
g.addEdge(0, 2);
g.addEdge(1, 4);
g.addEdge(1, 3);
g.addEdge(2, 7);
g.addEdge(2, 5);
g.addEdge(3, 6);
g.addEdge(4, 6);
g.addEdge(4, 7);
g.addEdge(4, 8);
g.addEdge(5, 7);
g.addEdge(6, 8);
g.addEdge(7, 8);




g.viewGraph()
print ("Following is a Topological Sort of the given graph")
g.topologicalSort()
#This code is contributed by Neelam Yadav

