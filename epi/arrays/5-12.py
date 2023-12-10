'''
5.12 Sample Offline Data
Implement an algorithm that takes as input an array of
distinct elements and a size, and returns a subset of the
given size of the array elements. All subsets should be
equally likely. Return the result in input array itself.


Input: A, N;
where A is an array of distinct element
and N is the size of the array A
and k is the size of the subset
Output:
returns a subset of the given size of the array elements

Hint: How would you construct a random subset of size k+1
given a random subset of size k?

Example: 
    Lets say the distinct elements in the array A are letters of the Alphabet
    [A,B,C,D,E,F], N = 6, K = 3
    returns a subset of the given size of the array elements
    i --> k
    random picker between i and N-1
    0,5 => swap indices => A,F = F,A 
    1,5 => swap indices => B,A = A,B
    2,5 => swap indices => C,B = B,C
    the random subset consists of the first three entries
    [F,B,C,D,E,A]
    [F,A,C,D,E,B]
    [F,A,B,D,E,C]
    where the answer is = [F,A,B]
    instruction to choose a random number: random.randint(n1,n2)
'''
import random
def sample_offline_data(k,A):
    N = len(A)
    for i in range(k):
        r = random.randint(i,N-1)
        A[i], A[r] = A[r],A[i]
        print(A)
    return A[0:k+1]
print("answer: ",sample_offline_data(3,['A','B','C','D','E','F']))
