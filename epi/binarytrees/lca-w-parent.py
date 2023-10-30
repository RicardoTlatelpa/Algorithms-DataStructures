'''
Find the lowest common ancestor with
parent pointers on each node.
'''

class TreeNode:
    def __init__(self,val,parent,left,right):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right
'''
If we have pointers to the parent
we can just traverse and find the nodes

1. Find the nodes
2. Balance their heights
3. traverse up their parent pointers until they're equal
4. return the equal TreeNode


'''   

def lca_(root,node0,node1):
    n0,n1 = None,None

    def dfs(root,height):
        nonlocal n0,n1
        if root is None:
            return
        if root == node0:
            n0 = (root,int(height))
        if root == node1:
            n1 = (root,int(height))
        dfs(root.left,height+1)
        dfs(root.right,height+1)

    dfs(root,0)

    if n0 == None or n1 == None:
        return -1 # ancestor cannot exist
    
    while(n0[1] != n1[1]):
        if n0[1] > n1[1]:
            n0[0] = n0[0].parent
            n0[1]-=1
        if n1[1] > n0[1]:
            n1[0] = n1[0].parent
            n1[1]-=1
    while(n0[0] != n1[0]):
        n0[0] = n0[0].parent
        n1[0] = n1[0].parent
    return n0[0]
