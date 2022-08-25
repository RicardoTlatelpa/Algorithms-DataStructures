"""
Solution
    This problem follows the Binary Tree Path Sum pattern. We can follow the same 
    DFS approach. But there will be four differences:
        - We will keep track of the current path in a list which will be passed to every recursive call.
        - Whenever we traverse a node we will do two things:
            1. Add the current node to the current path.
            2. As we added a new node to the current path, we should find the sums of all sub-paths
            ending at the current node. If the sum of any sub-path is equal to 'S' we will increment
            our path count.
        - We will traverse all paths and will not stop processing after finding the first path.
        - Remove the current node from the current path before returning from the function. This is needed
        to backtrack while we are going up the recursive call stack to process other paths.
"""
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def count_paths(root, S):
  return count_paths_recursive(root, S, [])

def count_paths_recursive(currentNode, S, currentPath):
    if currentNode is None:
        return 0
    currentPath.append(currentNode.val)
    pathCount, pathSum = 0, 0

    for i in range(len(currentPath)-1, -1, -1):
        pathSum += currentPath[i]
        if pathSum == S:
            pathCount += 1
    
    pathCount += count_paths_recursive(currentNode.left, S, currentPath)
    pathCount += count_paths_recursive(currentNode.right, S, currentPath)

    del currentPath[-1]

    return pathCount

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has paths: " + str(count_paths(root, 11)))


main()

"""
Time Complexity
    The time complexity of the above algorithm is O(N^2) in the worst case, where "N" is the total
    number of nodes in the tree. This is due to the fact that we traverse each node once, but for every
    node, we iterate the current path. The current path, in the worst case, can be O(N) (in the case of a skewed tree).
    But, if the tree is balanced, then the current path will be equal to the height of the tree,ie., O(logN).
    So the best case of our algorithm will be O(NlogN).

Space Complexity
    The space complexity of the above algorithm will be O(N). This space will be used to store the recursion
    stack. The worst case will happen the when the given tree is a linked list(i.e., every node has only one child).
    We also need O(N) space for storing the currentPath in the worst case.

    Overall space complexity of our algorithm is O(N).
"""