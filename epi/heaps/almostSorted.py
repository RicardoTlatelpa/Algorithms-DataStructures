'''
Write a program which takes as input a very long sequence of numbers and prints the numbers
in sorted order. Each number is at most k away from its correctly sorted position. (Such an array
is sometimes referrred to as being k-sorted). For example, no number in the sequence(3,-1,2,6,4,5,8)
is more than 2 away from its final sorted position.
'''

import heapq,itertools
def sort_k(sequence,k):
    '''
    sequence = 3,-1,2,6,4,5,8
    k = 2
    '''
    ans = []
    min_heap = heapq.heapify(sequence)
    while(min_heap):
        ans.append(heapq.heappop(min_heap))
    return ans

'''
Brute force solution is O(nLogn) and a O(n) time complexity.
'''

def sort_approximately_sorted_array(sequence,k):
    result = []
    min_heap = []
    for x in itertools.islice(sequence,k):
        heapq.heappush(min_heap,x)
    for x in sequence:
        smallest = heapq.heappushpop(min_heap,x)
        result.append(smallest)
    while min_heap:
        smallest = heapq.heappop(min_heap)
        result.append(smallest)
    return result

'''
The time complexity is O(nLogk). The space complexity is O(k)
'''
