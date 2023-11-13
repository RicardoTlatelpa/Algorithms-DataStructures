'''
12.2 Is an anoynmous letter constructible?

Write a program which takes a text for an anonymous letter and text for a magazine
and determines if it is possible to write the anonymous letter using the magazine.
The anonymous letter can be written using the magazine if for each character in the 
anonymous letter, the number of times it appears in the anonymous letter is no more
than the number of times it appears in the magazine.
'''
# lets assume lower and uppercase letters
import collections
def isLetterConstructible(letter_text,magazine_text):
    letter_ht,mag_ht = {},{}
    def valid_char(char):
        if (ord(char) >= ord('a') and ord(char) <= ord('z')) or (ord(char) >= ord('A') and ord(char) <= ord('Z')):
            return True
        return False
    for char in letter_text:
        if valid_char(char) and char not in letter_ht:
            letter_ht[char] = 1
        elif valid_char(char) and char in letter_ht:
            letter_ht[char] += 1
    for char in magazine_text:
        if valid_char(char) and char not in mag_ht:
            mag_ht[char] = 1
        elif valid_char(char) and char in mag_ht:
            mag_ht[char] +=1
    # length check
    if len(letter_ht.keys()) != len(mag_ht.keys()):
        return False
    # equality check, assuming same length
    for key in letter_ht:
        if letter_ht[key] != mag_ht[key] or key not in mag_ht:
            return False
    return True

def is_letter_constructible_from_magazine(letter_text,magazine_text):
    # Compute the frequencies for all chars in letter_text
    char_frequency_for_letter = collections.Counter(letter_text)

    # Check if characters in magazine_text can cover characters in
    # char_frequency_for_letter.
    for c in magazine_text:
        if c in char_frequency_for_letter:
            char_frequency_for_letter[c] -=1
            if char_frequency_for_letter[c] == 0:
                del char_frequency_for_letter[c]
                if not char_frequency_for_letter:
                    return True
    return not char_frequency_for_letter
def is_letter_constructible_from_magazine_pythonic(letter_text,magazine_text):
    return (not collections.Counter(letter_text)- collections.Counter(magazine_text))

'''
The time complexity is O(m+n) where m and n are the number of characters in 
the letter and magazine, respectively. The space complexity is the size of the 
hash table constructed in the pass over the letter, i.e., O(L) where L is the number
of distinct characters appearing in the letter.

If the characters are coded in ASCII, we could do away with the hah table and use a 256
entry integer array A, with A[i] being set to the number of times the character i appears in the letter.
'''
