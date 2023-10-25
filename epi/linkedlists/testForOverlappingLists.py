class Node():
    def __init__(self,val,next):
        self.val = val
        self.next = next
'''
Given two singly linked lists there may be list nodes that are common to both.
(This may not be a bug - it may be desirable from the perspective of reducing memory
footprint, as in the flyweight pattern, or maintaining a canonical form). For example
the lists in figure 7.7 on the following page overlap at Node I.

Write a program that takes two cycle-free singly linked lists,
and determines if there exist a node that is common to both lists.
'''
def testOverlapping(headA,headB):
    tempA = headA
    tempB = headB
    def getSize(h):
        if h is None:
            return 0
        length = 1
        while(h):
            h = h.next
            length+=1
        return length

    lenA = getSize(headA)
    lenB = getSize(headB)
    diff = abs(lenA-lenB)

    if lenA > lenB:
        for _ in range(diff):
            tempA = tempA.next
    if lenB > lenA:
        for _ in range(diff):
            tempB = tempB.next
    while(tempA and tempB):
        if tempA == tempB:
            return tempA
        tempA,tempB = tempA.next,tempB.next

    return None

def overlapping_no_cycle_lists(L1,L2):
    def length(L):
        length = 0
        while L:
            length +=1
            L = L.next
        return length
    L1_len,L2_len = length(L1), length(L2)
    if L1_len > L2_len:
        L1, L2 = L2, L1
    '''
    Trust that the longest list will always be contained in L2
    '''
    for _ in range(abs(L1_len-L2_len)):
        L2 = L2.next
    while L1 and L2 and L1 is not L2:
        L1,L2 = L1.next,L2.next
    return L1 # None implies there is no overlap between L1 and L2
