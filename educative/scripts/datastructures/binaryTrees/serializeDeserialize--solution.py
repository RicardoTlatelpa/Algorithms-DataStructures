"""
There can be multiple approaches to serialize and deserialize the tree. One way
To serialize the tree is as follows:
    -perform a depth-first traversal and serialize individual nodes to the stream
    -we use a pre-order(root,left,right) traversal here.
    -we also serialize the marker to represent a null pointer to help deserialize the tree.

Markers(M*) are added to this tree to represent null nodes. The number with each marker, such as 1 in m1 or 2 in M2, merely represents
the relative position of a marker in the stream

The serialized tree (pre order traversal) from the above example looks like the below list:
100,50,25,m1,m2,75,m3,m4,200,m5,350,m6,m7

To deserialize the tree, we against use the pre order traversal and create a new node for every non-marker node. Encountering
a marker indicates a null node.
"""

from binary_tree import *
from binary_tree_node import *

MARKER = float('inf')

def serialize_rec(node,stream):
    if(node == None):
        stream.append(MARKER)
        return
    
    stream.append(node.data)

    serialize_rec(node.left,stream)
    serialize_rec(node.right,stream)

def serialize(root):
    stream = []
    serialize_rec(root,stream)
    return stream

def deserialize(stream):
    val = stream.pop(0) #dequeue
    if(val == MARKER): # base case
        return None
    node = BinaryTreeNode(val)

    node.left = deserialize(stream)
    node.right = deserialize(stream)

    return node


"""
Time complexity
    The time complexity of this solution is linear, O(N)
Space complexity
    the space complexity of this solution is O(H), because 
    our recursive algorithm uses up space on the call
    stack, which can grow to the height h of the binary tree.
    The complexity will be O(logN) for a balanced tree
    and O(N) for a degenerate tree.

There is another algorithm that serialzes the tree in any two depth first traversal orders, 
for example, pre order and in order traversal. Remember that we can construct a tree(or deserialize) 
if two of its depth-first orders are given. This approach is similar to the above algorithm
for integer data in terms of space and time complexity

But if the data is user defined type with a relatively large node size, storing it twice is not that efficient.
For most practical purposes, store extra markers, significatly smaller than the data nodes.

We can serialize it like a heap data structure if we know that our tree is almost a complete binary tree.
We can use the below two rules to serialize and deserialize data:

 - Children of a node i are 2 * i and 2 * i + 1
 - Parent of a node i is i/2
"""