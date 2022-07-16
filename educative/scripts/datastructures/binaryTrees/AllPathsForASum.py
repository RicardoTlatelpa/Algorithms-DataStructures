"""
Problem statement
    Given a binary tree and a number 'S', find all paths from root-to-leaf 
    such that the sum of all the node values of each path equals 'S'.    

Pseduocode:
    Sum I'm looking for: 12
    I can take the root value: 1 
        Split into the left child and into the right child
            in those paths follow the path closest to the sum 12
            
            in the left sub tree, I sit at 7 with a current sum of 1
            if I add 7 to the current sum I get 8 which I do because it brings me closer to the sum I want 12
            I add 7 to the current sum and get 8, and I look at both left and right children
            if I add 5 to the current sum I get 13, which is close to the sum by 1
            if I add 4 to the current sum I get 12, which is close to the sum by 9
                I choose 4, if 4 is a leaf node, then I have a valid path, and I choose

"""
# PASSED ALL TEST CASES
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def find_paths_helper(allPaths, currentList, root,sum):
    if root == None:
        return
    currentSum = 0
    for i in range(len(currentList)):
        currentSum += currentList[i]
    currentSum += root.val
    if currentSum > sum:
        return    
    currentList.append(root.val)    
    if root.left == None and root.right == None and currentSum == sum:
        allPaths.append(currentList)
        return    
    else:
        find_paths_helper(allPaths, currentList, root.left, sum)        
        find_paths_helper(allPaths, currentList, root.right, sum)

def find_paths(root, sum):
  allPaths = []
  find_paths_helper(allPaths, [root.val], root.left, sum)
  find_paths_helper(allPaths, [root.val], root.right, sum)
  return allPaths

def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  sum = 23
  print("Tree paths with sum " + str(sum) +
        ": " + str(find_paths(root, sum)))


main()