from binary_tree import *
from binary_tree_node import *

"""
Solution 1 from educative 
We print the perimeter of the binary tree in three phases, the left boundary, leaf nodes, and the right boundary. 
The left and right boundaries will be printed iteratively while the leaf nodes will be printed recursively. Here 
is how the algorithm looks:
    - Print the root node
    - Print the left boundary in top-down order.
    - Print the leaf nodes in leaf-right order. We'll be traversing from one leaf node to the next using post-
    order traversal
    - Print the right boundary in bottom-up order
        - We push the node values in a stack here.
        - Once we hit the leaf node, we pop all stack elements while printing them.
"""

def print_left_perimeter(root,result):
    while root:
        # store integer of node in each iteration
        curr_val = root.data

        if root.left:
            root = root.left
        elif root.right:
            root = root.right
        else:
            # Break loop on leaf node
            break
        # Every node until 
        # We reached the end of the left side 
        # Has been added to the result string
        result.append(str(curr_val) + ", ")

def print_right_perimeter(root, result):
    r_values = []
    while root:
        curr_val = root.data
        if root.right:
            root = root.right
        elif root.left:
            root = root.left
        else:
            break
        r_values.append(curr_val)

def print_leaf_nodes(root,result):
    if root:
        print_leaf_nodes(root.left,result)
        print_leaf_nodes(root.right,result)
        if not root.left and not root.right:
            result.append(str(root.data) + ", ")

def display_tree_perimeter(root):
    result = []
    if root:
        result.append(str(root.data) + ", ")

        print_left_perimeter(root.left,result)

        if root.left or root.right:
            # We don't need to print if root is also the leaf node.
            print_leaf_nodes(root,result)
        
        print_right_perimeter(root.right, result)
    
    result = ('').join(result)
    result = result[:-2]
    print(result,end="")

def main():
    input1 = [100, 50, 200, 25, 75, 125, 350,
              250, 750, 12, 35, 60, 80, 110, 150]
    tree1 = BinaryTree(input1)

    tree2 = BinaryTree(100)
    tree2.insert(50)
    tree2.insert(200)
    tree2.insert(25)
    # Add a node at an incorrect position
    tree2.insert_bt(110)
    tree2.insert(125)
    tree2.insert(350)
    tree2.insert(250)
    tree2.insert(750)
    tree2.insert(12)
    tree2.insert(35)
    tree2.insert_bt(60)
    tree2.insert_bt(80)
    tree2.insert_bt(120)

    tree3 = BinaryTree(100)
    tree3.insert(50)
    tree3.insert(200)
    tree3.insert(25)
    tree3.insert(75)
    # Add a node at an incorrect position
    tree3.insert_bt(90)
    tree3.insert(350)
    tree3.insert(250)
    tree3.insert(750)
    tree3.insert(12)
    tree3.insert(35)
    tree3.insert_bt(60)
    tree3.insert_bt(80)
    tree3.insert_bt(110)

    input4 = [100, 50, 200, 25, 75, 125, 350]
    input4.sort()
    tree4 = BinaryTree(input4)

    input4.reverse()
    tree5 = BinaryTree(input4)

    tree6 = BinaryTree(100)

    # Defining test cases
    test_case_roots = [tree1.root, tree2.root, tree3.root,
                       tree4.root, tree5.root, tree6.root, None]

    for i in range(len(test_case_roots)):
        if (i > 0):
            print()
        print(str(i + 1) + ".\tBinary tree:")        
        print("\n\tTree Perimeter:\n\t", end="")        
        display_tree_perimeter(test_case_roots[i])
        print("\n----------------------------------------------------------------------------------------------------")
main()


"""
Time Complexity
    The Time complexity of this solution is linear, O(N)
Space Complexity
    The space complexity of this iterative solution is O(H) because the recursive algorithm for printing leaf nodes
    uses up space on the call stack up to the height, h, of the binary tree. Similiary, the algorithm for printing
    the right perimeter uses a stack that will contain at most h node. The complexity will be O(LogN) for a 
    balanced tree and O(N) for a degenerate tree.
"""