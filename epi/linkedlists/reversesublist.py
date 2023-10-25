'''
Write a program which takes a singly linked list L
and two integers s and f as arguments, and 
reverses the order of the nodes from the sth node to
the fth node, inclusive. The numbering begins at 
1, i., the head node is the first node. Do not 
allocate additional nodes.
'''

class Node():
    def __init__(self,val,next):
        self.val = val
        self.next = next
    def readList(self):
        temp = self
        while(temp):
            print(temp.val)
            temp = temp.next
    def insert(self,newNode):
        temp = self
        while(temp.next):
            temp = temp.next
        temp.next = newNode
        
def reverseSublist(L, start, finish):
    if start < 0:
        return L
    def reverse(head,start,end):
        # we want the end of the reversed
        # list to point to the end's next node
        end_next = None
        prev = None
        reverse_tail = head
        temp = head
        while(start <= end):
            nxt = None
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt
            if start == end:
                end_next = nxt
            start+=1
        # reversed list finished 
        reverse_tail.next = end_next
        return prev
    dummy_node = Node(0,L)
    s = 0
    t = dummy_node
    while(s < start-1):
        s+=1
        t = t.next
    print("current node @input 1",t.val)
    t.next = reverse(t.next,start,finish)
    return dummy_node.next


n1 = Node(1,None)
n2 = Node(2,None)
n3 = Node(3,None)
n4 = Node(4,None)
n5 = Node(5,None)
n6 = Node(6,None)

n1.insert(n2)
n1.insert(n3)
n1.insert(n4)
n1.insert(n5)
n1.insert(n6)
#n1.readList()


reverse = reverseSublist(n1,1,6)
reverse.readList()
def reverse_sublist(L,start,finish):
    dummy_head = sublist_head = Node(0,L)
    for _ in range(1,start):
        sublist_head = sublist_head.next
    # reverses sublist.
    sublist_iter = sublist_head.next
    for _ in range(finish - start):
        temp = sublist_iter.next
        sublist_iter.next,temp.next,sublist_head.next = (temp.next,
                                                         sublist_head.next,
                                                         temp)
    return dummy_head.next
