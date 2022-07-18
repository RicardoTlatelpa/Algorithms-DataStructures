"""
Count paths for a sum (medium)

Problem Statement
    Given a binary tree and a number 'S', find all paths in the tree such that the sum 
    of all the node values of each path equals 'S'. Please note that the path can start 
    or end at any node but all paths must follow direction from to child(top to bottom).    

    Pseudocode:
        We can traverse through the tree in level order

"""

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def count_paths_helper(root,S):
    return
def count_paths(root, S):
  # TODO: Write your code here
  return -1