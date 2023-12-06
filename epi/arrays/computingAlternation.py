'''
5.8 Computing an alternation


Write a program that takes an array A of n numbers, and 
rearranges A's elements to get a new array B having 
the property that B[0] < B[1] ≥ B[2] ≤ B[3] ≥ B[4] ≤ B[5] ≥ •*.
'''

'''

Example:
    [1,2,3] => [1,3,2]
    [1]
    [1,2]
'''
def rearrange(A):
    # we could rearrange the sorted array using 2 pointers
    # left pointer pointing to the smallest number; 0
    # right pointer pointing to the largest number; n-1
    A.sort() # logN
    n = len(A)-1 
    left = 1
    right = n
    while(left < right):
        A[left],A[right] = A[right],A[left]
        left+=1
        right-=1
    return A

def rearrange_solution(A):
    A.sort()
    for i in range(len(A)):
        A[i:i+2] = sorted(A[i:i+2], reverse=i%2==1)
    return A

print(rearrange_solution([5,6,3,10,7,1,0]))


