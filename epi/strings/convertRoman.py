def convert(input_string):

    roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
    }
    
    visited = [False] * len(input_string)
    
    ans = 0
    for i in range(len(input_string)-1):
        char = input_string[i]
        nextChar = input_string[i+1]

        if roman[char] < roman[nextChar] and visited[i] == False:
            ans += roman[nextChar] - roman[char]
            visited[i] = True
            visited[i+1] = True
        else:
            if visited[i] == False:
                ans += roman[char]
    if input_string[-2] >= input_string[-1]:
        ans += roman[input_string[-1]]
    if len(input_string) == 1:
        ans += roman[input_string[0]]


    return ans

print(convert("IXV"))

import functools

def roman_to_integer(s):
    T = {'I': 1, 'V': 5, 'X': 10, 'L':50,'C':100,'D':500,'M':1000}

    return functools.reduce(
            lambda val, i: val + (-T[s[i]] if T[s[i]] < T[s[i+1]] else T[s[i]]),
            reversed(range(len(s)-1), T[s[-1]])
            )
