'''
Design an algorithm that computes the successor of a node
in a binary tree. Assume that each node stores its parent.

'''
class TreeNode:
    def __init__(self,val,left,right,parent):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

        
def compute_successor(node:TreeNode):
    # pattern of inorder traversal, left,root,right
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node
    while node.parent and node.parent.right is node:
        node = node.parent
    return node.parent