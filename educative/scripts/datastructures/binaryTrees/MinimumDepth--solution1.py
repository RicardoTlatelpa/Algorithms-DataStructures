"""
Solution
    This problem follows the Binary Tree Level order Traversal pattern. 
    We can follow the same BFS approach. The only difference will be, instead 
    of keeping track of all the nodes in a level, we will only keep track the depth
    of the tree. As soon as we find our first leaf node, that level will represent
    the minmum depth of the tree.
"""

from collections import deque

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left,self.right = None, None

def find_minimum_depth(root):
    if root is None:
        return 0
    queue = deque()
    queue.append(root)
    minimumTreeDepth = 0
    while queue:
        minimumTreeDepth += 1 
        levelSize = len(queue)
        for _ in range(levelSize):
            currentNode = queue.popleft()
            if not currentNode.left and not currentNode.right:
                return minimumTreeDepth
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

"""
Time complexity
    The time complexity of the above algorithm is O(N) where N is the total number of nodes in the tree.
    This is due to the fact that we traverse each node once.

Space complexity
    The space complexity of the above algorithm will be O(N) which is required for the queue.
    Since we can have a maximum N/2 nodes at any level(this could happen only at the lowest level), 
    therefore we will need O(N) space to store them in the queue
"""