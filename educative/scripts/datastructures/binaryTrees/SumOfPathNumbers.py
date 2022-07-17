"""
Given a binary tree where each node can only have a digit(0-9) value, each root-to-leaf path will
represent a number. Find the total sum of all the numbers represented by all paths.
"""

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def find_sum_of_path_numbers(root):
  # TODO: Write your code here
    if root is None:
        return -1   
    allPaths = []    
    find_sum_of_path_numbers_helper(root, [], allPaths)
    return allPaths
    
def find_sum_of_path_numbers_helper(root,currentPath, allPaths):
    if root is None:
        return
    currentPath += str(root.val)
    if root.left is None and root.right is None:           
        integer = "".join(list(currentPath))
        if allPaths:
          allPaths.append(allPaths.pop() + int(integer))
        else:
          allPaths.append(int(integer))
    else:
        find_sum_of_path_numbers_helper(root.left, currentPath,allPaths)
        find_sum_of_path_numbers_helper(root.right, currentPath,allPaths)
    del currentPath[-1]  
    