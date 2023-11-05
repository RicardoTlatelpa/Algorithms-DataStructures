'''
Binary tree bootcamp
Full tree, leaves have no children, and 
nodes that do have children have two children

Complete tree
every non leaf node must have exactly two children

Perfect tree
Full tree + Complete tree
all the leaf nodes are at the same depth, and all non-leaf nodes
have two children.
the tree is completely filled with no gaps.

9.16 Compute the right sibling
Write a program that takes a perfect binary tree, and 
sets each node's level-next field to the node on its right,
if one exists.
'''

def connect(root):
    if not root:
        return root
    queue = [root]
    while(queue):
        n = len(queue)
        for i in range(n):
            deq = queue.pop(0)
            if i != n-1:
                deq.next = queue[0]
            if deq.left:
                queue.append(deq.left)
            if deq.right:
                queue.append(deq.right)
    return root

def construct_right_sibling(tree):
    def populate_children_next_field(start_node):
        while start_node and start_node.left:
            start_node.left.next = start_node.right
            start_node.right.next = start_node.next and start_node.next.left
            start_node = start_node.next
    while tree and tree.left:
        populate_children_next_field(tree)
        tree = tree.left