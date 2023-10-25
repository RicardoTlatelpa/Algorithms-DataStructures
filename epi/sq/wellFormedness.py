'''
Write a program that tests if a string made up of the characters '(', ')', '[', ']', '{', '}'
is well-formed.
'''

def wellFormed(st):
    MATCHING={
            '(': ')',
            '[': ']',
            '{': '}'
            }
    s = []
    
    for i in range(len(st)):
        char = st[i]
        if char == '(' or char == '[' or char == '{':
            s.append(char)
        else:
            if len(s) == 0:
                return False
            if MATCHING[s[-1]] != char:
                return False
            else:
                s.pop()
    if len(s) != 0:
        return False
    return True

print(wellFormed("{)"))
print(wellFormed("([]){()}"))
print(wellFormed("()(())"))

def is_well_formed(s):
    left_chars, lookup = [], {'(': ')', '{': '}', '[':']'}
    for c in s:
        if c in lookup:
            left_chars.append(c)
        elif not left_chars or lookup[left_chars.pop()] !=c:
            return False
    return not left_chars
