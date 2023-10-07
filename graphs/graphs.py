'''
Graph Fun Facts:
    Connected graphs have at least n-1 edges
'''
graph = {
    0: [1,5],
    1: [0,2],    
}

def dfs(start_vertex,visited):
    def f(v,visited):
        if visited[v] == False:
            visited[v] = True
            print(v,end=' ')
            for adj_v in graph[v]:
                f(adj_v, visited)
    f(start_vertex,visited)

def bfs(start_vertex):
    visited = [False] * len(graph)
    queue = [start_vertex]

    while(queue):
        popped_vertex = queue.pop(0)
        '''
        instead of popping from the end of the array
        we're going to pop from the start of the array
        '''
        if visited[popped_vertex] != True:
            visited[popped_vertex] = True
            print(popped_vertex, end=' ')
            for adj_vertex in graph[popped_vertex]:
                queue.append(adj_vertex)

def countComponents(graph):
    visited = [False] * len(graph)
    count = 0
    for v in graph:
        if visited[v] == False:
            dfs(v,visited)
            count +=1
    return count

def cycleDFS(graph):
    visited = [False] * len(graph)
    def detectCycle(v, parent_v):
        if visited[v] == False:
            visited[v] = True
            for adj_v in graph[v]:
                if visited[adj_v] == False:
                    if detectCycle(adj_v, v):
                        return True
                elif adj_v != parent_v:
                    return True
        return False
    for v in graph:
        if visited[v] == False:
            if detectCycle(v,-1) == True:
                return True
    return False

print(cycleDFS(graph))

def cycleBFS(graph,starting_vertex):
    visited = [False] * len(graph)
    q = [(starting_vertex,-1)]
    while(q):
        vertex, parent = q.pop(0)
        if visited[vertex] != True:
            visited[vertex] = True
            for adj_vertex in graph[vertex]:
                if visited[adj_vertex] == False:
                    q.append((adj_vertex, vertex))
                else:
                    if adj_vertex != parent:
                        return True
    return False

#print(cycleBFS(graph,0))