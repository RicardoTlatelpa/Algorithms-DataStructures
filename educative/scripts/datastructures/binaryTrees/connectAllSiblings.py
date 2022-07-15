from binary_tree import *
from binary_tree_node import *
from collections import deque
# Given a binary tree, connect its nodes so that it allows a level-order traversal of the tree

"""
    The task is to connect all nodes at the same hierarchal level. Connect them left to right,
    such that the next pointer of each node points to the node on its immediate right. The next
    pointer of the right-most node at each level should point to the first node of the next level
    in the tree.

    Each node in the given binary tree for this problem contains the next pointer, along with the left
    and right pointers. The next pointer is used to connect the same level nodes to each other and across
    levels.
"""
# PASSED ALL TEST CASES
def populate_next_node_pointers(node):
    # TODO: Write - Your - Code
    # Using queue for level order traversal
    queue = deque()
    queue.append(node)
    while queue:
        p = queue.popleft() # dequeue
        if p.left:
            queue.append(p.left)
        if p.right:
            queue.append(p.right)
        if len(queue):
            p.next = queue[0]
    