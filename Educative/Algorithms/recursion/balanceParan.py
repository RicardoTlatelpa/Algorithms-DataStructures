stack = []
def balanced(testVariable, startIndex = 0, currentIndex = 0) :
    if(startIndex >= len(testVariable)):
        stack = []
        return True
    if(testVariable[startIndex] == '('):
        stack.append('(')
    else:
        # closing parenthesis case
        if len(stack) == 0:            
            return False
        p = stack.pop()
        if p == ')':
            stack = []
            return False
    return balanced(testVariable, startIndex + 1, currentIndex + 1)


print(balanced(["(", ")", "(", ")"]))