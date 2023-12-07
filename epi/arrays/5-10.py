'''
5.10
Permute the elements of an array
Time complexity: N!
Space complexity: stack space
'''

def apply_permutation(A,p):
    permuted_array = [A[0]] * len(A)
    ht = {}
    for i in range(len(A)):
        ht[i] = A[i]

    for i in range(len(p)):
        permutation = p[i]
        permuted_array[permutation] = ht[i]

    return permuted_array

print(apply_permutation(['a','b','c','d'],[2,0,1,3]))
'''
Time Complexity: O(N)
Space Complexity: O(N)
'''

def apply_permutation_solution(A,perm):
    for i in range(len(A)):
        next = i
        while(perm[next] >= 0):
            A[i], A[perm[next]] = A[perm[next]], A[i]
            temp = perm[next]
            perm[next] -= len(perm)
            next = temp
    perm[:] = [a + len(perm) for a in perm]
    print(A)

apply_permutation_solution(['a','b','c','d'], [2,0,1,3])

'''
The above solution improves the space complexity
Time Complexity: O(N)
Space Complexity: O(1)
So the solution is much more efficient because of its space
efficiency
'''
