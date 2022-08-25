"""
Path with given sequence:
    Give a binary tree and a number sequence, find if the sequence
    is present as a root-to-leaf path in the given tree.
"""
# PASSED ALL TEST CASES
class TreeNode:
    def __init__(self,val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_path_helper(node, sequence, current_idx):
    # Edge case: root node does not exist
    if node is None:
        return False
    # Value of the current index of the sequence
    key = sequence[current_idx]
    # increment the current_idx for the next recursive call
    current_idx += 1    
    # only update next_key if within bounds of list
    if current_idx < len(sequence):            
      next_key = sequence[current_idx]
    else:
      next_key = float('inf')
  
    # Follow the path that leads to the next key
    if key == node.val:
        if node.left is None and node.right is None: # found path
            return True
        elif node.left and node.left.val == next_key:
            return find_path_helper(node.left, sequence, current_idx)
        elif node.right and node.right.val == next_key:
            return find_path_helper(node.right, sequence, current_idx)
        else:
            return False
    
def find_path(root, sequence):    
    return find_path_helper(root, sequence, 0)

"""
Time and space complexity
    Time is O(logN)
        In a list of N nodes and a sequence of the height of the tree,
        we follow the path that is most likely going to give us the sequence
    Space is O(logN)    
        Space is LogN because we are visiting LogN nodes and the call stack
        at worse case will store LogN nodes and that's only if it finds the path
        leading to a sequence

"""



    