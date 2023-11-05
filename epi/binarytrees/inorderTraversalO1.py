'''
Write a nonrecursive program for computing the inorder traversal
sequence for a binary tree. Assume nodes have parent fields
'''


class TreeNode:
    def __init__(self,parent,data,left,right):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right

def inorderTraversal(root:TreeNode):    
    previnorder = None
    inorder = root
    while(inorder):    
        if inorder.left:            
            previnorder = inorder
            inorder = inorder.left
        else:
            print(inorder.data)
            previnorder = inorder
            inorder = inorder.parent
            if inorder.right and inorder.right != previnorder:
                inorder = inorder.right

def inorder_traversal(tree:TreeNode):
    prev,result = None, []
    while tree:
        if prev is tree.parent:
            if tree.left:
                next = tree.left
            else:
                result.append(tree.data)
                next = tree.right or tree.parent
        elif tree.left is prev:
            result.append(tree.data)
            next = tree.right or tree.parent
        else:
            next = tree.parent
        prev,tree = tree,next
    return result