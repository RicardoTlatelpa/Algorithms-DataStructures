'''
Write a program that takes as input a singly linked list and a nonnegative integer k, and returns
the list cyclically shifted to the right by k. 

Hint: How does this problem differ from rotating an array?
'''
class ListNode():
    def __init__(self,val,next):
        self.val = val
        self.next = next
    def insert(self,val):
        temp = self
        while(temp.next):
            temp = temp.next
        temp.next = ListNode(val,None)
    def read(self):
        temp = self
        while(temp):
            print(temp.val)
            temp = temp.next

def cyclically(L,k):
    def length(head):
        l = 0
        while(head):
            head,l = head.next,l+1
        return l
    real_k = k % length(L)
    if real_k == 0:
        return L

    dummy_node = ListNode(None, L)
    slow = dummy_node
    fast = L
    for _ in range(real_k):
        fast = fast.next
    last_node = None
    while(fast):
        if fast.next == None:
            last_node = fast
        slow,fast = slow.next,fast.next

    new_head = slow.next
    slow.next = None
    last_node.next = L
    return new_head

n1 = ListNode(1,None)
n1.insert(2)
n1.insert(3)
n1.insert(4)
n1.insert(5)
n1.insert(6)
n1.insert(7)

cyclically(n1,2).read()


def cyclically_right_shift_list(L,k):
    if not L:
        return L
    # computes the length of L and the tail
    tail, n = L, 1
    while tail.next:
        n+=1
        tail = tail.next
    k %= n
    if k == 0:
        return L
    tail.next = L
    steps_to_new_head, new_tail = n-k, tail
    while(steps_to_new_head):
        steps_to_new_head -=1 
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None
    return new_head
