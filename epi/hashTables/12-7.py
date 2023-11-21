'''
12.7 Find Smallest Subarray sequentially covering all values

Write a program that takes two array of strings, and return the indicies of the starting
and ending index of a shortest subarray of the first array(the "parpagraph" array) that 
"sequentially covers" contains all the strings in the second array(the "keywords" array),
in the order in which they appear in the keywords array. You can assume all keywords are distinct.
For example, let the paragraph array be (apple, bannana, cat,apple) and the keywords
array be (bannana,apple). The paragraph subarray starting at index 0 and ending at index 1
does not fulfill the specification, even though it contains all the keywords, since they
do not appear in the specified order. on the other hand, the subarray starting at index 1 and 
ending at index 3 does fullfill the specification.
'''
def findSmallest(paragraph,keywords):
    # maintain the order of the keywords
    # find the smallest subarray
    ans = float('inf')
    paragraph = paragraph.split(" ")
    keywords_length = [False] * len(keywords)
    k = 0 # keyword pointer
    l = 0 # paragraph pointer
    for i in range(len(paragraph)):
        curr_word = paragraph[i]
        if k < keywords_length and curr_word == keywords[k]:
            seq_count += 1

    return ans
