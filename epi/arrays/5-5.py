'''
5.5 Delete duplicates from a sorted array

Write a prgoram whcih takes as input a sorted array and updates it so that all duplicates have been
removed and the remaining elements have been shifted left to fill the emptied indices. return
the number of valid elements. Many languages have library functions for performing this operation -
you cannot use these functions.
'''

def delete_duplicates(A):
    if not A:
        return 0
    write_index = 1
    for i in range(1,len(A)):
        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            write_index +=1
    return A[:6]

print(delete_duplicates([2,3,5,5,7,11,11,11,13]))
