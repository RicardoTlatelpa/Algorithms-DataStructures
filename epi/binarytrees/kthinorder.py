'''
inorder kth node

Write a program that efficiently computes the kth node appearing in an inorder 
traversal. Assume that eachj node stores the number of nodes in the subtree rooted
at that node.

'''
class TreeNode:
    def __init__(self,val,left,right):
        self.val=val
        self.left=left
        self.right=right

def find_kth_node_binary_tree(tree,k):
    while tree:
        left_size = tree.left.size
        if left_size + 1 < k:
            k-=left_size+1
            tree = tree.right
        elif left_size == k -1:
            return tree
        else:
            tree = tree.left
    return None

''' 
Since we descend the tree in each iteration, the time complexity is O(h), where h is the height of the tree.
'''