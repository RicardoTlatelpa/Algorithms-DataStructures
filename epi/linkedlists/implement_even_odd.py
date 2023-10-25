'''
Consider a singly linked list who nodes are numbered starting at 0. Define the even-odd merge
of the list to be the list consisting of the even-numbered nodes followed by the odd-numbered
nodes. The even-odd merge is illustrated in figure 7.10.

Write a program that computes the even-odd merge.
Hint: use temporary additional storage
'''


def evenOddMerge(L):
    '''
    3 pointers, 
    1 that keeps track of the even list
    1 that keeps track of the odd list
    1 that is the head of the even list, that will be returned in the end of the function
    '''
    evenHead = None
    oddHead = None
    evenPointer = None
    oddPointer = None
    temp = L
    while(temp):
        nxt = temp.next
        node_value = temp.val
        temp.next = None
        if node_value % 2 == 0:
            if evenHead == None:
                evenHead = temp
            if evenPointer == None:
                evenPointer = temp
            elif evenPointer != None:
                evenPointer.next = temp
                evenPointer = evenPointer.next
        else:
            if oddHead == None:
                oddHead = temp
            if oddPointer == None:
                oddPointer = temp
            elif oddPointer != None:
                oddPointer.next = temp
                oddPointer = oddPointer.next
        temp = nxt
    if evenHead == None:
        return oddHead
    if evenPointer:
        evenPointer.next = oddHead
    return evenHead

def even_odd_merge(L):
    if not L:
        return L
    even_dummy_head,odd_dummy_head = ListNode(0,None), ListNode(0,None)
    tails, turn = [even_dummy_head, odd_dummy_head], 0
    while L:
        tails[turn].next = L
        L = L.next
        tails[turn] = tails[turn].next
        turn ^= 1
    tails[1].next = None
    tails[0].next = odd_dummy_head.next
    return even_dummy_head.next
'''
The time complexity is O(n) and the space complexity is O(1)
'''
