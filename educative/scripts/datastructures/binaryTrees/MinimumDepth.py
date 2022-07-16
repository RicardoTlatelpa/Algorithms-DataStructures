"""
Problem Statement
    Find the minimum depth of a binary tree. The minimum
    depth is the number of nodes along the shortest 
    path from the root node to the nearest leaf node.
"""
from collections import deque

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left, self.right = None, None
# traversal in level order
def find_minimum_depth(root):
    
    # Edge case: tree does not exist
    if root == None:
        return -1
    # flag variable helps keep track of each level as we traverse
    level_marker = TreeNode(None)
    # queue to aid level order traversal
    queue = deque()
    queue.append(root)
    queue.append(level_marker)
    # level starts at 1 because we begin with the root node
    depth_level = 1

    while queue:
        dq = queue.popleft()
        peek = queue[0]
        
        # if we find leaf node return its current level
        if dq.left == None and dq.right == None:
            return depth_level

        if peek == level_marker:
            queue.popleft() # remove level marker 
            depth_level+=1 # increment depth_level
        
        # check if node has any children
        if dq.left:
            queue.append(dq.left)
        if dq.right:
            queue.append(dq.right)
        # add level flag to end of queue if there are any existing children
        if queue:
            queue.append(level_marker)