def lookAndSay(n):
    sequence = ["1"]
    for i in range(n):
        nth_ = sequence[i]
        streak = 0
        start_char = nth_[0]
        constructed_string = ""
        for i in range(len(nth_)):
            char = nth_[i]
            if char == start_char:
                streak+=1
            else:
                constructed_string += str(streak) + str(start_char)
                start_char = char
                streak = 1
            if i == len(nth_) -1:
                constructed_string += str(streak) + str(start_char)
        sequence.append(constructed_string)
            
            
            
    return sequence[n-1]

print(lookAndSay(6))


'''
Time Complexity is O(N^2), i --> N, and for every iteration
we are traversing through a string of size M.

As N increases, so does M, so the worst case time would be N * M or => O(N^2)
The time complexity would be O(N) because we are holding all sequences up to N.
'''

def look_and_say(n):
    def next_number(s):
        result,i=[], 0
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i + 1]:
                i += 1
                count += 1
            result.append(str(count) + s[i])
            i+=1
        return ''.join(result)
    
    s = '1'
    for _ in range(1,n):
        s = next_number(s)

    return s
import itertools
def look_and_say_pythonic(n):
    s = '1'
    for _ in range(n-1):
        s = ''.join(
                str(len(list(group))) + key for key, group in itertools.groupby(s))
    return s
