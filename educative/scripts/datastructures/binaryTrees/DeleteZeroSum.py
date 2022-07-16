"""
Given a binary tree, delete any sub-trees whose nodes sum up to zero.

So we have to find a subtree that adds up to zero

What is a sub tree?
    A subtree is a grouping of a tree that shares a connection together

We can traverse through the tree in level order, and each node that we traverse we can run 
a traversal that sums up itself and its children (sub tree), if the sum is zero
we delete all the children and then the root of the subtree node

deleting the sub tree, I can take advantage of the deletion in a binary tree and delete 
"""


# Check for sum of zero
def delete_zero_helper(root):
    stack = []
    i_stack = []
    current = root
    sumtree = 0
    while current or stack:
        if current:
            stack.append(current)
            current = current.left
        p = stack.pop()
        if p.right:
            current = p.right
        sumtree += p.data
        i_stack.append(p) # every node in the sub tree
    if sumtree == 0:
        # delete every node in the sub tree and delete
        for i in range(len(i_stack)):
            node_to_delete = i_stack[i]
            # set every child pointer to null
            if node_to_delete.left:
                node_to_delete.left = None
            if node_to_delete.right:
                node_to_delete.right = None
            # set the node itself to null            
        return True
    else:        
        return False

def delete_zero_sum_subtree(tree):
    if tree == None:
        return
    if delete_zero_helper(tree):     
        tree = None   
        return
    delete_zero_sum_subtree(tree.left)
    delete_zero_sum_subtree(tree.right)
    

