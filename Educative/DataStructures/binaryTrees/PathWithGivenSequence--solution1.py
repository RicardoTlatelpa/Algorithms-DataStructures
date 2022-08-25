"""
Solution
    This problem follows the Binary Tree Path sum pattern. We can follow the same DFS 
    approach and additionally, track the element of the given sequence that we should
    match with the current node. Also, we can return false as soon as we find a mismatch
    between the sequence and the node value.
"""


class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_path(root, sequence):
  if not root:
    return len(sequence) == 0
  # initial values are the root,sequence, and an index of 0
  return find_path_recursive(root, sequence, 0)

def find_path_recursive(currentNode, sequence, sequenceIndex):
    if currentNode is None:
        return False
    
    seqLen = len(sequence)
    # if we're over the bounds of the sequence or the currentNode does not equal the sequence value
    if sequenceIndex >= seqLen or currentNode.val != sequence[sequenceIndex]:
        return False
    # we reached a leaf node and the sequence list is exhausted
    if currentNode.left is None and currentNode.right is None and sequenceIndex == seqLen -1:
        return True
    # traverse every path
    return find_path_recursive(currentNode.left, sequence, sequenceIndex + 1) or \
        find_path_recursive(currentNode.right, sequence, sequenceIndex + 1)

"""
Time complexity
    The time complexity of the above algorithm is O(N), where 'N' is the total
    number of nodes in the tree. This is due to the fact that we traverse each node once.

Space complexity
    The space complexity of the above algorithm will be O(N) in the worst case. This space
    will be used to store the recursion stack. The worst case will happen when the given tree
    is a linked list (i.e., every node has only one child).
"""