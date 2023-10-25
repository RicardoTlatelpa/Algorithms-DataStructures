'''
Queue insertion and deletion follows first-in, first-out semantics; stack insertion and deletion is last-in, first-out.
How would you implement a queue given a library implementing stacks?
'''

class StackQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def enqueue(self,val):
        self.stack1.append(val)
        self.stack2.append(self.stack1.pop())
    def dequeue(self):
        if self.stack2:
            return self.stack2.pop()
    def top(self):
        if self.stack2:
            return self.stack2[-1]
    def read(self):
        print(self.stack1, self.stack2)

sq = StackQueue()

sq.enqueue(1)
sq.read()
sq.enqueue(2)
print(sq.top())
sq.read()
sq.enqueue(3)
print(sq.top())
