class TreeNode:
    def __init__(self,val,left,right):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root):
    stack = [root]
    ans = []
    while(stack):
        top = stack.pop()
        if top:
            ans.append(top.val)
            if top.right:
                stack.append(top.right)
            if top.left:
                stack.append(top.left)
    return ans
