'''
Each trade is encoded by a line in the following format:
    1232111,AAPL,30,456.12
- first number is the time of the trade expressed as the number of milliseconds since the
start of the day's trading

Lines within each file are sorted in increasing order of time
the remaining vlaues are the stock symbol
number of shares
price

you are to create a single file containing all the trades from the 500 lines, sorted
in order of increasing trades. The individual files are all of the order of 5-100megabytes

Write a program that takes as input a set of sorted sequences and conmputes the union of
these sequences as a sorted sequence. For example, if the input is [3,5,7],[0,6],[0,6,28],
then the output is [0,0,3,5,6,6,7,28]
'''
import heapq
class Solution:
    def mergeSortedFiles(self,arr):
        min_heap = []
        for i in range(len(arr)):
            for num in arr[i]:
                heapq.heappush(min_heap,num)
        ans = []
        while(min_heap):
            ans.append(heapq.heappop(min_heap))
        return ans

    def merge_sorted_arrays(self,sorted_arrays):
        min_heap = []
        # build a list of iterators for each array in sorted_arrays
        sorted_arrays_iters = [iter(x) for x in sorted_arrays]
        # puts first element from each iterator in min_heap
        for i, it in enumerate(sorted_arrays_iters):
            first_element = next(it,None)
            if first_element is not None:
                heapq.heappush(min_heap,(first_element,i))
        result = []
        while min_heap:
            smallest_entry, smallest_array_i = heapq.heappop(min_heap)
            smallest_array_iter = sorted_arrays_iters[smallest_array_i]
            result.append(smallest_entry)
            next_element = next(smallest_array_iter,None)
            if next_element is not None:
                heapq.heappush(min_heap, (next_element,smallest_array_i))
        return result
    def merge_s_arrays(self,sorted_arrays):
        return list(heapq.merge(*sorted_arrays))
