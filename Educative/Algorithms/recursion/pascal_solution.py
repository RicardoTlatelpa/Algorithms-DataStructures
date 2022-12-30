def printPascal(testVariable):
    # base case
    if testVariable == 0:
        return [1]
    else:
        line = [1]
    
        # Recursive case, build each array on the ascend
        previousLine = printPascal(testVariable - 1)
        for i in range(len(previousLine) - 1):
            line.append(previousLine[i] + previousLine[i + 1])
        line.append(1)
    return line

print(printPascal(5))