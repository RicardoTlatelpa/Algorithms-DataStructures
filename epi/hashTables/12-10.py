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

def find_substrings(s,words):
    
