'''
IN order traversal of binary tree without recursion.
'''
class TreeNode:
    def __init__(self,val,left,right):
        self.val = val
        self.left = left
        self.right = right
def inorder_traversal(root):
    '''
    So the idea is to use the stack and a variable
    
    1. We exhaust to the left of the node pointer
    once node equals None
    - we replace the Node with the node at the top of the stack
    - we add it's right child to the stack 
    '''
    ans = []
    node = root
    
    stack = []

    while(True):
        if len(stack) == 0 and node == None:
            break
        if node:
            # exhaust left by traversing to the left
            stack.append(node)
            node = node.left
        else:
            # pop from stack because node is None
            # read inorder value
            # traverse to the right
            node = stack.pop()
            ans.append(node.val)
            node = node.right

    return ans 
