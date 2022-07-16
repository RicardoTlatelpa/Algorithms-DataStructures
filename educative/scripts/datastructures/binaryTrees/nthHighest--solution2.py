"""
Solution 2 from educative

If each node in the BST has a tally of the total number of nodes in its sub tree, we can find the nth highest 
node in a non linear way. We have already sorted this tally for you in the count member of each node.


Here is the same BST used in the above example with counts populated:

The basic pseudocode to find the nth hgihest number nodes, using the count member, is as follows:

start at the root node.
initialize a variable k, where k = current node count - left subtree's node count.

if k equals n then
    node is the nth highest
if k is greater than n then 
    nth highest node eexists in right subtree so find nth node in right subtree
if k is less than n then
    nth highest node exists in left subtree so deduce k from n and find (n-k)th node in the left subtree
"""

from binary_tree import *
from binary_tree_node import *


def find_nth_highest_in_bst(root,n):
    if not root:
        return None
    left_count = 0

    if root.left:
        left_count = root.left.count

    k = root.count - left_count

    if k == n:
        return root
    elif k > n:
        return find_nth_highest_in_bst(root.right, n)
    else:
        return find_nth_highest_in_bst(root.left, n - k)
        
