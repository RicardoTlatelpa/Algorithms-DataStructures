"""
Given a binary tree, delete any sub-trees whose nodes sum up to zero.

So we have to find a subtree that adds up to zero

What is a sub tree?
    A subtree is a grouping of a tree that shares a connection together

We can traverse through the tree in level order, and each node that we traverse we can run 
a traversal that sums up itself and its children (sub tree), if the sum is zero
we delete all the children and then the root of the subtree node

deleting the sub tree, I can take advantage of the deletion in a binary tree and delete 
"""
from binary_tree import *
from binary_tree_node import *

def delete_zero_sub_subtree(tree):
    if not tree or not tree.root:
        return
    
