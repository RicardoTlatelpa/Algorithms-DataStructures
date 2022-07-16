"""
The in-order traversal of a BST is always sorted in ascending order. So, 
to find the nth highest node, we need to scan the tree in descending order
by performing a reverse in-order traversal
- The in order traversal is typically LPR, meaning left, child, parent node, and then right child.
- Reverse in-order traversal is RPL, meaning right child, parent node, and then left child.

Here is the algorithm for this solution:
    - Perform a reverse in-order traversal of the BST in RPL.
    - While traversing, keep a current count of the nodes visited so far
    - Once this current count reaches n, we return that node.    
"""

from binary_tree import * 
from binary_tree_node import *

current_count = 0

def find_nth_highest_in_bst_rec(node,n):
    # base case
    if not node:
        return None
    
    result = find_nth_highest_in_bst_rec(node.right,n)

    if result:
        return result

    global current_count
    current_count = current_count + 1

    if n == current_count:
        return node

    result = find_nth_highest_in_bst_rec(node.left,n)

    if result:
        return result

    return None

def find_nth_highest_in_bst(root,n):
    global current_count
    current_count = 0

    if not root:
        return None
    return find_nth_highest_in_bst_rec(root,n)

"""
Time Complexity
    The time complexity of this solution in linear O(N)
Space Complexity
    The space complexity of this solution is O(H) because our
    recursive algorithm uses up space on the call stack,
    which can grow to the heist h of the binary tree. The
    complexity will be O(LogN) for a balanced tree and O(N)
    for a degenerate tree.
"""