'''
10.2 Design an efficient algorithm for sorting a k-increasing
-decreasing-array.
'''
import heapq
def sort_k(A,k):
    ans = []
    min_heap = []
    for n in A:
        heapq.heappush(min_heap,n)
    LIMIT = len(A) // k
    count = 0
    reverse = False
    temp = []
    while(min_heap):
        pop = heapq.heappop(min_heap)
        if count == LIMIT:
            ans.append(temp)
            temp = []
            count = 0
            reverse = not reverse
        
        if reverse:
            temp.insert(0,pop)
        else:
            temp.append(pop)
        count +=1
    a = []
    for l in ans:
        a = a + l
    return a
