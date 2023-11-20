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
    print("Hello world!",paragraph,keywords)

find_smallest_subarray(test_case,key_words)
