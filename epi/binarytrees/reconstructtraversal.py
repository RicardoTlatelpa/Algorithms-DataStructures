'''
Given an inorder traversal sequence and a preorder traversal sequence of a binary tree
write a program to reconstruct the tree. Assume each node has a unique key.
'''

'''
inorder traversal we can always assume the left exhaust and then visit the right node

F,B,A,E,H,C,D,I,G

preorder traversal we can always assume we're exploring left then right
using a stack

H,B,F,E,A,C,D,G,I
'''


def binary_tree_from_preorder_inorder(preorder,inorder):
    
