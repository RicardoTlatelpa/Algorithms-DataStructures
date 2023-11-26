'''
5.4 Advancing through an array

Note: each positiion has a nonnegative integer associated with it, representing the maximum
you can advance from that position in one  move. You beging at the first position,
and win by getting to the last positiion. 

Write a program which takes an array of n integers, where A[i]
denotes the maximum you can advance from index i, and returns whether it is possible 
to advance to the last index starting from the beginning of the array

input: array
output: true/false

Example: [3,3,1,0,2,0,1]
'''

def canReachEnd(A):
    n = len(A) - 1
    def f(i):
        if i > n:
            return False
        if i == n:
            return True
        curr_max = A[i]
        for idx in range(1, curr_max+1):
            if f(i+idx) == True:
                return True
        return False

    return f(0)

print(canReachEnd([3,3,1,0,2,0,1]))
