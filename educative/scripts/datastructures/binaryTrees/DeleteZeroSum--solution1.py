"""
For the solution to this challenge, we do a post order traversal of the binary tree.
Here are the steps we follow for our post-order traversal algorithm:
    - Traverse the left sub tree by recursively calling the post-order function.
    - Traverse the right sub-tree by recursively calling the post-order function.
    - If the current node's left or right sub-tree reports a sum of zero, we delete that sub-tree.
    - If the root node returns zero, then we delete the entire tree.
"""
from binary_tree import *
from binary_tree_node import *

# Recursive function to remove any zero sum sub-trees

def delete_zero_sum_subtree_rec(root):
    if not root:
        return 0
    sum_left = delete_zero_sum_subtree_rec(root.left)
    sum_right = delete_zero_sum_subtree_rec(root.right)

    if sum_left == 0:
        root.left = None
    
    if sum_right == 0:
        root.right = None
    
    return (root.data + sum_left + sum_right)

def delete_zero_sub_subtree(tree):
    if not tree or not tree.root:
        return
    
    tree_sum = delete_zero_sum_subtree_rec(tree.root)
    # if the whole tree sums up to zero then delete the whole tree
    if tree_sum == 0:
        tree.root = None

"""
Time Complexity
    The time complexity of this solution is linear, O(N).
Space complexity
    The space complexity of this solution is O(H) because our recursive
    algorithm uses up space on the call stack, which can grow to the height
    h of the binary tree. The complexity will be O(logN) for a balanced tree
    and O(N) for a degenerate tree.
"""