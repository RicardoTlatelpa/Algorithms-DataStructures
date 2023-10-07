def mazeObstacles(n,m, grid):
    tabulation = [[0]*n] * m
    # base case 1
    for i in range(m-1):
        for j in range(n-1):
            if grid[i][j] == -1:
                tabulation[i][j] = 0
            elif i == 0 and j == 0:
                tabulation[i][j] = 1
            else:
                up,left = 0,0
                if i > 0:
                    up = tabulation[i-1][j]
                if j > 0:
                    left = tabulation[i][j-1]
                tabulation[i][j] = up + left
    print(tabulation)
    return tabulation[m-1][n-1]
n = 10
m = 10
grid = [[0]*n]*m
print(mazeObstacles(n,m,grid))
