'''
12.1 Is an anagram a palindrome
input: string

Assertion:
only one odd number count of a distinct character can exist in a string

The rest of the character counts have to be divisble by 2, we can test that with %2 == 0
'''

def canFormPalindrome(s):
    d = {}
    # constructing hash table
    for char in s:
        if char in d:
            d[char] +=1
        else:
            d[char] = 1
    # palindrome test
    print(d)
    for key in d:
        count = d[key]
        if count % 2 > 1:
            return False
    return True

print(canFormPalindrome("edified"))
