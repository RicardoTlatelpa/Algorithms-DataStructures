'''
Design an algorithm for reconstructing a binary tree from a preorder
traversal visit sequence that uses null to mark empty children.


'''
class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

    
def preorder(root):
    if root == None:
        return 
    print(root.val)
    preorder(root.left)
    preorder(root.right)
    
def reconstructPreOrder(preorder):
    #[3,9,None,None,20,15,None,None,7,None,None]
    def helper(preStart):
        if preorder[preStart] == None or preStart >= len(preorder):
            return None
        root = TreeNode(preorder[preStart])

        root.left = helper(preStart+1)
        if root.left == None:
            root.right = helper(preStart+1)
        else:
            root.right = helper(preStart+4)
        return root
    return helper(0)

my_input = [3,9,None,None,20,15,None,None,7,None,None]
pre = reconstructPreOrder(my_input)
#preorder(pre)


def reconstruct_preorder(preorder):
    def reconstruct_preorder_helper(preorder_iter):
        subtree_key = next(preorder_iter)
        if subtree_key is None:
            return None
        left_subtree = reconstruct_preorder_helper(preorder_iter)
        right_subtree = reconstruct_preorder_helper(preorder_iter)
        return TreeNode(subtree_key, left_subtree, right_subtree)
    return reconstruct_preorder_helper(iter(preorder))

pre2 = reconstruct_preorder(my_input)

preorder(pre2)
