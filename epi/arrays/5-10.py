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

