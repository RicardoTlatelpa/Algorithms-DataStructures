from binary_tree import *
from binary_tree_node import *

def display_tree_perimeter(root):
    result = ""
    if root == None:
        return result
    
    result += str(root.data) + ", "
    current_node = root.left
    # LEFT PERIMETER
    while current_node and current_node.left != None:
        result += str(current_node.data) + ", "
        current_node = current_node.left
    # BOTTOM PERIMETER
    stack = []
    current_node = root
    while current_node or stack:
        if current_node:
            stack.append(current_node)
            current_node = current_node.left
            continue
        p = stack.pop()
        
        if p.right:
            current_node = p.right

        if p.right == None and p.left == None:
            result += str(p.data) + ", "
    # RIGHT PERIMETER
    stack = []
    current_node = root.right

    while current_node and current_node.right != None:
        stack.append(current_node.data)
        current_node = current_node.right
    while stack:
        p = stack.pop()
        result += str(p) + ", "
    # Clean up result string to not include extra 2 characters: comma and space at the end
    result_ = result[:-2]
    print(str(result_), end="")