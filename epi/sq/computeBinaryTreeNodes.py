'''
Breadth first search on a binary tree
with a flag node
'''
class BinaryNode:
    def __init__(self,val,left,right):
        self.val = val
        self.left = left
        self.right = right


def computeBinaryTreeNode(root):
    flag = BinaryNode("Ricardo", None, None)
    q = [root,flag]
    levels = []
    level = []
    while(q and q[0] != flag):
        deq = q.pop(0)        
        level.append(deq.val)
        if deq.left:
            q.append(deq.left)
        if deq.right:
            q.append(deq.right)
        if q[0] == flag:            
            q.append(q.pop(0))
            levels.append(level)
            level = []
        
    return levels
b4 = BinaryNode(271,BinaryNode(28,None,None), BinaryNode(0,None,None))
b5 = BinaryNode(2, None, BinaryNode(1,BinaryNode(401,None, BinaryNode(641,None,None)),None))
b6 = BinaryNode(271, None, BinaryNode(28,None,None))
b7 = BinaryNode(561, None, BinaryNode(3, BinaryNode(17,None,None), None))
b2,b3 = BinaryNode(6,b4,b7), BinaryNode(6,b5,b6)
b1 = BinaryNode(314,b2, b3)

print(computeBinaryTreeNode(b1))