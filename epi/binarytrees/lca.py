'''
Lowest common ancestor

1. Look for both nodes
2. Find their height and parents
3. found_node1, found_node2 => bring them to equal height
4. go up the parent nodes until similar parent found


'''

def lca(root,node0,node1):
    ht = {}
    def trackPaths(root,path):
        if root is None:
            return None
        if root == node0:
            # make a copy of the path
            ht[node0.val] = list(path)
        if root == node1:
            # make a copy of the path
            ht[node1.val] = list(path)
        
        path.append(root.val)
        trackPaths(root.left,path)
        path.pop()
        path.append(root.val)
        trackPaths(root.right,path)
        path.pop()

    trackPaths(root,[])
    path0,path1 = ht[node0.val],ht[node1.val]

    if len(path0) == 0 or len(path1) == 0:
        return -1 # no common lca
    while(len(path0) != len(path1)):
        if len(path0) > len(path1):
            path0.pop()
        if len(path1) > len(path0):
            path1.pop()
    
    while(path0 and path1):
        p0, p1 = path0.pop(), path1.pop()
        if p0 == p1:
            return p0


