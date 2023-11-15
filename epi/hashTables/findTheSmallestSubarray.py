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
    # number of elements in keywords array is M
    # number of elements in paragraph is N
    # Must contain all strings in the keywords set 
    '''
    First thing we must do is process the paragraph. We're looking 
    for all the keywords in a sentence, order doesn't matter
    
    '''
    paragraph = paragraph.split(' ')
    kht,latest_ht = {},{}
    
    for word in keywords:
        if word in kht:
            kht[word] += 1
        else:
            kht[word] = 1
    # O(m) memory for keyword hash table
    smallest_pair = float('inf')
    result = (-1,-1)
    for i,p in enumerate(paragraph):
        if len(latest_ht) == len()
        if p in keywords and p not in latest_ht:
            latest_ht[p] = [i]
        elif p in keywords and p in latest_ht:
            latest_ht[p].append(i)
    print(latest_ht)
    return result
find_smallest_subarray(test_case,key_words)
