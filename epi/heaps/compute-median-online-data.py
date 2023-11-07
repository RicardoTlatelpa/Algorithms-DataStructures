'''
10.5 Compute the median of online data
'''

# in the odd case, it's the middle element
# in the even case, it's the middle element idx + middle element idx + 1 / 2 
import heapq
def compute_median(sequence):
    ans = []
    median_array = [] # maintain a sort
    for n in sequence:
        median_array.append(n)
        median_array.sort()# nLogn * n => n^2
        odd = len(median_array)%2!=0 or len(median_array) == 1
        mid_idx = (len(median_array)-1)//2
        if odd:
            ans.append(median_array[mid_idx])
        else:
            compute_median = (median_array[mid_idx] + median_array[mid_idx+1])/2
            ans.append(compute_median)
    return ans


print(compute_median([1,0,3,5,2,0,1]))

# slow as fuck O(N^2)

def online_median(sequence):
    min_heap,max_heap,result = [],[],[]
    for x in sequence:
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap,x))
        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap,-heapq.heappop(max_heap))
        result.append(0.5 * (min_heap[0] + (-max_heap[0])))
    return result
