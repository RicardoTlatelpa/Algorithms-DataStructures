def createStack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)

def pop(stack):
    
    if(isEmpty(stack)):
        print("Stack overflow")
        exit(1)
    return stack.pop()
