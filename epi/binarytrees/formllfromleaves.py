'''
9.14

Given a binary tree, commpute a linked list from the leaves of the binary tree. The leaves
should apppear in left-to-right order. For example,when applied to the binary tree in figure 
9.1 on page 112, your function should return D,E,H,M,N,P
'''

class TreeNode:
    def __init__(self,val,left,right):
        self.val = val
        self.left = left
        self.right = right

def create_ll(tree):
    
