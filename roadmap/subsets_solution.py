"""
Reflection on solution:

What I didn't catch up on was generating the actual subsets correctly
I knew the problem had to do with decision properties, but I never thought
of initializing an empty array and starting from there.
My solution dealt with different combinations of indices, and I ran 
into duplicates
"""
def find_subsets(nums, generation, answer, i):
    # Base Case
    if i == len(nums):   
        sub = generation.copy()
        answer.append(sub)
        return
    # 2 choices    
    # TAKE INDEX
    generation.append(nums[i])    
    find_subsets(nums,generation , answer, i + 1)
    generation.pop()
    # SKIP INDEX
    find_subsets(nums, generation, answer, i + 1)

def subsets(nums):
    answer = [] # array of unique subsets
    empty_lst = []
    find_subsets(nums, empty_lst, answer, 0)
    return answer
# TEST FUNCTION
lst = [1,2,3]
print(subsets(lst))