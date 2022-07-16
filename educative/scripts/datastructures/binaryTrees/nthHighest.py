"""
Given a binary search tree and an integer n, return node with the nth highest value.

What are the edge cases:
    n is greater than the amount of nodes that are in the tree
    or n is less than 1, because there are no 0th nodes and there are no 

Stack data structure to traverse the tree in binary order
"""

def find_nth_highest_in_bst(node,n):
    stack = [] # helps with traversal
    current = node # helps with traversal
    in_order_nodes = [] # stores the nodes in the binary tree in order
    while stack or current:
        if current:
            stack.append(current)
            current = current.left
            continue
        p = stack.pop()
        
        if p.right:
            current = p.right
        in_order_nodes.append(p)
    
    if n > len(in_order_nodes) or n < 1:
        return None
    # O(N) operation to find the nth largest node
    while n - 1:
        n -= 1
        stack.pop()
    return stack.pop()

