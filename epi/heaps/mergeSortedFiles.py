'''
10.1 Write a program that takes as input a set of sorted sequences
and computes the union of these sequences as a sorted sequence.
For example, if the input is [3,5,7], [0,6] and [0,6,28], then the
output is [0,0,3,5,6,6,7,28].
'''
import heapq
def mergeSortedArrays(lists):
    ans = []
    min_heap = []
    
    for l in lists:
        for n in l:
            heapq.heappush(min_heap,n)

    while(min_heap):
        ans.append(heapq.heappop(min_heap))

    return ans
