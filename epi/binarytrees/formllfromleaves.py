'''
9.14

Given a binary tree, commpute a linked list from the leaves of the binary tree. The leaves
should apppear in left-to-right order. For example,when applied to the binary tree in figure 
9.1 on page 112, your function should return D,E,H,M,N,P
'''

class TreeNode:
    def __init__(self,val,left,right):
        self.val = val
        self.left = left
        self.right = right

def create_ll(tree):
    dummy_node = TreeNode(None,None,None)
    tail = dummy_node

    def preorder(root):
        nonlocal tail
        if root is None:
            return
        if root and root.left == None and root.right == None:
            tail.right = root
            tail = tail.right
        preorder(root.left)
        preorder(root.right)

    preorder(tree)
    return dummy_node.right

left_subtree = TreeNode(6,
                    TreeNode(271,
                        TreeNode(28,None,None),
                        TreeNode(0,None,None)
                             ),
                    TreeNode(561,
                            None,
                             TreeNode(3,
                                TreeNode(17,None,None),
                                None
                                      )
                            )
                )
root = TreeNode(314,left_subtree,None)

ll = create_ll(root)

while(ll):
    print(ll.val)
    ll = ll.right

