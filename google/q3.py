def findSubstring(s1,s2):
    '''

    '''
    ht = {}
    ht_sum = 0
    for i in range(len(s1)):
        ht_sum +=1
        if s1[i] not in ht:
            ht[s1[i]] = 1
        else:
            ht[s1[i]] +=1

    i = 0
    n = len(s1) # size of window
    while(i < n):
        if s2[i] in ht:
            ht[s2[i]] -= 1
            if ht[s2[i]] > 0:
                ht_sum -= 1
        i+=1
    print(ht)
    if ht_sum == 0:
        return True
    while(i < len(s2)):
        # tail
        if s2[i-n] in ht:
            ht[s2[i-n]] +=1
            if ht[s2[i-n]] > 0:
                ht_sum +=1

        # head
        if s2[i] in ht:
            ht[s2[i]] -=1
            if ht[s2[i]] > 0:
                ht_sum -=1
        if ht_sum == 0:
            return True
        i+=1
    for (key) in ht:
        if ht[key] != 0:
            return False
    
        
    return True
print(findSubstring("abc", "bbb"))
