'''

'''

def countChars(arr):
    ht = {}
    ans = float('-inf')
    ansVal = -1
    for i in range(len(arr)):
        if arr[i] not in ht:
            ht[arr[i]] = 1
            if ht[arr[i]] > ans:
                ans = ht[arr[i]]
                ansVal = arr[i]
        else:
            
            ht[arr[i]] +=1
            ans = max(ans, ht[arr[i]]) 
