'''
5.9 Generate primes from N
'''


def generate_primes(n):
    primes = []
    is_prime = [False,False]  + [True] * (n-1)
    for p in range(2,n+1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p,n+1,p):
                is_prime[i] = False
    return primes

print(generate_primes(1000))

'''
The bound we gave for the trial-division approach, namely O(n^3/2), is based on O(sqrt(n)) bound for
each individual test. Since most numbers are not prime, the actual time complexity of trial-division
is actually lower on average, since the test frequently early-returns false. It is known that the 
time complexity of the trial-division approach is O(n^3/2/(logn)^2), so sieving is in fact superior
to trial-divison.
'''
