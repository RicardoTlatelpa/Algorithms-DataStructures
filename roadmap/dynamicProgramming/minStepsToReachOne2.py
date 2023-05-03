def getMinSteps_(n,memo):
    if (n==1):
        return 0
    # check our cache if we have it stored
    if (memo[n] != -1):
        return memo[n]
    
    # n-1 path goes first
    res = getMinSteps_(n-1,memo)
    
    if (n% 2 == 0):
        res = min(res,getMinSteps_(n//2,memo))
    if (n%3 == 0):
        res = min(res,getMinSteps_(n//3,memo))

    memo[n] = 1 + res
    return memo[n]
def getMinSteps(n):
    memo = [0 for i in range(n+1)]
    for i in range(n+1):
        memo[i] = -1
    ans = getMinSteps_(n,memo)
    print(memo)
    return ans

n = 10

print(getMinSteps(n))
