class Node():
    def __init__(self,val,next):
        self.val = val
        self.next = next

def test_cycle(head):
    if head is None:
        return None
    slow = head
    fast = head
    while(slow and fast.next and fast.next.next):
        slow,fast = slow.next, fast.next.next
        if slow == fast: # cycle is found
            slow = head
            while slow is not fast:
                slow,fast = slow.next,fast.next
            return slow
    return None


'''
Time complexity:
    O(N), worst case there is no cycle. We exhaust the fast pointer first
    which can be done in O(1/2*n) time. However, big O drops the constant,
    so the time complexity becomes O(N) where N is the number of nodes 
    inside of the linked list.
'''
