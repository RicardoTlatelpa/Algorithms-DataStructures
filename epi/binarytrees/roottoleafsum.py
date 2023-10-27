'''
Write a program which takes as input as integer and a binary tree with integer node weights,
and checks if there exists a leaf whose path weight equals the given integer.
'''


def find_sum(root,target):
    def f(root,s):
        if root is None:
            return False
        if root.left == None and root.right == None:
            if s + root.val == target:
                return True
            return 
        return f(root.left, s + root.val) or f(root.right, s+ root.val)

    return f(root,0)

def has_path_sum(tree,remaining_weight):
    if not tree:
        return False
    if not tree.left and not tree.right:
        return remaining_weight == tree.data
    return has_path_sum(tree.left,remaining_weight - tree.data) or
    has_path_sum(tree.right, remaining_weight - tree.data)
