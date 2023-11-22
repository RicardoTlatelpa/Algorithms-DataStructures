'''
12.8 Find the longest subarray with distinct entries
Write a program that takes an array and returns the 
length of a longest subarray with the property that 
all its elements are distinct. For example,
if the array is [f,s,f,e,t,w,e,n,w,e] than a 
longest subarray all of whose elements are 
distinct is {s,f,e,t,w}.
'''

def longest_subarray_with_distinct_entries(A):
    def is_distinct():
        '''
        originally,
        i had an idea that having an array
        that checks every distinct key's count,
        but when creating a count hash table
        it takes O(1) time already to check
        if an element exists in the subarray
        so a linear search is not optimal
        '''
        return True

    '''
    as i search through the array
    i try to increase from point i and make
    of its length to the ans variable
    '''
    ans = float('-inf')
    for i in range(len(A)):
        char = A[i]
        dist = {
            char: 1
        }
        r = i + 1
        while r < len(A) and A[r] not in dist:
            dist[A[r]] =1
            ans = max(ans, r - i + 1)
            r+=1

    return ans
A = ['f','s','f','e','t','w','e','n','w','e']
print(longest_subarray_with_distinct_entries(A))
