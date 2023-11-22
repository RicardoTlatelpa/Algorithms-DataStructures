'''
12.9 Find the length of a longest contained interval

Write a program which takes as input a set of integers
represented by an array, and returns the size of a largest
subset of integers in the array having the property that if
two integers are in the subset, then so are all integers
between them. For example, if the input is 
[3,-2,7,9,8,1,2,0,-1,5,8], the largest such subset is
[-2,-1,0,1,2,3], so you should return 6.
'''
import heapq
def longest_contained_range(A):
    heapq.heapify(A)
    largest_count = float('-inf')
    count = 0
    last_n = A[0]
    while(len(A)):
        popped = heapq.heappop(A)
        diff = abs(last_n - popped)
        last_n = popped
        if diff > 1:
            largest_count = max(largest_count,count)
            count = 1
        count +=1
    return largest_count
A = [10,5,3,11,6,100,4]
print(longest_contained_range(A))

def epi_longest_contained_range(A):
    # unprocessed_entries records the existence of each entry in A.
    unprocessed_entries = set(A)
    max_interval_size = 0
    while unprocessed_entries.pop():
        a = unprocessed_entries.pop()
        # finds the lower bound of the largest range containing a
        lower_bound = a - 1
        while lower_bound in unprocessed_entries:
            unprocessed_entries.remove(lower_bound)
            lower_bound -=1
        # finds the upper bound of the largest range containing a.
        upper_bound = a + 1
        while upper_bound in unprocessed_entries:
            unprocessed_entries.remove(upper_bound)
            upper_bound +=1
        max_interval_size = max(max_interval_size,
                                upper_bound - lower_bound - 1)
        return max_interval_size
'''
The time complexity of this approach is O(N), where n
is the array length, since we add and remove array elements 
in the hash table no more than once.
'''
