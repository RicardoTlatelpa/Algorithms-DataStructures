'''
Assume the lists are sorted. 
The merge of the two lists is a list consisting of the nodes of the two lists in which
numbers appear in ascending order. 
Write a program that takes two lists, assumed to be sorted, and returns their merge. The only
field your program can change in a node is its next field.

'''
class Node:
    def __init__(self,val,next_ptr):
        self.val = val
        self.next = next_ptr

    def read(self):
        temp = self
        while(temp):
            print(temp.val)
            temp = temp.next
    def insert(self,node):
        temp = self
        while(temp.next != None):
            temp = temp.next
        temp.next = node


def mergeLists(L1,L2):
    temp1,temp2 = L1,L2
    ans = Node(None,None)
    temp3 = ans
    while(temp1 and temp2):
        if temp1.val < temp2.val:
            temp3.next = temp1
            temp3 = temp3.next
            temp1 = temp1.next
        elif temp2.val < temp1.val:
            temp3.next = temp2
            temp3 = temp3.next
            temp2 = temp2.next
        else:
            temp3.next = temp1
            temp3 = temp3.next
            temp3.next = temp2
            temp3 = temp3.next
            temp1 = temp1.next
            temp2 = temp2.next
    if(temp1):
        temp3.next = temp1
    if(temp2):
        temp3.next = temp2

    return ans.next
'''
Tests
'''
n2 = Node(2,None)
n5 = Node(5,None)
n7 = Node(7,None)
n2.insert(n5)
n2.insert(n7)


n3 = Node(3,None)
n11 = Node(11,None)

n3.insert(n11)


#mergeLists(n2,None).read()

def merge_two_sorted_lists(L1,L2):
    dummy_head = tail = Node(None,None)
    while L1 and L2:
        if L1.val < L2.val:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next

    tail.next = L1 or L2
    return dummy_head.next
