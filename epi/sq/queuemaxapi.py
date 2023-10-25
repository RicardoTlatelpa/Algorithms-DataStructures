'''
Queue Max API
Implement a queue with enqueue, dequeue, and max operations. 
The max operation returns the maximum element currently stored in the queue.
'''

class QueueMax:
    def __init__(self):        
        self.q = []
        self.maxes = []

    def getMax(self):
        if self.maxes:
            return self.maxes[0]
        else:
            print('Queue is empty')
            
    def en(self,val):
        self.q.append(val)
        while(self.maxes and self.maxes[-1] < val):
            self.maxes.pop()
        self.maxes.append(val)

    def deq(self):
        if self.q:
            p = self.q.pop(0)
            if p == self.maxes[0]:
                self.maxes.pop(0)
            return p
        else:
            print('Queue is empty.')
        
    def top(self):
        if self.q:
            return self.q[0]        
        else:
            print('Queue is empty.')

q = QueueMax()

q.en(1)
q.en(2)
q.en(100)
q.en(-1)
q.en(1000)


while(q.q):
    print(q.getMax())
    q.deq()
'''
[(1,1), (2,2), (100,100), (-1,100)]


'''