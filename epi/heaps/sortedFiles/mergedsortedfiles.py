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
