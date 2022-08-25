from binary_tree import *
from binary_tree_node import *

"""
Solution 2 from educative
    This solution involves the same steps used for the previous solution. However, the left and right boundaries
    are also printed recursively in this solution.
"""

def print_left_perimeter(root,result):
    if not root:
        return

    # Setting root such that left boundary nodes are printed from top to bottom 
    if root.left:
        # Append current node to perimeter result
        result.append(str(root.data) + ", ")
        # recursive call to the left child
        print_left_perimeter(root.left, result)

    elif root.right:
        # Append current node to perimeter result
        result.append(str(root.data) + ", ")
        # If there's no left child, we make a recursive
        # call to the right child
        print_left_perimeter(root.right,result)
# Function to print right tree perimeter

def print_right_perimeter(root,result):
    if not root:
        return
    if root.right:
        print_right_perimeter(root.right,result)
        result.append(str(root.data) + ", ")
    elif root.left:
        # If there's no right child, we make a recursive 
        # call to the left child
        print_right_perimeter(root.left, result)
        # Append current node to perimeter result
        result.append(str(root.data) + ", ")
    
# Function to print leaf nodes perimeter

def print_leaf_nodes(root,result):
    if not root:
        return
    print_leaf_nodes(root.left,result)

    if not root.left and not root.right:
        result.append(str(root.data) + ", ")
    
    print_leaf_nodes(root.right,result)

def display_tree_perimeter(root):
    result = []
    if root:
        result.append(str(root.data) + ", ")

        print_left_perimeter(root.left,result)
        
        print_leaf_nodes(root.left,result)
        print_leaf_nodes(root.right,result)

        print_right_perimeter(root.right,result)

        result = ('').join(result)
        result = result[:-2]
        print(result,end="")

"""
Time complexity 
    The time complexity of this solution is linear, O(N).
Space Complexity 
    The space complexity of this solution is O(H) because our recursive algorithm
    uses up space on the call stack, which can grow to the height H of the binary tree.
    The complexity will be O(LogN) for a balanced tree and O(N) for a degenerate tree.
"""