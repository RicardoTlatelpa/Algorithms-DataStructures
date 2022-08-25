from binary_tree import *
from binary_tree_node import *
"""
Statement
    Given the root node of a binary tree, swap the left and right children for each node
"""
# PASSES ALL TEST CASES
def mirror_helper(root):
    if root == None:
        return
    # swap
    tmp = root.right
    root.right = root.left
    root.left = tmp
    #traverse through binary tree until exhausted, in level order
    mirror_helper(root.left)
    mirror_helper(root.right)

def mirror_binary_tree(root):
    if root == None:
        return
    mirror_helper(root)
    return root
