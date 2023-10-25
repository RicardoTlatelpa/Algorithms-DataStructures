'''
RLE compression offers a fast way to do efficient on-the-fly compression and 
decompression of strings. The idea is simple - encoding successive repeated characters by the 
repitition count and the character. For example, the RLE of "aaaabcccaa" is "4a1b3c2a".
The decoding of "3e4f2e" returns "eeeffffee"

Assume the string to be encoded consists of letters of the alphabet, with no digits,
and the string to be decoded is a valid encoding.
'''

def runLengthEncode(code):
    ans = ""
    curr_char = code[0]
    count = 0
    for i in range(len(code)):
        char = code[i]
        if char == curr_char:
            count+=1
        else:
            ans += str(count) + curr_char
            curr_char = char
            count = 1
        if i == len(code)-1:
            if count > 0:
                ans += str(count)+curr_char
    return ans
print(runLengthEncode("eeeffffeef"))
def runLengthDecode(code):
    n = 0
    decode = ""
    for char in code:
        if ord(char) >= ord("a") and ord(char) <= ord("z"):
            for i in range(n):
                decode+=char
        else:
            n = int(char)
    return decode

print(runLengthDecode("3e4f2e1f"))
