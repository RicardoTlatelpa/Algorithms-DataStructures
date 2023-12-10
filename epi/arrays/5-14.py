import random

def compute_random_permutations(A):
    permutations = []
    N = len(A)
    vis = [False] * N
    def f(i,vis,g):
        nonlocal permutations
        if i >= N:
            permutations.append(list(g)) # create a copy of g
            return
        for idx in range(N):
            if vis[idx] == False:
                g.append(A[idx])
                vis[idx] = True
                f(i+1,vis,g)
                vis[idx] = False
                g.pop()
    f(0,vis,[])
    # after computing permutations O(N!) Space and Time
    r = random.randint(0,len(permutations)-1)
    #print(permutations[r])

compute_random_permutations([2,3,4])
import random
def random_sampling(k,A):
    for i in range(k):
        r = random.randint(i,len(A)-1)
        A[i],A[r] = A[r],A[i]

def compute_random_permutation(n):
    permutation = list(range(n))
    random_sampling(n,permutation)
    return permutation
print(compute_random_permutation(10))
