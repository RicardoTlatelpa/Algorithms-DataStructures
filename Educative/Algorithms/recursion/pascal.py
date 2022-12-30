def computePascal(pascalArray, n):
    n -= 1
    prevPascal = pascalArray[len(pascalArray)-1]
    nextPascal = [1] * (len(prevPascal) + 1)
    for i in range(1, len(nextPascal) - 1):
        nextSum = prevPascal[i] + prevPascal[i-1]
        nextPascal[i] = nextSum
    pascalArray.append(nextPascal)
    print(nextPascal)
    if(n <= 0):
        return pascalArray[len(pascalArray)-1]
    else:
        return computePascal(pascalArray, n)
        

def printPascal(testVariable):
    # Write your code here
    pascalArray = [[1],[1,1]]
    if testVariable < 2 and testVariable >= 0:
        return pascalArray[testVariable]    
    else:
        return computePascal(pascalArray, testVariable-1)

print(printPascal(5))
