'''
Give a singly linked list and an integer k, write a program to remove the kth last
element from the list. Your algorithm cannot use more than a few words of storage, regardless
of the length of the list. In particular, you cannot assume that it is possible to record the length
of the list.
'''

class ListNode():
    def __init__(self,val,next):
        self.val = val
        self.next = next

def remove_kth_last(L,k):
    dummy_node = ListNode(None,L)

    fast = dummy_node.next

    for _ in range(k):
        fast = fast.next
    slow = dummy_node
    while(fast):
        slow,fast = slow.next,fast.next
    slow.next = slow.next.next
    return dummy_node.next


'''
Time Complexity: O(N)
Space Complexity: O(1)
Compared to the brute-froce approach, if k is small enough that we can keep the set of nodes
between the two iterators in memory, but the list is too big to fit in memory, 
the two iterator approach halves the number of disc accesses.
'''

