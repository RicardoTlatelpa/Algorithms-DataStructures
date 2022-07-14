from binary_tree import *
from binary_tree_node import *

def print_left_perimeter(root,result):
    if not root:
        return
    if root.left:
        result.append(str(root.data) + ", ")
        print_left_perimeter(root.left, result)
    elif root.right:
        result.append(str(root.data) + ", ")
        print_left_perimeter(root.right,result)
    
def print_right_perimeter(root,result):
    