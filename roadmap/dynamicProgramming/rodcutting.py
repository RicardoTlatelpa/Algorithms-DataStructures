n = 8
dp = [float('-inf')] * (n*2)
def rodcutting(n,prices):
    if n == 0:
        return 0

    if dp[n] != float('-inf'): return dp[n]

    ans = 0

    for i in range(1, n):
        ans = max(ans, prices[i] + rodcutting(n-i, prices))

    dp[n] = ans
    return dp[n]

prices = [1,3,4,5,7,8,9,10,11]
print(rodcutting(n,prices))

