def balanced(testVariable, startIndex = 0, currentIndex = 0):
    if startIndex == len(testVariable):
        return currentIndex == 0
    if currentIndex < 0:
        return False
    
    if testVariable[startIndex] == "(":
        return balanced(testVariable, startIndex + 1, currentIndex + 1)
    
    elif testVariable[startIndex] == ")":
        return balanced(testVariable, startIndex + 1, currentIndex - 1)
    