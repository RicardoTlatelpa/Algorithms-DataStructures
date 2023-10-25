'''
Insert and delete are local operations and have O(1) time complexity. Search
requires traversing the entire list, e.g., if the key is at the last node or is
absent, so its time complexity is O(n), where n is number of nodes.
'''
class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node
    def search_list(self,head,key):
        while head and head.data != key:
            head = head.next
        return head # if key not present in the list, head will have become null
    # Insert new_node after node.
    def insert_after(self,node,new_node):
        new_node.next = node.next
        node.next = new_node
    # Delete the node past this one. Assume node is not a tail
    def delete_after(self,node):
        node.next = node.next.next
    def insert(self,node):
        temp = self
        while temp.next != None:
            temp = temp.next
        temp.next = node

    def read_list(self): # linear time complexity
        temp = self
        print("READING LIST NOW")
        while(temp):
            print(temp.data)
            temp = temp.next


n1 = ListNode(1,None)
n2 = ListNode(2,None)
n3 = ListNode(3,None)
n4 = ListNode(4,None)
n5 = ListNode(5,None)
n6 = ListNode(6,None)
n7 = ListNode(7,None)
n1.insert(n2)
n1.insert(n3)
n1.insert(n4)
n1.insert(n5)
n1.insert(n6)
n1.insert(n7)
n1.read_list()

n8 = ListNode(8,None)
n9 = ListNode(9,None)
n10 = ListNode(10,None)

n8.insert(n9)
n8.insert(n10)

n8.read_list()
