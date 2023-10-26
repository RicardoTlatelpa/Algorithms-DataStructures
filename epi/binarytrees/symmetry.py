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