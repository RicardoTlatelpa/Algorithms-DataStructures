'''
12.6 Find the smallest subarray covering all values

Write a program which takes an array of strings and a set of strings,
and return the indicies of the starting and ending index of a shortest
subarray of the given array that "covers" the set ,i.e., contains all
strings in the set.
'''

test_case = "My paramount object in this struggle is to save the Union , and is not either to save or to destroy slavery. If I could save the Union without freeing any slave I would do it, and if I could save it by freeing all the slaves I would do it; and if I could save it by freeing some and leaving others alone I would also do that."
key_words = ["save", "Union"]

def find_smallest_subarray(paragraph, keywords):
    paragraph = paragraph.split(" ")
    ky_ht = {}
    for key in keywords:
        if key not in ky_ht:
            ky_ht[key] = 1
        else:
            ky_ht[key] += 1
    print(paragraph,ky_ht)
    sub_ht = {}
    l = 0
    ans = float('inf')
    ans_indices = [-1,-1]
    def contains_keywords(ky_ht,sub_ht):
        equality = True
        for key in ky_ht:
            if key not in sub_ht or ky_ht[key] != sub_ht[key]:
                equality = False
        return equality
    for i in range(len(paragraph)):
        # iterating through the words
        word = paragraph[i]
        if word not in sub_ht:
            sub_ht[word] = 1
        else:
            sub_ht[word]+=1
        while(contains_keywords(ky_ht,sub_ht)):
            size = i - l + 1
            if size < ans:
                ans = size
                ans_indices = [l,i]
            sub_ht[paragraph[l]] -=1
            if sub_ht[paragraph[l]] == 0:
                del sub_ht[paragraph[l]]
            l += 1
    
    return ans_indices
        

print(find_smallest_subarray(test_case,key_words))

import collections
def find_smallest_subarray_covering_set(paragraph,keywords):
    keywords_to_cover = collections.Counter(keywords)
    result = (-1,-1)
    remaining_to_cover = len(keywords)
    left = 0
    for right,p in enumerate(paragraph):
        if p in keywords:
            keywords_to_cover[p] -=1
            if keywords_to_cover[p] >= 0:
                remaining_to_cover -=1
        while remaining_to_cover == 0:
            if result == (-1,-1) or right - left < result[1] - result[0]:
                result = (left,right)
            pl = paragraph[left]
            if pl in keywords:
                keywords_to_cover[pl] += 1
                if keywords_to_cover[pl] > 0:
                    remaining_to_cover +=1
            left += 1
    return result

'''
The time complexity is O(n) where n is the length of the array,
since for each of the two indices we spent O(1) time per advance,
and each is advanced at most n-1 times.
The disadvatnage of this approach is that we need to keep the subarrays
in memory. We can achieve a steaming algorithm by keeping track of latest 
occurrences of query keywords as we process A. We use a doubly linked list
L to store the last occurrence(index) of each keyword in Q,
and a hash table H to map each keyword in Q to the corresponding node in L.
Each time a word in Q is encountered, we remove its node from L(which we find by 
using H), create a new node which records the current index in A, and append the new 
node to the end of L. We also update H. by doing this, each keyword in L is ordered
by its order in A; therefore, if L has N_Q words and the current index 
minus the index stored in the first node in L is less than the current best,
we update current best. The complexity is still O(n).

'''
