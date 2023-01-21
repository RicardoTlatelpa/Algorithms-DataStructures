def cut_rod(p,n):    
    if n == 0:
        return 0
    q = float('-inf')    
    for i in range(1,n+1):        
        r = p[i] + cut_rod(p, n - i)        
        if r > q:
            q = r        
    return q

p = [0,1,5,8,9,10,17,17,20,24,30]
answer = cut_rod(p, 4)
print(answer)