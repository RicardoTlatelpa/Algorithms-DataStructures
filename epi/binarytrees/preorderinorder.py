'''
Construct Binary Tree from Preorder and Inorder traversal
'''

class TreeNode:
    def __init__(self,val,left,right):
        self.val=val
        self.left=left
        self.right=right

def buildTree(preorder,inorder):
    # preorder root,left,right
    # inorder left,root,right
    # postorder left,right,root

    
    def helper(preStart:int,inStart:int, inEnd:int, preorder,inorder):
        '''
        prestart: index of root node
        inStart: starting index of inorder array
        inEnd: last index of inorder array
        preorder: just preorder array; nothing special
        inorder: just inorder; nothing special

        idea: 
        the root can be found with the preorder array
        1. find the root node in the inorder array
            - what's gonna be on the left side and what's gonna be on the right            
        '''
        if (preStart > len(preorder)-1 or inStart > inEnd):
            return None
        root = TreeNode(preorder[preStart])
        inIndex = 0 # inorder array pointer
        for i in range(inEnd+1):
            if root.val == inorder[i]:
                inIndex = i
        root.left = helper(preStart+1, inStart, inIndex-1,preorder,inorder)
        root.right = helper(preStart+ inIndex - inStart+1, inIndex+1, inEnd,preorder,inorder)
        
        return root

    return helper(0,0,len(inorder)-1,preorder,inorder)