from binary_tree import *
from binary_tree_node import *

"""
Given a binary tree, serialize is to a file and then deserialize it back to a tree.

Statement
    Serialize a given binary tree to a file and then deserialize it back to a tree. 
    Make sure that the original and the deserialized trees are identical

    Serialize: Write the tree in a file
    Deserialize: Read from a file and reconstruct the tree in memory


    Sample input:
    The input list below represents the level-order traversal of the binary tree:
    100,50,200,25,75,350

    Expected output:
    25,50,75,100,200,350
    
"""

def serialize(root):
    return None

def deserialize(stream):
    # the input is a level-order traversal of the binary tree that we have to construct
    result = ""
    root_value = stream[0]
    root = BinaryTree()
    root.insert(root_value)
    for i in range(len(stream),1):
        root.insert(stream[i])
    current = root.root # head of the tree
    stack = []
    while stack or current:
        if current:
            stack.append(current)
            current = current.left
            continue
        p = stack.pop()

        if p.right:
            current = p.right
        
        result += str(p.data) + ", "
    result_ = result[:-2]

    print(str(result_), end="")
    return None