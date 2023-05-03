'''
You are given a positive integer 'N'. You have to reduce it to one by performing following steps:
1. Reduce it to n-1.(n=>n-1)
2. If it is divisible by 2, then divide by 2.(n=>n/2)
3. If it is divisible by 3, then divide by 3.(n=>n/3)
'''


def minSteps(n):
    
    mem = [float('inf')]*(n+1)
    def minSteps(n,steps):
        if n <= 1:
            return steps
        n = int(n)
        ans = mem[n]
        if n % 3 == 0:
            ans = min(ans,minSteps(n/3,steps+1))
    
        if n % 2 == 0:
            ans = min(ans,minSteps(n/2,steps+1))
        ans = min(ans,minSteps(n-1,steps+1))
    
        return ans
    ans = minSteps(n,0)
    print(mem)
    return ans

print(minSteps(33))
