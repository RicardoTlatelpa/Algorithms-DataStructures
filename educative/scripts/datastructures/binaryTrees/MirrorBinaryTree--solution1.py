from binary_tree import *
from binary_tree_node import *

"""
Solution from educative
    For this solution, we do a post-order(left,right,parent)
    traversal of the binary tree. The algorithm is as follows:
        - Start at the root node
        - Perform a post-order traversal of the binary tree
        - On every node during the traversal, we swap its 
        left child with its right child
    Since we perform a depth first search traversal, the children 
    of any node are already mirrored even before we return the 
    node itself.
"""

def mirror_binary_tree(root):
    # recursive base case
    if not root:
        return
    # traverse left if the left path exists
    if root.left:
        mirror_binary_tree(root.left)
    # traverse right if the right path exists
    if root.right:
        mirror_binary_tree(root.right)
    # on every recursive call that is popped off the stack we perform this swapping operation
    temp = root.left
    root.left = root.right
    root.right = temp

"""

Time complexity
    The time complexity of this solution is linear, O(N)

Space complexity
    The space complexity of this solution is O(H), because our recursive 
    algorithm uses up space on the call stack, which can grow to the 
    height h of the binary tree. The complexity will be O(logN)
    for a balanced tree and O(N) for a degenerate tree.
    
"""