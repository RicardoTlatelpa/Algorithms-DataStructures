class Node:
    def __init__(self,x):
        self.val = x
        self.next = None

'''
If such a node exists, return a node that appears first when traversing the lists. This node
may not be unique-if one node ends in a cycle, the first cycle encountered when traversing it 
may be different from the first cycle node encountered when traversing it may be different
from the first cycle node encountered when traversing the second list, even though the cycle is the same.
'''

def overlappingLists(L1,L2):

