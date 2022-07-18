"""
Count paths for a sum (medium)

Problem Statement
    Given a binary tree and a number 'S', find all paths in the tree such that the sum 
    of all the node values of each path equals 'S'. Please note that the path can start 
    or end at any node but all paths must follow direction from to child(top to bottom).    

    Pseudocode:
        We can traverse through the tree in pre order or really use any traversal method
        At every node, we can perform a look_for_sum_paths operation, where 
        I can iterate through the child nodes and find every path that may add to the sum S.
        Once I have found this path, I can append it to the allPaths list

"""
# PASSES ALL TEST CASES
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def look_for_sum_paths(currentList, allPaths, root, S):
    # Base case, root does not exist, then we return
    if root is None:
        return
    # On each node, we subtract from S
    S -= root.val
    currentList.append(root.val)
    # Sum can not be completed in this path        
    # We found a sum Path
    if S == 0:         
        allPaths.append(list(currentList))        
    else:    
      look_for_sum_paths(currentList, allPaths, root.left, S)
      look_for_sum_paths(currentList, allPaths, root.right, S)
    del currentList[-1] # Backtracking case for every recursive call popped off stack

    

# Traverse through tree
def count_paths_helper(root,S, allPaths):
    # Base case are leaf nodes and nodes that don't exist
    if root is None:
        return
    look_for_sum_paths([], allPaths, root, S)
    # look_for_sum_paths operation
    # Tree Traversal
    count_paths_helper(root.left,S, allPaths)
    count_paths_helper(root.right,S,allPaths)
    

def count_paths(root, S):
  # TODO: Write your code here
    allPaths = []
    count_paths_helper(root,S,allPaths)
    print(allPaths)
    return len(allPaths)


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has paths: " + str(count_paths(root, 11)))


main()