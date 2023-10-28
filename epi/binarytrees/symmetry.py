class BinaryNode:
    def __init__(self,val,left,right):
        self.val = val
        self.left = left
        self.right = right

def is_symmetry(root):
    left_bfs,right_bfs = [],[]
    left,right = root.left,root.right
    dummy_node = BinaryNode(None,None,None)

    queue = [(left,"l"), dummy_node]

    while(queue and queue[0] != dummy_node):
        (deq,deq_dir) = queue.pop(0)
        left_bfs.append((deq.val, deq_dir))
        if(deq.left):
            queue.append((deq.left,"l"))
        if(deq.right):
            queue.append((deq.right,"r"))
        if queue[0] == dummy_node:
            queue.pop(0)
            queue.append(dummy_node)
    n = len(left_bfs)

    queue = [(right,"r"), dummy_node]

    while(queue and queue[0] != dummy_node):
        (deq,deq_dir) = queue.pop(0)
        right_bfs.append((deq.val, deq_dir))
        if(deq.left):
            queue.append((deq.left,"l"))
        if(deq.right):
            queue.append((deq.right,"r"))
        if queue[0] == dummy_node:
            queue.pop(0)
            queue.append(dummy_node)
    
    if n!=len(right_bfs):
        return False
    
    for i in range(n):
        (l_val, l_dir), (r_val, r_dir) = left_bfs[i],right_bfs[i]
        if l_val != r_val or l_dir == r_dir:
            return False
    return True

'''
Hint: the definition of symmetry is recursive

Computing the mirror image of a tree is as simple
as swapping the left and right subtrees, and recursively 
continuing. The time and space complexity are both O(n), where
n is the number of nodes in the tree.
'''

def is_symmetric(tree):
    def check_symmetric(subtree_0, subtree_1):
        if not subtree_0 and not subtree_1:
            return True
        elif subtree_0 and subtree_1:
            return (subtree_0.val == subtree_1.val
                    and check_symmetric(subtree_0.left, subtree_1.right)
                    and check_symmetric(subtree_0.right, subtree_1.left)
                    )
        return False
    return not tree or check_symmetric(tree.left,tree.right)
