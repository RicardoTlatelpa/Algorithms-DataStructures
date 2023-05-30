def frogJump(array):
    # frog can jump one idx or two indices
    dp = [-1] * (len(array)+1)
    def f(i,dp):
        if i == 0: 
            return 0
        if dp[i] != -1:
            return dp[i]

        left = f(i-1,dp) + abs(array[i] - array[i-1])
        right = float('inf')

        if i > 1:
            right = f(i-2,dp) + abs(array[i] - array[i-2])
        
        dp[i] = min(left,right)
        return dp[i]


    return f(len(array)-1,dp)

def frogTabulation(a):
    
    dp = [0] * (len(a)) 

    for i in range(1,len(a)):
        fs = dp[i-1] + abs(a[i] - a[i-1])
        ss = 1000000
        if i > 1:
            ss = dp[i-2] + abs(a[i] - a[i-2])
        dp[i] = min(fs,ss)
    return dp[len(a)-1]

def frogSpace(a):
    # optimizing tabulation solution using variables
    prev = 0
    prev2 = 0

    for i in range(1,len(a)):
        fs = prev + abs(a[i] - a[i-1])
        ss = float('inf')
        if i > 1:
            ss = prev2 + abs(a[i] - a[i-2])
        curi = min(fs,ss)

        prev2 = prev 
        prev = curi
    return prev 


array = [7,4,4,2,6,6,3,4]

print(frogJump(array))
print(frogTabulation(array))
print(frogSpace(array))
