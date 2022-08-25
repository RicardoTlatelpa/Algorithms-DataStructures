from binary_tree import *
from binary_tree_node import *

"""
Solution 1 from educative

We keep two pointers: current and last. The current node is the tree node we are currently working on,
while the last node is the last node of the current linked list in which the next nodes are already connected.

We'll follow the below pseudocode to connect all the next nodes in the tree:

While current node is not null
    if current node has a left child
        append this left node to the last and make it last node

    if current node has a right child
        append this right node to the last and make it last node
    update current node to current node's next node

After we connect all the next nodes, a structure similar to a linked list is formed whose head is the root node.

Let's connect all the next nodes in the above example to under this algorithm:

"""

def populate_next_node_pointers(root):
    if root:
        current = root
        last = root

    while current:
        # If left child is not null the connect it to the
        # current last of the level-order linked list
        if current.left:
            last.next = current.left
            last = current.left
        # If right child is not null then connect it to the
        # current last of the level-order linked list
        if current.right:
            last.next = current.right
            last = current.right
        
        # Set the next pointer of the last node
        # to null
        last.next = None
        
        # Update the current pointer, to traverse through the tree
        current = current.next

# Function to find the given node and return its next node

"""
Time Complexity
the time complexity of this solution is linear, O(N)

Space Complexity
the space complexity of this solution is constant, O(1)
"""