'''
Write a program that takes as input a single linked list of intergers in sorted order,
and removes duplicates from it. The list should be sorted.
'''
class ListNode():
    def __init__(self,val,next):
        self.val = val
        self.next = next    
    def insert(self,node):
        temp = self
        while(temp.next):
            temp = temp.next
        temp.next = node # appended to the end of the ll
    def read(self):
        temp = self
        while(temp):
            print(temp.val)
            temp = temp.next

def removeDuplicates(L):
    '''
    How do we know if a number we are traversing through is a duplicate,
    if we have seen that number before --> memory with fast read access: Hash table O(1) read and O(1) write
    If we have seen the val before, delete it
    if we have not seen the val before, record it
    '''

    ht = {}

    aux = L
    while(aux):
        if aux.next and (aux.val == aux.next.val):
            aux.next = aux.next.next
        else:
            aux = aux.next

    return L
n1 = ListNode(2,None)
n2 = ListNode(2,None)
n3 = ListNode(3,None)
n4 = ListNode(5,None)
n5 = ListNode(7,None)
n6 = ListNode(11,None)
n7 = ListNode(11,None)

n1.insert(n2)
n1.insert(n3)
n1.insert(n4)
n1.insert(n5)
n1.insert(n6)
n1.insert(n7)
#n1.read()

removeDuplicates(n1)
n1.read()

'''
Time Complexity: O(N)
Space Complexity: O(1)
'''

def remove_duplicates_solution(L):
    it = L
    while it:
        next_distinct = it.next
        while next_distinct and next_distinct.data == it.data
            next_distinct = next_distinct.next
        it.next = next_distinct
        it = next_distinct
    return L
