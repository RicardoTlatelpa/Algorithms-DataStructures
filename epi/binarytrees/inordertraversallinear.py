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

    while(stack and node):
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            ans.append(node.val) 
            if node:
                stack.append(node.right)
            
