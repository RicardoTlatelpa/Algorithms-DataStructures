def f(i,j,dp):
    if i == 0 and j == 0:
        return 0
    if i < 0 or j < 0:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    up = f(i-1,j,dp)
    left = f(i, j-1,dp)
    dp[i][j] = up + left
    return dp[i][j]


def uniquePathTabulation(m,n):
    dp = [[-1]*m]*n
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = 1
            else:
                up = 0
                left = 0
                if i > 0:
                    up = dp[i-1][j]
                if j > 0:
                    left = dp[i][j-1]
                dp[i][j] = up + left

    return dp[m-1][n-1]

def uniquePathsOptimized(m,n):
    prev = [0] * n

    for i in range(m):
        temp = [0] * n
        for j in range(n):
            if i == 0 and j == 0:
                temp[j] = 1
            else:
                up = 0
                left = 0
                if i > 0:
                    up = prev[j]
                if j > 0:
                    left = temp[j-1]
                temp[j] = up + left
        prev = temp

    return prev[n-1]


def uniquePaths(m,n):
    dp = [[-1]*m] * n
    return f(m-1, n-1,dp) 

ans=uniquePaths(10,10)
ans=uniquePathsOptimized(10,10)
print(ans)
