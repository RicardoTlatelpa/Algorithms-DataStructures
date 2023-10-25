'''
Implement a function which takes as input a singly linked list 
and an integer k and performs a pivot of the list with respect to 
k. The relative ordering of nodes that appear before k, and after k,
must remain unchanged; the same must hold for nodes holding keys equal
to k.
'''

class ListNode():
    def __init__(self,val,next):
        self.val = val
        self.next = next

def listPivot(L,k):
    head = L

    def length(head):
        length = 0
        while(head):
            length +=1
            head = head.next
        return length
    def reverse(head,k):
        if length(head) < k:
            nxt = head.next
            head.next = None
            return (head,nxt)
        tail = head
        prev = None
        for _ in range(k):
            nxt = tail.next
            tail.next = prev
            prev = tail
            tail = nxt
        return (prev,tail)
    temp = head
    dummy_node = ListNode(None,None)
    append_node = dummy_node
    while(temp):
        (reverse_head,nxt) = reverse(temp,k)
        print(reverse_head.nxt)
        while(append_node.next):
            append_node = append_node.next
        append_node.next = reverse_head
        temp = nxt
    return dummy_node.next

def list_pivoting(L,x):
    less_head = less_iter = ListNode(None,None)
    equal_head = equal_iter = ListNode(None,None)
    greater_head = greater_iter = ListNode(None,None)
    # populates the three lists
    while L:
        L.val < x:
            less_iter.next = L
            less_iter = less_iter.next
        elif L.val == x:
            equal_iter.next = L
            equal_iter = equal_iter.next
        else: # L.val > x
            greater_iter.next = L
            greater_iter = greater_iter.next
        L = L.next
    greater_iter.next = None
    equal_iter.next = greater_head.next
    less_iter.next = equal_head.next
    return less_head.next
'''
The time to compute the three lists is O(n). Combining the lists takes O(n)
time, yielding an overall O(n) time complexity. The space complexity is O(1)
'''
