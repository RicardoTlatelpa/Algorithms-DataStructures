'''
5.11 Compute the next permutation

Solution, compute all the permutations (N! time)
sort the permutations array and find the next permutation
if the permutation is the last permutation of the sorted
permutations array, pass the first element
'''

def next_permutation(perm):
    all_permutations = [] # permutations as integers
    visited = [False] * len(perm)
    N = len(perm)
    # i is the index
    # visited is the visited array
    # g is the generated string
    def findPermutations(i,visited,g):
        nonlocal all_permutations
        if(len(g) == len(perm)):
            # we found a permutation
            all_permutations.append(int(g))
            return
        for idx in range(len(visited)):
            if visited[idx] == False:
                visited[idx] = True
                findPermutations(idx,visited,g+perm[idx])
                visited[idx] = False
    findPermutations(0,visited,"")
    all_permutations.sort()
    curr_perm = int(''.join(perm))
    for i in range(len(all_permutations)):
        p = all_permutations[i]
        if p ==curr_perm:
            return_idx = (i+1)%len(all_permutations)
            return all_permutations[return_idx]
print(next_permutation(["1","2","3"]))

def next_permutation_solution(perm):
    inversion_point = len(perm-2)
    while(inversion_point >= 0 and perm[inversion_point] >= perm[inversion_point+1]):
        inversion_point-=1
    if inversion_point == -1:
        return []
    for i in reversed(range(inversion_point+1,len(perm))):
        if perm[i] > perm[inversion_point]:
            perm[inversion_point],perm[i] = perm[i],perm[inversion_point]
            break
    perm[inversion_point+1:] = reversed(perm[inversion_point+1:])
    return perm
'''
Time complexity: O(N)
space complexity: O(1)
'''
