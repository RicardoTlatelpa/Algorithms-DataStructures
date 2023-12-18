'''
12.10 Compute All string decompositions

Write a program which takes as input a string(the "sentence")
and an array of strings(the "words"), and returns the starting
indices of substrings of the sentence string which are the 
concatentation of all the strings in the words array. Each
string must appear exactly once, and their ordering is 
immaterial. Assume all strings in the words array have equal
length. It is possible for the words array to contain 
duplicates.

Hint: Exploit the fact that the words have the same length
'''
import collections
def find_substrings(s,words):
    def match_all_words_in_dict(start):
        curr_string_to_freq = collections.Counter()
        for i in range(start, start+len(words) * unit_size, unit_size):
            curr_word = s[i:i + unit_size]
            it = word_to_freq[curr_word]
            if it == 0:
                return False
            curr_string_to_freq[curr_word]+=1
            if curr_string_to_freq[curr_word] > it:
                return False
        return True
    word_to_freq = collections.Counter(words)
    unit_size = len(words[0])
    return [
            i for i in range(len(s) - unit_size * len(words)+1)
            if match_all_words_in_dict(i)
            ]
