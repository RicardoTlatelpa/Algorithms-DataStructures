"""
A good string search algorithm is fundamental to the performance of many applications.
Several clever algorithms have been proposed for string search, each with its own
trade-offs. As a resul,t, there is no single perfect answer. If someone asks you this
question in an interview, the best way to approach this would be to work through one 
good algorithm in detail and discuss at a high level other algorithms.

Given two strings s(the search string) and t(the text), find the first occurrence of s 
in t.
"""

def find_substring(s,t):
    if s == "":
        return (-1,-1)
    ht = {}
    max_ht = {}
    char_count = 0
    for char in s:
        if char not in ht:
            ht[char] = 1
            max_ht[char] = 1
        else:
            ht[char] += 1
            max_ht[char] +=1
        char_count +=1
    print(ht,char_count)

    n = len(s)
    # sliding window algorithm
    j = 0
    i = 0
    while(i < n):
        char = t[i]
        if char in ht and ht[char] > 0:
            ht[char] -= 1
            char_count-=1
        i+=1
    if char_count == 0:
        return t[j:i]
    
    while(i < len(t)):
       char = t[i]
       # tail
       if char in ht and ht[char] < max_ht[char]:
            ht[char] +=1
            char_count +=1
       #head
       print(j,i,char_count)
       if char in ht and ht[char] > 0:
            ht[char] -=1
            char_count -=1
        
       if char_count == 0:
           return t[j:i+1]
       j+=1
       i+=1
    return (-1,-1)

print(find_substring("ricardo", "was here ricardo"))

