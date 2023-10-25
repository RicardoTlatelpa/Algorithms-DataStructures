'''
Design a stack that includes a max operation, in addition to push and pop. The
max method should return the maximum value stored in the stack.

'''

class Max_Stack:
    def __init__(self):
        self.stack = []
    def getMax(self):
        if self.stack:
            return self.stack[-1][1]
        else:            
            return float('-inf')
    def addVal(self,val):
        self.stack.append((val, max(val,self.getMax())))
    def popVal(self):
        if len(self.stack) == 0:
            print('Stack is empty')
            return float('-inf')
        return self.stack.pop()[0]
    def readStack(self):
        print(self.stack)

   

my_max_stack = Max_Stack()
my_max_stack.getMax()
my_max_stack.addVal(1)
my_max_stack.addVal(1)
my_max_stack.addVal(1)
my_max_stack.addVal(100)
my_max_stack.addVal(1)
my_max_stack.addVal(2)
my_max_stack.addVal(-1)
my_max_stack.addVal(3)
my_max_stack.addVal(4)
my_max_stack.addVal(-4)
while(my_max_stack.stack):    
    print(my_max_stack.getMax())
    my_max_stack.popVal()