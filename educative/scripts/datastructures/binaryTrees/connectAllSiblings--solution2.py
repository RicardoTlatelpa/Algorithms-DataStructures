from binary_tree import *
from binary_tree_node import *
from collections import deque
"""
Solution 2 from educative
In this solution, we maintain a queue by travering the binary tree nodes 
and maintaining the last node pointer. The algorithm is as follows:

    add root at the end of the queue
    initialize last node to null

    while queue is not empty
        current = dequeued element - remove and get the first element of queue
        if last is not null
            last->next = current
        last = current

        if left child of current is not null
            add it at the end of the queue - enqueue current-> left
        if right child of current is not null
            add it at the end of the queue - enqueue current-> right
"""

def populate_next_node_pointers(root):
    if not root:
        return
    queue = deque() 
    queue.append(root)
    last_node = None

    while queue:
        current = queue.popleft()
        if last_node:
            last_node.next = current
        
        last_node = current
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    last_node.next = None

"""
Time complexity
    The time complexity of this solution is linear, O(N)

Space complexity
    The space complexity of this solution is linear, O(N) because we use a queue who maximum size 
    is proportional to n, the number of nodes in the tree.
"""