'''
5.16 Generate NonUniform Random Numbers

Given a random number generator that produces values in 
[0,1) uniformly, how would you generatea one of the n numbers
according to the specified probabilities? For example,
if the numbers are 3,5,7,11, and the probabilities
are 9/18 = 50%, 6/18 = 33%, 2/18 = 11%, 1/18 = 6%

Input: 
    n, numbers 
    p, probabilities

'''
import itertools,bisect,random
def generate_nonuniform(values,probabilities):
    prefix_sum_of_probabilities = list(itertools.accumulate(probabilities))
    interval_idx = bisect.bisect(prefix_sum_of_probabilities, random.random())
    return values[interval_idx]

print(generate_nonuniform([3,5,7,11],[9/18,6/18,2/18,1/18]))
