'''
Test if a binary tree is balanaced.
A binary tree is balanced when the height
difference of the left subtree and the right subtree
is not greater than 1. If that ever is the case
then the binary tree is not balanced.


Caveats:

    1 caveat would be the counting of the heights
    to count a height we start at 1, but we do not
    count the leaf node

    2 assume we use depth first search to find 
    the height of every node,
    we can use the recurrence relation
    left,right = 0,0
    if node.left:
        left = 1 + dfs(node.left)
    if node.right:
        right = 1 + dfs(node.right)
    if abs(left - right) > 1:
        return float('inf')
    return max(left,right)
'''
def checkHeight(root):
    def checkHeightBalance_(root):
        if root is None:
            return 0
        left,right = 0,0
        if root.left:
            left = 1 + checkHeightBalance_(root.left)
        if root.right:
            right = 1 + checkHeightBalance_(root.right)
        if abs(left-right) > 1:
            return float('inf')
        return max(left,right)
    return checkHeightBalance_(root) == float('inf')
