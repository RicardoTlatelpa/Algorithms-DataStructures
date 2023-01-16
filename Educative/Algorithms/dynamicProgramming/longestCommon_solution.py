def longest_common_substr_length_recursive(s1,s2,i1,i2,count):
    if i1 == len(s1) or i2 == len(s2):
        return count
    if s1[i1] == s2[i2]:
        count = longest_common_substr_length_recursive(s1,s2,i1+1, i2+1, count+1)
    c1 = longest_common_substr_length_recursive(s1,s2,i1+1,i2+1, count + 1)
    c2 = longest_common_substr_length_recursive(s1,s2,i1+1, i2, 0)

    return max(count, max(c1,c2))

def longest_common_substr_length(s1,s2):
    return longest_common_substr_length_recursive(s1,s2,0,0,0)


S1 = "0abc321"
S2 = "123abcdef"
print(longest_common_substr_length(S1,S2))