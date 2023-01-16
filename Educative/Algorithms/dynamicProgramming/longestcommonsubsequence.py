def longestCommonSubU(s1,s2, curr, curr2):
    
    if curr < 0 or curr >= len(s2) or curr2 < 0 or curr2 >= len(s1):
        return 0
    c1 = 0
    print(curr,curr2)
    if(s2[curr] == s1[curr2]):
        c1 = 1 + longestCommonSubU(s1,s2,curr+1, curr2+1)
    
    c1 = longestCommonSubU(s1, s2, curr+1, curr2)    
    c2 = longestCommonSubU(s1,s2, curr, curr2+1)
    return max(c1,c2)

def longestCommonSub(s1,s2):
    return longestCommonSubU(s1,s2, 0,0) -1

s1 = "EducativeIsFunsasdasdads"
s2 = "AlgorithmsAreFunsasdasdasd"
#print(s1[0], s2[0])
print(longestCommonSub(s1,s2))
