class ListNode:
    def__init__(self,val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        def reverse(head):
            if head.next == None:
                return head
            answer = reverse(head.next)
            head.next.next = head
            h.next = None 
            return answer
        s = head
        f = head.next
        while(f.next != None and fast.next != None):
            s = s.next
            f = f.next.next
        # reverse half of list
        
        second = s.next
        slow.next = None

        second = reverse(second)
        first = head

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1 
            second = tmp2



        
