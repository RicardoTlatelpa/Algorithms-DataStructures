def generateCombinations(n, t,g):
    if n > t:
        return 
    if n == t:
        print(g)
        return

    for i in range(1, t):
        g.append(i)
        generateCombinations(n + i, t,g)
        g.pop()

generateCombinations(0,8,[])
